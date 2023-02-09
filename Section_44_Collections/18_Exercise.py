"""
Exercise No. 18

Using the built-in collections module and the namedtuple() function, a class called Student was implemented.

Then four students with the given data were created:

    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')

And assigned to the students list.

Sort the students list by age (age attribute) in ascending order. In response, print the students list to the console.

Tip:

    #>>> help(namedtuple)

    Help on function namedtuple in module collections:

    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.

Expected result:

    [Student(name='Kate', age=20, specialization='mathematics'), Student(name='Mike', age=21, specialization='physics'),
     Student(name='Bob', age=21, specialization='information technology'),
     Student(name='Mark', age=22, specialization='biology')]
"""
from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

students = [
    Student('Mike', 21, 'physics'),
    Student('Mark', 22, 'biology'),
    Student('Kate', 20, 'mathematics'),
    Student('Bob', 21, 'information technology')
]

students.sort(key=lambda student: student.age)

print(students)
