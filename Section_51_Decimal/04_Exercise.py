"""
Exercise No. 04

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

Rounding numbers.

Using the standard built-in function round() round the following number:

    1+.345

to two decimal places. Print the result to the console.

Then, using the built-in decimal module create a number with the same value, assign it to the variable number and also
round to two decimal places using the built-in function round(). Print the result to the console.

Using the decimal.Decimal.quantize() method round the number up (two decimal places, set the parameter rounding=decimal.
ROUND_UP) and print the result to the console.

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


    #>>> help(decimal.Decimal.quantize)

    Help on method_descriptor:

    quantize(self, /, exp, rounding=None, context=None)
        Return a value equal to the first operand after rounding and having the
        exponent of the second operand.

            #>>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')

        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.

        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.

        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.

Expected result:

    19.34
    19.34
    19.35
"""
import decimal

print(round(19.345, 2))

number = decimal.Decimal(19.345)
result = round(number, 2)
print(result)

result = decimal.Decimal(number).quantize(
    decimal.Decimal('0.00'), rounding=decimal.ROUND_UP
)

print(result)
