from items.påsitem import Item
import cv2

class BildItem(Item):
    def __init__(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            raise Exception("Kunde inte ta bilden.")
        
        super().__init__("bild", frame)

    def __str__(self):
        image = self.innehåll
        max_width = 40
        height, width = image.shape[:2]
        aspect_ratio = width / height
        width = max(max_width, int(max_width * aspect_ratio))
        height = int(width / aspect_ratio)
        image = cv2.resize(image, (width, height))
        lines = f"ID: {self.id}, Typ: Bild, Storlek: {width}x{height}\n"

        for y in range(0, height, 2):
            line = ""
            for x in range(width):
                if y + 1 < height:
                    upper_pixel = image[y, x]
                    lower_pixel = image[y + 1, x]
                    line += f"\033[38;2;{upper_pixel[2]};{upper_pixel[1]};{upper_pixel[0]}m\033[48;2;{lower_pixel[2]};{lower_pixel[1]};{lower_pixel[0]}m▀"
                else:
                    pixel = image[y, x]
                    line += f"\033[38;2;{pixel[2]};{pixel[1]};{pixel[0]}m▀"
            lines += line + "\033[0m\n"
        return lines

    def open(self):
        cv2.imshow("Bild", self.innehåll)
        cv2.waitKey(0)
        cv2.destroyAllWindows()