#!/usr/bin/env python 

import qrcode


img = qrcode.make(input("INPUT: "))  # if link, put whole adress as  https://....
filename = input("QR name: ")
img.save("QR_"+ filename + ".png", "PNG")

