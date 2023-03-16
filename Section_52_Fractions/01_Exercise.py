"""
Exercise No. 01

Using the built-in fractions module create the fraction 13/15 and assign it to the variable frac.

In response, print frac variable to the console. Then its numerator and denominator as shown below.

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

    fraction: 13/15
    numerator: 13
    denominator: 15
"""
from fractions import Fraction

frac = Fraction(13, 15)

print("fraction: {}".format(frac))
print("numerator: {}".format(frac.numerator))
print("denominator: {}".format(frac.denominator))
