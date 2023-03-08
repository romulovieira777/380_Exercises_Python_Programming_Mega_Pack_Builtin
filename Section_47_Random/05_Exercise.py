"""
Exercise No. 05

The following list is given:

    techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

Using the built-in random module set the random seed to 32, then randomly select one element from the techs list and
print it to the console.

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

    # >>> help(random.choice)

    Help on method choice in module random:

    choice(seq) method of random.Random instance
        Choose a random element from a non-empty sequence.

Expected result:

    python
"""
import random

random.seed(43)

techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

print(random.choice(techs))
