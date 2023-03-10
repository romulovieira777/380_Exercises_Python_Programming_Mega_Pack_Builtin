"""
Exercise No. 06

The following set of file names is given:

    fnames = {
        "01_stream.txt",
        "02_stream.txt",
        "03_stream.txt",
        "04_stream.txt",
        "05_stream.txt",
    }

Using the built-in math module count how many ways you can set the names of the given files in the queue.

Tip:

    # >>> help(math.factorial)

    Help on built-in function factorial in module math:

    factorial(...)
        factorial(x) -> Integral

        Find x!. Raise a ValueError if x is negative or non-integral.

Expected result:

    120
"""
import math

fnames = {
    "01_stream.txt",
    "02_stream.txt",
    "03_stream.txt",
    "04_stream.txt",
    "05_stream.txt",
}

result = math.factorial(len(fnames))

print(result)
