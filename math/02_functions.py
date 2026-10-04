import numpy as np
import matplotlib as plt


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


if __name__ == "__main__":
    assert np.allclose(relu(np.array([-1, 0.5, 2, -3])), [0, 0.5, 2, 0])
    assert np.isclose(sigmoid(0.0), 0.5)
    assert np.isclose(sigmoid(np.log(3)), 0.75)
    assert np.all(np.isfinite(sigmoid(np.array([-1000.0, 1000.0]))))
    assert np.allclose(softmax(np.array([2.0, 1.0, 0.1])), [0.659, 0.242, 0.099], atol = 1e-3)
    assert np.allclose(softmax(np.array([1000.0, 999])), [0.731, 0.269], atol=1e-3)
    assert np.isclose(softmax(np.array([5.0, -2.0, 0.3])).sum(), 1.0)
    
    # softmax([2.0, 1.0, 0.1])
    print("all checks passed")
    