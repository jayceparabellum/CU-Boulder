####As an alternative approach, let's train a Linear Discriminant Analysis (LDA) model and compare its performance.

# Grade Cell: Question 10
#
# Task: Train an LDA model and evaluate its accuracy.
#
# Instructions:
# 1. Initialize a `LinearDiscriminantAnalysis` model.
# 2. Train the model on the scaled training data.
# 3. Make predictions on the scaled test data.
# 4. Calculate the accuracy and store it in `accuracy_lda`.

lda = LinearDiscriminantAnalysis()

lda.fit(X_train_scaled, y_train)

y_pred_lda = lda.predict(X_test_scaled)

accuracy_lda = accuracy_score(y_test, y_pred_lda)

print(f"LDA Model Accuracy: {accuracy_lda:.4f}")
print(f"Baseline Logistic Regression Accuracy: {accuracy_baseline:.4f}")
