"""
Exercise No. 06

The following tuple is given:

    techs = ('python', 'java', 'sql', 'aws')

Sor this tuple from a to z and print it to the console.

Tip: Tuple are immutable. You have to create a new one.

Expected result:

    ('aws', 'java', 'python', 'sql')
"""
techs = ('python', 'java', 'sql', 'aws')

techs = tuple(sorted(techs))
print(techs)
