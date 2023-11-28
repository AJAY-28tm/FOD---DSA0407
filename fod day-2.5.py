import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# Creating a sample DataFrame
np.random.seed(42)  
control_group = np.random.normal(loc=50, scale=10, size=50)
treatment_group = np.random.normal(loc=55, scale=10, size=50)

data = pd.DataFrame({
    'Control': control_group,
    'Treatment': treatment_group
})
data.head()
# Visualizing the data using boxplots
data.boxplot(column=['Control', 'Treatment'])
plt.ylabel('Value')
plt.title('Boxplot of Control and Treatment Groups')
plt.show()
# Performing a two-sample t-test
t_stat, p_value = stats.ttest_ind(data['Control'], data['Treatment'])
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")
# Visualizing the p-value
plt.bar(0, p_value, align='center', alpha=0.5)
plt.xticks([0], ['P-value'])
plt.ylabel('P-value')
plt.title('P-value of the Two-Sample T-test')
plt.show()
