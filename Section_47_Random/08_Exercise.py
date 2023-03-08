"""
Exercise No. 08

The following list is given:

    techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

In Python, the order of the items in a list is important. Using the built-in random module, set the random seed to 32,
then shuffle the items in the techs list.

In response, print the techs list to the console.

Tip:

    # >>> help(random.shuffle)

    Help on method shuffle in module random:

    shuffle(x, random=None) method of random.Random instance
        Shuffle list x in place, and return None.

        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.

Expected result:

    ['php', 'javascript', 'c++', 'c#', 'java', 'python']
"""
import random

random.seed(32)

techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

random.shuffle(techs)

print(techs)
