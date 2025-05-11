import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# 设置中文字体为宋体
plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel("C:\\Users\\bryennt\\Desktop\\graph.xlsx")

# 确保按照原始顺序排列
df['城市'] = pd.Categorical(df['城市'], categories=df['城市'], ordered=True)

# 一线、二线、三线城市定义
first_tier = ['北京', '上海', '广州', '深圳']
second_tier = ['天津', '石家庄', '太原', '呼和浩特', '沈阳', '大连', '长春', '哈尔滨', '南京', '杭州', '宁波', '合肥',
               '福州', '厦门', '南昌', '济南', '青岛', '郑州', '武汉', '长沙', '南宁', '海口', '重庆', '成都', '贵阳',
               '昆明', '西安', '兰州', '西宁', '银川', '乌鲁木齐']
third_tier = ['唐山', '秦皇岛', '包头', '丹东', '锦州', '吉林', '牡丹江', '无锡', '徐州', '扬州', '温州', '金华', '蚌埠',
              '安庆', '泉州', '九江', '赣州', '烟台', '济宁', '洛阳', '平顶山', '宜昌', '襄阳', '岳阳', '常德', '韶关',
              '湛江', '惠州', '桂林', '北海', '三亚', '泸州', '南充', '遵义', '大理']

# ---------- 第一张图 ----------
fig1, ax1 = plt.subplots(figsize=(14, 12))

for i, (city, wage) in df[['城市', 'wage']].iterrows():
    if city in first_tier:
        color = '#ffc4a8'
    elif city in second_tier:
        color = '#fa8e73'
    else:
        color = '#bd5943'
    ax1.barh(city, wage, color=color)

# 竖线与标注
vlines_red = [7629, 6537, 5720]
vlines_blue = [10865, 9821, 7803]
for x in vlines_red:
    ax1.axvline(x, color='red', linestyle='--', linewidth=1, label="普通众包骑手月均收入" if x == vlines_red[0] else "")
    ax1.text(x, -0.5, str(x), rotation=90, color='red', va='bottom', ha='center', fontsize=10)

for x in vlines_blue:
    ax1.axvline(x, color='black', linestyle=':', linewidth=1, label="乐跑骑手月均收入" if x == vlines_blue[0] else "")
    ax1.text(x, -0.5, str(x), rotation=90, color='black', va='bottom', ha='center', fontsize=10)

ax1.set_xlabel("工资（元）", fontsize=12)
ax1.tick_params(axis='y', labelsize=7)

# 图例（城市分类 + 收入线）
tier_legend_elements = [
    Patch(facecolor='#ffc4a8', label='一线城市'),
    Patch(facecolor='#fa8e73', label='二线城市'),
    Patch(facecolor='#bd5943', label='三线城市')
]
income_legend_elements = [
    Line2D([0], [0], color='red', linestyle='--', linewidth=1, label='普通众包骑手月均收入'),
    Line2D([0], [0], color='black', linestyle=':', linewidth=1, label='乐跑骑手月均收入')
]
ax1.legend(handles=tier_legend_elements + income_legend_elements, loc='upper right', fontsize=12)

plt.tight_layout()
plt.savefig("图1：外卖骑手实际收入与生存工资的比较.png", dpi=300)

# ---------- 第二张图 ----------
fig2, ax2 = plt.subplots(figsize=(14, 12))

for i, (city, wage) in df[['城市', 'wage']].iterrows():
    if city in first_tier:
        color = '#ffd687'
    elif city in second_tier:
        color = '#bfaa52'
    else:
        color = '#6b7e2c'
    ax2.barh(city, wage, color=color)

# 差值条形与标注
for i, (city, wage, gap) in df[['城市', 'wage', 'gap']].iterrows():
    new_val = wage + gap
    color = '#1b5013' if gap >= 0 else '#a03e08'
    ax2.barh(city, new_val - wage, left=wage, color=color)
    ax2.text(wage + gap / 2, i, f"{int(gap):+d}", 
             va='center', ha='center', fontsize=10, color='white')

ax2.set_xlabel("工资（元）", fontsize=12)
ax2.tick_params(axis='y', labelsize=7)

# 仅添加城市级别图例（不加“实际工资”图例）
tier_legend_elements2 = [
    Patch(facecolor='#ffd687', label='一线城市'),
    Patch(facecolor='#bfaa52', label='二线城市'),
    Patch(facecolor='#6b7e2c', label='三线城市')
]
ax2.legend(handles=tier_legend_elements2, loc='upper right', fontsize=12)

plt.tight_layout()
plt.savefig("图2：网约车司机实际收入与生存工资的比较.png", dpi=300)

plt.show()
