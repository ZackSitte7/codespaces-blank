import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# 读取标准化后的平均值数据
standardized_averages_df = pd.read_csv('./standardized_averages.csv')

# 设置Seaborn的样式
sns.set()

# 生成热图
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(standardized_averages_df.set_index('diet_group'), annot=True, fmt=".2f", cmap='coolwarm')

# 设置标题
plt.title('Heatmap of Standardized Averages by Diet Group')

# 显示图表
plt.show()
