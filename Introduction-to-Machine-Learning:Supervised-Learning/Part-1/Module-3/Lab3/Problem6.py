#####The confusion matrix provides a detailed breakdown of correct and incorrect classifications, which is essential for understanding a model's performance beyond a single accuracy score.

#####Note: For autograding, only the computed conf_matrix_baseline variable will be checked, not the plot itself.



# Grade Cell: Question 6
#
# Task: Compute and visualize the confusion matrix for the baseline model.
#
# Instructions:
# 1. Compute the confusion matrix using `y_test` and `y_pred_baseline`. Store it in `conf_matrix_baseline`.
# 2. Use `seaborn.heatmap` to visualize the confusion matrix.

conf_matrix_baseline = confusion_matrix(y_test, y_pred_baseline)

plt.figure(figsize =(6, 5))
sns.heatmap(
    conf_matrix_baseline,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Benign (0)","Malignant (1)"],
    yticklabels=["Benign (0)","Malignant (1)"],
)

print("Baseline confusion matrix computed successfully.")
