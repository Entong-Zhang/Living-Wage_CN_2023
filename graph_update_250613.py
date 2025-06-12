#--------------------美团 81.95万
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

# 设置宋体字体
font_path = "C:/Windows/Fonts/simsun.ttc"
font_prop = font_manager.FontProperties(fname=font_path, size=12)

# g 从 0 到 1
g = np.linspace(0, 1, 1000)

# 各项计算
subsidy = 777129547.483184 * g *12
profit_remaining = 13857331000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 单位换算：百万元
subsidy_million = subsidy / 1e6
gdp_growth_million = gdp_growth_value / 1e6
profit_billion = profit_remaining / 1e6

# 找利润剩余 = 0 的临界 g
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 第一张图：三条线
fig, ax = plt.subplots(figsize=(10, 6))
l1, = ax.plot(g, subsidy_million, linestyle='--', label="补贴额（百万元）")
l2, = ax.plot(g, profit_billion, linestyle='-.', label="利润剩余（百万元）")
l3, = ax.plot(g, gdp_growth_million, linestyle=':', label="GDP增长值（百万元）")
ax.set_xlabel("g（补贴率）", fontproperties=font_prop)
ax.set_ylabel("金额", fontproperties=font_prop)
ax.legend(loc='upper left', prop=font_prop)
ax.grid(True)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}"))
if g_zero:
    ax.axvline(x=g_zero, color='gray', linestyle=':', linewidth=1)
    ax.text(g_zero, ax.get_ylim()[1], f"g ≈ {g_zero:.3f}", rotation=0, ha='center', va='bottom',
    color='black', fontproperties=font_prop)

plt.tight_layout()
plt.show()

# 第二张图：面积堆叠图（利润剩余占比 vs GDP增长率）
subsidy = 777129547.483184 * g *12
profit_remaining = 13857331000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 临界点
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 比例和增速换算
profit_ratio = profit_remaining / 13857331000 * 100  # %
gdp_growth_rate = gdp_growth_value / 126058200000000 * 100  # %

# 限定范围
profit_ratio_clipped = np.clip(profit_ratio, 0, 100)
gdp_growth_rate_clipped = np.clip(gdp_growth_rate, 0, 0.03)

# 绘图
fig, ax1 = plt.subplots(figsize=(10, 6))
p1 = ax1.fill_between(g, profit_ratio_clipped, label="利润剩余占比", hatch='////', facecolor='none', edgecolor='black')
ax1.set_ylabel("利润剩余占比（%）", fontproperties=font_prop)
ax1.set_ylim(0, 100)

ax2 = ax1.twinx()
p2 = ax2.fill_between(g, gdp_growth_rate_clipped, label="GDP增长率", hatch='\\\\', facecolor='none', edgecolor='blue')
ax2.set_ylabel("GDP增长率（%）", fontproperties=font_prop)
ax2.set_ylim(0, 0.03)

ax1.set_xlabel("g（补贴率）", fontproperties=font_prop)

if g_zero:
    gdp_at_g_zero = gdp_growth_rate_clipped[np.argmin(np.abs(g - g_zero))]
    ax2.text(g_zero, gdp_at_g_zero, f"g = {g_zero:.3f}\nGDP增长率 ≈ {gdp_at_g_zero:.4f}%",
             rotation=0, ha='left', va='bottom', color='black', fontproperties=font_prop, 
             backgroundcolor='white', fontsize=12, fontweight='bold')

handles = [p1, p2]
labels = [h.get_label() for h in handles]
ax1.legend(handles, labels, loc='upper left', prop=font_prop)

plt.xlabel("g（补贴率）", fontproperties=font_prop)
plt.grid(True)
plt.tight_layout()
plt.show()
#-----------------------------美团 745万
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

# 设置宋体字体
font_path = "C:/Windows/Fonts/simsun.ttc"
font_prop = font_manager.FontProperties(fname=font_path, size=12)

# g 从 0 到 1
g = np.linspace(0, 1, 1000)

# 各项计算
subsidy = -7064814068.02895 * g *12
profit_remaining = 13857331000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 单位换算：百万元
subsidy_million = subsidy / 1e6
gdp_growth_million = gdp_growth_value / 1e6
profit_billion = profit_remaining / 1e6

# 找利润剩余 = 0 的临界 g
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 第一张图：三条线
fig, ax = plt.subplots(figsize=(10, 6))
l1, = ax.plot(g, subsidy_million, linestyle='--', label="补贴额（百万元）")
l2, = ax.plot(g, profit_billion, linestyle='-.', label="利润剩余（百万元）")
l3, = ax.plot(g, gdp_growth_million, linestyle=':', label="GDP增长值（百万元）")
ax.set_xlabel("g（补贴率）", fontproperties=font_prop)
ax.set_ylabel("金额", fontproperties=font_prop)
ax.legend(loc='upper left', prop=font_prop)
ax.grid(True)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}"))
if g_zero:
    ax.axvline(x=g_zero, color='gray', linestyle=':', linewidth=1)
    ax.text(g_zero, ax.get_ylim()[1], f"g ≈ {g_zero:.3f}", rotation=0, ha='center', va='bottom',
    color='black', fontproperties=font_prop)

plt.tight_layout()
plt.show()

# 第二张图：面积堆叠图（利润剩余占比 vs GDP增长率）
subsidy = -7064814068.02895 * g *12
profit_remaining = 13857331000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 临界点
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 比例和增速换算
profit_ratio = profit_remaining / 13857331000 * 100  # %
gdp_growth_rate = gdp_growth_value / 126058200000000 * 100  # %

# 限定范围
profit_ratio_clipped = np.clip(profit_ratio, 0, 100)
gdp_growth_rate_clipped = np.clip(gdp_growth_rate, 0, 0.3)

# 绘图
fig, ax1 = plt.subplots(figsize=(10, 6))
p1 = ax1.fill_between(g, profit_ratio_clipped, label="利润剩余占比", hatch='////', facecolor='none', edgecolor='black')
ax1.set_ylabel("利润剩余占比（%）", fontproperties=font_prop)
ax1.set_ylim(0, 100)

ax2 = ax1.twinx()
p2 = ax2.fill_between(g, gdp_growth_rate_clipped, label="GDP增长率", hatch='\\\\', facecolor='none', edgecolor='blue')
ax2.set_ylabel("GDP增长率（%）", fontproperties=font_prop)
ax2.set_ylim(0, 0.3)

ax1.set_xlabel("g（补贴率）", fontproperties=font_prop)

if g_zero:
    gdp_at_g_zero = gdp_growth_rate_clipped[np.argmin(np.abs(g - g_zero))]
    ax2.text(g_zero, gdp_at_g_zero, f"g = {g_zero:.3f}\nGDP增长率 ≈ {gdp_at_g_zero:.4f}%",
             rotation=0, ha='left', va='bottom', color='black', fontproperties=font_prop, 
             backgroundcolor='white', fontsize=12, fontweight='bold')

handles = [p1, p2]
labels = [h.get_label() for h in handles]
ax1.legend(handles, labels, loc='upper left', prop=font_prop)

plt.xlabel("g（补贴率）", fontproperties=font_prop)
plt.grid(True)
plt.tight_layout()
plt.show()
#------------------------------滴滴
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

# 设置宋体字体
font_path = "C:/Windows/Fonts/simsun.ttc"
font_prop = font_manager.FontProperties(fname=font_path, size=12)

# g 从 0 到 1
g = np.linspace(0, 1, 1000)

# 各项计算
subsidy = 3028433893.11489 * g *12
profit_remaining = 535000000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 单位换算：百万元
subsidy_million = subsidy / 1e6
gdp_growth_million = gdp_growth_value / 1e6
profit_billion = profit_remaining / 1e6

# 找利润剩余 = 0 的临界 g
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 第一张图：三条线
fig, ax = plt.subplots(figsize=(10, 6))
l1, = ax.plot(g, subsidy_million, linestyle='--', label="补贴额（百万元）")
l2, = ax.plot(g, profit_billion, linestyle='-.', label="利润剩余（百万元）")
l3, = ax.plot(g, gdp_growth_million, linestyle=':', label="GDP增长值（百万元）")
ax.set_xlabel("g（补贴率）", fontproperties=font_prop)
ax.set_ylabel("金额", fontproperties=font_prop)
ax.legend(loc='upper left', prop=font_prop)
ax.grid(True)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x:.1f}"))
if g_zero:
    ax.axvline(x=g_zero, color='gray', linestyle=':', linewidth=1)
    ax.text(g_zero, ax.get_ylim()[1], f"g ≈ {g_zero:.3f}", rotation=0, ha='center', va='bottom',
    color='black', fontproperties=font_prop)

plt.tight_layout()
plt.show()

# 第二张图：面积堆叠图（利润剩余占比 vs GDP增长率）
subsidy = 3028433893.11489 * g *12
profit_remaining = 535000000 - subsidy
gdp_growth_value = 3.54 * subsidy

# 临界点
zero_idx = np.argmax(profit_remaining < 0)
g_zero = g[zero_idx] if zero_idx > 0 else None

# 比例和增速换算
profit_ratio = profit_remaining / 535000000 * 100  # %
gdp_growth_rate = gdp_growth_value / 126058200000000 * 100  # %

# 限定范围
profit_ratio_clipped = np.clip(profit_ratio, 0, 100)
gdp_growth_rate_clipped = np.clip(gdp_growth_rate, 0, 0.2)

# 绘图
fig, ax1 = plt.subplots(figsize=(10, 6))
p1 = ax1.fill_between(g, profit_ratio_clipped, label="利润剩余占比", hatch='////', facecolor='none', edgecolor='black')
ax1.set_ylabel("利润剩余占比（%）", fontproperties=font_prop)
ax1.set_ylim(0, 100)

ax2 = ax1.twinx()
p2 = ax2.fill_between(g, gdp_growth_rate_clipped, label="GDP增长率", hatch='\\\\', facecolor='none', edgecolor='blue')
ax2.set_ylabel("GDP增长率（%）", fontproperties=font_prop)
ax2.set_ylim(0, 0.2)
ax1.set_xlabel("g（补贴率）", fontproperties=font_prop)


if g_zero:
    ax1.axvline(x=g_zero, color='gray', linestyle='--', linewidth=1) 
    gdp_at_g_zero = gdp_growth_rate_clipped[np.argmin(np.abs(g - g_zero))]
    ax2.text(g_zero, gdp_at_g_zero, f"g = {g_zero:.3f}\nGDP增长率 ≈ {gdp_at_g_zero:.4f}%",
             rotation=0, ha='left', va='bottom', color='black', fontproperties=font_prop, 
             backgroundcolor='white', fontsize=12, fontweight='bold')


handles = [p1, p2]
labels = [h.get_label() for h in handles]
ax1.legend(handles, labels, loc='upper left', prop=font_prop)

plt.xlabel("g（补贴率）", fontproperties=font_prop)
plt.grid(True)
plt.tight_layout()
plt.show()
