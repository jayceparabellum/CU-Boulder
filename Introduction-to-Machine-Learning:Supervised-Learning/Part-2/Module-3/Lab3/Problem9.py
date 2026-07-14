# Grade Cell: Question 9
#
# Task: Analyze K-Means stability across different initializations
#
# Instructions:
# 1. Run KMeans with K=3, n_init=1 for 10 different random_state values (0-9)
# 2. Record the inertia from each run
# 3. Compute mean and std of inertias
# 4. Determine if results are stable (low coefficient of variation)

q9_inertias: List[float] = []
for rs in range(10):
    km = KMeans(n_clusters=3, random_state=rs, n_init=1)
    km.fit(q2_scaled_data)
    q9_inertias.append(float(km.inertia_))

q9_mean_inertia: float = round(float(np.mean(q9_inertias)), 2)
q9_std_inertia: float = round(float(np.std(q9_inertias)), 2)

q9_is_stable: bool = bool((np.std(q9_inertias) / np.mean(q9_inertias)) < 0.05)

print(f"Inertias from 10 runs: {q9_inertias}")
print(f"Mean inertia: {q9_mean_inertia}")
print(f"Std inertia: {q9_std_inertia}")
print(f"Coefficient of variation: {q9_std_inertia/q9_mean_inertia*100:.2f}%")
print(f"Is stable (CV < 5%): {q9_is_stable}")
