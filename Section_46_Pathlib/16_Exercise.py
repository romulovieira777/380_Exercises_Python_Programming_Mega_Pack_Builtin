"""
Exercise No. 16

Using the pathlib built-in module create the following list:

    [
        PosixPath("eval/media/music/playlist_01"),
        PosixPath("eval/media/music/playlist_02"),
        PosixPath("eval/media/music/playlist_03"),
        PosixPath("eval/media/music/playlist_04"),
        PosixPath("eval/media/music/playlist_05"),
        PosixPath("eval/media/music/playlist_06"),
        PosixPath("eval/media/music/playlist_07"),
        PosixPath("eval/media/music/playlist_08"),
        PosixPath("eval/media/music/playlist_09"),
        PosixPath("eval/media/music/playlist_10"),
    ]

and assign it to paths variable (try to automate it). Then create these directories.

In response, print all directories in the eval/media/music directory sorted alphabetically as shown below.

Expected result:

    /eval/media/music/playlist_01
    /eval/media/music/playlist_02
    /eval/media/music/playlist_03
    /eval/media/music/playlist_04
    /eval/media/music/playlist_05
    /eval/media/music/playlist_06
    /eval/media/music/playlist_07
    /eval/media/music/playlist_08
    /eval/media/music/playlist_09
    /eval/media/music/playlist_10
"""
from pathlib import Path

# Solution I
paths = [Path.cwd() / f"media/music/playlist_{str(i).zfill(2)}" for i in range(1, 11)]

for path in paths:
    path.mkdir(parents=True)

for dir in sorted(Path.cwd().joinpath("media/music").iterdir()):
    print(dir)


# Solution II
paths = [Path.cwd() / f"media/music/playlist_{str(i).zfill(2)}" for i in range(1, 11)]

for path in paths:
    path.mkdir(parents=True)

dirs = sorted(Path.cwd().joinpath("media/music").iterdir())

for dir in dirs:
    print(dir)
