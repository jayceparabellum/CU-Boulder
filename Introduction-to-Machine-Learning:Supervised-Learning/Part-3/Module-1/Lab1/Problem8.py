8. Manual Forward Pass Function (15 points)
To reinforce your understanding of neural network mathematics, implement a function that performs a forward pass manually using NumPy.

Implement manual_forward_pass(X: np.ndarray, weights: List) -> np.ndarray that:

Takes input data X (shape: n_samples × n_features)
Takes weights from model.get_weights() (a list of weight matrices and bias vectors)
Applies the forward pass through all layers:
For hidden layers: Z = X @ W + b, then A = ReLU(Z) where ReLU(x) = max(0, x)
For output layer: Z = A @ W + b, then output = sigmoid(Z)
Returns the final output probabilities
Store the predictions for the first 5 test samples in q8_manual_preds (shape: 5×1).

def manual_forward_pass(X: np.ndarray, weights: List) -> np.ndarray:
    """Perform a forward pass through the network manually using NumPy.

    Parameters
    ----------
    X : np.ndarray
        Input data, shape (n_samples, n_features).
    weights : List
        Output of model.get_weights(): alternating [W1, b1, W2, b2, W3, b3].

    Returns
    -------
    np.ndarray
        Output probabilities, shape (n_samples, 1).
    """
    A = np.asarray(X, dtype=float)

    n_layers = len(weights) // 2

    for layer in range(n_layers):
        W = weights[2 * layer]
        b = weights[2 * layer + 1]

        Z = A @ W + b

        if layer < n_layers - 1:
            # Hidden layer: ReLU
            A = np.maximum(0, Z)
        else:
            # Output layer: sigmoid
            A = 1.0 / (1.0 + np.exp(-Z))

    return A


q8_manual_preds = manual_forward_pass(X_test_scaled[:5], model.get_weights())

print(f"Manual predictions shape: {q8_manual_preds.shape}")
print(f"Manual predictions:\n{q8_manual_preds}")

keras_preds = model.predict(X_test_scaled[:5], verbose=0)
print(f"Manual forward pass predictions (first 5):\n{q8_manual_preds.flatten()}")
