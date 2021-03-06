> Link to github repository>> <https://github.com/OmarMo7/CNN-Params-Test>

# The Full Test Report

## Basic Initial Structure

---

- number of filters: 8
- filter size: 3
- pool size: 2
- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

- Model has three layers

  - Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer
- Epochs: 5
- Batch Size: 32

---

## Test 1

### Initial test with the basic structure

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4997
  - 0.9307
  - 0.9493
  - 0.9580
  - 0.9649
- Final accuracy: 0.9649

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   6ms 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

- Epochs: 5
- Batch size: 32
- Accuracy: 96.49%

**It's thought that the low learning rate of 0.01 had caused the model to result this accuracy**

## Test 2

### Testing with epochs of 15

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4832
  - 0.9255
  - 0.9493
  - 0.9589
  - 0.9644
- Final accuracy: 0.9805

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   6ms 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

- Epochs: 15
- Batch size: 32
- Accuracy: 98.05%

## Test 3

### Testing with epochs of 20

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4630
  - 0.9167
  - 0.9458
  - 0.9556
  - 0.9626
- Final accuracy: 0.9818

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   6ms 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

  - Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

- Epochs: 20
- Batch size: 32
- Accuracy: 98.18%

## Test 4

### Testing with learning rate of 0.05

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7443
  - 0.9674
  - 0.9767
  - 0.9801
  - 0.9817
- Final accuracy: 0.9926

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
- Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32
- Accuracy: 99.26%

## Test 5

### Testing with learning rate of 0.03

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7276
  - 0.9576
  - 0.9684
  - 0.9751
  - 0.9792
- Final accuracy: 0.9912

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

  - Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.03
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32
- Accuracy: 99.12%

## Test 6

### Testing with learning rate of 0.02

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.6619
  - 0.9513
  - 0.9664
  - 0.9722
  - 0.9754
- Final accuracy: 0.9902

2. The number of parameters in the model:.
   7,426

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

  - Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.02
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32
- Accuracy: 99.02%

## Test 7

### Testing with 2 CNN layers and 2 FC layers 32,16

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4893
  - 0.9256
  - 0.9493
  - 0.9596
  - 0.9657
- Final accuracy: 0.9796

2. The number of parameters in the model:.
   7,794

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 32 units and activation of _relu_

- Layer4: FCLayer with 16 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 97.96%

## Test 8

### Testing with 2 CNN layers and 2 FC layers 32,16 _0.05_

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7219
  - 0.9670
  - 0.9757
  - 0.9777
  - 0.9810
- Final accuracy: 0.9937

2. The number of parameters in the model:.
   7,794

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 32 units and activation of _relu_

- Layer4: FCLayer with 16 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.37%

## Test 9

### Testing with 2 CNN layers and 3 FC layers 128,64,32

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7668
  - 0.9724
  - 0.9803
  - 0.9852
  - 0.9869
- Final accuracy: 0.9977

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.77%

## Test 10

### Testing with 3 CNN layers and 3 FC layers 128,64,32

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.5757
  - 0.9366
  - 0.9512
  - 0.9576
  - 0.9630
- Final accuracy: 0.9786

2. The number of parameters in the model:.
   13,066

3. The average time to train in each epoch:.
   6s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer4: FCLayer with 128 units and activation of _relu_

- Layer5: FCLayer with 64 units and activation of _relu_

- Layer6: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 97.86%

**It's decided that the best layers sequence structure are: 3 CNN and 3 FC: 128,64,32**

## Test 11

### Testing with batch size of 64

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.6651
  - 0.9590
  - 0.9722
  - 0.9769
  - 0.9819
- Final accuracy: 0.9974

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   3s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 64
- Accuracy: 99.74%

## Test 12

### Testing with batch size of 128

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4847
  - 0.9519
  - 0.9698
  - 0.9730
  - 0.9785
- Final accuracy: 0.9942

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   3s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 128
- Accuracy: 99.42%

## Test 13

### Testing with Activation functoin: Sigmoid

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.1048
  - 0.2429
  - 0.8120
  - 0.9315
  - 0.9581
- Final accuracy: 0.9956

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _sigmoid_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.56%

## Test 14

### Testing with Activation functoin: tanh

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.8122
  - 0.9735
  - 0.9821
  - 0.9876
  - 0.9885
- Final accuracy: 0.9999

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.99%

## Test 15

### Testing with Activation functoin: elu

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.8315
  - 0.9758
  - 0.9834
  - 0.9870
  - 0.9887
- Final accuracy: 0.9980

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _elu_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.80%

## Test 16

### Testing with optimizer Adamax (Osccilating between 95% - 96% since the 5th epoch)

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7672
  - 0.9437
  - 0.9537
  - 0.9520
  - 0.9598
- Final accuracy: 0.9630

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adamax

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 96.30%

## Test 17

### Testing with optimizer Adagrad (Improving accuracy so fast)

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.8955
  - 0.9817
  - 0.9871
  - 0.9906
  - 0.9924
- Final accuracy: 0.9999

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   5s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adagrad

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 99.99%

## Test 18

### Testing with dropout of 0.5 placed after the 2nd layer

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.8011
  - 0.9343
  - 0.9434
  - 0.9501
  - 0.9542
- Final accuracy: 0.9696

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   6s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adagrad **Best**

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 96.96%

## Test 19

### Testing with dropout of 0.5 for both placed after the 2nd layer, and the 4th.

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7368
  - 0.8998
  - 0.9164
  - 0.9220
  - 0.9289
- Final accuracy: 0.9495

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   6s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adagrad **Best**

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 94.95%

## Test 20

### Testing with dropout of 0.3 and 0.5 placed after the 2nd layer, and the 4th.

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.7784
  - 0.9160
  - 0.9270
  - 0.9387
  - 0.9407
- Final accuracy: 0.9604

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   6s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adagrad **Best**

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 96.04%

## Test 21

### Testing with dropout of 0.3 and 0.1 placed after the 2nd layer, and the 4th.

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.8681
  - 0.9628
  - 0.9722
  - 0.9736
  - 0.9767
- Final accuracy: 0.9867

2. The number of parameters in the model:.
   37,058

3. The average time to train in each epoch:.
   6s 3ms/step

4. The average test time in each epoch:.
   ?

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

- Layer3: FCLayer with 128 units and activation of _relu_

- Layer4: FCLayer with 64 units and activation of _relu_

- Layer5: FCLayer with 32 units and activation of _relu_

- Activation _tanh_ layer **Best**

6. The learning rate used and configuration of the optimizers:.

- optimizer: Adagrad

  - learning rate: 0.05 **Best**
  - momentum: 0.0

- Epochs: 20 **Best**
- Batch size: 32 **Best**
- Accuracy: 98.67%

---

# Final Version of Code

```python
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
# Build the model.
optimizer = keras.optimizers.Adagrad(
learning_rate=0.05, name="Adagrad")

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
print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]
# Check our predictions against the ground truths.
print(test_labels[:5]) # [7, 2, 1, 0, 4]
```
