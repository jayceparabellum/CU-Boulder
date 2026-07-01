####With a trained model, you can now make predictions and evaluate its performance using key classification metrics.


# Grade Cell: Question 5
#
# Task: Make predictions and calculate performance metrics.
#
# Instructions:
# 1. Use the baseline model to make predictions on the scaled test data. Store them in `y_pred_baseline`.
# 2. Calculate accuracy, precision, recall, and F1-score. Store them in `accuracy_baseline`, `precision_baseline`, `recall_baseline`, and `f1_baseline`.

y_pred_baseline = log_reg_baseline.predict(X_test_scaled)

accuracy_baseline = accuracy_score(y_test, y_pred)
precision_baseline = precision_score(y_test, y_pred)
recall_baseline = recall_score(y_test, y_pred)
f1_baseline = f1_score(y_test, y_pred)

print(f"Accuracy:  {accuracy_baseline:.4f}")
print(f"Precision: {precision_baseline:.4f}")
print(f"Recall:    {recall_baseline:.4f}")
print(f"F1 Score:  {f1_baseline:.4f}")
