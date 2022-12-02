"""
Exercise No. 01

Generate all even numbers from 2 to 18 inclusive. Then write each number on a separate line to the file called num.txt.

File num.txt after saving:

    2
    4
    6
    8
    10
    12
    14
    16
    18
"""

# Solution I
with open('../File/num.txt', 'w') as f:
    for i in range(2, 19, 2):
        f.write(str(i) + '\n')


# Solution II
numbers = list(range(1, 20))
even = [number for number in numbers if number % 2 == 0]

with open('../File/num.txt', 'w') as file:
    for number in even:
        file.write(str(number) + '\n')
