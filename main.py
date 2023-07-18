import matrix_math as mm
import nn
import random



def main():
    training_data = [
        {
            "inputs":[0,0],
            "targets": [0]
        },
        {
            "inputs":[1,0],
            "targets": [1]
        },
        {
            "inputs":[0,1],
            "targets": [1]
        },
        {
            "inputs":[1,1],
            "targets": [0]
        }
    ]

    network = nn.NeuralNetwork(2, 64, 1)

    for i in range(50000):
        data = random.choice(training_data)
        network.train(data["inputs"], data["targets"])

    print(network.feed_forward([0,0]))
    print(network.feed_forward([1,0]))
    print(network.feed_forward([0,1]))
    print(network.feed_forward([1,1]))


if __name__ == "__main__":
    main()