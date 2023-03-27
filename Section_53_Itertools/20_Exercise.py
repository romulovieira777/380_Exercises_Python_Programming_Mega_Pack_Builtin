"""
Exercise No. 20

Two data streams are given:

    stream1 = [0.5, 9.9, 8.53, 4.6, 5.58, 7.07, None, 4.5, 3.61, 9.31]
    stream2 = [3.75, 9.51, 7.32, None, 1.56, 1.56, 0.58, 8.66, 6.01, 7.08]

In case of an error in the data, the value None is sent. Create an iterator to iterate sequentially over both stream1
and stream2. If None is encountered in the data stream further values in this stream are ignored (only in a single
stream). Assign iterator to the results variable.

In response, print all elements of the results iterator to the.

Tip:

     #>>> help(itertools.takewhile)

    Help on class takewhile in module itertools:

    class takewhile(builtins.object)
     |  takewhile(predicate, iterable, /)
     |
     |  Return successive entries from an iterable as long as the predicate evaluates to true for each entry.


    #>>> help(itertools.chain)

    Help on class chain in module itertools:

    class chain(builtins.object)
     |  chain(*iterables) --> chain object
     |
     |  Return a chain object whose .__next__() method returns elements from the
     |  first iterable until it is exhausted, then elements from the next
     |  iterable, until all of the iterables are exhausted.

Expected result:

    0.5
    9.9
    8.53
    4.6
    5.58
    7.07
    3.75
    9.51
    7.32
"""
import itertools

stream1 = [0.5, 9.9, 8.53, 4.6, 5.58, 7.07, None, 4.5, 3.61, 9.31]
stream2 = [3.75, 9.51, 7.32, None, 1.56, 1.56, 0.58, 8.66, 6.01, 7.08]

results = itertools.chain(itertools.takewhile(bool, stream1), itertools.takewhile(bool, stream2))

for result in results:
    print(result)
