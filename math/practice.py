import numpy as np

z = np.random.uniform(-8, 8, 5)
print(z)

left = 1 - (1 / (1+(np.exp(-z))))
right = 1 / (1+(np.exp(z)))


print(left)
print(right)

is_true = np.allclose(left, right)

if is_true:
    print("galing mo tanginamo")
else:
    print("ulet pa boi") 