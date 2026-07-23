# monitor.py
from curl_cffi import requests
import time

URL = "https://iloto88.info/UserService.aspx"

def check():
    start = time.perf_counter()
    try:
        # Giả lập Chrome để tránh lỗi 403
        resp = requests.post(URL, impersonate="chrome110", timeout=15)
        latency = (time.perf_counter() - start) * 1000
        print(f"[{time.ctime()}] Status: {resp.status_code} | Speed: {latency:.2f}ms")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    check()
