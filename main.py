import matrix_math as mm
import nn

def main():
    network = nn.NeuralNetwork(2, 2, 1)

    input = [1, 0]

    output = network.feed_forward(input)

    print(output)

if __name__ == "__main__":
    main()