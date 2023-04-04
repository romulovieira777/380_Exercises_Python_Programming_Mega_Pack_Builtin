"""
Exercise No. 02

Using the built-in module functools and the partial class create from following function:

    def power(x, y):
        return x ** y

two functions named:

    - square
    - cube

Which will respectively return the square and the cube of the passed (functions take only one argument).

Only implement these functions.

Tip:

    #>>> help(functools.partial)

    Help on class partial in module functools:

    class partial(builtins.object)
        |  partial(func, *args, **keywords) - new function with partial application
        |  of the given arguments and keywords.
"""
from functools import partial


def power(x, y):
    return x ** y


square = partial(power, y=2)
cube = partial(power, y=3)

print(square(5))
print(cube(5))
