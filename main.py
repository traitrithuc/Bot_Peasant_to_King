import time
import config
from navigation import go_to
from scenes import estate, market
from adb_controller import capture_screen, tap, swipe
from vision import decode, read_number


def read_grain():
    img = decode(capture_screen())
    return read_number(img, config.GRAIN_REGION, "grain_crop")


def run_once():
    """Ở màn Farm: lúa đủ ngưỡng thì kéo thanh Send tới cuối rồi bấm Send."""
    grain = read_grain()
    print("Lương thực:", grain)
    if grain is None or grain < config.GRAIN_THRESHOLD:
        return False
    swipe(*config.SLIDER_START, *config.SLIDER_END, 600)
    time.sleep(0.5)
    tap(*config.SEND_BUTTON)
    time.sleep(3)
    return True


def thu_gui_lua():
    go_to("farm")
    time.sleep(1)
    truoc = read_grain()
    run_once()
    time.sleep(2)
    sau = read_grain()
    go_to("estate")
    time.sleep(1)

    if truoc is not None and sau is not None and sau < truoc:
        print("Đã gửi lúa")
        return True
    print("Không gửi được lúa")
    return False


def main():
    go_to("estate")
    time.sleep(1)
    estate.hire_workers()
    estate.chup_mau_bua()

    loi_than = 0           # số lần liên tiếp đọc than thất bại
    mua_hut = 0            # số lần liên tiếp mua than xong mà vẫn thấp
    lua_cho_tay = False    # True = đã báo không gửi được lúa, đợi bạn xử lý tay

    while True:
        try:
            # 0. Đọc than
            than = estate.doc_than()
            if than is None:
                loi_than += 1
                print("Không đọc được than, lần", loi_than)
                if loi_than % 5 == 0:
                    go_to("estate")
                time.sleep(2)
                continue
            loi_than = 0

            # 1. Than thấp thì đi mua
            if than[0] < config.COAL_LOW:
                market.restock_coal()
                go_to("estate")
                time.sleep(1)
                moi = estate.doc_than()
                if moi is None or moi[0] < config.COAL_LOW:
                    mua_hut += 1
                    print("Mua than xong mà vẫn thấp, lần", mua_hut,
                          "- đợi 30 giây rồi thử lại")
                    time.sleep(30)
                else:
                    mua_hut = 0
                continue

            # 2. Kéo búa, đợi búa về
            if not estate.forge_round():
                print("Búa chưa về, vòng sau thử lại")

            # 3. Có nút HIRE thì tuyển
            estate.hire_workers()

            # 4. Kiếm đầy thì gửi
            kiem = estate.doc_kiem()
            print("Kiếm:", kiem)
            if kiem is not None and kiem[0] >= kiem[1]:
                estate.gui_kiem()

            # 5. Lúa đạt ngưỡng thì sang Farm gửi
            lua = read_grain()
            if lua is not None:
                if lua < config.GRAIN_THRESHOLD:
                    lua_cho_tay = False          # lúa đã giảm, bật lại
                elif not lua_cho_tay:
                    if not thu_gui_lua():
                        lua_cho_tay = True       # báo một lần, để bạn thao tác tay

        except RuntimeError as e:
            print("Lỗi:", e, "- đợi 5 giây rồi thử lại")
            time.sleep(5)

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Đã dừng bot.")