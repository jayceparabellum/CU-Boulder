9. Compare with Logistic Regression Baseline (15 points)
Train a LogisticRegression model (with max_iter=1000 and random_state=RANDOM_STATE) on the same scaled training data and evaluate it on the test set.

Store:

q9_logreg_acc: Test accuracy of logistic regression (float, rounded to 3 decimals)
q9_nn_better: Boolean indicating whether the neural network achieved higher test accuracy than logistic regression
Note: For simple datasets like this, logistic regression often performs comparably to neural networks. Neural networks shine with more complex, high-dimensional data.

print(f"Logistic regression test accuracy: {q9_logreg_acc}")
print(f"Neural network test accuracy: {nn_acc}")
print(f"Neural network better: {q9_nn_better}")
logreg = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
logreg.fit(X_train_scaled, y_train)

logreg_preds = logreg.predict(X_test_scaled)
q9_logreg_acc: float = round(float(accuracy_score(y_test, logreg_preds)), 3)

nn_acc = q7_test_metrics[1]

q9_nn_better: bool = bool(nn_acc > q9_logreg_acc)

print(f"Logistic Regression Test Accuracy: {q9_logreg_acc:.3f}")
print(f"Neural Network Test Accuracy: {q7_test_metrics[1]:.3f}")
print(f"Neural Network performed better: {q9_nn_better}")
