from gettext import find
from fperceptron import *
import pickle
import os


def findWeights():
    print("Training")
    
    # put training data there.
    training_data = []

    with open ('training_data', 'rb') as fp:
        training_data = pickle.load(fp)


    weights = train_perception(training_data, 0.1, 5000)

    print("The weights for the inputs are: " + str(weights))

    # writes that list to a data file
    with open('weights_data', 'wb') as fp:
        pickle.dump(weights, fp)

if __name__ == "__main__":
    findWeights()
