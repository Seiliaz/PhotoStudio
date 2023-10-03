# import modules
from tkinter import *
from tkinter import filedialog, ttk
import cv2, scipy, numpy as np
from scipy.interpolate import UnivariateSpline
from PIL import ImageEnhance
# Lookup Table function for some specific usages
def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline
# Classes and functions for editing, resizing and saving
class PhotoEditor:
    def __init__(self, image, blurAmount = 10):
        self.image = image
        self.blurAmount = blurAmount
    def grayscale(self):
        grayscaleImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return grayscaleImage
    def bright(self):
        brightImage = cv2.convertScaleAbs(self.image, beta=30)
        return brightImage
    def dark(self):
        darkImage = cv2.convertScaleAbs(self.image, beta=-30)
        return darkImage
    def sharp(self):
        kernel = np.array(
            [
                [-1, -1, -1],
                [-1, 9.5, -1],
                [-1, -1, -1]
            ]
        )
        sharpImage = cv2.filter2D(self.image, -1, kernel)
        return sharpImage
    def blur(self):
        if self.blurAmount <= 0:
            self.blurAmount = 10
        blurImage = cv2.blur(self.image, (self.blurAmount, self.blurAmount))
        return blurImage
    def emboss(self):
        kernel = np.array(
            [
                [-2, -1, 0],
                [-1, 1, 1],
                [0, 1, 2]
            ]
        )
        embossImage = cv2.filter2D(self.image, -1, kernel)
        return embossImage
    def sepia(self):
        temporaryImage = cv2.transform(
            np.array(self.image, np.float64),
            np.matrix(
                [
                    [0.272, 0.534, 0.131],
                    [0.349, 0.686, 0.168],
                    [0.393, 0.769, 0.189]
                ]
            )
        )
        temporaryImage[np.where(temporaryImage > 255)] = 255
        sepiaImage = np.array(temporaryImage, dtype=np.uint8)
        return sepiaImage
    def sketchGray(self):
        temporaryImage = cv2.pencilSketch(
            self.image,
            sigma_s=60,
            sigma_r=0.07,
            shade_factor=0.1
        )
        sketchGrayImage = self.grayscale(temporaryImage)
        return sketchGrayImage
    def sketchColor(self):
        sketchColorImage = cv2.pencilSketch(
            self.image,
            sigma_s=60,
            sigma_r=0.07,
            shade_factor=0.1
        )
        return sketchColorImage
    def HDR(self):
        HDRImage = cv2.detailEnhance(
            self.image,
            sigma_s=12,
            sigma_r=0.15
        )
        return HDRImage
    def invert(self):
        invertImage = cv2.bitwise_not(self.image)
        return invertImage

def save(image, format):
    savepath = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save image",
        filetypes=(
            ("{} Image".format(format), "*.{}".format(format)),
            ("", "*.*")
        )
    )
    cv2.imwrite("{0}.{1}".format(savepath, format), image)

def edit():
    path = filedialog.askopenfilename(
        initialdir="/",
        title="Select Image",
        filetypes=(
            ("JPG Image","*.jpg"),
            ("PNG Image","*.png"),
            ("JPEG Image","*.jpeg"),
            ("DIB Image","*.dib"),
            ("BMP Image","*.bmp"),
            ("WEBP Image","*.webp")
        )
    )
    image = cv2.imread(path)
    imageFormat = str(formatCombo.get())
    imageEffect = str(effectName.get())
    imageResize = str(resizeMethod.get())
    imageBlur = int(kernelSpin.get())
    Editor = PhotoEditor(image, imageBlur)
    if imageEffect == "original":
        photo = image
    elif imageEffect == "grayscale":
        photo = Editor.grayscale()
    elif imageEffect == "bright":
        photo = Editor.bright()
    elif imageEffect == "dark":
        photo = Editor.dark()
    elif imageEffect == "sharp":
        photo = Editor.sharp()
    elif imageEffect == "blur":
        photo = Editor.blur()
    elif imageEffect == "emboss":
        photo = Editor.emboss()
    elif imageEffect == "sepia":
        photo = Editor.sepia()
    elif imageEffect == "sketchColor":
        photo = Editor.sketchColor()
    elif imageEffect == "sketchGray":
        photo = Editor.sketchGray()
    elif imageEffect == "hdr":
        photo = Editor.HDR()
    elif imageEffect == "invert":
        photo = Editor.invert()
    else:
        photo = image

    if imageResize == "scale":
        scaleAmount = float(spin.get())
        picture = cv2.resize(
            photo,
            None,
            fx=scaleAmount,
            fy=scaleAmount
        )
    elif imageResize == "quantity":
        width = int(widthSpin.get())
        height = int(heightSpin.get())
        picture = cv2.resize(photo, (width, height))
    elif imageResize == "rotate":
        rotationAngle = int(rotationSpin.get())
        if rotationAngle == 90:
            picture = cv2.rotate(photo, cv2.ROTATE_90_CLOCKWISE)
        elif rotationAngle == 180:
            picture = cv2.rotate(photo, cv2.ROTATE_180)
        elif rotationAngle == 270:
            picture = cv2.rotate(photo, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            picture = photo
    else:
        picture = photo
    cv2.imshow("Result Image", picture)
    save(picture, imageFormat)


# make a Graphical User Interface
win = Tk()
win.title("Photo Studio")
win.geometry("900x600")
win.minsize(900,600)
# make menubar
menubar = Menu(win)
win.config(menu=menubar)
menubar.add_command(label="Convert",command=edit)
# make frames
leftFrame = Frame(win)
leftFrame.pack(expand=True,fill=BOTH,side=LEFT)
centerFrame = Frame(win)
centerFrame.pack(expand=True,fill=BOTH,side=LEFT)
rightFrame = Frame(win)
rightFrame.pack(expand=True,fill=BOTH,side=LEFT)
formatFrame = LabelFrame(rightFrame,text="Format")
formatFrame.pack(expand=True,fill=BOTH)
filterFrame = LabelFrame(rightFrame,text="Filter")
filterFrame.pack(expand=True,fill=BOTH)
resizeFrame = LabelFrame(centerFrame,text="Resize")
resizeFrame.pack(expand=True,fill=BOTH)
quantityFrame = LabelFrame(centerFrame,text="Quantity")
quantityFrame.pack(expand=True,fill=BOTH)
scaleFrame = LabelFrame(leftFrame,text="Scale")
scaleFrame.pack(expand=True,fill=BOTH)
cropFrame = LabelFrame(leftFrame,text="Crop")
cropFrame.pack(expand=True,fill=BOTH)
rotateFrame = LabelFrame(leftFrame,text="Rotate")
rotateFrame.pack(expand=True,fill=BOTH)
blurFrame = LabelFrame(centerFrame,text="Blur")
blurFrame.pack(expand=True,fill=BOTH)
# format frame configuration
formatList = ["JPG","PNG","DIB","BMP","WEBP"]
Label(formatFrame,text="Format: ").pack()
formatCombo = ttk.Combobox(formatFrame,values=formatList)
formatCombo.set("Pick a format")
formatCombo.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
# filter frame configuration
filtersList = [
    ("Original","original"),
    ("Grayscale","grayscale"),
    ("Bright","bright"),
    ("Dark","dark"),
    ("Sharp","sharp"),
    ("Blur","blur"),
    ("Emboss","emboss"),
    ("Sepia","sepia"),
    ("Pencil Sketch (Color)","sketchColor"),
    ("Pencil Sketch (Gray)","sketchGray"),
    ("HDR","hdr"),
    ("Invert","invert")
]
effectName = StringVar()
effectName.set("original")
Label(filterFrame,text="Filter: ").pack()
for (text,value) in filtersList:
    Radiobutton(
        filterFrame,
        text=text,
        variable=effectName,
        value=value,
        indicatoron=0,
        bd=0
        ).pack( expand=True,fill=BOTH,ipady=5,padx=15)
# resize frame configuration
resizeList = [
    ("None","None"),
    ("Scale","scale"),
    ("Quantity","quantity"),
    ("Crop","crop"),
    ("Rotation","rotate")
    ]
resizeMethod = StringVar()
resizeMethod.set("None")
Label(resizeFrame,text="Resize by:").pack(expand=True,fill=BOTH,ipady=15)
for (text,value) in resizeList:
    Radiobutton(
        resizeFrame,
        text=text,
        variable=resizeMethod,
        value=value,
        indicatoron=0,
        bd=0
        ).pack(expand=True,fill=BOTH,ipady=5,padx=15,pady=5)
# quantity frame configuration
Label(quantityFrame,text="Enter width: ").pack()
widthSpin = Spinbox(quantityFrame,from_=0,to=100)
widthSpin.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
Label(quantityFrame,text="Enter height: ").pack()
heightSpin = Spinbox(quantityFrame,from_=0,to=100)
heightSpin.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
# scale frame configuration
Label(scaleFrame,text="Enter scale: ").pack()
spin = Spinbox(scaleFrame,from_=0,to=100)
spin.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
# crop frame configuration
Label(cropFrame,text="Enter width: ").pack()
cropWidth = Spinbox(cropFrame,from_=0,to=100)
cropWidth.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
Label(cropFrame,text="Enter height: ").pack()
cropHeight = Spinbox(cropFrame,from_=0,to=100)
cropHeight.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
# rotation frame configuration
Label(rotateFrame,text="Enter rotation angle: ").pack()
#rotationSpin = Spinbox(rotateFrame,from_=0,to=360)
rotationList = ["90","180","270"]
rotationSpin = ttk.Combobox(rotateFrame,values=rotationList)
rotationSpin.set("Pick a rotation angle")
rotationSpin.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
Label(rotateFrame,text="Note: angles are clockwise").pack()
# blur frame configuration
Label(blurFrame,text="Enter a blur amount: ").pack()
kernelSpin = Spinbox(blurFrame,from_=0,to=100)
kernelSpin.pack(pady=10,expand=True,fill=X,padx=15,ipady=4)
Label(blurFrame,text="Note: default amount is 10").pack()
# make a loop for window
win.mainloop()
