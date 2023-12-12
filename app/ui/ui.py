from tkinter import *
from tkinter import ttk
from app.ui.edit import edit

win = Tk()
win.title("Photo Studio")
win.geometry("900x600")
win.minsize(900, 600)
# make menubar
menubar = Menu(win)
win.config(menu=menubar)
menubar.add_command(label="Convert", command=edit)
# make frames
leftFrame = Frame(win)
leftFrame.pack(expand=True, fill=BOTH, side=LEFT)
centerFrame = Frame(win)
centerFrame.pack(expand=True, fill=BOTH, side=LEFT)
rightFrame = Frame(win)
rightFrame.pack(expand=True, fill=BOTH, side=LEFT)
formatFrame = LabelFrame(rightFrame, text="Format")
formatFrame.pack(expand=True, fill=BOTH)
filterFrame = LabelFrame(rightFrame, text="Filter")
filterFrame.pack(expand=True, fill=BOTH)
resizeFrame = LabelFrame(centerFrame, text="Resize")
resizeFrame.pack(expand=True, fill=BOTH)
quantityFrame = LabelFrame(centerFrame, text="Quantity")
quantityFrame.pack(expand=True, fill=BOTH)
scaleFrame = LabelFrame(leftFrame, text="Scale")
scaleFrame.pack(expand=True, fill=BOTH)
cropFrame = LabelFrame(leftFrame, text="Crop")
cropFrame.pack(expand=True, fill=BOTH)
rotateFrame = LabelFrame(leftFrame, text="Rotate")
rotateFrame.pack(expand=True, fill=BOTH)
blurFrame = LabelFrame(centerFrame, text="Blur")
blurFrame.pack(expand=True, fill=BOTH)
# format frame configuration
formatList = ["JPG", "PNG", "DIB", "BMP", "WEBP"]
Label(formatFrame, text="Format: ").pack()
formatCombo = ttk.Combobox(formatFrame, values=formatList)
formatCombo.set("Pick a format")
formatCombo.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
# filter frame configuration
filtersList = [
    ("Original", "original"),
    ("Grayscale", "grayscale"),
    ("Bright", "bright"),
    ("Dark", "dark"),
    ("Sharp", "sharp"),
    ("Blur", "blur"),
    ("Emboss", "emboss"),
    ("Sepia", "sepia"),
    ("Pencil Sketch (Color)", "sketchColor"),
    ("Pencil Sketch (Gray)", "sketchGray"),
    ("HDR", "hdr"),
    ("Invert", "invert")
]
effectName = StringVar()
effectName.set("original")
Label(filterFrame, text="Filter: ").pack()
for (text, value) in filtersList:
    Radiobutton(
        filterFrame,
        text=text,
        variable=effectName,
        value=value,
        indicatoron=0,
        bd=0
    ).pack(expand=True, fill=BOTH, ipady=5, padx=15)
# resize frame configuration
resizeList = [
    ("None", "None"),
    ("Scale", "scale"),
    ("Quantity", "quantity"),
    ("Crop", "crop"),
    ("Rotation", "rotate")
]
resizeMethod = StringVar()
resizeMethod.set("None")
Label(resizeFrame, text="Resize by:").pack(expand=True, fill=BOTH, ipady=15)
for (text, value) in resizeList:
    Radiobutton(
        resizeFrame,
        text=text,
        variable=resizeMethod,
        value=value,
        indicatoron=0,
        bd=0
    ).pack(expand=True, fill=BOTH, ipady=5, padx=15, pady=5)
# quantity frame configuration
Label(quantityFrame, text="Enter width: ").pack()
widthSpin = Spinbox(quantityFrame, from_=0, to=100)
widthSpin.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
Label(quantityFrame, text="Enter height: ").pack()
heightSpin = Spinbox(quantityFrame, from_=0, to=100)
heightSpin.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
# scale frame configuration
Label(scaleFrame, text="Enter scale: ").pack()
spin = Spinbox(scaleFrame, from_=0, to=100)
spin.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
# crop frame configuration
Label(cropFrame, text="Enter width: ").pack()
cropWidth = Spinbox(cropFrame, from_=0, to=100)
cropWidth.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
Label(cropFrame, text="Enter height: ").pack()
cropHeight = Spinbox(cropFrame, from_=0, to=100)
cropHeight.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
# rotation frame configuration
Label(rotateFrame, text="Enter rotation angle: ").pack()
# rotationSpin = Spinbox(rotateFrame,from_=0,to=360)
rotationList = ["90", "180", "270"]
rotationSpin = ttk.Combobox(rotateFrame, values=rotationList)
rotationSpin.set("Pick a rotation angle")
rotationSpin.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
Label(rotateFrame, text="Note: angles are clockwise").pack()
# blur frame configuration
Label(blurFrame, text="Enter a blur amount: ").pack()
kernelSpin = Spinbox(blurFrame, from_=0, to=100)
kernelSpin.pack(pady=10, expand=True, fill=X, padx=15, ipady=4)
Label(blurFrame, text="Note: default amount is 10").pack()
# make a loop for window
win.mainloop()
