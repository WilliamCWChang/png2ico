from PIL import Image
import os
path = '.'
files = os. listdir(path)
for name in files:
    if ".png" in name:
        filename = name.split('.')[0]
        img = Image.open(name)
        img.save(filename + '.ico')
