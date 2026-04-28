# 基础镜像：使用轻量级的 Java 21
FROM eclipse-temurin:21-jdk-alpine

# 将 target 下的 jar 包复制到容器里并改名为 app.jar
COPY target/*.jar app.jar

# 运行命令
ENTRYPOINT ["java", "-jar", "/app.jar"]