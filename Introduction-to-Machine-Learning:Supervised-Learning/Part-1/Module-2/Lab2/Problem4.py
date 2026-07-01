model = LinearRegression()
model.fit(X_train, y_train)

model = LinearRegression().fit(X_train, y_train)

print(f"Model trained successfully with {len(model.coef_)} coefficients")
