"""
Exercise No. 09

The file structure is given as follows:
    images/images_jpg
        001_image.jpg
        004_image.jpg
        006_image.jpg
        007_image.jpg
        010_image.jpg
        016_image.jpg
        017_image.jpg
        019_image.jpg
    images/images_png
        002_image.png
        003_image.png
        005_image.png
        008_image.png
        009_image.png
        011_image.png
        012_image.png
        013_image.png
        014_image.png
        015_image.png
        018_image.png

Using the code below:
    for root, dirs, files in os.walk(base_dir):
         # enter your solution here

Print to the console sorted names of all files (each name on a separate line) in the following directory:
    base_dir = 'images'

Expected result:
    001_image.jpg
    004_image.jpg
    006_image.jpg
    007_image.jpg
    010_image.jpg
    016_image.jpg
    017_image.jpg
    019_image.jpg
    002_image.png
    003_image.png
    005_image.png
    008_image.png
    009_image.png
    011_image.png
    012_image.png
    013_image.png
    014_image.png
    015_image.png
    018_image.png
"""
import os
import random

random.seed(30)
images = [f"{str(i).zfill(3)}_image.{random.choice(['png', 'jpg'])}" for i in range(1, 20)]

base_dir = 'images'
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')

if not os.path.exists(base_dir):
    os.mkdir(base_dir)

if not os.path.exists(png_dir):
    os.mkdir(png_dir)

if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

for image in images:
    if image.endswith('.png'):
        open(os.path.join(png_dir, image), 'w').close()
    elif image.endswith('.jpg'):
        open(os.path.join(jpg_dir, image), 'w').close()

for root, dirs, files in os.walk(base_dir):
    for file in sorted(files):
        print(file)
