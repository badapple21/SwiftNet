import matrix_math as mm
import numpy as np
import pickle


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def fake_desigmoid(x):
    return x * (1-x)

def get_max(x):
    index = 0
    max = x[0]
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
            index = i

    return index
class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes
        self.hidden_nodes = hidden_nodes
    
        self.weights_ih = mm.matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = mm.matrix(self.output_nodes, self.hidden_nodes)
    
        self.weights_ho.randomize()
        self.weights_ih.randomize()
    
        self.bias_h = mm.matrix(self.hidden_nodes, 1)
        self.bias_o = mm.matrix(self.output_nodes, 1)
    
        self.bias_h.randomize()
        self.bias_o.randomize()

        self.learning_rate = .03

        self.net = [self.weights_ih, self.weights_ho, self.bias_h, self.bias_o]

    def load(self, path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        self.weights_ih = data[0]
        self.weights_ho = data[1]
        self.bias_h = data[2]
        self.bias_o = data[3]

    def feed_forward(self, input_array):

        inputs = mm.from_array(input_array)

        hidden = mm.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        hidden.map(sigmoid)

        outputs = mm.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

        return outputs.to_array()

    def train(self, inputs_array, targets_array):

        inputs = mm.from_array(inputs_array)
        hidden = mm.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(sigmoid)

        outputs = mm.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(sigmoid)

        # convert array to matrix
        targets = mm.from_array(targets_array)

        output_errors = mm.subtract(targets, outputs)
        
        #calculates the gradients
        gradients = outputs
        gradients.multiply(output_errors)
        gradients.multiply(self.learning_rate)


        hidden_t = mm.transpose(hidden)
        weights_ho_deltas = mm.multiply(gradients, hidden_t)

        self.weights_ho.add(weights_ho_deltas)
        self.bias_o.add(gradients)


        who_t = mm.transpose(self.weights_ho)
        hidden_errors = mm.multiply(who_t, output_errors)

        hidden_gradients = hidden
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        inputs_t = mm.transpose(inputs)
        weight_ih_deltas = mm.multiply(hidden_gradients, inputs_t)

        self.weights_ih.add(weight_ih_deltas)
        self.bias_h.add(hidden_gradients)

    def test_net(self, test_images, test_labels):
        print("testing . . .")

        correct = 0
        total = 0
        for i in range(len(test_images)):
            output = self.feed_forward(test_images[i])
            if(get_max(output)==test_labels[i]):
                correct+=1
            total+=1

        return  (correct/total)*100



def main():
    return 

if __name__ == "__main__":
    main()