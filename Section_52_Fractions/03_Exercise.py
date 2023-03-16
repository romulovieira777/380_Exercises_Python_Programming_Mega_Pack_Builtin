"""
Exercise No. 03

Using the built-in fractions module, build a fraction:

    - 1/4

and assign to variable f1. Perform the following operations on the f1 fraction:

    - calculate the square
    - calculate the cube
    - using the built-in math module calculate the square root of the fraction (the math.sqrt() function will return a
      float object)
    - using the built-in math module calculate the square root of the fraction (return the result as a fractions.Fraction
      object)

Print the results of each operation to the console as shown below.

Tip:

    #>>> help(fractions.Fraction)

    Help on class Fraction in module fractions:

    class Fraction(numbers.Rational)
        |  Fraction(numerator=0, denominator=None, *, _normalize=True)
        |
        |  This class implements rational numbers.
        |
        |  In the two-argument form of the constructor, Fraction(8, 6) will
        |  produce a rational number equivalent to 4/3. Both arguments must
        |  be Rational. The numerator defaults to 0 and the denominator
        |  defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.
        |
        |  Fractions can also be constructed from:
        |
        |    - numeric strings similar to those accepted by the
        |      float constructor (for example, '-2.3' or '1e10')
        |
        |    - strings of the form '123/456'
        |
        |    - float and Decimal instances
        |
        |    - other Rational instances (including integers)

Expected result:

    1/4 ** 2 = 1/16
    1/4 ** 3 = 1/64
    math.sqrt(1/4) = 0.5
    math.sqrt(1/4) = 1/2
"""
from fractions import Fraction
import math

f1 = Fraction(1, 4)

print("{} ** 2 = {}".format(f1, f1 ** 2))
print("{} ** 3 = {}".format(f1, f1 ** 3))
print("math.sqrt({}) = {}".format(f1, math.sqrt(f1)))
print(f'math.sqrt(Fraction({f1}) = {Fraction(math.sqrt(f1))}')
