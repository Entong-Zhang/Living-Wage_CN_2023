import pandas as pd

# 读表
housing = pd.read_excel(r"C:\Users\bryennt\Desktop\housing_city.xlsx")
food   = pd.read_excel(r"C:\Users\bryennt\Desktop\food_exp_province.xlsx")

# 从 food 表里抽出需要的列并合并
need = ['省份', 'family_food_exp_month', 'single_food_exp_month']
merged = housing.merge(food[need], on='省份', how='left')

# 把新列插到“城市类别”后面
cols = merged.columns.tolist()
insert_pos = cols.index('城市类别') + 1

# 先 pop 出来
ffm = merged.pop('family_food_exp_month')
sfm = merged.pop('single_food_exp_month')

# 再 insert 回去
merged.insert(insert_pos, 'family_food_exp_month', ffm)
merged.insert(insert_pos+1, 'single_food_exp_month', sfm)

# 5. 写回 Excel
merged.to_excel(r"C:\Users\bryennt\Desktop\housing_with_food.xlsx", index=False)
