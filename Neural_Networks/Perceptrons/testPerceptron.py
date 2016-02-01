###
# This class is for testing the finished perceptron
###

import logging
import random
from pprint import pprint
from logging import debug
from logging import info
from Perceptron import Perceptron
from Trainer import Trainer

# Output logs to console
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")

debug("Program Start")

# Holder for our training points
training = []
TRAININGPOINTS = 2000
TESTINGPOINTS = 2000

# Size of our "view"
WIDTH = 640
HEIGHT = 360

# Our formula (To show to the user)
FORMULA = "y = 2x + 1"

# The formula for our line
# We are training our perceptron to understand if a point is above or below this
# Change this equation to train the perceptron for different cases
def f(x):
    # Change this to change the perceptrons training regimine
    return 2*x+1

# Determine if the pont is above or below the line using MATH!
# Returns True if point is above f(x) returnes false if it is below
def evaluateIfPointAboveFx(inputs):
    return False if inputs[1] < f(inputs[0]) else True

# Determine if the perceptron's guess is correct
# Returns true if the perceptron is correct, and false if it is not
def evaluatePerceptron(perceptron, answer):
    return True if perceptron.getDeterminationInBoolean() == answer else False

def setup():

    for i in range(0, TRAININGPOINTS):
        x = random.uniform(-WIDTH/2, WIDTH/2)
        y = random.uniform(-HEIGHT/2, HEIGHT/2)
        # Is the correct answer 1 or -1?
        answer = 1
        if y < f(x):
            answer = -1;
        training.append(Trainer(x, y, answer))

def runTraining():
    ptron = Perceptron(3, None)
    total = 0
    for i in range(0, TRAININGPOINTS):
        ptron.train(training[i].inputs, training[i].answer)
        for j in range(0, TRAININGPOINTS):
            guess = ptron.feedforeward(training[j].inputs)
        total = i
    return ptron

def runTestingVerbose():
    correctGuesses = 0

    # 1. Set the neuron's inputs
    # 2. Run f(x) and Perceptron
    # 3. Compare Perceptron's Guess to the Mathematically Derived Answer
    print("")
    print("\t\t\t   ---Printing Results---")
    header = "Point \t\t\t\t Perceptron \t\t\t Formula: %s " %(FORMULA)
    print(header)
    for i in range(0, int(TESTINGPOINTS)):
        neuron.setInputs(training[i].inputs)
        guessIsCorrect = evaluatePerceptron(neuron, evaluateIfPointAboveFx(training[i].inputs))
        if(guessIsCorrect):
            correctGuesses += 1
        output = "%s \t %s \t %s" %\
         (training[i].inputs,\
          neuron.getDeterminationInEnglish(),\
          guessIsCorrect)
        print(output)
    print("")
    print("Total Number of Training Points: " + str(TRAININGPOINTS))
    print("Total Number of Test Points: " + str(TESTINGPOINTS))
    print("Perceptron Success: " + str((correctGuesses/TESTINGPOINTS) * 100) + "%")
    print("")
    debug("Done.")

def runTesting():
    correctGuesses = 0

    # 1. Set the neuron's inputs
    # 2. Run f(x) and Perceptron
    # 3. Compare Perceptron's Guess to the Mathematically Derived Answer
    for i in range(0, int(TESTINGPOINTS)):
        neuron.setInputs(training[i].inputs)
        guessIsCorrect = evaluatePerceptron(neuron, evaluateIfPointAboveFx(training[i].inputs))
        if(guessIsCorrect):
            correctGuesses += 1
    print("")
    print("Total Number of Training Points: " + str(TRAININGPOINTS))
    print("Total Number of Test Points: " + str(TESTINGPOINTS))
    print("Perceptron Success1: " + str(correctGuesses)+"/"+str(TESTINGPOINTS))
    print("Perceptron Success2: " + str((correctGuesses/TESTINGPOINTS) * 100) + "%")
    print("")
    debug("Done.")

debug("Initializing Perceptron")
setup()
debug("Finished")
debug("Running Perceptron Training Simulation...")
debug("---")

# Setup our final Perceptron for testing
neuron = runTraining()
info("Trained Perceptron: " + str(neuron.weights))


# Uncomment to speed up testing
#runTesting()
runTestingVerbose()
