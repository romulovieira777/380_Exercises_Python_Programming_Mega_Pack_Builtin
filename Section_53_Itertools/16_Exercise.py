"""
Exercise No. 16

Using the built-in itertools modules string and itertools with the islice class create an iterator to iterate over every
third lowercase letter (ascii_lowercase) and assign to the variable results.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.islice)

    Help on class islice in module itertools:

    class islice(builtins.object)
        |  islice(iterable, stop) --> islice object
        |  islice(iterable, start, stop[, step]) --> islice object
        |
        |  Return an iterator whose next() method returns selected values from an
        |  iterable.  If start is specified, will skip all preceding elements;
        |  otherwise, start defaults to zero.  Step defaults to one.  If
        |  specified as another value, step determines how many values are
        |  skipped between successive calls.  Works like a slice() on a list
        |  but returns an iterator.

Expected result:

    ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y']
"""
import itertools
import string

results = itertools.islice(string.ascii_lowercase, 0, None, 3)

print(list(results))
