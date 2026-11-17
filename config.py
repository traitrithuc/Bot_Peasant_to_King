ADB_PATH = r"D:\platform-tools\adb.exe"                 
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ============ Thanh trên cùng (giống nhau ở mọi màn) ============
GRAIN_REGION = (452, 36, 514, 68)      # số lúa: x1, y1, x2, y2

# ============ Thanh điều hướng dưới ============
NAV_FARM   = (90, 1550)
NAV_MARKET = (224, 1550)
NAV_ESTATE = (358, 1550)

# ============ Thanh "Send to Port" (Farm và Estate dùng chung) ============
SLIDER_START = (248, 1437)
SLIDER_END   = (450, 1437)
SEND_BUTTON  = (566, 1437)
GRAIN_THRESHOLD = 4000                 # lúa từ mức này trở lên thì sang Farm gửi

# ============ Estate ============
COAL_REGION  = (352, 96, 428, 128)     # chữ "0 / 500"
COAL_LOW     = 20                      # than dưới mức này thì đi mua
BUY_COAL_BTN = (360, 177)              # nút "BUY coal FROM MARKET"

SWORD_REGION = (555, 897, 657, 925)    # chữ "97 / 100" ở mục SWORDS

HAMMER_POS     = (598, 408)            # điểm bắt đầu kéo búa
FORGE_POS      = (598, 570)            # thả xuống nhà thợ rèn
HAMMER_REGION  = (558, 380, 640, 440)  # khung quanh icon búa (để biết búa đã về)
HAMMER_TIMEOUT = 60                    # đợi búa về tối đa (giây)

HIRE_MINER             = (119, 728)    # điểm bấm
HIRE_BLACKSMITH        = (600, 728)
HIRE_MINER_REGION      = (17, 709, 222, 747)    # vùng nhìn xem có chữ HIRE không
HIRE_BLACKSMITH_REGION = (497, 709, 703, 747)

# ============ Market ============
M_SLIDER_START = (50, 337)             # núm đầu trái thanh
M_SLIDER_END   = (656, 337)            # đầu phải = max
ACTION_PILL    = (325, 451)            # nút "Buy 0" / "Sell 0"
SWAP_BTN       = (483, 450)            # nút đảo Buy <-> Sell (hiện chưa dùng)
