# Grade Cell: Question 5
#
# Task: Compute silhouette scores for different values of K
#
# Instructions:
# 1. Loop through K = 2 to 6 (silhouette requires at least 2 clusters)
# 2. Fit KMeans and get cluster labels
# 3. Compute silhouette_score for each K
# 4. Find the K with the highest score

q5_silhouette_scores: Dict[int, float] = {}
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    labels = km.fit_predict(q2_scaled_data)
    score = silhouette_score(q2_scaled_data, labels)
    q5_silhouette_scores[k] = round(float(score), 3)

q5_best_k_silhouette: int = max(q5_silhouette_scores, key=q5_silhouette_scores.get)

print(f"Silhouette scores: {q5_silhouette_scores}")
print(f"Best K by silhouette: {q5_best_k_silhouette}")
