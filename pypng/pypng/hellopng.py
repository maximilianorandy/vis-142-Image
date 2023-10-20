# a hello pypng example
# note: your distro may not have pypng:
# $ pip3 install pypng
# and if you don't have pip3:
# $ sudo apt install python3-pip
# there may be other ways to install, varies by distro. Welcome to Linux!

import png
png.from_array([[255, 0, 0, 255],
                [0, 255, 255, 0]], 'L').save("smite.png")
