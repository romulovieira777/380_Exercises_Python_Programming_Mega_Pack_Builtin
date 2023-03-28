"""
Exercise No. 23

Two lists are given. Then eurusd list includes the EUR/USD exchange rate at the end of each month from the beginning of
the year. The revenues list contains the monthly revenues earned by enterprise since the beginning of the year (the
number of items in both lists does not match).

    eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
    revenues = [20000, 21000, 20500, 18000, 22000, 25000]

Using the built-in zip class create an iterator that allows you to iterate simultaneously on corresponding elements of
eurusd and revenues lists.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>> help(zip)

    Help on class zip in module builtins:

    class zip(object)
        |  zip(*iterables) --> zip object
        |
        |  Return a zip object whose .__next__() method returns a tuple where
        |  the i-th element comes from the i-th iterable argument.  The .__next__()
        |  method continues until the shortest iterable in the argument sequence
        |  is exhausted and then it raises StopIteration.

Expected result:

    1.18425 20000
    1.17928 21000
    1.17211 20500
    1.17505 18000
"""
eurusd = [1.18425, 1.17928, 1.17211, 1.17505]
revenues = [20000, 21000, 20500, 18000, 22000, 25000]

for rate, revenue in zip(eurusd, revenues):
    print(rate, revenue)
