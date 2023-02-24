""""
Exercise No. 01

Using the built-in pathlib module print the path to the working directory to the console.

Tip:

    # >>> help(pathlib.Path.cwd)

    Help on method cwd in module pathlib:

    cwd() method of builtins.type instance
        Return a new path pointing to the current working directory
        (as returned by os.getcwd()).

Expected result:

    /eval
"""
import pathlib

print(pathlib.Path.cwd())
