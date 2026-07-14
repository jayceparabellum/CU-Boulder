2. Create Rating Matrix and Compute Sparsity (10 points)
Convert the long-format ratings to a rating matrix where:

Rows represent users (user_id)
Columns represent movies (movie_id)
Each cell contains the rating, or NaN if the user hasn't rated that movie
Then compute the sparsity of the matrix, which is the fraction of entries that are missing.





Store the results as:

q2_rating_matrix: A numpy array of shape (n_users, n_movies) with NaN for missing
q2_n_missing: Total number of missing entries (NaN values)
q2_sparsity: Fraction of entries that are missing (float, rounded to 3 decimals)
# Grade Cell: Question 2
#
# Task: Create the rating matrix and compute sparsity
#
# Instructions:
# 1. Initialize a matrix of NaN values with shape (n_users, n_movies)
# 2. Fill in the observed ratings from the DataFrame
# 3. Count NaN values and compute sparsity as n_missing / total_entries





​
user_ids = sorted(q1_df["user_id"].unique())
movie_ids = sorted(q1_df["movie_id"].unique())
user_to_idx = {uid: i for i, uid in enumerate(user_ids)}
movie_to_idx = {mid: j for j, mid in enumerate(movie_ids)}
​
q2_rating_matrix = np.full((q1_n_users, q1_n_movies), np.nan)
​
for row in q1_df.itertuples(index=False):
    i = user_to_idx[row.user_id]
    j = movie_to_idx[row.movie_id]
    q2_rating_matrix[i, j] = row.rating
​
q2_n_missing: int = int(np.isnan(q2_rating_matrix).sum())
total_entries = q2_rating_matrix.size
q2_sparsity: float = round(float(q2_n_missing / total_entries), 3)
​
print(f"Matrix shape: {q2_rating_matrix.shape}")
print(f"Missing entries: {q2_n_missing} of {total_entries}")
print(f"Sparsity: {q2_sparsity}")
