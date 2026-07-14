# Grade Cell: Question 7
#
# Task: Standardize the data using StandardScaler
#
# Instructions:
# 1. Create a StandardScaler instance
# 2. Fit and transform the data
# 3. Convert back to DataFrame with original index and columns
# 4. Compute means and stds of the scaled data (should be ~0 and ~1)

scaler = StandardScaler()

scaled_array = scaler.fit_transform(df)

q7_scaled_data = q7_scaled_data = pd.DataFrame(scaled_array, index=df.index, columns=df.columns)

q7_scaled_means: Dict[str, float] = {
    col: round(float(q7_scaled_data[col].mean()), 2) for col in q7_scaled_data.columns
}
q7_scaled_stds: Dict[str, float] = {
    col: round(float(q7_scaled_data[col].std(ddof=0)), 2) for col in q7_scaled_data.columns
}

print(f"Scaled means (should be ~0): {q7_scaled_means}")
print(f"Scaled stds (should be ~1): {q7_scaled_stds}")
