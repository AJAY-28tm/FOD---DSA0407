
import numpy as np
from scipy import stats
np.random.seed(42)
sample_revenue = np.random.normal(loc=50, scale=10, size=100)  
sample_mean = np.mean(sample_revenue)
standard_error = stats.sem(sample_revenue)
confidence_level = 0.95

degrees_of_freedom = len(sample_revenue) - 1
confidence_interval = stats.t.interval(confidence_level, degrees_of_freedom, loc=sample_mean, scale=standard_error)

print(f"Sample Mean: {sample_mean}")
print(f"Confidence Interval ({confidence_level*100}%): {confidence_interval}")
