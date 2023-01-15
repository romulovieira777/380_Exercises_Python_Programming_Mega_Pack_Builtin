"""
Exercise No. 16

Dot product of vectors v, w:
    v = [v1,..., vn] e Rn
    w = [w1,..., wn] e Rn

We defne as:
    v.w = v1w1 + ... + vnw1

Implement a function called dot_product() that takes two lists of the same length (vectors) and calculate the dot
product. We assume that user gives a correctly defined vector.

Example:
    [IN]: dot_product([1, 2], [5, 2])
    [OUT]: 9

Note: You only need to implement this function.
"""


# Solution I
def dot_product(v, w):
    return sum([v[i] * w[i] for i in range(len(v))])


print(dot_product([1, 2], [5, 2]))


# Solution II
def dot_product(vec1, vec2):
    return sum([v * w for v, w in zip(vec1, vec2)])


print(dot_product([1, 2], [5, 2]))
