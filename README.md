# Basic Structure

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

# Initial testing with the basic structure

---

## Test 1

1. Final accuracy of the model and the accuracy in the first 5 epoch:.

- First 5 epochs:
  - 0.4997
  - 0.9307
  - 0.9493
  - 0.9580
  - 0.9649
- Final accuracy: 0.9649

2. The number of parameters in the model:.
   **I do not know**

3. The average time to train in each epoch:.
   6ms

4. The average test time in each epoch:.
   6ms

5. The layers of each model (including activations):.

- Layer1: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_

  - Layer2: Convolutional 2D with input shape of ($28 \times 28$) comes with max pooling and activation of _relu_
  - Layer3: FCLayer with 32 units and activation of _relu_

- Activation _softmax_ layer

6. The learning rate used and configuration of the optimizers:.

- optimizer: SGD

  - learning rate: 0.01
  - momentum: 0.0

## It's thought that the low learning rate of 0.01 had caused the model to result this accuracy
