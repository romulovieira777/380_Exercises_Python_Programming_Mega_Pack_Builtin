"""
Exercise No. 17

The following paths list is given:

    [
        PosixPath("eval/media/music/playlist_01"),
        PosixPath("eval/media/music/playlist_02"),
        PosixPath("eval/media/music/playlist_03"),
        PosixPath("eval/media/music/playlist_04"),
        PosixPath("eval/media/music/playlist_05"),
        PosixPath("eval/media/music/playlist_06"),
    ]

Each of the directories in the paths list was created.

Create a directory that takes as keys successive paths from the paths list, and the values will be a list of five files
with the names 01_music - 05_music with the extension .mp3 or .wav. Set the file extensions randomly with choice()
function from the random built-in module. Assign the dictionary to the paths_dict variable.

In response, print the paths_dict dictionary using the pprint() function from the pprint module to the console.

Expected result:

    {PosixPath('/eval/media/music/playlist_01'): ['01_music.mp3',
                                                  '02_music.mp3',
                                                  '03_music.wav',
                                                  '04_music.mp3',
                                                  '05_music.mp3'],
     PosixPath('/eval/media/music/playlist_02'): ['01_music.mp3',
                                                  '02_music.mp3',
                                                  '03_music.mp3',
                                                  '04_music.wav',
                                                  '05_music.mp3'],
     PosixPath('/eval/media/music/playlist_03'): ['01_music.mp3',
                                                  '02_music.mp3',
                                                  '03_music.mp3',
                                                  '04_music.mp3',
                                                  '05_music.mp3'],
     PosixPath('/eval/media/music/playlist_04'): ['01_music.mp3',
                                                  '02_music.wav',
                                                  '03_music.mp3',
                                                  '04_music.wav',
                                                  '05_music.wav'],
     PosixPath('/eval/media/music/playlist_05'): ['01_music.mp3',
                                                  '02_music.mp3',
                                                  '03_music.wav',
                                                  '04_music.wav',
                                                  '05_music.wav'],
     PosixPath('/eval/media/music/playlist_06'): ['01_music.mp3',
                                                  '02_music.mp3',
                                                  '03_music.wav',
                                                  '04_music.mp3',
                                                  '05_music.mp3']}
"""
from pathlib import Path
from pprint import pprint
import random

random.seed(42)

paths = [Path.cwd() / f"media/music/playlist_{str(i).zfill(2)}" for i in range(1, 7)]

for path in paths:
    path.mkdir(parents=True)

paths_dict = {
    path: [
        f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}"
        for i in range(1, 6)
    ]
    for path in paths
}

pprint(paths_dict)
