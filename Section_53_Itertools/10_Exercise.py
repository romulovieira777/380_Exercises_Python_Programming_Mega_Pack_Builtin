"""
Exercise No. 10

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

Using the built-in itertools module and the accumulate class create an iterator that allows you to iterate through a
series of cumulative minimum of closing price values from this dictionary (the Close key) and assign to the results
variable.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.accumulate)

    Help on class accumulate in module itertools:

    class accumulate(builtins.object)
     |  accumulate(iterable, func=None, *, initial=None)
     |
     |  Return series of accumulated sums (or other binary function results).

Expected result:

    1499.11
    1476.49
    1476.49
    1417.0
    1417.0
    1417.0
    1417.0
    1417.0
    1417.0
    1417.0
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

results = itertools.accumulate(tesla['Close'].values(), min)

for result in results:
    print(result)
