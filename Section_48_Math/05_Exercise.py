"""
Exercise No. 05

Using the built-in math module, calculate the probability to hit exactly:

    - 6 numbers
    - 5 numbers
    - 4 numbers
    - 3 numbers
    - 2 numbers
    - 1 number
    - 0 numbers

in the Big Lotek game. The game consists of drawing exactly six numbers from 1 to 49 inclusive.

In response, print the result to the console as shown below.

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

    hit: 6 prob: 0.0000071511%
    hit: 5 prob: 0.0018449900%
    hit: 4 prob: 0.0968619724%
    hit: 3 prob: 1.7650403867%
    hit: 2 prob: 13.2378029002%
    hit: 1 prob: 41.3019450485%
    hit: 0 prob: 43.5964975512%
"""
import math

# Solution I
for i in range(6, -1, -1):
    result = math.comb(6, i) * math.comb(43, 6 - i) / math.comb(49, 6)
    print(f"hit: {i} prob: {result * 100:.10f}%")


# Solution II
for k in range(0, 7)[::-1]:
    hits = math.comb(6, k) * math.comb(49 - 6, 6 - k)
    result = hits / math.comb(49, 6)
    print(f"hit: {k} prob: {result * 100:.10f}%")
