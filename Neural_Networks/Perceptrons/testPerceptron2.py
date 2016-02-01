from Perceptron import Perceptron

weights = [-8.474109968136872, 3.525175929701409, 0.3503913051612264]
Brain = Perceptron(3, weights)

Brain.setInputs([1,3,-1])
print(str(Brain.getDeterminationInEnglish()))
