# Grade Cell: Question 3
#
# Task: Fit a K-Means model with K=3 clusters
#
# Instructions:
# 1. Create a KMeans instance with n_clusters=3, random_state=RANDOM_STATE, n_init=10
# 2. Fit the model to q2_scaled_data
# 3. Get the cluster labels from .labels_
# 4. Get the inertia from .inertia_
# 5. Count samples per cluster

q3_kmeans = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init=10)
q3_kmeans.fit(q2_scaled_data)

q3_labels = q3_kmeans.labels_
q3_inertia: float = round(float(q3_kmeans.inertia_), 2)

unique, counts = np.unique(q3_labels, return_counts=True)
q3_cluster_counts: Dict[int, int] = {int(u): int(c) for u, c in zip(unique, counts)}

print(f"Cluster labels: {q3_labels[:10]}... (first 10)")
print(f"Inertia: {q3_inertia}")
print(f"Samples per cluster: {q3_cluster_counts}")
