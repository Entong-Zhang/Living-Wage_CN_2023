import pandas as pd

# Step 1: 读取数据
input_path = "C:\\Users\\bryennt\\Desktop\\gross_living_wage1.xlsx"
df = pd.read_excel(input_path)

# Step 2: 计算 gross_living_wage（x）
df['gross_living_wage'] = (df['food'] + df['rent']) * (1 + df['ratio']) / ((0.9 - (1+ df['ratio']) * 0.094))

# Step 3: 回代计算各项
df['saving'] = 0.1 * df['gross_living_wage']
df['housing'] = df['rent'] + 0.094 * df['gross_living_wage']
df['food_housing'] = df['food'] + df['housing']
df['non'] = df['food_housing'] * df['ratio']
df['housing_other'] = 0.094 * df['gross_living_wage']

# Step 4: 保存结果到桌面
output_path = r"C:\Users\bryennt\Desktop\gross_living_wage_calculated1.xlsx"
df.to_excel(output_path, index=False)

print("计算完成，结果已保存到桌面！")
