#! Python3
from random import uniform

class Perceptron(object):

    # Adjusts the rate of learning
    # Larger constant creates more drastic changes in behavior
    # Smaller constant creates more gradual, but accurate approximations.
    LEARNINGCONSTANT = 0.01;

    # Constructor
    def __init__(self, numInputs):
        self.weights = []
        
        for i in range(0, numInputs):
            self.weights.append(uniform(-1,1))

    def activate(self, sum):
        return 1 if sum > 0 else -1

    def feedforeward(self, inputs):
        self.sum = 0;
        for i in range(0, len(self.weights)):
            self.sum += inputs[i] * self.weights[i]
        return self.activate(self.sum)

    # Trains the neural network against known data
    # Takes inputs and the 'known' answer
    def train(inputs, desired):
        guess = feedforeward(inputs)

        # Error, the difference between the known answer and the perceptron's guess
        error = desired - guess

        # Adjust weights according to error & learning constant
        for i in range(len(weights)):
            # New weight is Learning Constant * Error * Delta Weight
            # Delta Weight = Error * Input
            weights[i] += LEARNINGCONSTANT * error * inputs[i]
