"""
Exercise No. 02

Using the built-in os module, print the to the console a list containing the names of all files in the working directory.

Tip:
    #>>> help(os.listdir)

    Help on built-in function listdir in module nt:

    listdir(path=None)
        Return a list containing the names of the files in the directory.

        path can be specified as either str, bytes, or a path-like object.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
Expected result:
    ['exercise.py', 'run_unittest.py', '__pycache__', 'evaluate.py', 'result.py']
"""
import os

print(os.listdir())
