"""
Exercise No. 03

The Euler number is defined as the limit of the following sequence:

    an = (1 + 1 / n) ** n

with n approaches infinity (n > 0). Create a function called calculate_seq() was implemented to calculate the n-th
element of this sequence.

Using the built-in module math determine the index of the element for which the value is close to the Euler's number.
Use the math.isclose() function with the rel_tol = 1e-06 argument.

In response print the smallest index of a sequence for which, with the tolerance level, the value is close to the Euler's
number.

Tip:

    # >>> help(math.isclose)

    Help on built-in function isclose in module math:

    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool

        Determine whether two floating point numbers are close in value.

           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values

        Return True if a is close in value to b, and False otherwise.

        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.

        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.

Expected result:

    499982
"""
import math


def calculate_seq(n):
    return (1 + 1 / n) ** n


# Solution I
for i in range(1, 1000000):
    if math.isclose(calculate_seq(i), math.e, rel_tol=1e-06):
        print(i)
        break


# Solution II
i = 1
while True:
    item = calculate_seq(i)
    if math.isclose(item, math.e, rel_tol=1e-06):
        print(i)
        break
    i += 1
