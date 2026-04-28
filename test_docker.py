import docker

# 初始化客户端
client = docker.from_env()

# 列出所有正在运行的容器
print("正在检查你的 Docker 容器...")
for container in client.containers.list():
    print(f"找到容器: {container.name}, 状态: {container.status}")