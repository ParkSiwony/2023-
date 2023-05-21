import numpy as np
import pandas as pd


class RNN:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.whh = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.hnodes))
        self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        self.lr = learningrate
        self.hidden_state = np.zeros((self.hnodes, 1))

    def activation_function(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs) + np.dot(self.whh, self.hidden_state)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                     np.transpose(hidden_outputs))
        self.whh += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                     np.transpose(self.hidden_state))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
        self.hidden_state = hidden_outputs

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs) + np.dot(self.whh, self.hidden_state)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        self.hidden_state = hidden_outputs
        return final_outputs


# Load the MNIST dataset from CSV file
data = pd.read_csv('C:\\Users\\psw00\\PycharmProjects\\pythonProject1\\mnist.csv')

# Separate the features (pixels) and labels (targets)
X = data.iloc[:, 1:].values / 255.0  # Normalize pixel values to the range [0, 1]
y = data.iloc[:, 0].values

# Set the input, hidden, and output nodes
input_nodes = 784  # 28x28 pixels
hidden_nodes = 100
output_nodes = 10  # 10 possible labels (0-9)

# Set the learning rate
learning_rate = 0.1

# Create an instance of the recurrent neural network
rnn = RNN(input_nodes, hidden_nodes, output_nodes, learning_rate)

# Train the recurrent neural network using the MNIST dataset
for i in range(len(X)):
    inputs = X[i]
    targets = np.zeros(output_nodes) + 0.01
    targets[y[i]] = 0
    RNN.train(inputs, targets)

# Test the neural network on a sample image
sample_image_index = 0
sample_image = X[sample_image_index]
predicted_label = np.argmax(RNN.query(sample_image))
print("Predicted label:", predicted_label)
