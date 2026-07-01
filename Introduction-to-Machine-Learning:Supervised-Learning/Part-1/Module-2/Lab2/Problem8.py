coefficients = pd.Series(model.coef_, index=FEATURE_COLUMNS)

q8_strongest_negative_feature: str = coefficients.idxmin()

print(f"Feature with most negative coefficient: {q8_strongest_negative_feature}")
