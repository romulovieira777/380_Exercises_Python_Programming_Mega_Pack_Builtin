"""
Exercise No. 24

Two lists are given. Then eurusd list includes the EUR/USD exchange rate at the end of each month from the beginning of
the year. The revenues list contains the monthly revenues earned by enterprise since the beginning of the year (the
number of items in both lists does not match).

    eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
    revenues = [20000, 21000, 20500, 18000, 22000, 25000]

Using the built-in module itertools and the zip_longest class create an iterator that allows you to iterate over the
corresponding elements of the eurusd and revenues lists simultaneously.

In response, print the elements of the results iterator to the console as shown below.


Tip:

    #>>> help(itertools.zip_longest)

    Help on class zip_longest in module itertools:

    class zip_longest(builtins.object)
     |  zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object
     |
     |  Return a zip_longest object whose .__next__() method returns a tuple where
     |  the i-th element comes from the i-th iterable argument.  The .__next__()
     |  method continues until the longest iterable in the argument sequence
     |  is exhausted and then it raises StopIteration.  When the shorter iterables
     |  are exhausted, the fillvalue is substituted in their place.  The fillvalue
     |  defaults to None or can be specified by a keyword argument.

Expected result:

    1.18425 20000
    1.17928 21000
    1.17211 20500
    1.17505 18000
    None 22000
    None 25000
"""
import itertools

eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]

for rate, revenue in itertools.zip_longest(eurusd, revenues):
    print(rate, revenue)
