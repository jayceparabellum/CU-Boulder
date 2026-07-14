5. Compile and Train the Model (10 points)
Compile the model with:

Optimizer: 'adam'
Loss: 'binary_crossentropy'
Metrics: ['accuracy']
Train the model for 50 epochs with batch_size=32 using the training data and validation data. Set verbose=0 to suppress output.

Store the training history object in history and the final training accuracy (last epoch) in q5_final_train_acc (float, rounded to 3 decimals).


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

history = model.fit(
    X_train_scaled, y_train,
    validation_data=(X_val_scaled, y_val),
    epochs=50,
    batch_size=32,
    verbose=0,
)

q5_final_train_acc: float = round(float(history.history["accuracy"][-1]), 3)

print(f"Final training accuracy: {q5_final_train_acc:.3f}")
