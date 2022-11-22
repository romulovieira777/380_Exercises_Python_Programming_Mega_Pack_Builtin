"""
Exercise No. 02

Write a program that finds all three-digit numbers divisible by 11 and indivisible by 3 (use a for loop). Print the
result to the console as comma-separated values as shown below.

Expected result:

    11, 22, 44, 55, 77, 88
"""
result = []
for i in range(10, 100):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))
print(','.join(result))
