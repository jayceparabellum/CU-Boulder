#####Regularization is a technique to prevent overfitting by penalizing large model coefficients. You will now train a logistic regression model with L2 regularization.

log_reg_l2 = LogisticRegression(penalty="l2", C=0.1, random_state=RANDOM_STATE)
log_reg_l2.fit(X_train_scaled, y_train)

y_pred_l2 = log_reg_l2.predict(X_test_scaled)
accuracy_l2 = accuracy_score(y_test, y_pred_l2)

print(f"L2 Regularized Model Accuracy: {accuracy_l2:.4f}")
