"""
Exercise No. 03

Suppose that in a given population, height can be described by a normal distribution with the following parameters:

    - expected value: 170 cm
    - standard deviation: 15 cm

Using the built-in statistics module calculate the probability that a randomly selected person from this population will
have a height within the range [170, 180). Round the result to two decimal places and print to the console as shown
below.

Tip:

    #>>> help(statistics.NormalDist.cdf)

    Help on function cdf in module statistics:

    cdf(self, x)
        Cumulative distribution function.  P(X <= x)

Expected result:

    Probability: 24.75%
"""
from statistics import NormalDist

# Solution I
mu = 170
sigma = 15
x = 180

nd = NormalDist(mu, sigma)
result = nd.cdf(x) - nd.cdf(mu)
print(f'Probability: {result * 100:.2f}%')


# Solution II
height = NormalDist(mu=170, sigma=15)
prob = round(height.cdf(180) - height.cdf(170), 4)

print(f'Probability: {prob * 100}%')
