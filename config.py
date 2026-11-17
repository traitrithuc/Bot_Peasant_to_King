ADB_PATH = r"D:\platform-tools\adb.exe"                  # giữ như bạn đang dùng
DEVICE_ID = "192.168.2.162:40449"               # giữ như bạn đang dùng
#TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cảnh Farm (tọa độ trên ảnh gốc 720x1600, ước lượng, kiểm tra lại bằng pick.py)
GRAIN_REGION = (440, 35, 505, 70)    # x1, y1, x2, y2 của số lương thực
SLIDER_START = (248, 1437)
SLIDER_END = (450, 1437)
SEND_BUTTON = (566, 1437)
GRAIN_THRESHOLD = 4000
CHECK_INTERVAL = 300                  # giây giữa các lần kiểm tra

# --- Thanh điều hướng dưới ---
NAV_FARM   = (100, 1540)
NAV_ESTATE = (260, 1540)
NAV_MARKET = (420, 1540)

# --- Estate ---
HIRE_BLACKSMITH = (200, 800)     # nút hire thợ rèn
HIRE_MINER      = (500, 800)     # nút hire thợ mỏ ore
HAMMER_POS      = (150, 1200)    # điểm bắt đầu kéo búa
FORGE_POS       = (360, 900)     # lò rèn (điểm thả búa)
COAL_REGION     = (440, 90, 505, 125)   # vùng số than
FORGE_PER_ROUND = 5              # số lần kéo búa mỗi vòng

# --- Market ---
BUY_TAB   = (180, 300)
SELL_TAB  = (540, 300)
COAL_ITEM = (360, 600)           # dòng than trong danh sách
M_SLIDER_START = (200, 1300)
M_SLIDER_END   = (520, 1300)     # đầu kia của thanh = max
BUY_CONFIRM  = (360, 1437)
SELL_CONFIRM = (360, 1437)
MARKET_CYCLES = 1                # số lần Buy-Sell trước khi mua lần cuối