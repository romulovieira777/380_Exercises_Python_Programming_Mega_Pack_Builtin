"""
Exercise No. 01

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

Using the built-in statistics module calculate:

    - arithmetic average
    - geometric mean
    - harmonic mean
    - median

Round the values to two decimal places and print to the console.

Tip:

    #>>> help(statistics.mean)

    Help on function mean in module statistics:

    mean(data)
        Return the sample arithmetic mean of data.


    #>>> help(statistics.geometric_mean)

    Help on function geometric_mean in module statistics:

    geometric_mean(data)
        Convert data to floats and compute the geometric mean.


    #>>> help(statistics.harmonic_mean)

    Help on function harmonic_mean in module statistics:

    harmonic_mean(data)
        Return the harmonic mean of data.


    #>>> help(statistics.median)

    Help on function median in module statistics:

    median(data)
        Return the median (middle value) of numeric data.

        When the number of data points is odd, return the middle data point.
        When the number of data points is even, the median is interpolated by
        taking the average of the two middle values

Expected result:

    78.66
    77.44
    76.2
    80.3
"""
import statistics

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
    68.21
]

print(round(statistics.mean(data), 2))
print(round(statistics.geometric_mean(data), 2))
print(round(statistics.harmonic_mean(data), 2))
print(round(statistics.median(data), 2))
