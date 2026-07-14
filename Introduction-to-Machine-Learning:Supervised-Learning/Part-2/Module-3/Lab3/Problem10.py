# Grade Cell: Question 10
#
# Task: Implement a reusable clustering analysis function
#
# Instructions:
# 1. Create a function that takes data and K as inputs
# 2. Fit KMeans and compute labels, inertia, and silhouette score
# 3. Return results as a dictionary
# 4. Test with K=3 and K=4


def q10_cluster_analysis(data, k: int) -> Dict:
    """Fit K-Means with the given k and return labels, inertia, silhouette, and cluster sizes."""
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    labels = km.fit_predict(data)

    # Count samples per cluster
    unique, counts = np.unique(labels, return_counts=True)
    cluster_sizes = {int(u): int(c) for u, c in zip(unique, counts)}

    return {
        "k": k,
        "labels": labels,
        "inertia": round(float(km.inertia_), 2),
        "silhouette": round(float(silhouette_score(data, labels)), 3),
        "cluster_sizes": cluster_sizes,
    }

q10_result_k3: Dict = q10_cluster_analysis(q2_scaled_data, 3)
q10_result_k4: Dict = q10_cluster_analysis(q2_scaled_data, 4)

q10_better_k: int = 3 if q10_result_k3["silhouette"] >= q10_result_k4["silhouette"] else 4

print("K=3 results:")
print(f"  Inertia: {q10_result_k3['inertia']}")
print(f"  Silhouette: {q10_result_k3['silhouette']}")
print(f"  Cluster sizes: {q10_result_k3['cluster_sizes']}")
print("\nK=4 results:")
print(f"  Inertia: {q10_result_k4['inertia']}")
print(f"  Silhouette: {q10_result_k4['silhouette']}")
print(f"  Cluster sizes: {q10_result_k4['cluster_sizes']}")
print(f"\nBetter K by silhouette: {q10_better_k}")
