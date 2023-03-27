"""
Exercise No. 21

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

Using the built-in itertools module and the dropwhile class create an iterator that allows iterating through the closing
prices from this dictionary (the Close key) from the moment a price greater than 1500 is found and assign to the results
variable.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.dropwhile)

    Help on class dropwhile in module itertools:

    class dropwhile(builtins.object)
     |  dropwhile(predicate, iterable, /)
     |
     |  Drop items from the iterable while predicate(item) is true.
     |
     |  Afterwards, return every element until the iterable is exhausted.

Expected result:

    1539.6
    1417.0
    1513.07
    1592.33
    1568.36
    1643.0
    1500.84
    1500.64
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

results = itertools.dropwhile(lambda price: price <= 1500, tesla['Close'].values())

print(*results, sep='\n')
