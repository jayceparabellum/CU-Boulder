9. Compare with K-Means (10 points)
Now let's compare hierarchical clustering results with K-Means. This helps us understand whether the two methods agree on the data structure.

Use the Adjusted Rand Index (ARI) to measure agreement between the two clusterings. ARI ranges from -1 to 1:

ARI = 1: Perfect agreement
ARI = 0: Random labeling
ARI < 0: Worse than random
Store the results as:

q9_kmeans: A fitted KMeans object with K=3
q9_kmeans_labels: Cluster labels from K-Means (0-indexed)
q9_ari_score: Adjusted Rand Index comparing hierarchical and K-Means (rounded to 3 decimals)
q9_agreement: String indicating agreement level ("high", "moderate", or "low")
# Grade Cell: Question 9
#
# Task: Compare hierarchical clustering with K-Means
#
# Instructions:
# 1. Fit KMeans with n_clusters=3, random_state=RANDOM_STATE, n_init=10
# 2. Get the cluster labels
# 3. Compute the Adjusted Rand Index between hierarchical (q6_labels) and K-Means
# 4. Determine agreement level: "high" if ARI > 0.7, "moderate" if 0.4-0.7, "low" if < 0.4
​
q9_kmeans = KMeans(n_clusters=3, random_state=RANDOM_STATE, n_init=10)
q9_kmeans_labels = q9_kmeans.fit_predict(q2_scaled_data)
​
q9_ari_score: float = round(float(adjusted_rand_score(q6_labels, q9_kmeans_labels)), 3)
​
if q9_ari_score > 0.7:
    q9_agreement: str = "high"
elif q9_ari_score >= 0.4:
    q9_agreement: str = "moderate"
else:
    q9_agreement: str = "low"
​
print(f"ARI score: {q9_ari_score}")
print(f"Agreement level: {q9_agreement}")
