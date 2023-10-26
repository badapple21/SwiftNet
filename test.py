import nn
from mnist import MNIST
mndata = MNIST('samples')
test_images, test_labels = mndata.load_testing()


test_net = nn.NeuralNetwork(784, 1, 10)

test_net.load("saved_nets/1 10%.pickle")
print(test_net.test_net(test_images, test_labels))

