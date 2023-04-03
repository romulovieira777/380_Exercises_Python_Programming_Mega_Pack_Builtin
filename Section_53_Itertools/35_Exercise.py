"""
Exercise No. 35

Using the built-in itertools module and the product class create an iterator that allows you to iterate over the
following elements:

    ('a', 1)
    ('a', 2)
    ('a', 3)
    ('b', 1)
    ('b', 2)
    ('b', 3)
    ('c', 1)
    ('c', 2)
    ('c', 3)

and assign to the iterator variable. Then, using the tee class create two iterators from the iterator and assign it to
the variables iter1 and iter2 respectively.

In response, print the elements of the iterators: iter1 and iter2 to the console as a list as shown below.

Tip:

    #>>> help(itertools.product)

    Help on class product in module itertools:

    class product(builtins.object)
        |  product(*iterables, repeat=1) --> product object
        |
        |  Cartesian product of input iterables.  Equivalent to nested for-loops.
        |
        |  For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
        |  The leftmost iterators are in the outermost for-loop, so the output tuples
        |  cycle in a manner similar to an odometer (with the rightmost element changing
        |  on every iteration).
        |
        |  To compute the product of an iterable with itself, specify the number
        |  of repetitions with the optional repeat keyword argument. For example,
        |  product(A, repeat=4) means the same as product(A, A, A, A).
        |
        |  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
        |  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

    #>>> help(itertools.tee)

    Help on built-in function tee in module itertools:

    tee(iterable, n=2, /)
        Returns a tuple of n independent iterators.

Expected result:

    [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
    [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
"""
import itertools

iterable = itertools.product('abc', range(1, 4))
iter1, iter2 = itertools.tee(iterable, 2)

print(list(iter1))
print(list(iter2))
