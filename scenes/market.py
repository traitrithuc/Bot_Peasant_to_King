import time
import config
from adb_controller import tap, swipe

def _max_and_confirm(confirm):
    swipe(*config.M_SLIDER_START, *config.M_SLIDER_END, 600)
    time.sleep(0.5)
    tap(*confirm)
    time.sleep(1.5)

def buy_coal_full():
    tap(*config.BUY_TAB);   time.sleep(0.8)
    tap(*config.COAL_ITEM); time.sleep(0.8)
    _max_and_confirm(config.BUY_CONFIRM)

def sell_coal_full():
    tap(*config.SELL_TAB);  time.sleep(0.8)
    tap(*config.COAL_ITEM); time.sleep(0.8)
    _max_and_confirm(config.SELL_CONFIRM)

def restock_coal():
    for _ in range(config.MARKET_CYCLES):
        buy_coal_full()
        sell_coal_full()
    buy_coal_full()          # lần mua cuối để mang về Estate