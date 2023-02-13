"""
Exercise No. 19

Using the built-in collections module and the namedtuple() function, a class called Student was implemented.

Three dictionaries are given:

    st1 = {'name': 'Kate', 'age': 20, 'specialization': 'mathematics'}
    st2 = {'name': 'Mike', 'age': 21, 'specialization': 'physics'}
    st3 = {'name': 'Bob', 'age': 21, 'specialization': 'information technology'}

Create Student objects from these dictionaries and assign them to the students list. Then, iterating through the
students list, print each student to the console.

Tip:

    #>>> help(namedtuple)

    Help on function namedtuple in module collections:

    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.

Expected result:

    Student(name='Kate', age=20, specialization='mathematics')
    Student(name='Mike', age=21, specialization='physics')
    Student(name='Bob', age=21, specialization='information technology')
"""
from collections import namedtuple

Student = namedtuple(typename='Student', field_names=['name', 'age', 'specialization'])

st1 = {"name": "Kate", "age": 20, "specialization": "mathematics"}
st2 = {"name": "Mike", "age": 21, "specialization": "physics"}
st3 = {
    "name": "Bob",
    "age": 21,
    "specialization": "information technology",
}

students = [Student(**st1), Student(**st2), Student(**st3)]

for student in students:
    print(student)
