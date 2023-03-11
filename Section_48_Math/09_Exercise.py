"""
Exercise No. 09

A point centroid (variable centroid) is given:

    centroid = (0.5, 0.5)

and 10 points with coordinates in the range [0, 1):

    points = [(rand(), rand()) for i in range(10)]

Using the built-in math module calculate the distance of each point from the points list to the centroid.

Then print the index of the closest point to the centroid with the distance to the centroid as shown below.

Tip:

    # >>> help(math.dist)

    Help on built-in function dist in module math:

    dist(p, q, /)
        Return the Euclidean distance between two points p and q.

        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.

        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))

Expected result:

    (7, 0.15647709534399296)
"""
import math
import random
from random import random as rand

random.seed(42)
centroid = (0.5, 0.5)
points = [(rand(), rand()) for i in range(10)]

# Solution I
distances = [math.dist(point, centroid) for point in points]
index = distances.index(min(distances))
print((index, distances[index]))


# Solution II
distances = [math.dist(point, centroid) for point in points]
result = min(list(enumerate(distances)), key=lambda item: item[1])

print(result)
