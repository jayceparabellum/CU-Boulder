####Now it's time to train our first classification model. You will use LogisticRegression from Scikit-learn to build a baseline model.


# Grade Cell: Question 4
#
# Task: Train a baseline logistic regression model.
#
# Instructions:
# 1. Initialize a `LogisticRegression` model, setting `random_state` to `RANDOM_STATE`.
# 2. Train the model using the scaled training data (`X_train_scaled`, `y_train`).
# 3. Store the trained model in a variable called `log_reg_baseline`.

log_reg_baseline = LogisticRegression (random_state=RANDOM_STATE)
log_reg_baseline.fit(X_train_scaled, y_train)
print("Baseline model training successful!")
