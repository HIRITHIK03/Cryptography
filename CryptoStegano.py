from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #pip install stegano
import pyqrcode



#QR code Generator
img = qrcode.make('Some data here')
type(img)
img.save("outputqr.png")

root.mainloop()
