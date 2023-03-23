"""
Exercise No. 14

The following dictionary is given:

    tesla = {
        'Close': {
            0: 1499.11,
            1: 1476.49,
            2: 1539.6,
            3: 1417.0,
            4: 1513.07,
            5: 1592.33,
            6: 1568.36,
            7: 1643.0,
            8: 1500.84,
            9: 1500.64,
        },
        'Date': {
            0: '2020-07-29',
            1: '2020-07-28',
            2: '2020-07-27',
            3: '2020-07-24',
            4: '2020-07-23',
            5: '2020-07-22',
            6: '2020-07-21',
            7: '2020-07-20',
            8: '2020-07-17',
            9: '2020-07-16',
        },
        'Volume': {
            0: 9426893,
            1: 15808700,
            2: 16048669,
            3: 19396616,
            4: 24328504,
            5: 14161080,
            6: 16157280,
            7: 17121367,
            8: 9329972,
            9: 14300785,
        },
    }

Using the built-in itertools module and the islice class create an iterator to iterate through ever second date from
this dictionary (Date key) and assign to the variable results.

In response, print the elements of the results iterator to the console as shown below.

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

    2020-07-29
    2020-07-27
    2020-07-23
    2020-07-21
    2020-07-17
"""
import itertools

tesla = {
    'Close': {
        0: 1499.11,
        1: 1476.49,
        2: 1539.6,
        3: 1417.0,
        4: 1513.07,
        5: 1592.33,
        6: 1568.36,
        7: 1643.0,
        8: 1500.84,
        9: 1500.64,
    },
    'Date': {
        0: '2020-07-29',
        1: '2020-07-28',
        2: '2020-07-27',
        3: '2020-07-24',
        4: '2020-07-23',
        5: '2020-07-22',
        6: '2020-07-21',
        7: '2020-07-20',
        8: '2020-07-17',
        9: '2020-07-16',
    },
    'Volume': {
        0: 9426893,
        1: 15808700,
        2: 16048669,
        3: 19396616,
        4: 24328504,
        5: 14161080,
        6: 16157280,
        7: 17121367,
        8: 9329972,
        9: 14300785,
    },
}

# Solution I
for date in itertools.islice(tesla['Date'].values(), 0, None, 2):
    print(date)


# Solution II
results = itertools.islice(tesla['Date'].values(), 0, None, 2)

for date in results:
    print(date)
