"""
Exercise No. 02

Using the Template class from the string built-in module, create an e-mail template. Sample e-mail below:
    Hello John,

    Thank you for visiting our website.
    Team, XYZ.

The template should allow you to change the name in the first line of the message.

Then for the following list:
    names = ['John', 'Paul', 'Lisa', 'Michael']

Print the content of personalized e-mails to the console. Separate each e-mail with a line consisting of 35 characters
"-" as shown below.

Tip:
    #>>> help(string.Template)

    Help on class Template in module string:

    class Template(builtins.object)
     |  Template(template)
     |
     |  A string class for supporting $-substitutions.

Expected result:
    Hello John,

    Thank you for visiting our website.
    Team, XYZ
    -----------------------------------
    Hello Paul,

    Thank you for visiting our website.
    Team, XYZ
    -----------------------------------
    Hello Lisa,

    Thank you for visiting our website.
    Team, XYZ
    -----------------------------------
    Hello Michael,

    Thank you for visiting our website.
    Team, XYZ
    -----------------------------------
"""
from string import Template

names = ['John', 'Paul', 'Lisa', 'Michael']

email = """Hello $name,
 
Thank you for visiting our website.
Team, XYZ"""

template = Template(email)

for name in names:
    print(template.substitute(name=name))
    print('-' * 35)
