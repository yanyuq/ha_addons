# 使用官方 Python 运行环境镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 拷贝文件
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口（与你代码中配置一致）
EXPOSE 20255

# 启动服务
CMD ["python", "server.py"]