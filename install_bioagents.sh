#!/bin/bash

# 安装 Docker
install_docker() {
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    echo "Docker installed successfully."
}

# 克隆 bioagents.tech 代码库
clone_repo() {
    echo "Cloning bioagents.tech repository..."
    git clone https://github.com/bio-agents/bioagents-registry.git
    cd bioagents-registry || exit
    echo "Repository cloned."
}

# 构建 Docker 镜像
build_docker_images() {
    echo "Building Docker images..."
    docker-compose build
    echo "Docker images built."
}

# 启动 Docker 容器
start_docker_containers() {
    echo "Starting Docker containers..."
    docker-compose up -d
    echo "Docker containers are up and running."
}

# 执行数据库迁移和其他初始化操作
initialize_database() {
    echo "Initializing database..."
    docker exec bioagents-backend python manage.py makemigrations
    docker exec bioagents-backend python manage.py migrate
    docker cp initial_db.sql bioagents-mysql:/root
    docker cp load_initial_db.sh bioagents-mysql:/root
    docker exec bioagents-mysql bash /root/load_initial_db.sh
    echo "Database initialized."
}

# 清除 Elasticsearch 数据并重新生成索引
setup_elasticsearch() {
    echo "Setting up Elasticsearch..."
    docker exec bioagents-backend python manage.py es_purge
    docker exec bioagents-backend python manage.py es_regenerate
    echo "Elasticsearch is set up."
}

# 主安装函数
main() {
    #install_docker
    #clone_repo
    build_docker_images
    start_docker_containers
    initialize_database
    setup_elasticsearch
    echo "bioagents.tech setup complete. Visit http://localhost:8000 to access the site."
}

# 执行主安装函数
main