"""
Exercise No. 04

Using the built-in fractions and math modules calculate the approximation of pi and Euler's number in the form of a
fraction.

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

    pi = 884279719003555/281474976710656
    e = 6121026514868073/2251799813685248
"""
from fractions import Fraction
import math

pi = Fraction(math.pi)
e = Fraction(math.e)

print("pi = {}".format(pi))
print("e = {}".format(e))
