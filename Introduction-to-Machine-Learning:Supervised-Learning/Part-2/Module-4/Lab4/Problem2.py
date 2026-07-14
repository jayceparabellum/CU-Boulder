2. Standardize the Data (10 points)
Just like with K-Means, standardization is crucial for hierarchical clustering because it uses distance calculations. Features with larger scales would dominate the distance calculations otherwise.

Apply z-score standardization to the data using StandardScaler:
𝑧𝑗=𝑥𝑗−𝜇𝑗𝜎𝑗
 

Store the results as:

q2_scaled_data: A numpy array of the standardized data
q2_scaled_means: A numpy array of column means of the scaled data (should all be ~0)
q2_scaled_stds: A numpy array of column stds of the scaled data (should all be ~1)
# Grade Cell: Question 2
#
# Task: Standardize the data using StandardScaler
#
# Instructions:
# 1. Create a StandardScaler instance
# 2. Fit and transform the data (df.values or df as input)
# 3. Compute the column means and stds of the scaled data to verify
​
scaler = StandardScaler()
​
q2_scaled_data = scaler.fit_transform(df.values)
​
q2_scaled_means = q2_scaled_data.mean(axis=0)
q2_scaled_stds = q2_scaled_data.std(axis=0, ddof=0)
​
print(f"Scaled data shape: {q2_scaled_data.shape}")
print(f"Scaled means (should be ~0): {q2_scaled_means}")
print(f"Scaled stds (should be ~1): {q2_scaled_stds}")
