import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42) 
data = pd.DataFrame({
    'temperature': np.random.randint(60, 100, 365),
    'rainfall': np.random.uniform(0, 10, 365)
})
print(data.head())
correlation_coefficient = data['temperature'].corr(data['rainfall'])
print(f'Correlation Coefficient: {correlation_coefficient}')
plt.figure(figsize=(10, 6))
plt.scatter(data['temperature'], data['rainfall'], alpha=0.5)
plt.title('Temperature vs Rainfall')
plt.xlabel('Temperature (°F)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
