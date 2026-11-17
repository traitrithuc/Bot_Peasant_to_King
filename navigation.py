import time
import config
from adb_controller import tap

SCENES = {
    "farm": config.NAV_FARM,
    "estate": config.NAV_ESTATE,
    "market": config.NAV_MARKET,
}

def go_to(scene):
    tap(*SCENES[scene])
    time.sleep(1.5)      