#! Python3
from random import uniform

class Perceptron(object):

    # Constructor
    # Modified to include a parameter for weights
    #  -This will allow us to test our newly trained perceptron
    #   By entering in pre-trained weights.
    def __init__(self, numInputs, weights):
        self.weights = []

        # Placeholder for testing
        self.inputs = []

        # Adjusts the rate of learning
        # Larger constant creates more drastic changes in behavior
        # Smaller constant creates more gradual, but accurate approximations.
        self.LEARNINGCONSTANT = 0.01;

        if weights is not None:
            self.weights = weights
        else:
            for i in range(0, numInputs):
                self.weights.append(uniform(-1,1))

    # My method to explicitly set the inputs
    def setInputs(self, inputs):
        self.inputs = inputs

    # PLAIN ENGLISH (Returns String)
    # My method to get an explicit determination
    def getDeterminationInEnglish(self):
        determination = self.feedforeward(self.inputs)
        if determination > 0:
            return "I think that this point is above the line."
        else:
            return "I think that this point is below the line."

    # BOOLEAN (Returns Bool)
    # My method to get an explicit determination
    def getDeterminationInBoolean(self):
        determination = self.feedforeward(self.inputs)
        return True if  determination > 0 else False

    def activate(self, sum):
        return 1 if sum > 0 else -1

    def feedforeward(self, inputs):
        self.sum = 0;
        for i in range(0, len(self.weights)):
            self.sum += inputs[i] * self.weights[i]
        return self.activate(self.sum)

    # Trains the neural network against known data
    # Takes inputs and the 'known' answer
    def train(self, inputs, desired):
        guess = self.feedforeward(inputs)

        # Error, the difference between the known answer and the perceptron's guess
        error = desired - guess

        # Adjust weights according to error & learning constant
        for i in range(len(self.weights)):
            # New weight is Learning Constant * Error * Delta Weight
            # Delta Weight = Error * Input
            self.weights[i] += self.LEARNINGCONSTANT * error * inputs[i]
