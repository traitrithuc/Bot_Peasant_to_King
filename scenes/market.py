import time
import config
from adb_controller import tap, swipe

def keo_max():
    swipe(*config.M_SLIDER_START, *config.M_SLIDER_END, 600)
    time.sleep(0.5)

def xac_nhan():
    tap(*config.ACTION_PILL)
    time.sleep(1)

def doi_che_do():
    tap(*config.SWAP_BTN)
    time.sleep(0.8)

def restock_coal():
    tap(*config.BUY_COAL_BTN)      # từ Estate sang Market, đã chọn than
    time.sleep(1.5)
    keo_max(); xac_nhan()          # Buy full
    doi_che_do()                   # sang Sell
    keo_max(); xac_nhan()          # Sell full
    doi_che_do()                   # về Buy
    keo_max(); xac_nhan()          # Buy full lần cuối