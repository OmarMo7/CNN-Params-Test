import numpy as np
import mnist
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical


train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

# Normalize the images.
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

# Reshape the images.
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)


# Basic parameters
num_filters = 8
filter_size = 3
pool_size = 2

optimizer = keras.optimizers.Adagrad(
    learning_rate=0.05, name="Adagrad")


# Build the model.
model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(
        28, 28, 1), activation='relu'),
    MaxPooling2D(pool_size=pool_size),
    Conv2D(num_filters, filter_size, input_shape=(
        28, 28, 1), activation='relu'),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(128, activation='tanh'),
    Dense(64, activation='tanh'),
    Dense(32, activation='tanh'),
    Dense(10, activation='softmax'),
])

model.summary()

# Compile the model.
model.compile(
    optimizer=optimizer,
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

# Train the model.
model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=20,
    batch_size=32,
    validation_data=(test_images, to_categorical(test_labels)),
)


# Predict on the first 5 test images.
predictions = model.predict(test_images[:5])

# Print our model's predictions.
print(np.argmax(predictions, axis=1))  # [7, 2, 1, 0, 4]

# Check our predictions against the ground truths.
print(test_labels[:5])  # [7, 2, 1, 0, 4]
