6. Plot Training Curves (10 points)
Create a figure with two subplots side by side:

Left subplot: Training and validation loss over epochs
Right subplot: Training and validation accuracy over epochs
Both plots should include:

X-axis label: "Epoch"
Y-axis labels: "Loss" and "Accuracy" respectively
Legend showing "Train" and "Validation"
Store the matplotlib figure object in q6_fig.

Note: Looking at these curves helps identify overfitting (when validation loss increases while training loss continues to decrease).

q6_fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(history.history["loss"], label="Train")
axes[0].plot(history.history["val_loss"], label="Validation")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].set_title("Loss over Epochs")
axes[0].legend()

axes[1].plot(history.history["accuracy"], label="Train")
axes[1].plot(history.history["val_accuracy"], label="Validation")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].set_title("Accuracy over Epochs")
axes[1].legend()

plt.tight_layout()
plt.show()

print("Training curves plotted successfully!")
