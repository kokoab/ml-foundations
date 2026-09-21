import math


def mean(values):
    total = 0
    for value in values:
        total += value
    return total / (len(values)) 

def mean_squared_error(true_values, guesses) :
    total = 0    
    for y, y_hat in zip(true_values, guesses):
        total += (y - y_hat) ** 2
    return total / len(true_values)

def sum_of_logs(probabilities):
    total = 0
    for p in probabilities:
        total += math.log(p)
    return total
        
def lowest_point(a, b):
    return -b / (2 * a)
        
if __name__ == "__main__":
    assert mean([2,4,9]) == 5
    assert mean_squared_error([3,5], [2,7]) == 2.5
    assert abs(sum_of_logs([0.01] * 1000) - (-4605.17)) < 0.01
    assert  lowest_point(1, -6) == 3
    assert lowest_point(5, -24) == 2.4
    
    print("all checks passed")
