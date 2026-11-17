import time
import config
from adb_controller import capture_screen, tap, swipe
from vision import decode, read_number

def hire_workers():
    tap(*config.HIRE_BLACKSMITH); time.sleep(0.5)
    tap(*config.HIRE_MINER);      time.sleep(0.5)

def forge_once():
    # kéo búa xuống lò, giữ lâu một chút để game nhận là "kéo"
    swipe(*config.HAMMER_POS, *config.FORGE_POS, 400)
    time.sleep(0.3)

def forge_round():
    for _ in range(config.FORGE_PER_ROUND):
        forge_once()

def out_of_coal():
    img = decode(capture_screen())
    coal = read_number(img, config.COAL_REGION, "coal_crop")
    print("Than:", coal)
    return coal == 0         # None (đọc lỗi) KHÔNG coi là hết than