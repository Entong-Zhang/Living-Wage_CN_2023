import pandas as pd

# 1. 读取数据，假设列名已为 'region', 'category', 'consumption'
consumption_df = pd.read_excel(r"C:\Users\bryennt\Desktop\consumption2.xlsx")
price_df = pd.read_excel(r"C:\Users\bryennt\Desktop\price.xlsx")

# 打印列名以确认
print("消费量表列名：", consumption_df.columns.tolist())
print("价格表列名：", price_df.columns.tolist())

# 2. 定义需要除以1000的分类
thousand_cats = ["粮食", "谷物", "食用油", "食用植物油", "食糖", "奶类"]

# 3. 根据分类调整消费量
consumption_df['consumption_adj'] = consumption_df.apply(
    lambda row: row['consumption'] / (1000 if row['category'] in thousand_cats else 500),
    axis=1
)
print(consumption_df[['region', 'category', 'consumption', 'consumption_adj']].head())
# 4. 合并价格数据
merged = consumption_df.merge(price_df, on='category', how='left')
print("合并后列：", merged.columns.tolist())
# 5. 检查是否生成了必要列，然后计算支出
if 'consumption_adj' not in merged.columns or 'price' not in merged.columns:
    raise KeyError("缺少必要列 'consumption_adj' 或 'price'，请检查输入表格")

merged['expenditure'] = merged['consumption_adj'] * merged['price']

# 6. 按地区汇总总支出
result = merged.groupby('region', as_index=False)['expenditure'].sum()

# 7. 输出并保存结果
print("各地区食品总支出：")
print(result)
result.to_excel(r"C:\Users\bryennt\Desktop\region_expenditure2.xlsx", index=False)

# 注意：
# - 请确保 price_df 包含 'category' 和 'price' 两列，且与消费表品类一致。
# - 如果发现有品类名称不匹配，可用：
#     print(set(consumption_df['category']) - set(price_df['category']))
# - 完成调试后，可删除打印语句。
