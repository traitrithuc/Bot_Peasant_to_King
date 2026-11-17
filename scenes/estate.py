import time
import config
from adb_controller import capture_screen, tap, swipe
from vision import decode, read_fraction, co_chu, cat_vung, giong_nhau

_mau_bua = None


def chup_mau_bua():
    """Gọi 1 lần lúc búa đang nằm yên ở vị trí cũ."""
    global _mau_bua
    _mau_bua = cat_vung(decode(capture_screen()), config.HAMMER_REGION)


def doc_than():
    img = decode(capture_screen())
    kq = read_fraction(img, config.COAL_REGION, "coal_crop")
    print("Than:", kq)
    return kq


def doc_kiem():
    img = decode(capture_screen())
    return read_fraction(img, config.SWORD_REGION, "sword_crop")


def forge_once():
    """Kéo búa xuống nhà thợ rèn rồi đợi búa về. True = búa đã về."""
    if _mau_bua is None:
        chup_mau_bua()
    swipe(*config.HAMMER_POS, *config.FORGE_POS, 400)
    time.sleep(1)                                   # chờ game nhận cú kéo
    bat_dau = time.time()
    while time.time() - bat_dau < config.HAMMER_TIMEOUT:
        img = decode(capture_screen())
        if giong_nhau(img, _mau_bua, config.HAMMER_REGION):
            return True
        time.sleep(0.5)
    print("Búa không về sau", config.HAMMER_TIMEOUT, "giây")
    return False


def forge_round():
    return forge_once()


def _tuyen(region, diem_bam, ten, toi_da=5):
    """Thấy chữ HIRE (còn slot) thì bấm, kiểm tra lại sau mỗi lần."""
    for _ in range(toi_da):
        img = decode(capture_screen())
        if not co_chu(img, region, "HIRE", debug_name="hire_" + ten):
            return
        tap(*diem_bam)
        print("Tuyển", ten)
        time.sleep(1)


def hire_workers():
    _tuyen(config.HIRE_MINER_REGION, config.HIRE_MINER, "tho_mo")
    _tuyen(config.HIRE_BLACKSMITH_REGION, config.HIRE_BLACKSMITH, "tho_ren")


def gui_kiem():
    swipe(*config.SLIDER_START, *config.SLIDER_END, 600)   # kéo thanh tới cuối
    time.sleep(0.5)
    tap(*config.SEND_BUTTON)                               # bấm Send
    time.sleep(2)