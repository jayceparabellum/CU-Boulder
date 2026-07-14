# Grade Cell: Question 4
#
# Task: Implement the elbow method to find optimal K
#
# Instructions:
# 1. Loop through K = 1 to 10
# 2. Fit KMeans with each K and record inertia
# 3. Use random_state=RANDOM_STATE and n_init=10 for consistency
# 4. Identify the elbow point (where inertia stops decreasing rapidly)

q4_inertias: List[float] = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=10)
    km.fit(q2_scaled_data)
    q4_inertias.append(float(km.inertia_))

q4_elbow_k: int = 3

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), q4_inertias, marker="o")
plt.axvline(q4_elbow_k, color="red", linestyle="--", label=f"Elbow at K={q4_elbow_k}")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.legend()
plt.tight_layout()
plt.show()

print(f"Inertias: {[round(v, 2) for v in q4_inertias]}")
print(f"Elbow at K = {q4_elbow_k}")
