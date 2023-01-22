"""
Exercise No.05

Using the built-in os module create images directory in your working directory. Then go to the images directory and
print the current path to the working directory.

Tip:
    #>>> help(os.getcwd)

    Help on built-in function mkdir in module nt:

    mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

        The mode argument is ignored on Windows.


    #>>> help(os.chdir)

    Help on built-in function chdir in module nt:

    chdir(path)
        Change the current working directory to the specified path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
Expected result:
    /eval/images
"""
import os

os.mkdir('images')
os.chdir('images')
print(os.getcwd())
