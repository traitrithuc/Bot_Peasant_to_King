import cv2
import numpy as np
import pytesseract
import re
from config import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def cat_vung(img, region):
    x1, y1, x2, y2 = region
    return img[y1:y2, x1:x2].copy()

def _nhi_phan(img, region, he_so):
    """Cắt vùng, phóng to, đổi thành ảnh đen trắng cho OCR dễ đọc."""
    crop = cat_vung(img, region)
    crop = cv2.resize(crop, None, fx=he_so, fy=he_so, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return bw

def decode(image_bytes):
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise RuntimeError("Không đọc được ảnh màn hình")
    return img

def read_number(img, region, debug_name=None):
    x1, y1, x2, y2 = region
    crop = img[y1:y2, x1:x2]
    crop = cv2.resize(crop, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    if debug_name:
        cv2.imwrite(f"screenshots/{debug_name}.png", bw)   # xem bằng mắt để kiểm tra OCR
    text = pytesseract.image_to_string(
        bw, config="--psm 7 -c tessedit_char_whitelist=0123456789").strip()
    return int(text) if text.isdigit() else None

def read_fraction(img, region, debug_name=None):
    x1, y1, x2, y2 = region
    crop = img[y1:y2, x1:x2]
    crop = cv2.resize(crop, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    if debug_name:
        cv2.imwrite(f"screenshots/{debug_name}.png", bw)
    text = pytesseract.image_to_string(
        bw, config="--psm 7 -c tessedit_char_whitelist=0123456789/").strip()
    m = re.search(r"(\d+)\s*/\s*(\d+)", text)
    return (int(m.group(1)), int(m.group(2))) if m else None

def co_chu(img, region, tu_khoa, debug_name=None):
    x1, y1, x2, y2 = region
    crop = img[y1:y2, x1:x2]
    crop = cv2.resize(crop, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    if debug_name:
        cv2.imwrite(f"screenshots/{debug_name}.png", bw)
    text = pytesseract.image_to_string(bw, config="--psm 7").upper()
    return tu_khoa in text

def giong_nhau(img, mau, region, nguong=0.9):
    """So vùng hiện tại với ảnh mẫu, giống từ 90% trở lên thì True."""
    cur = cat_vung(img, region)
    diem = cv2.matchTemplate(cur, mau, cv2.TM_CCOEFF_NORMED).max()
    return diem >= nguong