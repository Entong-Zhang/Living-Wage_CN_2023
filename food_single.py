import pandas as pd
from scipy.optimize import linprog

path = "C:\\Users\\bryennt\\Desktop\\food.xlsx"
df = pd.read_excel(path)

# 主流程
adjusted = []
for region, group in df.groupby('地区'):
    if group.shape[1] < 6:
        print(f"警告: 地区 {region} 数据列数不足，已跳过。")
        continue
    print(f"开始优化地区: {region}")
    # 原始提取
    foods = group['食品种类'].values
    cons_orig = group['消费量'].values
    cal_orig  = group['热量'].values
    prot_orig = group['蛋白质'].values
    fat_orig  = group['脂肪'].values
    carb_orig = group['碳水化合物'].values
    # 定义类别掩码：0:果蔬 1:奶类 2:食糖 3:其他
    fv_mask    = (foods == '鲜瓜果') | (foods == '蔬菜及食用菌')
    milk_mask  = (foods == '奶类')
    sugar_mask = (foods == '食糖')
    other_mask = ~(fv_mask | milk_mask | sugar_mask)
    masks = [fv_mask, milk_mask, sugar_mask, other_mask]
    cat_cons = [cons_orig[m].sum() for m in masks]
    # 计算每类别的营养密度
    cat_cal = [cal_orig[m].sum() for m in masks]
    cat_prot = [prot_orig[m].sum() for m in masks]
    cat_fat = [fat_orig[m].sum() for m in masks]
    cat_carb = [carb_orig[m].sum() for m in masks]
    # 单位密度
    d_cal   = [cat_cal[i]/cat_cons[i]   if cat_cons[i]>0 else 0 for i in range(4)]
    d_prot  = [cat_prot[i]/cat_cons[i]  if cat_cons[i]>0 else 0 for i in range(4)]
    d_fat   = [cat_fat[i]/cat_cons[i]   if cat_cons[i]>0 else 0 for i in range(4)]
    d_macro = [d_prot[i]+d_fat[i]+(cat_carb[i]/cat_cons[i] if cat_cons[i]>0 else 0) for i in range(4)]
    # 构建 LP 变量：Y0-Y3, s_fv_L, s_fv_U, s_milk_L, s_sugar_U,
    # s_prot_L, s_prot_U, s_fat_L, s_fat_U, e_cal_U, e_cal_L
    num_Y = 4
    slacks = [ 's_fv_L','s_fv_U','s_milk_L','s_sugar_U',
               's_prot_L','s_prot_U','s_fat_L','s_fat_U',
               'e_cal_U','e_cal_L']
    n_vars = num_Y + len(slacks)
    A_ub, b_ub = [], []
    # 1. 果蔬 350 <= Y0 <= 375
    # lower: 350 - Y0 <= s_fv_L
    row = [0]*n_vars
    row[0] = -1
    row[num_Y + 0] = -1  # s_fv_L on RHS, bring to LHS as -s_fv_L => <= -350
    A_ub.append(row.copy()); b_ub.append(-350)
    # upper: Y0 - 375 <= s_fv_U
    row = [0]*n_vars
    row[0] = 1
    row[num_Y + 1] = -1  # -s_fv_U
    A_ub.append(row.copy()); b_ub.append(375)
    # 2. 奶类比例: 0.02*sum(Y)-Y1 <= s_milk_L
    row = [0]*n_vars
    for i in range(num_Y): row[i] = 0.02
    row[1] = row[1] - 1
    row[num_Y + 2] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    # 3. 食糖比例: Y2 - 0.05*sum(Y) <= s_sugar_U
    row = [0]*n_vars
    for i in range(num_Y): row[i] = -0.05
    row[2] = row[2] + 1
    row[num_Y + 3] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    # 4. 蛋白质 10%<=prot<=15%
    # lower: 0.10*sum(d_macro*Y) - sum(d_prot*Y) <= s_prot_L
    row = [0]*n_vars
    for i in range(num_Y): row[i] = 0.10*d_macro[i] - d_prot[i]
    row[num_Y + 4] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    # upper: sum(d_prot*Y) - 0.15*sum(d_macro*Y) <= s_prot_U
    row = [0]*n_vars
    for i in range(num_Y): row[i] = d_prot[i] - 0.15*d_macro[i]
    row[num_Y + 5] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    # 5. 脂肪 12%<=fat<=14%
    row = [0]*n_vars
    for i in range(num_Y): row[i] = 0.12*d_macro[i] - d_fat[i]
    row[num_Y + 6] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    row = [0]*n_vars
    for i in range(num_Y): row[i] = d_fat[i] - 0.14*d_macro[i]
    row[num_Y + 7] = -1
    A_ub.append(row.copy()); b_ub.append(0)
    # 6. 热量误差: sum(d_cal*Y)-e_cal_U <= 2665
    row = [0]*n_vars
    for i in range(num_Y): row[i] = d_cal[i]
    row[num_Y + 8] = -1
    A_ub.append(row.copy()); b_ub.append(2665)
    #            -sum(d_cal*Y)-e_cal_L <= -2665
    row = [0]*n_vars
    for i in range(num_Y): row[i] = -d_cal[i]
    row[num_Y + 9] = -1
    A_ub.append(row.copy()); b_ub.append(-2665)
    # all slacks and Y >=0 bounds
    bounds = [(0, None)] * n_vars
    # 目标: 最小化 slack 之和
    c = [0]*num_Y + [1]*len(slacks)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if not res.success:
        print(f"  💥 地区 {region} 优化失败：", res.message)
        continue
    sol = res.x
    Y = sol[:num_Y]
    print(f"  ✅ 优化成功，slack: {dict(zip(slacks, sol[num_Y:]))}")
    # 按原始比例二次分配
    new_cons = cons_orig.copy()
    for i, m in enumerate(masks):
        if cat_cons[i] > 0:
            new_cons[m] = Y[i] * cons_orig[m] / cat_cons[i]
    group['调整后消费量'] = new_cons
    adjusted.append(group)

# 合并保存
if adjusted:
    result_df = pd.concat(adjusted, ignore_index=True)
    result_df.to_excel("C:\\Users\\bryennt\\Desktop\\adjusted_food_data_by_region2.xlsx", index=False)
    print("✅ 已保存到桌面")
else:
    print("没有地区优化成功。")
