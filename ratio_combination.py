import pandas as pd

# 1. 读入两个表格
wage = pd.read_excel(r"C:\Users\bryennt\Desktop\living_wage.xlsx")
ratio = pd.read_excel(r"C:\Users\bryennt\Desktop\ratio.xlsx")

# 2. 重命名 ratio 的“地区”为“省份”，以便合并
ratio = ratio.rename(columns={'地区': '省份'})

# 3. 合并数据（左连接，保留工资表的全部城市）
merged = wage.merge(ratio[['省份', 'food_housing_to_non']], on='省份', how='left')

# 4. 把比例列插入到 rent 后面
cols = merged.columns.tolist()
insert_pos = cols.index('rent') + 1
col_data = merged.pop('food_housing_to_non')
merged.insert(insert_pos, 'food_housing_to_non', col_data)

# 5. 导出结果
merged.to_excel(r"C:\Users\bryennt\Desktop\wage_with_ratio.xlsx", index=False)
