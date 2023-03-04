"""
Exercise No. 21

Using the built-in pathlib module, all files with paths defined in the fname_paths list were created:

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

Using the built-in pathlib module display the number of files with extensions .mp3 and .wav in the directory
/eval/media/music/playlist_05 as shown below.

Tip:

    # >>> help(pathlib.Path.glob)

    Help on function glob in module pathlib:

    glob(self, pattern)
        Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given pattern.

Expected result:

    fnames_mp3: 2
    fnames_wav: 3
"""
from pathlib import Path
from pprint import pprint
import random


random.seed(42)
paths = [Path.cwd() / f'media/music/playlist_{str(i).zfill(2)}' for i in range(1, 7)]

for path in paths:
    path.mkdir(parents=True)

paths_dict = {path: [f"{str(i).zfill(2)}_music.{random.choice(['mp3', 'wav'])}"
                     for i in range(1, 6)] for path in paths}

fname_paths = []
for path, fnames in paths_dict.items():
    for fname in fnames:
        fname_paths.append(path.joinpath(fname))

for fname_path in fname_paths:
    fname_path.touch()

# Solution I
fnames_mp3 = 0
fnames_wav = 0
for fname_path in Path.cwd().glob('media/music/playlist_05/*'):
    if fname_path.suffix == '.mp3':
        fnames_mp3 += 1
    elif fname_path.suffix == '.wav':
        fnames_wav += 1

print(f'fnames_mp3: {fnames_mp3}')
print(f'fnames_wav: {fnames_wav}')


# Solution II
path = Path.cwd() / "media/music/playlist_05"
fnames_mp3 = list(path.glob("*.mp3"))
fnames_wav = list(path.glob("*.wav"))

print(f"fnames_mp3: {len(fnames_mp3)}")
print(f"fnames_wav: {len(fnames_wav)}")
