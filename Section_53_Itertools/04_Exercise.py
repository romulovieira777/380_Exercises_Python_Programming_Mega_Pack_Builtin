"""
Exercise No. 04

Using the built-in itertools module and the repeat class create an iterator that allows you to iterate infinitely over
the following '#' character. Then using a loop display the first 10 elements of the iterator to the console.

Tip:

    #>>> help(itertools.repeat)

    Help on class repeat in module itertools:

    class repeat(builtins.object)
     |  repeat(object [,times]) -> create an iterator which returns the object
     |  for the specified number of times.  If not specified, returns the object
     |  endlessly.

Expected result:

    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
"""
import itertools

# Solution I
counter = itertools.repeat('#')

for i in range(10):
    print(next(counter))


# Solution II
repeat = itertools.repeat('#')
results = [next(repeat) for i in range(10)]

for result in results:
    print(result)
