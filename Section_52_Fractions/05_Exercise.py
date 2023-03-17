"""
Exercise No. 05

Using the built-in fractions and math modules calculate the approximation of pi and Euler's number in the form of a
fraction. Using the limit_denominator() function limit the size of the denominator to:

    - 10
    - 100
    - 1000

Print the result to the console as shown below. Set the indentation by inserting a tab character \t.

Tip:

    #>>> help(fractions.Fraction.limit_denominator)

    Help on function limit_denominator in module fractions:

    limit_denominator(self, max_denominator=1000000)
        Closest Fraction to self with denominator at most max_denominator.

        #>>> Fraction('3.141592653589793').limit_denominator(10)
        Fraction(22, 7)
        #>>> Fraction('3.141592653589793').limit_denominator(100)
        Fraction(311, 99)
        #>>> Fraction(4321, 8765).limit_denominator(10000)
        Fraction(4321, 8765)

Expected result:

    limit: 10
    	pi = 22/7
    	e = 19/7
    limit: 100
    	pi = 311/99
    	e = 193/71
    limit: 1000
    	pi = 355/113
    	e = 1457/536
"""
from fractions import Fraction
import math

# Solution I
pi = Fraction(math.pi)
e = Fraction(math.e)

print("limit: 10")
print("\tpi = {}".format(pi.limit_denominator(10)))
print("\te = {}".format(e.limit_denominator(10)))
print("limit: 100")
print("\tpi = {}".format(pi.limit_denominator(100)))
print("\te = {}".format(e.limit_denominator(100)))
print("limit: 1000")
print("\tpi = {}".format(pi.limit_denominator(1000)))
print("\te = {}".format(e.limit_denominator(1000)))


# Solution II
pi = Fraction(math.pi)
e = Fraction(math.e)

for limit in [10, 100, 1000]:
    print("limit: {}".format(limit))
    print("\tpi = {}".format(pi.limit_denominator(limit)))
    print("\te = {}".format(e.limit_denominator(limit)))
