from SimpleCV import VirtualCamera, Color
import datetime
from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory

root = Tk()
root.fileName = askopenfilename(filetypes=[("AVI files", "*.avi")])
root.directory = askdirectory()
fmt = '%Y-%m-%d-%H_%M_%S'
vir = VirtualCamera(root.fileName, "video")
n = 1
while True:
    img = vir.getFrame(n).resize(320, 240)
    invr = img.invert()
    bine = invr.binarize(80)
    bine2 = bine.binarize()
    blobs = bine.findBlobs(200)
    blobs.draw(color=Color.BLUE, width=2)
    img.addDrawingLayer(bine.dl())
    d = datetime.datetime.now()
    d_string = d.strftime(fmt)
    filepath = root.directory + "/" + str(n) + "-" + d_string + ".jpg"
    img.save(filepath)
    n += 5


print "wn, te dai cuenta que no tenis nada documentadooooooo"   
