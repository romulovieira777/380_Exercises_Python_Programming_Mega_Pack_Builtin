"""
Exercise No. 01

The following values are given:

    values = [1.0, '2.0', '2', None, False, True]

Using the built-in numbers module and the isinstance() function check if the elements in the list are numbers.

In response, print the element, its type, and the result of the isinstance() function as shown below.

Tip:

    #>>> help(numbers.Number)

    Help on class Number in module numbers:

    class Number(builtins.object)
     |  All numbers inherit from this class.
     |
     |  If you just want to check if an argument x is a number, without
     |  caring what kind, use isinstance(x, Number).

Expected result:

    2.0   : <class 'float'>    : True
    2     : <class 'int'>      : True
    2.0   : <class 'str'>      : False
    2     : <class 'str'>      : False
    None  : <class 'NoneType'> : False
    False : <class 'bool'>     : True
    True  : <class 'bool'>     : True
"""
import numbers

values = [1.0, '2.0', '2', None, False, True]

for value in values:
    print(f'{str(value).ljust(6)}: {str(type(value)).ljust(18)} : '
          f'{isinstance(value, numbers.Number)}')
