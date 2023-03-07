"""
Exercise No. 04

Using the built-in random module set the random seed to 42, then generate a pseudo-randomly generate six integers from
the range [1, 49) and assign to the list called numbers.

In response, print the numbers list to the console.

Tip:

    # >>> help(random.seed)

    Help on method seed in module random:

    seed(a=None, version=2) method of random.Random instance
        Initialize internal state from hashable object.

        None or no argument seeds from current time or from an operating
        system specific randomness source if available.

        If *a* is an int, all bits are used.

        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.


    # >>> help(random.randint)

    Help on method randint in module random:

    randint(a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.

Expected result:

    [41, 8, 2, 48, 18, 16]
"""
import random

random.seed(42)

numbers = [random.randint(1, 49) for _ in range(6)]
print(numbers)
