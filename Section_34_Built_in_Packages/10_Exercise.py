"""
Exercise No. 10

Using the math built-in module, implement the function called sigmoid() expressed by the formula:

    f(x) = 1 / (1 + e^-x)

Note: All you have to do is implement the function.
"""


def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))


print(sigmoid(0))
