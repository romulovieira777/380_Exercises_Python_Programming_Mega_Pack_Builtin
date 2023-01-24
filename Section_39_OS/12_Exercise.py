"""
Exercise No. 12

The list of absolute directory paths is given:
    [
        "/eval/dir_01",
        "/eval/dir_02",
        "/eval/dir_03",
        "/eval/dir_04",
        "/eval/dir_05",
        "/eval/dir_06",
        "/eval/dir_07",
        "/eval/dir_08",
        "/eval/dir_09",
        "/eval/dir_10",
        "/eval/dir_11",
        "/eval/dir_12",
        "/eval/dir_13",
    ]

Create the given directories using the built-in os module. Then remove the directory dir_13.

In response, print the sorted directory names from the working directory with exactly six characters long.

Tip:
    #>>> help(os.rmdir)

    Help on built-in function rmdir in module nt:

    rmdir(path, *, dir_fd=None)
        Remove a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

Expected result:
    ['dir_01', 'dir_02', 'dir_03', 'dir_04', 'dir_05', 'dir_06', 'dir_07', 'dir_08', 'dir_09', 'dir_10', 'dir_11',
     'dir_12']
"""
import os

# Solution I
paths = [os.path.join(os.getcwd(), f"dir_{str(i).zfill(2)}") for i in range(1, 14)]
for path in paths:
    os.mkdir(path)
os.rmdir(paths[-1])
print(sorted([path for path in os.listdir(os.getcwd()) if len(path) == 6]))


# Solution II
paths = [
    os.path.join(os.getcwd(), f"dir_{str(i).zfill(2)}")
    for i in range(1, 14)
]

for path in paths:
    if not os.path.exists(path):
        os.mkdir(path)

os.rmdir(os.path.join(os.getcwd(), "dir_13"))
fnames = [fname for fname in sorted(os.listdir()) if len(fname) == 6]
print(fnames)
