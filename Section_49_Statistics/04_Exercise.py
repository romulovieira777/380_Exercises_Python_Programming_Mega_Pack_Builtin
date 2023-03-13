"""
Exercise No. 04

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

Using the built-in statistics module calculate the quartiles of the order 1/4, 1/2 (median) and 3/4

Print each quartile to the console as shown below.

Tip:

    #>>> help(statistics.quantiles)

    Help on function quantiles in module statistics:

    quantiles(data, *, n=4, method='exclusive')
        Divide *data* into *n* continuous intervals with equal probability.

        Returns a list of (n - 1) cut points separating the intervals.

        Set *n* to 4 for quartiles (the default).  Set *n* to 10 for deciles.
        Set *n* to 100 for percentiles which gives the 99 cuts points that
        separate *data* in to 100 equal sized groups.

        The *data* can be any iterable containing sample.
        The cut points are linearly interpolated between data points.

        If *method* is set to *inclusive*, *data* is treated as population
        data.  The minimum value is treated as the 0th percentile and the
        maximum value is treated as the 100th percentile.

Expected result:

    67.17
    80.3
    92.11
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
    68.21,
]

# Solution I
print(round(statistics.quantiles(data, n=4, method='exclusive')[0], 2))
print(round(statistics.quantiles(data, n=4, method='exclusive')[1], 2))
print(round(statistics.quantiles(data, n=4, method='exclusive')[2], 2))

# Solution II
quartiles = statistics.quantiles(data, n=4)

for quartil in quartiles:
    print(round(quartil, 2))
