"""
Exercise No. 06

The following tuple is given (name, age):

    info = (('Monica', 19), ('Tom', 21), ('John', 18))

Sort this tuple:
    - ascending by age
    - descending by name

And print the result to the console as shown below.

Expected result:

    Ascending: (('John', 18), ('Monica', 19), ('Tom', 21))
    Descending: (('Tom', 21), ('Monica', 19), ('John', 18))
"""
info = (('Monica', 19), ('Tom', 21), ('John', 18))

ascending = sorted(info, key=lambda x: x[1])
descending = sorted(info, key=lambda x: x[0], reverse=True)

print(f"Ascending: {tuple(ascending)}")
print("Descending:", tuple(descending))
