"""
Exercise No. 03

Tuples are immutable. The following tuple is given:

    members = (('Kate', 23), ('Tom', 19))

Insert a tuple ('John', 26) between Kate and Tom as shown below. Print the result to the console.

Tip: You have to create a new tuple.

Expected result:

    (('Kate', 23), ('John', 26), ('Tom', 19))
"""

# Solution I
members = (('Kate', 23), ('Tom', 19))

members = members[:1] + (('John', 26),) + members[1:]
print(members)


# Solution II
members = (('Kate', 23), ('Tom', 19))

members = (members[0], ('John', 26), members[1])
print(members)
