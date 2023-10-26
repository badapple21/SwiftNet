import matrix_math as mm
import nn
from mnist import MNIST
import os
import pickle


mndata = MNIST('samples')



images, labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()

def get_correct(label):
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x[label] = 1
    return x

def main(images, labels, test_images, test_labels, epochs, nodes):
    

    network = nn.NeuralNetwork(784, nodes, 10)

    print("training . . .")
    for j in range(epochs):
        for i in range(len(images)):
            network.train(images[i], get_correct(labels[i]))
            print((i/60000*100))

    print("testing . . .")

    correct = 0
    total = 0
    for i in range(len(test_images)):
        output = network.feed_forward(test_images[i])
        if(nn.get_max(output)==test_labels[i]):
            correct+=1
        total+=1
        print(i/10000*100)

    accuracy = (correct/total)*100


    HERE ="saved_nets"
    with open(f"saved_nets/{nodes} {int(accuracy)}%.pickle","wb") as f:
        pickle.dump(network.net, f)                    
        f.close()

    print(f"{correct}/{total}, {accuracy} % accuarcy")
    


if __name__ == "__main__":
    main(images, labels, test_images, test_labels, 1, 16)