import cv2
from adb_controller import capture_screen
from vision import decode

image = decode(capture_screen())
scale = min(1.0, 800 / image.shape[0])
small = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Tọa độ thật: ({int(x / scale)}, {int(y / scale)})")

cv2.imshow("Phone Screen", small)
cv2.setMouseCallback("Phone Screen", on_click)
cv2.waitKey(0)
cv2.destroyAllWindows()