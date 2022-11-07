"""
Exercise No. 03

The following codes are giuven:

    code1 = 'FVNISJND-XX-2020'
    code2 = 'FVNISJND-XY-2019'

Using the appropriate method, check if the codes end in '2020'. Print the result to the console as shown below.

Expected result:

    code1: True
    code2: False
"""
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f"code1: {code1.endswith('2020')}")
print(f"code2: {code2.endswith('2020')}")
