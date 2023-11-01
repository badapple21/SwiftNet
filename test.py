import nn
import numpy as np
import csv

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

    train_images = images[:38000]
    train_labels = labels[:38000]

    test_images = images[38000:]
    test_labels = labels[38000:]

    tests = test_net.test_and_train(
        test_images, test_labels, train_images, train_labels, 5
    )

    avg = 0
    for i, test in enumerate(tests):
        print(test)
        avg += test

    print(avg / len(tests))

    # print(len(images[6]))

    # for i in range(epochs):
    #     for i in range(len(images)):
    #         test_net.train(images[i], get_correct(labels[i]))
    #         print((i / 60000 * 100))

    # accuracy = test_net.test_net(test_images, test_labels)
    # print(accuracy)
    # test_net.save_net(f"kaggle_nets/{nodes} {int(accuracy)}")


def predict():
    test_net = nn.NeuralNetwork(784, [2000], 10, sigmoid)
    test_net.load("kaggle_nets/[2000] 91.pickle")
    with open("test.csv", "r") as f:
        with open("file.csv", "w", newline="") as w:
            reader = csv.reader(f)
            writer = csv.writer(w)
            for i, row in enumerate(reader):
                print(i)
                image = [int(j) for j in row]
                writer.writerow(
                    [f"{i+1},{nn.get_max(test_net.feed_forward(image)[-1])}"]
                )


main([4], 1)
