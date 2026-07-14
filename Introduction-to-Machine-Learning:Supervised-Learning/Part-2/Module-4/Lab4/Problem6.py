6. Cut Dendrogram to Extract Clusters (10 points)
To obtain a specific number of clusters, we "cut" the dendrogram at a chosen height. All branches below the cut belong to the same cluster.

Use scipy's fcluster() function to cut the dendrogram and extract cluster assignments. We'll use the complete linkage dendrogram and cut it to get exactly 3 clusters (matching the known iris species).

Store the results as:

q6_labels: A numpy array of cluster labels (1-indexed) for each sample
q6_n_clusters: The number of unique clusters (should be 3)
q6_cluster_counts: A dictionary mapping cluster label to sample count
# Grade Cell: Question 6
#
# Task: Cut the dendrogram to extract cluster assignments
#
# Instructions:
# 1. Use scipy.cluster.hierarchy.fcluster() to cut the dendrogram
# 2. Use criterion='maxclust' to specify the number of clusters
# 3. Set t=3 to get 3 clusters
# 4. Count samples per cluster
​
q6_labels = fcluster(q3_linkage_matrix, t=3, criterion="maxclust")
​
q6_n_clusters: int = len(np.unique(q6_labels))
​
unique, counts = np.unique(q6_labels, return_counts=True)
q6_cluster_counts: Dict[int, int] = {int(u): int(c) for u, c in zip(unique, counts)}
​
print(f"Number of clusters: {q6_n_clusters}")
print(f"Cluster counts: {q6_cluster_counts}")
