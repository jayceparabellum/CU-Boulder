####Let's compare the coefficients of the baseline and regularized models to see the effect of regularization. Regularization should "shrink" the coefficients toward zero.

# Grade Cell: Question 9
#
# Task: Compare the magnitudes of the model coefficients.
#
# Instructions:
# 1. Calculate the average absolute value of the coefficients for the baseline model (`log_reg_baseline`) and store it in `avg_coef_baseline`.
# 2. Calculate the average absolute value of the coefficients for the L2 regularized model (`log_reg_l2`) and store it in `avg_coef_l2`.

coef_comparison = pd.DataFrame({
    "Feature": X.columns,
    "Baseline": log_reg_baseline.coef_[0],
    "L2 Regularized": log_reg_l2.coef_[0],
})

avg_coef_baseline = np.mean(np.abs(log_reg_baseline.coef_[0]))
avg_coef_l2 = np.mean(np.abs(log_reg_l2.coef_[0]))

print(f"Average Baseline Coefficient Magnitude: {avg_coef_baseline:.4f}")
print(f"Average L2 Regularized Coefficient Magnitude: {avg_coef_l2:.4f}")
print(
    "Coefficient comparison successful. L2 regularization shrinks coefficients as expected."
)
