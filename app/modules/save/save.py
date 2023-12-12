import cv2
from tkinter import filedialog

def save(image, format):
    savepath = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save image",
        filetypes=(
            (f"{format} Image", f"*.{format}"),
            ("", "*.*")
        )
    )
    if savepath == "":
        return
    cv2.imwrite(f"{savepath}.{format}", image)
