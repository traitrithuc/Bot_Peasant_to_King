ADB_PATH = r"D:\platform-tools\adb.exe"                  # giữ như bạn đang dùng
DEVICE_ID = "192.168.2.162:40449"               # giữ như bạn đang dùng
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cảnh Farm (tọa độ trên ảnh gốc 720x1600, ước lượng, kiểm tra lại bằng pick.py)
GRAIN_REGION = (440, 35, 505, 70)    # x1, y1, x2, y2 của số lương thực
SLIDER_START = (248, 1437)
SLIDER_END = (450, 1437)
SEND_BUTTON = (566, 1437)
GRAIN_THRESHOLD = 500
CHECK_INTERVAL = 30                  # giây giữa các lần kiểm tra