import matplotlib.pyplot as plt

import numpy as np


def relu(x):
    return np.maximum(0, x)

def sigmoid(z):
    t = np.exp(-np.abs(z))
        
    return np.where(z >= 0, 1 / (t + 1), t / (t + 1))

def softmax(z):
    largest_number = np.max(z)
    z_norm = z - largest_number
    e = np.exp(z_norm)
    total = np.sum(e)    
    probs = e / total
    
    return probs

def relu_plot(x):
    f = (2*x) + 1
    chain_relu = (3*relu(f)) - 1

    plain_chain = (3*f) - 1

    plt.figure()
    plt.plot(x, plain_chain, label="plain chain")
    plt.plot(x, chain_relu, label="with relu")
    plt.legend()
    plt.title("with and without relu")
    plt.xlabel("x")
    plt.ylabel("output")


def sigmoid_plot(z):
    j = sigmoid(z)
    
    plt.figure()
    plt.scatter(0,0.5, color="red", label="center")
    plt.plot(z, j, label="sigmoid")
    plt.text(6, 0.90, "saturated")
    plt.text(-7, 0.10, "saturated")
    plt.legend()
    plt.title("sigmoid")
    plt.xlabel("z")
    plt.ylabel("output")
    
def sigmoid_symmetry(z):
    left = 1 - (sigmoid(-z))
    right = sigmoid(z)
    
    assert np.allclose(left, right), "mali mo boi"


if __name__ == "__main__":
    assert np.allclose(relu(np.array([-1, 0.5, 2, -3])), [0, 0.5, 2, 0])
    assert np.isclose(sigmoid(0.0), 0.5)
    assert np.isclose(sigmoid(np.log(3)), 0.75)
    assert np.all(np.isfinite(sigmoid(np.array([-1000.0, 1000.0]))))
    assert np.allclose(softmax(np.array([2.0, 1.0, 0.1])), [0.659, 0.242, 0.099], atol = 1e-3)
    assert np.allclose(softmax(np.array([1000.0, 999])), [0.731, 0.269], atol=1e-3)
    assert np.isclose(softmax(np.array([5.0, -2.0, 0.3])).sum(), 1.0)
    
    
    sigmoid_symmetry(z = np.random.uniform(-8, 8, 5))
    print("all checks passed")
    relu_plot(x = np.linspace(-5, 5, 200))
    sigmoid_plot(z = np.linspace(-8, 8, 200))
    plt.show()
    