6. Choose Number of Components (10 points)
How many components should we keep? Common approaches include:

Variance threshold: Keep enough components to explain a target amount (e.g., 80%) of variance
Scree plot elbow: Look for where variance drops off sharply
Find the minimum number of components needed to explain at least 80% of the variance.

Store the results as:

q6_threshold: The variance threshold we're using (0.8)
q6_n_components_80: The minimum number of components to explain ≥80% variance (integer)
q6_actual_variance: The actual variance explained by those components (float, rounded to 3 decimals)


# Grade Cell: Question 6
#
# Task: Find minimum components to explain 80% of variance
#
# Instructions:
# 1. Use the cumulative variance from Q5
# 2. Find the first index where cumulative variance >= 0.8
# 3. Remember: the number of components is index + 1

q6_threshold: float = 0.8

cumulative = np.cumsum(q4_explained_variance_ratio)

q6_n_components_80: int = int(np.argmax(cumulative >= q6_threshold)) + 1

q6_actual_variance: float = round(float(cumulative[q6_n_components_80 - 1]), 3)

print(f"Threshold: {q6_threshold*100:.0f}%")
print(f"Components needed: {q6_n_components_80}")
print(f"Actual variance explained: {q6_actual_variance*100:.1f}%")
