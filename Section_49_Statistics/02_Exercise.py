"""
Exercise No. 02

The following list is given:

    data = [
        59.19,
        72.05,
        66.82,
        81.15,
        66.33,
        94.87,
        99.65,
        70.13,
        55.75,
        87.71,
        95.43,
        93.17,
        98.54,
        68.31,
        59.24,
        88.94,
        79.44,
        83.91,
        84.4,
        68.21,
    ]

Using the built-in statistics module calculate the mean value and standard deviation of the given data. Then create a
NormalDist object with the calculated parameters and generate a 10-element sample from the normal distribution (round
the values to three decimal places) and assign to the result list.

In response, print result list to the console.

Tip:

    #>>> help(statistics.mean)

    Help on function mean in module statistics:

    mean(data)
        Return the sample arithmetic mean of data.


    #>>> help(statistics.stdev)

    Help on function stdev in module statistics:

    stdev(data, xbar=None)
        Return the sample standard deviation of data.


    #>>> help(statistics.NormalDist)

    Help on class NormalDist in module statistics:

    class NormalDist(builtins.object)
     |  NormalDist(mu=0.0, sigma=1.0)
     |
     |  Normal distribution of a random variable


    #>>> help(statistics.NormalDist.samples)

    Help on function samples in module statistics:

    samples(self, n, *, seed=None)
        Generate *n* samples for a given mean and standard deviation.

Expected result:

    [76.637, 76.232, 77.098, 88.526, 76.869, 57.622, 83.331, 74.906, 75.613, 80.29]
"""
import statistics
import random

data = [
    59.19,
    72.05,
    66.82,
    81.15,
    66.33,
    94.87,
    99.65,
    70.13,
    55.75,
    87.71,
    95.43,
    93.17,
    98.54,
    68.31,
    59.24,
    88.94,
    79.44,
    83.91,
    84.4,
    68.21,
]

random.seed(42)

# Solution I
mean = statistics.mean(data)
stdev = statistics.stdev(data)
nd = statistics.NormalDist(mean, stdev)
result = [round(x, 3) for x in nd.samples(10)]

print(result)


# Solution II
mu = statistics.mean(data)
sigma = statistics.stdev(data)
dist = statistics.NormalDist(mu, sigma)
result = dist.samples(10)
result = [round(val, 3) for val in result]

print(result)
