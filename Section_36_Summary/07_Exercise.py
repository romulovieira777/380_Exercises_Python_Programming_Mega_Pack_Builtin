"""
Exercise No. 07

For any:

    x = [x1,...,xn] e Rn
    y = [y1,...,yn] e Rn

We define the Euclidean distance by the formula:

    d(x, y) = sqrt((x1 - y1)^2)

Implement a function called euclidean_distance() that computes the distance between two points.

Example:

    [IN]: euclidean_distance([0, 3], [4, 0])
    [OUT]: 5.0

Note: You only need to implement this function.
"""


# Solution I
def euclidean_distance(x, y):
    return sum([(x[i] - y[i]) ** 2 for i in range(len(x))]) ** 0.5


print(euclidean_distance([0, 3], [4, 0]))


# Solution II
def euclidean_distance(x, y):
    squared_diff = [(i - j) ** 2 for i, j in zip(x, y)]
    return sum(squared_diff) ** 0.5


print(euclidean_distance([0, 3], [4, 0]))
