import os
from Weights_finder import findWeights

if os.path.exists("training_data"):
    generateNewData = input("Would you like to retrain the AI? Yes (1) or No (2): ")
    if generateNewData == "1":
        os.system('python Data_generator.py')
        print("----------------------Data Generated----------------------")
        findWeights()
        print("----------------------Trained AI----------------------")
else:
    os.system('python Data_generator.py')
    findWeights()

os.system('python Perceptron.py')
