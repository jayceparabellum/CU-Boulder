4. Build a Neural Network Model (10 points)
Using Keras, build a neural network with the following architecture:

Input shape: (n_features,) where n_features is from Question 2
Hidden Layer 1: 16 neurons with ReLU activation
Hidden Layer 2: 8 neurons with ReLU activation
Output Layer: 1 neuron with Sigmoid activation (for binary classification)
Store the model in a variable called model and the total number of trainable parameters in q4_n_params (an integer).

Hint: Use model.count_params() to get the parameter count.

print(f"Total trainable parameters: {q4_n_params}")
model = Sequential([
    Dense(16, activation="relu", input_shape=(q2_n_features,)),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid"),
])

q4_n_params: int = model.count_params()

model.summary()
print(f"Total trainable parameters: {q4_n_params}")
