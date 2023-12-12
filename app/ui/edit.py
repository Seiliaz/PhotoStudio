from tkinter import filedialog
from app.modules.edit.PhotoEditor import PhotoEditor
from app.modules.edit.Resize import Resize
import app.ui.ui as ui
from app.modules.save.save import save
import cv2

def edit():
    path = filedialog.askopenfilename(
        initialdir="/",
        title="Select Image",
        filetypes=(
            ("JPG Image", "*.jpg"),
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpeg"),
            ("DIB Image", "*.dib"),
            ("BMP Image", "*.bmp"),
            ("WEBP Image", "*.webp")
        )
    )
    image = cv2.imread(path)
    imageFormat = str(ui.formatCombo.get())
    imageEffect = str(ui.effectName.get())
    imageResize = str(ui.resizeMethod.get())
    imageBlur = int(ui.kernelSpin.get())
    Editor = PhotoEditor(image, imageBlur)

    match imageEffect:
        case "original":
            photo = image
        case "grayscale":
            photo = Editor.grayscale()
        case "bright":
            photo = Editor.bright()
        case "dark":
            photo = Editor.dark()
        case "sharp":
            photo = Editor.sharp()
        case "blur":
            photo = Editor.blur()
        case "emboss":
            photo = Editor.emboss()
        case "sepia":
            photo = Editor.sepia()
        case "sketchColor":
            photo = Editor.sketchColor()
        case "sketchGray":
            photo = Editor.sketchGray()
        case "hdr":
            photo = Editor.HDR()
        case "invert":
            photo = Editor.invert()
        case _ :
            photo = image

    Resizer = Resize(photo)

    match imageResize:
        case "scale":
            scaleAmount = float(ui.spin.get())
            picture = Resizer.scale(scaleAmount)
        case "quantity":
            width = int(ui.widthSpin.get())
            height = int(ui.heightSpin.get())
            picture = Resizer.quantity(width, height)
        case "rotate":
            rotationAngle = int(ui.rotationSpin.get())
            picture = Resizer.rotate(rotationAngle)

    cv2.imshow("Result Image", picture)
    save(picture, imageFormat)
