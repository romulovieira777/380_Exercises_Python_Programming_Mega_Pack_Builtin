"""
Exercise No. 19

The following fname_paths list is given:

    /eval/media/music/playlist_01/01_music.mp3
    /eval/media/music/playlist_01/02_music.mp3
    /eval/media/music/playlist_01/03_music.wav
    /eval/media/music/playlist_01/04_music.mp3
    /eval/media/music/playlist_01/05_music.mp3
    /eval/media/music/playlist_02/01_music.mp3
    /eval/media/music/playlist_02/02_music.mp3
    /eval/media/music/playlist_02/03_music.mp3
    /eval/media/music/playlist_02/04_music.wav
    /eval/media/music/playlist_02/05_music.mp3
    /eval/media/music/playlist_03/01_music.mp3
    /eval/media/music/playlist_03/02_music.mp3
    /eval/media/music/playlist_03/03_music.mp3
    /eval/media/music/playlist_03/04_music.mp3
    /eval/media/music/playlist_03/05_music.mp3
    /eval/media/music/playlist_04/01_music.mp3
    /eval/media/music/playlist_04/02_music.wav
    /eval/media/music/playlist_04/03_music.mp3
    /eval/media/music/playlist_04/04_music.wav
    /eval/media/music/playlist_04/05_music.wav
    /eval/media/music/playlist_05/01_music.mp3
    /eval/media/music/playlist_05/02_music.mp3
    /eval/media/music/playlist_05/03_music.wav
    /eval/media/music/playlist_05/04_music.wav
    /eval/media/music/playlist_05/05_music.wav
    /eval/media/music/playlist_06/01_music.mp3
    /eval/media/music/playlist_06/02_music.mp3
    /eval/media/music/playlist_06/03_music.wav
    /eval/media/music/playlist_06/04_music.mp3
    /eval/media/music/playlist_06/05_music.mp3

Create all files with paths defined in the fname_paths list.

In response print all paths to files with extension .mp3 sorted alphabetically from
/eval/media/music/playlist_01directrory.

Tip:

    # >>> help(pathlib.Path.glob)

    Help on function glob in module pathlib:

    glob(self, pattern)
        Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given pattern.

Expected result:

    /eval/media/music/playlist_01/01_music.mp3
    /eval/media/music/playlist_01/02_music.mp3
    /eval/media/music/playlist_01/04_music.mp3
    /eval/media/music/playlist_01/05_music.mp3
"""
from pathlib import Path
import random

random.seed(42)
paths = [
    Path.cwd() / f"media/music/playlist_{str(i).zfill(2)}"
    for i in range(1, 7)
]

for path in paths:
    path.mkdir(parents=True)

paths_dict = {
    path: [
        f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}"
        for i in range(1, 6)
    ]
    for path in paths
}

fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))

for fname_path in fname_paths:
    fname_path.touch()

path = Path.cwd() / "media/music/playlist_01"
for path in sorted(list(path.glob("*.mp3"))):
    print(path)
