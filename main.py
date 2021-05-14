import numpy as np
from mlxtend.data import loadlocal_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical


def ExtractAndReshape(imagesPath, labelsPath):
    images, images_labels = loadlocal_mnist(
        images_path=imagesPath,
        labels_path=labelsPath)
    return images, images_labels


train_images, train_labels = ExtractAndReshape(
    "train-images.idx3-ubyte", "train-labels.idx1-ubyte")
test_images, test_labels = ExtractAndReshape(
    "t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte")


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


# Build the model.
model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='ReLU'),
])


# Compile the model.
model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

# Train the model.
model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
)
