import cv2

class Resize:
    def __init__(self, photo) -> None:
        self.photo = photo

    def scale(self, amount):
        return cv2.resize(
            self.photo, None, fx=amount, fy=amount
        )

    def quantity(self, width, height):
        return cv2.resize(self.photo, (width, height))

    def rotate(self, angle=0):
        match angle:
            case 90:
                parameter = cv2.ROTATE_90_CLOCKWISE
            case 180:
                parameter = cv2.ROTATE_180
            case 270:
                parameter = cv2.ROTATE_90_COUNTERCLOCKWISE
            case _:
                return self.photo
        return cv2.rotate(self.photo, parameter)
