"""
Exercise No. 37

Using the built-in module itertools and the tee class implement make_three() function that allows you to create
an iterator that returns a triple for an iterable object:

    - (previous value, present value, next value)

For the missing boundary values, put the value None as shown below:

    [1, 2, 3, 4] -> [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, None)]

Then, using the implemented function, create iterators from the following objects:

    - [3, 5, 1, 8, 9, 4]
    - ['a', 'b', 'c', 'd', 'e']
    - 'Python'

In response, print these iterators as a list to the console as shown below.

Tip:

    #>>> help(itertools.tee)

    Help on built-in function tee in module itertools:

    tee(iterable, n=2, /)
        Returns a tuple of n independent iterators.

Expected result:

    [3, 5, 1, 8, 9, 4] -> [(None, 3, 5), (3, 5, 1), (5, 1, 8), (1, 8, 9), (8, 9, 4), (9, 4, None)]
    ['a', 'b', 'c', 'd', 'e'] -> [(None, 'a', 'b'), ('a', 'b', 'c'), ('b', 'c', 'd'), ('c', 'd', 'e'), ('d', 'e', None)]
    'Python' -> [(None, 'P', 'y'), ('P', 'y', 't'), ('y', 't', 'h'), ('t', 'h', 'o'), ('h', 'o', 'n'), ('o', 'n', None)]
"""
import itertools


def make_three(iterable):
    iter1, iter2, iter3 = itertools.tee(iterable, 3)
    next(iter3)
    return zip(
        itertools.chain([None], iter1),
        iter2,
        itertools.chain(iter3, [None]),
    )


print(f'[1, 2, 3, 4] -> {list(make_three([1, 2, 3, 4]))}')
print(
    f"['a', 'b', 'c', 'd', 'e'] -> "
    f"{list(make_three(['a', 'b', 'c', 'd', 'e']))}"
)
print(f"'Python' -> {list(make_three('Python'))}")
