"""
Exercise No. 03

In mathematics, the symmetric difference of two sets is the set of elements which are in either of the sets, but not in
their intersection.

Two following sets are given:

    A = {2, 4, 6, 8}
    B = {4, 10}

Using the appropriate method, extract the symmetric difference of the sets A and B and print the result to the console
as shown below.

Expected result:

    {2, 6, 8, 10}
"""

# Solution I
A = {2, 4, 6, 8}
B = {4, 10}

print(f"Symmetric difference: {A ^ B}")


# Solution II
A = {2, 4, 6, 8}
B = {4, 10}

sym_diff = A.symmetric_difference(B)
print(f"Symmetric difference: {sym_diff}")
