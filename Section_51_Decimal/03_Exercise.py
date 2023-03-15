"""
Exercise No. 03

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

Precision control for a single operation.

Using the built-in decimal module and the function decimal.localcontext() create a local context and set the precision
locally to 40. Then create two decimal numbers 0.1 and 0.2 and calculate their sum. Display the result to the console.
Perform the same calculation again outside the local context and also display the result to the console.

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

    localcontext(ctx=None)
        Return a context manager that will set the default context to a copy of ctx
        on entry to the with-statement and restore the previous default context when
        exiting the with-statement. If no context is specified, a copy of the current
        default context is used.

Expected result:

    0.3000000000000000166533453693773481063545
    0.3000000000000000166533453694
"""
import decimal

with decimal.localcontext() as ctx:
    ctx.prec = 40

    result = decimal.Decimal(0.1) + decimal.Decimal(0.2)

    print(result)

result = decimal.Decimal(0.1) + decimal.Decimal(0.2)

print(result)
