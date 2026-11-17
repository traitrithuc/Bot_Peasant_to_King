import time
import config
from navigation import go_to
from scenes import estate, market
from adb_controller import capture_screen, swipe, tap 
from vision import decode, read_number

def read_grain():
    img = decode(capture_screen())
    return read_number(img, config.GRAIN_REGION, "grain_crop")

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

def main():
    go_to("estate")
    estate.hire_workers()
    scene = "estate"

    while True:
        if scene == "estate":
            if estate.out_of_coal():
                scene = "market"
                continue
            estate.forge_round()
            grain = read_grain()
            if grain is not None and grain >= config.GRAIN_THRESHOLD:
                scene = "farm"

        elif scene == "market":
            go_to("market")
            market.restock_coal()
            go_to("estate")
            scene = "estate"

        elif scene == "farm":
            go_to("farm")
            run_once()            # hàm Farm cũ của bạn
            go_to("estate")
            scene = "estate"

        time.sleep(0.5)

if __name__ == "__main__":
    main()