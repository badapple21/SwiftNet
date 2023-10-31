import nn
import numpy as np

# mndata = MNIST("samples")
# test_images, test_labels = mndata.load_testing()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def get_correct(label):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x[label] = 1
    return x


def main(nodes, epochs):
    test_net = nn.NeuralNetwork(784, nodes, 10, sigmoid)

    images = []
    labels = []

    with open("train.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            images.append([int(i) for i in row[1:]])
            labels.append(int(row[0]))

    train_images = images[:41000]
    train_labels = labels[:41000]

    test_images = images[41000:]
    test_labels = labels[41000:]

    print(len(images[6]))

    for i in range(epochs):
        for i in range(len(images)):
            test_net.train(images[i], get_correct(labels[i]))
            print((i / 60000 * 100))

    accuracy = test_net.test_net(test_images, test_labels)
    print(accuracy)
    test_net.save_net(f"kaggle_nets/{nodes} {int(accuracy)}")


main([2000], 5)
