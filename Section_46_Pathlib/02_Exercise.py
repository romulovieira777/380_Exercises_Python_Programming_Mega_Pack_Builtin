"""
Exercise No. 02

Using the built-in pathlib module print the path to the home directory to the console.

Tip:

    # >>> help(pathlib.Path.home)

    Help on method home in module pathlib:

    home() method of builtins.type instance
        Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).

Expected result:

    /home/evaluator
"""
import pathlib

print(pathlib.Path.home())
