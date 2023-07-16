import matrix_math as mm
import math
    
def sigmoid(x):
    return 1 /( 1 +math.exp(-x))

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

    def feed_forward(self, input_array):

        inputs = mm.from_array(input_array)

        hidden = mm.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        hidden.map(sigmoid)

        output = mm.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sigmoid)

        return output.to_array()



def main():
    return 

if __name__ == "__main__":
    main()