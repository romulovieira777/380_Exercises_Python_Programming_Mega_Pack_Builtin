"""
Exercise No. 36

Using the built-in module itertools and the tee class create pairwise() function that allows you to create an iterator
that returns adjacent pairs for an iterable object, for example:

    [3, 5, 1, 8, 9, 4] -> [(3, 5), (5, 1), (1, 8), (8, 9), (9, 4)]

Then, using the implemented function create iterators from the following objects:

    - [3, 5, 1, 8, 9, 4]
    - ['a', 'b', 'c', 'd', 'e']
    - 'Python'

and print their items as a list to the console as shown below.

Tip:

    #>>> help(itertools.tee)

    Help on built-in function tee in module itertools:

    tee(iterable, n=2, /)
        Returns a tuple of n independent iterators.

Expected result:

    [3, 5, 1, 8, 9, 4] -> [(3, 5), (5, 1), (1, 8), (8, 9), (9, 4)]
    ['a', 'b', 'c', 'd', 'e'] -> [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    'Python' -> [('P', 'y'), ('y', 't'), ('t', 'h'), ('h', 'o'), ('o', 'n')]
"""
import itertools


def pairwise(iterable):
    iter1, iter2 = itertools.tee(iterable)
    next(iter2)
    return zip(iter1, iter2)


print(f'[3, 5, 1, 8, 9, 4] -> {list(pairwise([3, 5, 1, 8, 9, 4]))}')
print(
    f"['a', 'b', 'c', 'd', 'e'] -> "
    f"{list(pairwise(['a', 'b', 'c', 'd', 'e']))}"
)
print(f"'Python' -> {list(pairwise('Python'))}")
