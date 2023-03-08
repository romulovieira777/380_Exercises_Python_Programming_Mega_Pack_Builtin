"""
Exercise No. 06

The following list is given:

    techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

Using the built-in random module set the random seed to 32, then using the random,choices() method, randomly select
three items from the techs list and print to the console.

Note that the random.choices() select values with replacement.

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

    # >>> help(random.choices)

    Help on method choices in module random:

    choices(population, weights=None, *, cum_weights=None, k=1) method of random.Random instance
        Return a k sized list of population elements chosen with replacement.

        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.

Expected result:

    ['python', 'java', 'java']
"""
import random

random.seed(32)

techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

print(random.choices(population=techs, k=3))
