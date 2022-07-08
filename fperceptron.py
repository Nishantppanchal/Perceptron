def perceptron(inputs, weights):
    # our total input_signal is a weighted sum of the inputs from the
    # dendrites
    # inputs came from out coords
    # inputs = [0.1, 0.3]

    # weights are just random for now
    # the first element in our weights list will now be the threshold
    # weights = [0.5, 0.7, 0.4]

    n = 1
    input_signal = weights[0]
    while n < len(weights):
        input_signal = input_signal + (inputs[n-1] * weights[n])
        n = n + 1

    # simulate axon being activated
    # input
    # output
    # when the input <= threshold, output = 0
    # when the input > threshold, output = 1

    if input_signal <= 0:
        output_signal = 0
    else:
        output_signal = 1

    return output_signal

def train_perception(training_data, learning_rate, epochs):
    # the aim of this function is to return a list of weights
    # initialise all our weights
    weights = []
    # the number of weights we need will be equal to the number
    # of inputs + 1
    n = 0
    # set all our initial weights to 0
    while n < len(training_data[0]):
        weights.append(0)
        n = n + 1

    current_epochs = 0
    while current_epochs < epochs:
        # where we will do the learning

        row = 0
        while row < len(training_data):
            # for each row of our training data
            actual = training_data[row][-1]
            prediction = perceptron(training_data[row], weights)

            error = actual - prediction

            # update the threshold
            weights[0] = weights[0] + error * learning_rate
            w = 1
            while w < len(weights):
                # update each of the weights
                #note that we need to use w - 1 to take into account
                # the threshold having the index of 0
                weights[w] = weights[w] + error * learning_rate * training_data[row][w - 1]
                w = w +1
            row = row + 1

        # decreasing the learning rate in order to get
        # the best results
        decrease_rate = learning_rate/epochs
        learning_rate = learning_rate - decrease_rate

        current_epochs += 1
    # we are now ready to return out final set of weights
    return weights


