"""
Exercise No. 01

Write a program that compares two lists and returns True if the lists contain at least one of the same element.
Otherwise, it will return False. Use break statement in the solution and print the result to the console.

Lists:

    list1 = [1, 2, 0]
    list2 = [4, 5, 6, 1]

Expected result:

    True
"""

# Solution I
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

for i in list1:
    for j in list2:
        if i == j:
            print(True)
            break


# Solution II
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

for item1 in list1:
    if item1 in list2:
        result = True
        break
print(result)
