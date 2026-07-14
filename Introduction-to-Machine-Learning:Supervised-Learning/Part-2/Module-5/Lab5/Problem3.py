3. Center the Rating Matrix (10 points)
Before applying matrix completion, we need to center the data by subtracting the mean rating for each movie (column mean). This removes the baseline popularity of movies and focuses on deviations.

Important: When computing column means, only use observed (non-NaN) values. Then subtract these means from the observed values.

Store the results as:

q3_movie_means: A numpy array of length n_movies with each movie's mean rating
q3_centered_matrix: The centered rating matrix (still has NaN for missing)
q3_centered_mean: The overall mean of the centered observed values (should be ~0)
# Grade Cell: Question 3
#
# Task: Center the rating matrix by movie means
#
# Instructions:
# 1. Compute the mean of each column, ignoring NaN values (use np.nanmean)
# 2. Subtract these means from the observed values
# 3. Verify that the centered matrix has mean ~0
​
q3_movie_means = np.nanmean(q2_rating_matrix, axis=0)
​
q3_centered_matrix = q2_rating_matrix - q3_movie_means
​
q3_centered_mean: float = float(np.nanmean(q3_centered_matrix))
​
print(f"Movie means (first 5): {q3_movie_means[:5].round(2)}")
print(f"Centered mean: {q3_centered_mean}")
