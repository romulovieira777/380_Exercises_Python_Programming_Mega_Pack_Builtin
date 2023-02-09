"""
Exercise No. 17

Using the built-in collections module and the namedtuple() function create a class called Student to store data about
students. Set the following attributes / fields:

    - 'name'
    - 'age'
    - 'specialization'

Then create three students with the given data:

    Student('Mike', 21, 'physics'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')

And assign it to the students list. Iterate through the students list and print basic information about the students to
the console as shown below.

Tip:

    #>>> help(namedtuple)

    Help on function namedtuple in module collections:

    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.

Expected result:

    Mike : 21: physics
    Kate : 20: mathematics
    Bob  : 21: information technology
"""
from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = [
    Student('Mike', 21, 'physics'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
]

for student in students:
    print(f'{student.name:5}: {student.age}: {student.specialization}')
