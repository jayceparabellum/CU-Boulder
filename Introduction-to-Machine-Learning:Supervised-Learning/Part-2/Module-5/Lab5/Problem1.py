1. Load and Explore the Ratings Dataset (10 points)
Load the ratings data from ratings.csv. This file contains user-movie ratings in long format with columns: user_id, movie_id, rating.

Each row represents one rating that a user gave to a movie. Most user-movie combinations are missing (not rated), which is typical of recommender system data.

Store the following in the required variables:

q1_df: The loaded DataFrame
q1_n_ratings: Total number of ratings (rows in the DataFrame)
q1_n_users: Number of unique users
q1_n_movies: Number of unique movies
q1_rating_range: A tuple containing (min_rating, max_rating)


# Grade Cell: Question 1
#
# Task: Load the ratings dataset and explore its structure
#
# Instructions:
# 1. Read the CSV file using pd.read_csv()
# 2. Count total ratings, unique users, and unique movies
# 3. Find the minimum and maximum rating values




​
q1_df = pd.read_csv(_DATA_PATH)
​
q1_n_ratings: int = len(q1_df)
q1_n_users: int = q1_df["user_id"].nunique()
q1_n_movies: int = q1_df["movie_id"].nunique()
​
q1_rating_range: Tuple[float, float] = (
    float(q1_df["rating"].min()),
    float(q1_df["rating"].max()),
)
​
print(f"Total ratings: {q1_n_ratings}")
print(f"Unique users: {q1_n_users}")
print(f"Unique movies: {q1_n_movies}")
print(f"Rating range: {q1_rating_range}")
