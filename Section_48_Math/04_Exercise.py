"""
Exercise No. 04

Using the built-in math module calculate the probability of hitting exactly six numbers out of 49 numbers (from 1 to 49
inclusive). Print the result as shown below.

Example hit:

    23, 2, 5, 14, 43, 3

Tip:

    # >>> help(math.comb)

    Help on built-in function comb in module math:

    comb(n, k, /)
    Number of ways to choose k items from n items without repetition and without order.

    Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
    to zero when k > n.

    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of the
    expression (1 + x)**n.

    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.

Expected result:

    0.0000071511%
"""
import math

result = 1 / math.comb(49, 6)

print(f"{result * 100:.10f}%")
