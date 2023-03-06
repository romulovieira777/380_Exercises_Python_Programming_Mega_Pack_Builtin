"""
Exercise No. 01

Using the built-in random module set the random seed to 42, then generate a pseudo-random number between [0, 1) and
assign to the var variable. Print the var variable rounded to five decimal places to the console.

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

    0.63943
"""
import random

random.seed(42)

var = random.random()
print(round(var, 5))
