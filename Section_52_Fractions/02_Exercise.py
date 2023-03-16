"""
Exercise No. 02

Using the built-in fractions module create two fractions:

    - 1/4
    - 1/2

and assign to the variables f1 and f2 respectively. Perform the following operations on the fractions f1 and f2:

    - addition
    - subtraction
    - multiplication
    - division

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

    1/4 + 1/2 = 3/4
    1/4 - 1/2 = -1/4
    1/4 * 1/2 = 1/8
    1/4 / 1/2 = 1/2
"""
from fractions import Fraction

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

print("{} + {} = {}".format(f1, f2, f1 + f2))
print("{} - {} = {}".format(f1, f2, f1 - f2))
print("{} * {} = {}".format(f1, f2, f1 * f2))
print("{} / {} = {}".format(f1, f2, f1 / f2))
