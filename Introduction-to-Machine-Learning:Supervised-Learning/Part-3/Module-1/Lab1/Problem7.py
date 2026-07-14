7. Evaluate on Test Set (10 points)
Evaluate the trained model on the test set (using the scaled test features).

Store the results as a tuple q7_test_metrics = (test_loss, test_accuracy) with both values rounded to 3 decimals.

print(f"Test loss: {q7_test_metrics[0]}")
print(f"Test accuracy: {q7_test_metrics[1]}")
test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)

q7_test_metrics: Tuple[float, float] = (
    round(float(test_loss), 3),
    round(float(test_accuracy), 3),
)

print(f"Test Loss: {test_loss:.3f}, Test Accuracy: {test_acc:.3f}")
