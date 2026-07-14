# Grade Cell: Question 2
#
# Task: Standardize the data using StandardScaler
#
# Instructions:
# 1. Create a StandardScaler instance
# 2. Fit and transform the data (df.values or df as input)
# 3. Compute the column means and stds of the scaled data to verify

scaler = StandardScaler()

q2_scaled_data = scaler.fit_transform(df.values)

q2_scaled_means = q2_scaled_data.mean(axis=0)
q2_scaled_stds = q2_scaled_data.std(axis=0, ddof=0)

print(f"Scaled data shape: {q2_scaled_data.shape}")
print(f"Scaled means (should be ~0): {q2_scaled_means}")
print(f"Scaled stds (should be ~1): {q2_scaled_stds}")
