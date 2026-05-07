import requests
import time
from datetime import datetime

URL = "http://localhost:8080/status"

print(f"开始监控 {URL} ...")

while True:
    try:
        resp = requests.get(URL, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            now = datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] ✅ 正常 | OSPF: {data['ospf_status']} | BGP: {data['bgp_neighbor']}")
        else:
            print(f"⚠️ 返回异常状态码: {resp.status_code}")
    except Exception as e:
        print(f"❌ 连接失败: {e}")

    time.sleep(5)