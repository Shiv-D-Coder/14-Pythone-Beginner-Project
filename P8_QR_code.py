'''
PROJECT 8 : QR Code

QR is short for Quick Response, and they are named so because they can be 
read quickly by a cell phone. 
They are used to take information from transitory media and put it on your 
cell phone.
'''

#  C  O  D  E

import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code 
AnimeXplay="https://www.kaggle.com/datasets/shivd24coder/powerful-data-for-power-bi"

# Generate QR code 
url=pyqrcode.create(AnimeXplay)

# Create and save the png file naming "myqr.png" 
url.svg("Dmon Slayer.svg",scale=10)