"""
Exercise No. 20

Using the built-in collections module and the namedtuple() function, a class called Student was implemented.

The students.txt file containing student data is attached to this exercise.

    {'name': 'Kate', 'age': 20, 'specialization': 'mathematics'}
    {'name': 'Mike', 'age': 21, 'specialization': 'physics'}
    {'name': 'Bob', 'age': 21, 'specialization': 'information technology'}

Load the file students.txt and create Student objects from the given dictionaries and assign them to the students list.

Then print the students list to the console.

Tip:

    #>>> help(namedtuple)

    Help on function namedtuple in module collections:

    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.

Expected result:

    [
        Student(name='Kate', age=20, specialization='mathematics'), Student(name='Mike', age=21, specialization='physics'),
        Student(name='Bob', age=21, specialization='information technology')
    ]
"""
from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

# Solution I
with open(file='../Files/students.txt', mode='r', encoding='utf-8') as file:
    students = [Student(**eval(line)) for line in file]

print(students)


# Solution II
students = []

with open('../Files/students.txt', 'r') as file:
    lines = [eval(line.strip()) for line in file.readlines()]
    for line in lines:
        students.append(Student(**line))

print(students)
