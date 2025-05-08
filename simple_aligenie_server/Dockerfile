# 从nodejs构建
FROM node:22-alpine

# 设置工作目录
WORKDIR /app
# WORKDIR /data

# 将项目文件复制到容器中
COPY . /app

# # Install requirements for add-on
RUN npm config set registry https://registry.npmmirror.com/ \
    && npm install --force 

# 启动应用
CMD ["app.js"]
