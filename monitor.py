
import requests
import time
import docker

# 配置区
URL = "http://java-service:8080/status"
CONTAINER_NAME = "my-net-app"
MAX_RETRIES = 3  # 连续失败 3 次就重启

# 初始化 Docker 遥控器
client = docker.from_env()

def restart_service():
    print(f"🚨 [ALERT] 服务连续失败 {MAX_RETRIES} 次，尝试自愈重启...")
    try:
        container = client.containers.get(CONTAINER_NAME)
        container.restart()
        print(f"✅ [SUCCESS] {CONTAINER_NAME} 已重启，等待 15 秒让 Java 加载...")
        time.sleep(15)
    except Exception as e:
        print(f"❌ [ERROR] 无法重启容器: {e}")

def monitor():
    fail_count = 0
    print(f"🚀 智能监控系统已启动，正在监听 {CONTAINER_NAME}...")

    while True:
        try:
            response = requests.get(URL, timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"[{time.strftime('%H:%M:%S')}] 状态正常: OSPF={data.get('ospf_status')}")
                fail_count = 0  # 只要成功一次，计数器就清零
            else:
                fail_count += 1
        except Exception:
            fail_count += 1
            print(f"⚠️ [WARNING] 无法访问接口，异常计数: {fail_count}/{MAX_RETRIES}")

        # 判断是否需要启动“自愈”
        if fail_count >= MAX_RETRIES:
            restart_service()
            fail_count = 0

        time.sleep(5)

if __name__ == "__main__":
    monitor()
"""
import requests
import time
import docker # 新引入的库

client = docker.from_env() # 连接本地 Docker 引擎
CONTAINER_NAME = "my-net-app"
URL = "http://localhost:8080/status"

def heal_container():
    print(f"🚨 检测到服务彻底崩溃，正在尝试自愈重启...")
    container = client.containers.get(CONTAINER_NAME)
    container.restart()
    print(f"✅ 容器 {CONTAINER_NAME} 已重启，等待服务恢复...")
    time.sleep(10) # 给 Java 启动留出时间

# 在你的 while 循环里加入逻辑：
# 如果 requests.get 连续报错三次 -> 调用 heal_container()



import requests
import time

# 你刚才 Docker 跑起来的接口地址
URL = "http://localhost:8080/status"

def check_network():
    try:
        # 发送 HTTP GET 请求
        response = requests.get(URL)
        data = response.json()

        # 提取 Java 接口返回的数据
        ospf = data.get("ospf_status")
        bgp = data.get("bgp_neighbor")

        print(f"[{time.strftime('%H:%M:%S')}] 监控检查中...")
        print(f"OSPF 状态: {ospf}")
        print(f"BGP 邻居: {bgp}")

        # 模拟自动化判断
        if "Established" not in bgp:
            print("⚠️ [FATAL]：BGP 邻居断开")
        else:
            print("✅ 网络邻居状态正常")

    except Exception as e:
        print(f"❌ 无法连接到监控服务: {e}")


if __name__ == "__main__":
    # 每隔 5 秒检查一次
    while True:
        check_network()
        print("-" * 30)
        time.sleep(5)
"""