from flask import Flask, render_template
import nn
from mnist import MNIST
import numpy as np
import cv2
import random

mndata = MNIST("samples")


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


images, labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()

app = Flask(__name__)


@app.route("/")
def hello_world():
    img_num = random.randint(0, 9999)

    test_net = nn.NeuralNetwork(784, [2000], 10, sigmoid)

    test_net.load("saved_nets/2000 96%.pickle")

    image = test_images[img_num]
    image_array = []
    for i in range(len(image)):
        if (i + 1) % 28 == 0:
            image_array.append(image[i - 27 : i + 1])
    image_array = np.array(image_array)

    cv2.imwrite("static/images/num.png", image_array)

    return render_template(
        "index.html",
        image="static/images/num.png",
        text=nn.get_max(test_net.feed_forward(image)[-1]),
    )
