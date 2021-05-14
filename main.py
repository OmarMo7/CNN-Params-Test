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
