import pandas as pd
import numpy as np

# 读取数据
df = pd.read_excel('C:/Users/bryennt/Desktop/income.xlsx')

# 找到非空的人均可支配收入，计算年增长率
valid_data = df[df['人均可支配收入'].notna()].copy()
valid_data['增长率'] = valid_data['人均可支配收入'].pct_change()

# 计算平均增长率（排除第一个NaN）
avg_growth = valid_data['增长率'][1:].mean()

# 从最早的非缺失值往前回推
first_valid_index = valid_data.index[0]
first_valid_value = valid_data.loc[first_valid_index, '人均可支配收入']

# 回推前两个值
for i in range(2, 0, -1):
    idx = first_valid_index - i
    df.loc[idx, '人均可支配收入'] = first_valid_value / ((1 + avg_growth) ** i)

# 保存结果
output_path = 'C:/Users/bryennt/Desktop/filled_income.xlsx'
df.to_excel(output_path, index=False)

print(f"已使用平均增长率回推填充，保存至：{output_path}")
