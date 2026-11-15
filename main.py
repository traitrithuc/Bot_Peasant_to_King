import time
from pathlib import Path
import config
from scenes import farm

Path("screenshots").mkdir(exist_ok=True)

def main():
    print("Bot bắt đầu. Nhấn Ctrl+C để dừng.")
    try:
        while True:
            farm.run_once()
            time.sleep(config.CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("Đã dừng.")

if __name__ == "__main__":
    main()