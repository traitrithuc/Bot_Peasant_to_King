import subprocess
from config import ADB_PATH

def tim_thiet_bi():
    kq = subprocess.run([ADB_PATH, "devices"], capture_output=True, text=True)
    dong = kq.stdout.strip().splitlines()[1:]    # bỏ dòng tiêu đề
    ds = [d.split()[0] for d in dong if d.split() and d.split()[-1] == "device"]
    if not ds:
        raise RuntimeError("Không thấy thiết bị nào. Hãy kết nối ADB trước.")
    return ds[0]

_device = None 

def adb_command(*args):
    global _device
    if _device is None:
        _device = tim_thiet_bi()
        print("Dùng thiết bị:", _device)
    kq = subprocess.run([ADB_PATH, "-s", _device, *args], capture_output=True)
    if kq.returncode != 0:
        _device = None    # lần sau tìm lại, phòng khi cổng đã đổi
        loi = (kq.stderr or kq.stdout).decode(errors="ignore").strip()
        raise RuntimeError(f"ADB lỗi: {loi}")
    return kq

def capture_screen():
    return adb_command("exec-out", "screencap", "-p").stdout   # trả về bytes ảnh PNG

def tap(x, y):
    adb_command("shell", "input", "tap", str(x), str(y))

def swipe(x1, y1, x2, y2, duration_ms=500):
    adb_command("shell", "input", "swipe",
                str(x1), str(y1), str(x2), str(y2), str(duration_ms))