import pandas as pd
import os

wage_path = r"C:\Users\bryennt\Desktop\gross_living_wage_single.xlsx"
ins_path  = r"C:\Users\bryennt\Desktop\insurance.xlsx"
# 结果输出路径
output_path = r"C:\Users\bryennt\Desktop\net_living_wage_single.xlsx"
# ----------------------------------------------single

# 1. 读取数据
wage_df = pd.read_excel(wage_path)     # 包含列 “城市” 和 “省份” 以及 “gross_living_wage”
ins_df  = pd.read_excel(ins_path)      # 包含列 “地区”（省份名称） 和 “insurance”

# 2. 合并 insurance 信息到工资表
#    按照 wage_df["省份"] 对应 ins_df["地区"]，把保险比例插入到新列 "insurance"：
merged = wage_df.merge(
    ins_df.rename(columns={"地区":"省份"}), 
    on="省份", 
    how="left"
)

cols = list(wage_df.columns) + ["insurance"]
merged = merged[cols]

# 3. 计算累进税率 tax 列
def calc_tax(x):
    """
    按照：
    1–5000 元： 0%
    5000–8000 元：3%
    8000–17000 元：10% （含 17000）
    其他（<1 或 >17000）：按需求可自行扩展或设为 0
    """
    if x < 1:
        return 0.0
    elif x < 5000:
        rate = 0.00
    elif x < 8000:
        rate = 0.03
    elif x <= 17000:
        rate = 0.10
    else:
        rate = 0.0
    return x * rate

merged["tax"] = merged["gross_living_wage"].apply(calc_tax)

# 4. 计算 net_living_wage = gross + tax + insurance
merged["net_living_wage"] = (
    merged["gross_living_wage"] + merged["tax"] + merged["insurance"]
)

# 5. 保存到桌面
#    如果文件已存在，会被覆盖
merged.to_excel(output_path, index=False)
print(f"已将合并后的结果保存到：{output_path}")
