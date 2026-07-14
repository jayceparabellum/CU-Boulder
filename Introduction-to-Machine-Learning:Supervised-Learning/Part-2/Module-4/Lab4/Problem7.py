7. Cluster Profiling (10 points)
To interpret clusters, we compute the mean of each feature within each cluster. This helps us understand what makes each cluster distinct.

Profile the hierarchical clusters by computing feature means per cluster.

Store the results as:

q7_cluster_means: A DataFrame with clusters as rows and features as columns
q7_largest_cluster: The cluster label with the most samples
q7_cluster_1_dominant_feature: The feature name where cluster 1 has the highest mean
# Grade Cell: Question 7
#
# Task: Profile clusters by computing feature means
#
# Instructions:
# 1. Create a DataFrame with standardized data and cluster labels
# 2. Group by cluster and compute mean of each feature
# 3. Find the largest cluster and the dominant feature for cluster 1
​
scaled_df = pd.DataFrame(q2_scaled_data, columns=q1_columns)
scaled_df["cluster"] = q6_labels
​
q7_cluster_means = scaled_df.groupby("cluster").mean()
​
q7_largest_cluster: int = int(pd.Series(q6_labels).value_counts().idxmax())
​
q7_cluster_1_dominant_feature: str = q7_cluster_means.loc[1].idxmax()
​
print("Cluster means (standardized scale):")
print(q7_cluster_means.round(2))
print(f"\nLargest cluster: {q7_largest_cluster}")
print(f"Cluster 1 dominant feature: {q7_cluster_1_dominant_feature}")
