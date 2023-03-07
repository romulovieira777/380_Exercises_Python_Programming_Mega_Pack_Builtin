"""
Exercise No. 02

Using the built-in random module set the random seed to 42, then generate a pseudo-randomly generate 10 numbers from the
range [0, 1) rounded to four decimal places and assign to a list called numbers.

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


    # >>> help(random.random)

    Help on built-in function random:

    random(...) method of random.Random instance
        random() -> x in the interval [0, 1).

Expected result:

    [0.6394, 0.025, 0.275, 0.2232, 0.7365, 0.6767, 0.8922, 0.0869, 0.4219, 0.0298]
"""
import random

random.seed(42)

numbers = [round(random.random(), 4) for _ in range(10)]
print(numbers)
