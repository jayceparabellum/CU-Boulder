# Grade Cell: Question 7
#
# Task: Profile clusters by computing feature means
#
# Instructions:
# 1. Fit KMeans with your chosen K (q6_chosen_k)
# 2. Add cluster labels to a copy of the original data
# 3. Compute mean of each feature per cluster
# 4. Identify the largest cluster and the dominant feature for cluster 0

km = KMeans(n_clusters=q6_chosen_k, random_state=RANDOM_STATE, n_init=10)
labels = km.fit_predict(q2_scaled_data)

scaled_df = pd.DataFrame(q2_scaled_data, columns=q1_columns)
scaled_df["cluster"] = labels

q7_cluster_means = scaled_df.groupby("cluster").mean()

q7_largest_cluster: int = int(pd.Series(labels).value_counts().idxmax())

q7_cluster_0_dominant_feature: str = q7_cluster_means.loc[0].idxmax()

print("Cluster means (standardized scale):")
print(q7_cluster_means.round(2))
print(f"\nLargest cluster: {q7_largest_cluster}")
print(f"Cluster 0 dominant feature: {q7_cluster_0_dominant_feature}")
