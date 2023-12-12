from tkinter import filedialog
from app.modules.edit.PhotoEditor import PhotoEditor
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
        scaleAmount = float(ui.spin.get())
        picture = cv2.resize(
            photo,
            None,
            fx=scaleAmount,
            fy=scaleAmount
        )
    elif imageResize == "quantity":
        width = int(ui.widthSpin.get())
        height = int(ui.heightSpin.get())
        picture = cv2.resize(photo, (width, height))
    elif imageResize == "rotate":
        rotationAngle = int(ui.rotationSpin.get())
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
