import time
import config
from adb_controller import capture_screen, tap, swipe
from vision import decode, read_number

def run_once():
    img = decode(capture_screen())
    grain = read_number(img, config.GRAIN_REGION, "grain_crop")
    print("Lương thực:", grain)
    if grain is None or grain < config.GRAIN_THRESHOLD:
        return False
    swipe(*config.SLIDER_START, *config.SLIDER_END, 600)   # kéo thanh tới cuối
    time.sleep(0.5)
    tap(*config.SEND_BUTTON)                               # bấm Send
    time.sleep(3)
    return True