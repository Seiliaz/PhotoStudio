import cv2
import numpy as np

class PhotoEditor:
    def __init__(self, image, blurAmount=10):
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
        temporaryImage = self.sketchColor()
        sketchGrayImage = self.grayscale(temporaryImage)
        return sketchGrayImage

    def sketchColor(self):
        sketchColorImage = cv2.pencilSketch(
            self.image,
            sigma_s=6,
            sigma_r=0.01,
            shade_factor=0.1
        )
        return sketchColorImage[1]

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
