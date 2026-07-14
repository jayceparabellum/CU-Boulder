10. Reusable Hierarchical Clustering Function (10 points)
Create a reusable function that performs hierarchical clustering and returns comprehensive results including the linkage matrix, cluster labels, and cluster statistics.

Store the results as:

q10_hierarchical_analysis: The function you implement
q10_result_complete: Result of calling the function with complete linkage
q10_result_average: Result of calling the function with average linkage
q10_better_linkage: Which linkage produces more balanced clusters ("complete" or "average")
# Grade Cell: Question 10
#
# Task: Implement a reusable hierarchical clustering analysis function
#
# Instructions:
# 1. Create a function that takes data, n_clusters, and linkage method as inputs
# 2. Compute linkage matrix and extract cluster labels
# 3. Return results as a dictionary
# 4. Test with complete and average linkage
​
​
def q10_hierarchical_analysis(data, n_clusters: int = 3, method: str = "complete") -> Dict:
    """Run hierarchical clustering and return linkage, labels, and cluster stats."""
    Z = linkage(data, method=method)
    labels = fcluster(Z, t=n_clusters, criterion="maxclust")
​
    unique, counts = np.unique(labels, return_counts=True)
    cluster_sizes = {int(u): int(c) for u, c in zip(unique, counts)}
​
    return {
        "method": method,
        "n_clusters": n_clusters,
        "linkage_matrix": Z,
        "labels": labels,
        "cluster_sizes": cluster_sizes,
        "max_distance": round(float(Z[-1, 2]), 2),
    }
​
q10_result_complete: Dict = q10_hierarchical_analysis(q2_scaled_data, n_clusters=3, method="complete")
q10_result_average: Dict = q10_hierarchical_analysis(q2_scaled_data, n_clusters=3, method="average")
​
# More balanced = smaller spread in cluster sizes (lower std of the counts)
std_complete = np.std(list(q10_result_complete["cluster_sizes"].values()))
std_average = np.std(list(q10_result_average["cluster_sizes"].values()))
q10_better_linkage: str = "complete" if std_complete <= std_average else "average"
​
print("Complete linkage results:")
print(f"  Max distance: {q10_result_complete['max_distance']}")
print(f"  Cluster sizes: {q10_result_complete['cluster_sizes']}")
print("\nAverage linkage results:")
print(f"  Max distance: {q10_result_average['max_distance']}")
print(f"  Cluster sizes: {q10_result_average['cluster_sizes']}")
print(f"\nMore balanced clusters: {q10_better_linkage}")
