####To evaluate the model's performance on unseen data, we must split the dataset into training and testing sets. We will also scale the features, which is crucial for distance-based and optimization-based algorithms like Logistic Regression and LDA.


# Grade Cell: Question 3
#
# Task: Split and scale the data.
#
# Instructions:
# 1. Split `X` and `y` into `X_train`, `X_test`, `y_train`, and `y_test` with a `test_size` of 0.2 and `random_state=RANDOM_STATE`.
# 2. Initialize a `StandardScaler` and fit it on `X_train`.
# 3. Transform both `X_train` and `X_test` using the fitted scaler, naming them `X_train_scaled` and `X_test_scaled`.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Data splitting and scaling successful!")
