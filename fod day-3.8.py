import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)
n_samples = 100
car_data = pd.DataFrame({
    'mpg': np.random.uniform(10, 40, n_samples),
    'horsepower': np.random.uniform(80, 300, n_samples),
    'weight': np.random.uniform(2000, 5000, n_samples),
    'acceleration': np.random.uniform(5, 20, n_samples),
    'origin': np.random.choice(['USA', 'Europe', 'Japan'], n_samples)
})
print(car_data.head())
plt.figure(figsize=(10, 6))
sns.scatterplot(x='horsepower', y='mpg', hue='acceleration', size='weight', data=car_data, palette='viridis')
plt.title('Multivariate Scatterplot')
plt.show()

sns.set(style="ticks")
sns.pairplot(car_data, vars=['mpg', 'horsepower', 'weight', 'acceleration'], hue='origin', palette='viridis')
plt.suptitle("Scatter Plot Matrix", y=1.02)
plt.show()
