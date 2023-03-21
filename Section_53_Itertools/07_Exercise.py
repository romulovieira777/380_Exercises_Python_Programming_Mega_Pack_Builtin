"""
Exercise No. 07

Using the built-in itertools module and the permutations class create an iterator that iterates through all permutations
of the list:

    names = ['Bob', 'Mark', 'Guido']

Print the result to the console as shown below.

Tip:

    #>>> help(itertools.permutations)

    Help on class permutations in module itertools:

    class permutations(builtins.object)
     |  permutations(iterable, r=None)
     |
     |  Return successive r-length permutations of elements in the iterable.
     |
     |  permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

Expected result:

    ('Bob', 'Mark', 'Guido')
    ('Bob', 'Guido', 'Mark')
    ('Mark', 'Bob', 'Guido')
    ('Mark', 'Guido', 'Bob')
    ('Guido', 'Bob', 'Mark')
    ('Guido', 'Mark', 'Bob')
"""
import itertools

# Solution I
names = ['Bob', 'Mark', 'Guido']

for name in itertools.permutations(names):
    print(name)


# Solution II
names = ['Bob', 'Mark', 'Guido']

results = itertools.permutations(names)

for result in results:
    print(result)
