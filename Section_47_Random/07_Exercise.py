"""
Exercise No. 07

The following list is given:

    techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

Using the built-in random module return a sample consisting of three elements from the techs list and print it to the
console.

Use the random.sample() method for this.

Tip:

    # >>> help(random.sample)

    Help on method sample in module random:

    sample(population, k) method of random.Random instance
        Chooses k unique random elements from a population sequence or set.

        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).

        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.

        To choose a sample in a range of integers, use range as an argument.
        This is especially fast and space efficient for sampling from a
        large population:   sample(range(10000000), 60)

Expected result:

    ['python', 'java', 'c#']
"""
import random

random.seed(32)

techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

print(random.sample(population=techs, k=3))
