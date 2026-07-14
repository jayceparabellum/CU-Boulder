# Grade Cell: Question 6
#
# Task: Choose the optimal K and justify your decision
#
# Instructions:
# 1. Consider evidence from both elbow method and silhouette analysis
# 2. Choose a K value and explain why
# 3. Compute final inertia and silhouette for your chosen K

q6_chosen_k: int = 3

q6_justification: str = (
    "The elbow method shows inertia bends at K=3, and the Iris data has 3 true "
    "species. While silhouette may slightly favor K=2 (setosa separates cleanly "
    "while versicolor and virginica overlap), K=3 best matches the known structure "
    "and balances both sources of evidence."
)

km_final = KMeans(n_clusters=q6_chosen_k, random_state=RANDOM_STATE, n_init=10)
final_labels = km_final.fit_predict(q2_scaled_data)

q6_final_inertia: float = round(float(km_final.inertia_), 2)
q6_final_silhouette: float = round(float(silhouette_score(q2_scaled_data, final_labels)), 3)

print(f"Chosen K: {q6_chosen_k}")
print(f"Justification: {q6_justification}")
print(f"Final inertia: {q6_final_inertia}")
print(f"Final silhouette: {q6_final_silhouette}")
