####The ROC curve illustrates the diagnostic ability of a classifier as its discrimination threshold is varied. The Area Under the Curve (AUC) provides an aggregate measure of performance across all thresholds.

Note: For autograding, only the computed roc_auc_baseline variable will be checked, not the plot itself.


# Grade Cell: Question 7
#
# Task: Generate the ROC curve for the baseline model.
#
# Instructions:
# 1. Get the prediction probabilities for the positive class.
# 2. Compute the false positive rate (`fpr`), true positive rate (`tpr`), and thresholds.
# 3. Calculate the Area Under the ROC Curve (`roc_auc_baseline`).
# 4. Plot the ROC curve.

y_proba_baseline = log_reg_baseline.predict_proba(X_test_scaled)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_proba_baseline)
roc_auc_baseline = auc(fpr, tpr)


plt.figure(figsize=(7, 6))
plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {roc_auc_baseline:4f})")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random classifier")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Baseline Logistic Regression")
plt.legend(loc="lower right")
plt.show()
print(f"Baseline Model AUC: {roc_auc_baseline:.4f}")
