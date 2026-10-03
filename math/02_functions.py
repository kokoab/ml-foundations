import numpy as np


def relu(x):
    return np.maximum(0,x)

def sigmoid(z):
    t = np.exp(-np.abs(z))
        
    return np.where(z >= 0, 1 / (t + 1), t / (t + 1))

    
    

if __name__ == "__main__":
    assert np.allclose(relu(np.array([-1, 0.5, 2, -3])), [0, 0.5, 2, 0])
    assert np.isclose(sigmoid(0.0), 0.5)
    assert np.isclose(sigmoid(np.log(3)), 0.75)
    assert np.all(np.isfinite(sigmoid(np.array([-1000.0, 1000.0]))))
    
    print("all checks passed")