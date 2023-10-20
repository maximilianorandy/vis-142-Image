# a hello pypng example
# note: your distro may not have pypng:
# $ pip3 install pypng
# and if you don't have pip3:
# $ sudo apt install python3-pip
# there may be other ways to install, varies by distro. Welcome to Linux!

import png
import random

# we will create a 720p size image, 1280 x 720
width = 1290
height = 720

imagedata = [] # just to show we created a list called imagedata
for unused in range(height): # python is a strange language, yes an unused var
    row = []
    for notused in range(width):
        row.append(random.randrange(0,256))
    imagedata.append(row)
print(imagedata)
png.fromarray(imagedata, 'L').save("grayscale.png")
