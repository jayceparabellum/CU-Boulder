####Train a DecisionTreeClassifier and evaluate accuracy and confusion matrix.


# Grade Cell: Question 5
#
# Task: Train classification tree and evaluate.
#
# Instructions:
# 1. Split df_cls into X_cls, y_cls; then stratified train/test with test_size=0.25, random_state=RANDOM_STATE.
# 2. Fit DecisionTreeClassifier(criterion='gini', random_state=RANDOM_STATE) as tree_cls.
# 3. Compute `acc_tree_cls` and `conf_mat_tree_cls` on TEST.


def split_classification_data():
    X = df_cls.drop(columns=["target"])
    y = df_cls["target"]
    return train_test_split(X, y, test_size=0.2, random_state=RANDOM_STATE)

X_train_cls, X_test_cls, y_train_cls, y_test_cls = split_classification_data()
print(f"Train: {X_train_cls.shape}, Test: {X_test_cls.shape}")

X_cls = df_cls.drop(columns=["target"])
y_cls = df_cls["target"]

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_cls, y_cls, test_size=0.2, random_state=RANDOM_STATE
)

tree_cls = DecisionTreeClassifier(random_state=RANDOM_STATE)
tree_cls.fit(X_train_c, y_train_c)

y_pred_c = tree_cls.predict(X_test_c)

acc_tree_cls = accuracy_score(y_test_c, y_pred_c)
conf_mat_tree_cls = confusion_matrix(y_test_c, y_pred_c)

print(f"Test accuracy: {acc_tree_cls:.3f}")
print("Confusion matrix:")
print(conf_mat_tree_cls)
