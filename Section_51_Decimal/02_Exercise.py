"""
Exercise No. 02

First, check the result of the following operation:

    0.1 + 0.2

You can expect 0.3, but Python will return:

    0.30000000000000004

Check on more operation:

    0.1 + 0.1 + 0.1 - 0.3

which, instead of the expected zero, returns a number very close to zero:

    5.551115123125783e-17

In fact that's the nature of a binary floating point representation. This is common issue in any programming language.
The precision of the calculations is very easy to lose if the numbers are not handled correctly. Python provides a
built-in decimal module with which we can manage decimal numbers in our programs to ensure precision, formatting and
performing calculations.

Using the built-in decimal module, set the precision to 40. Then create two decimal numbers 0.1 and 0.2 and calculate
their sum. Display the result to the console. Pay attention to the number of decimal places (precision).

Tip:

    #>>> help(decimal.Decimal)

    Help on class Decimal in module decimal:

    class Decimal(builtins.object)
        |  Decimal(value='0', context=None)
        |
        |  Construct a new Decimal object. 'value' can be an integer, string, tuple,
        |  or another Decimal object. If no value is given, return Decimal('0'). The
        |  context does not affect the conversion and is only passed to determine if
        |  the InvalidOperation trap is active.


    #>>> help(decimal.getcontext)

    Help on built-in function getcontext in module decimal:

    getcontext()
        Get the current default context.

Expected result:

    0.3000000000000000166533453693773481063545
"""
import decimal

decimal.getcontext().prec = 40

result = decimal.Decimal(0.1) + decimal.Decimal(0.2)

print(result)
