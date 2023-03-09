"""
Exercise No. 02

The Euler's number is defined as the limit of the following sequence:

    an = (1 + 1/n)**n

with n approaches infinity (n > 0). Create a function called calculate_seq() that takes one argument n and calculates
the n-th element of this sequence.

In response, print the values for the first twenty elements of this sequence as shown below.

Expected result:

    2.0
    2.25
    2.37037037037037
    2.44140625
    2.4883199999999994
    2.5216263717421135
    2.546499697040712
    2.565784513950348
    2.5811747917131984
    2.5937424601000023
    2.6041990118975287
    2.613035290224676
    2.6206008878857308
    2.6271515563008685
    2.6328787177279187
    2.6379284973666
    2.64241437518311
    2.6464258210976865
    2.650034326640442
    2.653297705144422
"""


# Solution I


def calculate_seq(n):
    return (1 + 1 / n) ** n


for i in range(1, 21):
    print(calculate_seq(i))


# Solution II


def calculate_seq(n):
    return (1 + 1 / n) ** n


sequence = [calculate_seq(i) for i in range(1, 21)]

for item in sequence:
    print(item)
