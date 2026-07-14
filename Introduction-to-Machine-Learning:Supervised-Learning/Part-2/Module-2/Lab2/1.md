3. Standardize the Data (10 points)
As we saw in Question 2, features have vastly different scales (e.g., proline ranges from ~280 to ~1680, while hue ranges from ~0.5 to ~1.7). Without standardization, proline would dominate PCA because it has the largest variance.

Apply z-score standardization to the data:
𝑧𝑗=𝑥𝑗−𝜇𝑗𝜎𝑗
 

Use sklearn.preprocessing.StandardScaler to standardize all features.

Store the results as:

q3_scaled_data: A numpy array of the standardized data
q3_scaled_means: A numpy array of column means of the scaled data (should all be ~0)
q3_scaled_stds: A numpy array of column stds of the scaled data (should all be ~1)


# Grade Cell: Question 3
#
# Task: Standardize the data using StandardScaler
#
# Instructions:
# 1. Create a StandardScaler instance
# 2. Fit and transform the data (df.values or df as input)
# 3. Compute the column means and stds of the scaled data to verify

scaler = StandardScaler()

q3_scaled_data = scaler.fit_transform(df.values)

q3_scaled_means = q3_scaled_data.mean(axis=0)
q3_scaled_stds = q3_scaled_data.std(axis=0, ddof=0)

print(f"Scaled data shape: {q3_scaled_data.shape}")
print(f"Scaled means (should be ~0): {q3_scaled_means}")
print(f"Scaled stds (should be ~1): {q3_scaled_stds}")
