# Single Layer Perceptron Network Implementation

## Introduction
This Markdown document provides an implementation of a Single Layer Perceptron (SLP) network. The SLP is implemented using Python and NumPy, and it is used to solve logical AND and OR gate problems.

## Implementation

```python
import numpy as np

class SLP(object):
    def __init__(self, input_size, learning_rate=1, epochs=1000):
        self.Weights = np.zeros(input_size + 1)
        print("Creating weight vector, 1D Array with Zeros", self.Weights)
        self.epochs = epochs
        self.learning_rate = learning_rate

    def activation_function(self, input_value):
        return 1 if input_value >= 0 else 0

    def predict(self, input_value):
        z = self.Weights.T.dot(input_value)
        a = self.activation_function(z)
        return a

    def perceptronLearning(self, given_input, desired_output):
        for j in range(self.epochs):
            for i in range(desired_output.shape[0]):
                x = np.insert(given_input[i], 0, 1)
                y = self.predict(x)
                e = desired_output[i] - y

                print("Error: ", e)
                print("Predicted Output: ", y)
                self.Weights = self.Weights + self.learning_rate * e * x

# AND Gate
given_input_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
desired_output_and = np.array([0, 0, 0, 1])

slp_and = SLP(input_size=2, epochs=10)
slp_and.perceptronLearning(given_input_and, desired_output_and)

print("Input Weight with bias (AND gate): ", slp_and.Weights)
print("Learning Rate: ", slp_and.learning_rate)
print("Total Epochs: ", slp_and.epochs)

# OR Gate
given_input_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
desired_output_or = np.array([0, 1, 1, 1])

slp_or = SLP(input_size=2, epochs=10)
slp_or.perceptronLearning(given_input_or, desired_output_or)

print("Input Weight with bias (OR gate): ", slp_or.Weights)
print("Learning Rate: ", slp_or.learning_rate)
print("Total Epochs: ", slp_or.epochs)
```

## Results

- **Input Weight with bias:** [bias, weight1, weight2]
- **Learning Rate:** Learning rate used during training
- **Total Epochs:** Number of epochs used for training

The provided Python code implements a Single Layer Perceptron network and solves both the AND and OR gate problems. The SLP is trained using the given input and desired output, and the resulting weights with bias, learning rate, and total epochs are displayed for each gate.
