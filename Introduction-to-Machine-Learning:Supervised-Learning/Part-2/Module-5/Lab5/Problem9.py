9. Recommender System: Predict User Ratings (10 points)
Now let's use our completed matrix as a recommender system. Given a user and a movie they haven't rated, we can predict their rating.

Implement a function that:

Takes a user ID and movie ID
Returns the predicted rating (un-centered, on the original 1-5 scale)
Then use it to generate top-5 movie recommendations for a specific user.

Store the results as:

q9_predict_rating: A function that predicts ratings
q9_user_0_predictions: Dictionary of {movie_id: predicted_rating} for user 0's unrated movies
q9_top_5_movies: List of top 5 movie IDs recommended for user 0
# Grade Cell: Question 9
#
# Task: Build a recommender system using the completed matrix
#
# Instructions:
# 1. Create a function that looks up the completed value and un-centers it
# 2. For user 0, predict ratings for all unrated movies
# 3. Sort by predicted rating to get top recommendations




final_completed, _ = q6_complete_matrix(q3_centered_matrix, rank=5, max_iter=20)

def q9_predict_rating(user_id: int, movie_id: int, completed_matrix, movie_means) -> float:
    """Predict a user's rating for a movie on the original 1-5 scale."""
    i = user_to_idx[user_id]
    j = movie_to_idx[movie_id]
    prediction = completed_matrix[i, j] + movie_means[j]
    return float(np.clip(prediction, 1.0, 5.0))

user_id = 0
i = user_to_idx[user_id]

unrated_movies: List[int] = [
    int(movie_id)
    for movie_id, j in movie_to_idx.items()
    if np.isnan(q2_rating_matrix[i, j])
]

q9_user_0_predictions: Dict[int, float] = {
    m: q9_predict_rating(user_id, m, final_completed, q3_movie_means)
    for m in unrated_movies
}

q9_top_5_movies: List[int] = [
    int(m) for m in sorted(
        q9_user_0_predictions, key=q9_user_0_predictions.get, reverse=True
    )[:5]
]

print(f"User 0 has {len(unrated_movies)} unrated movies")
print(f"Top 5 recommendations: {q9_top_5_movies}")
for m in q9_top_5_movies:
    print(f"  Movie {m}: predicted {q9_user_0_predictions[m]:.2f}")
