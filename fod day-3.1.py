import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# Generate a synthetic dataset (replace this with your actual dataset)
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'TotalAmountSpent': [100, 300, 150, 500, 200, 600, 350, 800, 400, 700],
    'FrequencyOfVisits': [2, 4, 3, 5, 2, 6, 4, 8, 3, 7]
}
df = pd.DataFrame(data)
# Select features for clustering
X = df[['TotalAmountSpent', 'FrequencyOfVisits']]
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose the number of clusters (you may need to tune this based on your data)
num_clusters = 3
# Build the K-Means model
kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans_model.fit_predict(X_scaled)
# Visualize the clusters
plt.scatter(df['TotalAmountSpent'], df['FrequencyOfVisits'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation with K-Means Clustering')
plt.show()
# Display the cluster centers
cluster_centers = scaler.inverse_transform(kmeans_model.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=['TotalAmountSpent', 'FrequencyOfVisits'])
print("Cluster Centers:")
print(cluster_centers_df)
