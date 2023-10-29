import nn
from mnist import MNIST
import numpy as np
import csv

# mndata = MNIST("samples")
# test_images, test_labels = mndata.load_testing()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


test_net = nn.NeuralNetwork(784, [2000], 10, sigmoid)

path = "saved_nets/2000 96%.pickle"

test_net.load("saved_nets/2000 96%.pickle")
test_images = []
test_labels = []

with open("file.csv", 'w') as f:
    with open("test.csv") as r:
        reader = csv.reader(r)
        for row in reader:
            test_images.append([int(i) for i in row[0:]])
            test_labels.append(int(row[0]))

print(test_net.test_net(test_images, test_labels))
    # writer = csv.writer(f)
    # writer.writerow(['ImageId','Label'])
    # for i in range(len(test_images)):
    #     output = test_net.feed_forward(test_images[i])
    #     writer.writerow(i+1, nn.get_max(output[-1]))
    #     print(i/10000*100)

    

