import matrix_math as mm
import math
    
def sigmoid(x):
    return 1 /( 1 +math.exp(-x))

def fake_desigmoid(x):
    return x * (1-x)
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

        self.learning_rate = .1

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

        outputs = self.feed_forward(inputs_array)

        # convert array to matrix
        outputs = mm.from_array(outputs)
        targets = mm.from_array(targets_array)

        output_errors = mm.subtract(targets, outputs)
        
        #calculates the gradients
        gradients = mm.map(outputs, fake_desigmoid)
        gradients.multiply(output_errors)
        gradients.multiply(self.learning_rate)


        hidden_t = mm.transpose(hidden)
        weights_ho_deltas = mm.multiply(gradients, hidden_t)

        self.weights_ho.add(weights_ho_deltas)
        self.bias_o.add(gradients)


        who_t = mm.transpose(self.weights_ho)
        hidden_errors = mm.multiply(who_t, output_errors)

        hidden_gradients = mm.map(hidden, fake_desigmoid)
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        inputs_t = mm.transpose(inputs)
        weight_ih_deltas = mm.multiply(hidden_gradients, inputs_t)

        self.weights_ih.add(weight_ih_deltas)
        self.bias_h.add(hidden_gradients)


def main():
    return 

if __name__ == "__main__":
    main()