import subprocess
from config import ADB_PATH, DEVICE_ID

def adb_command(*args):
    return subprocess.run([ADB_PATH, "-s", DEVICE_ID, *args],
                          capture_output=True, check=True)

def capture_screen():
    return adb_command("exec-out", "screencap", "-p").stdout   # trả về bytes ảnh PNG

def tap(x, y):
    adb_command("shell", "input", "tap", str(x), str(y))

def swipe(x1, y1, x2, y2, duration_ms=500):
    adb_command("shell", "input", "swipe",
                str(x1), str(y1), str(x2), str(y2), str(duration_ms))