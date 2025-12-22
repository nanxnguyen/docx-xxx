# 🐳 Q63: Docker & Containerization for Frontend

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Docker containerize frontend: Multi-stage builds (build stage + nginx stage), layer caching, .dockerignore. Docker Compose cho local dev. Production: health checks, non-root user, security hardening."**

**🔑 Docker Concepts:**

**1. Image vs Container:**

- **Image**: Template immutable (như blueprint) - `node:20-alpine`, `nginx:alpine`
- **Container**: Running instance của image (như VM nhẹ) - isolated process
- **Dockerfile**: Script build image từ base image + commands

**2. Multi-Stage Builds:**

- **Stage 1 (Builder)**: Install deps, build app (Node.js, npm/yarn)
- **Stage 2 (Production)**: Copy built files vào nginx, serve static files
- **Benefit**: Final image nhỏ (chỉ nginx + dist), không có dev dependencies

**3. Layer Caching:**

- Docker cache layers theo thứ tự Dockerfile
- **Strategy**: Copy `package.json` trước → install deps → copy source code sau
- **Why**: `package.json` ít thay đổi → cache hit → build nhanh hơn

**🔑 Dockerfile Best Practices:**

**1. Multi-Stage Build:**

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

**2. Security:**

- **Non-root user**: Chạy container với user không phải root
- **Minimal base image**: Dùng `alpine` (nhỏ, ít attack surface)
- **Update packages**: `apk update && apk upgrade` trong build

**3. Optimization:**

- **.dockerignore**: Exclude `node_modules`, `.git`, `.env`
- **Layer ordering**: Copy files ít thay đổi trước (package.json)
- **Health checks**: `HEALTHCHECK` command cho monitoring

**🔑 Docker Compose:**

**Use cases:**

- **Local development**: Frontend + Backend + Database cùng lúc
- **Service orchestration**: Define networks, volumes, environment variables
- **Quick setup**: `docker-compose up` → chạy toàn bộ stack

**⚠️ Lỗi Thường Gặp:**

- Không dùng multi-stage → final image lớn (có dev deps)
- Copy toàn bộ code trước install → cache miss mỗi lần code thay đổi
- Chạy root user → security risk
- Không có health check → khó monitor container health
- Hardcode secrets trong Dockerfile → security vulnerability

**💡 Kiến Thức Senior:**

- **BuildKit**: Parallel builds, better caching (`DOCKER_BUILDKIT=1`)
- **Docker layer caching**: CI/CD cache layers giữa builds
- **Multi-platform builds**: `docker buildx` cho ARM64 + AMD64
- **Kubernetes**: Container orchestration cho production scale
- **Container registries**: Docker Hub, AWS ECR, Google GCR

> **Câu hỏi phỏng vấn Senior Frontend Developer** > **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [Docker Fundamentals](#1-docker-fundamentals)
2. [Dockerfile Best Practices](#2-dockerfile-best-practices)
3. [Multi-Stage Builds](#3-multi-stage-builds)
4. [Docker Compose](#4-docker-compose)
   - [4.1. Basic Docker Compose](#41-basic-docker-compose)
   - [4.2. Production Docker Compose](#42-production-docker-compose)
   - [4.3. Docker Compose Commands](#43-docker-compose-commands)
   - [4.4. Docker Commands Reference - Cheat Sheet](#44-docker-commands-reference---cheat-sheet)
5. [Security Hardening](#5-security-hardening)
6. [Performance Optimization](#6-performance-optimization)
7. [CI/CD Integration](#7-cicd-integration)
   - [7.1. Complete CI/CD Pipeline with Docker](#71-complete-cicd-pipeline-with-docker)
   - [7.2. GitHub Actions Docker Build & Push](#72-github-actions-docker-build--push)
   - [7.3. Docker Layer Caching in CI](#73-docker-layer-caching-in-ci)
   - [7.4. Deployment Strategies with Docker](#74-deployment-strategies-with-docker)
   - [7.5. Environment Management với Docker](#75-environment-management-với-docker)
   - [7.6. Monitoring & Rollback với Docker](#76-monitoring--rollback-với-docker)
   - [7.7. Docker Compose trong CI/CD](#77-docker-compose-trong-cicd)
8. [Kubernetes Basics](#8-kubernetes-basics)

---

## 1. Docker Fundamentals

### **1.1. Core Concepts**

```typescript
// ===================================================
// 🎯 **DOCKER CONCEPTS** - Khái niệm cốt lõi
// ===================================================

interface DockerConcepts {
  image: {
    definition: 'Template immutable để tạo containers';
    analogy: 'Như blueprint/khuôn mẫu';
    example: 'node:20-alpine, nginx:alpine';
    storage: 'Stored in registry (Docker Hub, ECR)';
  };

  container: {
    definition: 'Running instance của image';
    analogy: 'Như virtual machine nhẹ (không có OS riêng)';
    example: 'Web server đang chạy từ nginx image';
    lifecycle: 'Created → Running → Stopped → Removed';
  };

  dockerfile: {
    definition: 'Script để build image từ base image';
    analogy: 'Như recipe/công thức nấu ăn';
    example: 'FROM node:20 + COPY + RUN commands';
    format: 'Text file với instructions';
  };

  volume: {
    definition: 'Persistent storage cho containers';
    analogy: 'Như external hard drive';
    example: 'Database data, log files, user uploads';
    types: 'Named volumes, bind mounts, tmpfs';
  };

  network: {
    definition: 'Isolated network cho containers';
    analogy: 'Như LAN network';
    example: 'Frontend container talk to backend container';
    types: 'bridge, host, overlay, macvlan';
  };
}
```

### **1.2. Docker vs Virtual Machines**

```markdown
# ===================================================

# ⚖️ **DOCKER VS VIRTUAL MACHINES**

# ===================================================

| Aspect        | Docker Containers    | Virtual Machines     |
| ------------- | -------------------- | -------------------- |
| **OS**        | Share host OS kernel | Full OS (Guest OS)   |
| **Size**      | ~10-100 MB           | ~1-10 GB             |
| **Startup**   | Seconds              | Minutes              |
| **Resource**  | Lower overhead       | Higher overhead      |
| **Isolation** | Process-level        | Hardware-level       |
| **Use Case**  | Microservices, apps  | Legacy apps, full OS |

# ✅ Docker Advantages:

- Lightweight: Chỉ chứa app + dependencies
- Fast startup: Không cần boot OS
- Efficient: Share kernel, ít resource hơn
- Portable: Chạy giống nhau mọi nơi

# ⚠️ Docker Limitations:

- Security: Share kernel → nếu kernel có lỗi, tất cả containers bị ảnh hưởng
- OS-specific: Linux containers chạy tốt trên Linux host
- Windows/Mac: Cần Docker Desktop (VM wrapper)
```

### **1.3. Docker Architecture**

```bash
# ===================================================
# 🏗️ **DOCKER ARCHITECTURE**
# ===================================================

┌─────────────────────────────────────────┐
│         Docker Client (CLI)              │
│  docker build, docker run, docker ps    │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Docker Daemon (dockerd)            │
│  - Image management                      │
│  - Container lifecycle                  │
│  - Network management                   │
│  - Volume management                    │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Container Runtime (containerd)     │
│  - OCI (Open Container Initiative)      │
│  - RunC (container runtime)             │
└─────────────────────────────────────────┘
```

---

## 2. Dockerfile Best Practices

### **2.1. Basic Dockerfile Structure**

```dockerfile
# ===================================================
# 📝 **BASIC DOCKERFILE** - Cấu trúc cơ bản
# ===================================================

# ✅ Stage 1: Build stage - Build ứng dụng
FROM node:20-alpine AS builder

# ✅ Set working directory - Thư mục làm việc
WORKDIR /app

# ✅ Copy package files first (layer caching) - Copy package.json trước
COPY package*.json ./
COPY yarn.lock ./

# ✅ Install dependencies - Cài đặt dependencies
RUN yarn install --frozen-lockfile

# ✅ Copy source code - Copy mã nguồn
COPY . .

# ✅ Build application - Build ứng dụng
RUN yarn build

# ✅ Stage 2: Production stage - Stage production
FROM nginx:1.25-alpine

# ✅ Copy built files from builder - Copy files đã build
COPY --from=builder /app/dist /usr/share/nginx/html

# ✅ Copy nginx configuration - Copy cấu hình nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ✅ Expose port - Mở port
EXPOSE 80

# ✅ Health check - Kiểm tra sức khỏe container
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

# ✅ Start nginx - Khởi động nginx
CMD ["nginx", "-g", "daemon off;"]
```

### **2.2. Advanced Multi-Stage Build**

```dockerfile
# ===================================================
# 🚀 **ADVANCED MULTI-STAGE BUILD** - Build nâng cao
# ===================================================

# ✅ Stage 1: Dependencies stage - Stage cài đặt dependencies
FROM node:20-alpine AS deps

WORKDIR /app

# ✅ Copy only package files - Chỉ copy package files
COPY package*.json yarn.lock ./

# ✅ Install dependencies (cached layer) - Cài đặt dependencies (cache layer)
RUN yarn install --frozen-lockfile --production=false

# ✅ Stage 2: Builder stage - Stage build
FROM node:20-alpine AS builder

WORKDIR /app

# ✅ Copy dependencies from deps stage - Copy dependencies từ stage deps
COPY --from=deps /app/node_modules ./node_modules

# ✅ Copy source code - Copy mã nguồn
COPY . .

# ✅ Build arguments - Build arguments
ARG VITE_API_URL
ARG VITE_SENTRY_DSN
ARG NODE_ENV=production

# ✅ Set environment variables - Đặt biến môi trường
ENV NODE_ENV=$NODE_ENV
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_SENTRY_DSN=$VITE_SENTRY_DSN

# ✅ Build application - Build ứng dụng
RUN yarn build

# ✅ Stage 3: Production stage - Stage production
FROM nginx:1.25-alpine

# ✅ Security: Update packages - Cập nhật packages
RUN apk update && apk upgrade && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# ✅ Security: Create non-root user - Tạo user không phải root
RUN addgroup -g 1001 -S nginx-group && \
    adduser -S nginx-user -u 1001 -G nginx-group

# ✅ Copy built files with proper ownership - Copy files với quyền sở hữu đúng
COPY --from=builder --chown=nginx-user:nginx-group /app/dist /usr/share/nginx/html

# ✅ Copy nginx configuration - Copy cấu hình nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ✅ Health check - Kiểm tra sức khỏe
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# ✅ Switch to non-root user - Chuyển sang user không phải root
USER nginx-user

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### **2.3. .dockerignore File**

```dockerignore
# ===================================================
# 🚫 **.DOCKERIGNORE** - Files không copy vào image
# ===================================================

# ✅ Dependencies - Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-store/

# ✅ Git - Git files
.git/
.gitignore
.gitattributes

# ✅ IDE - IDE files
.vscode/
.idea/
*.swp
*.swo
*~

# ✅ Build outputs - Build outputs
dist/
build/
.next/
out/
coverage/
.nyc_output/

# ✅ Environment files - Environment files
.env
.env.local
.env.*.local
.env.production
.env.development

# ✅ Documentation - Documentation
README.md
CHANGELOG.md
LICENSE
docs/

# ✅ Test files - Test files
*.test.ts
*.test.tsx
*.spec.ts
*.spec.tsx
__tests__/
__mocks__/

# ✅ CI/CD - CI/CD files
.github/
.gitlab-ci.yml
azure-pipelines.yml

# ✅ Docker files - Docker files
Dockerfile*
docker-compose*.yml
.dockerignore

# ✅ Misc - Misc
.DS_Store
Thumbs.db
*.log
```

---

## 3. Multi-Stage Builds

### **3.1. Why Multi-Stage Builds?**

```markdown
# ===================================================

# 🎯 **WHY MULTI-STAGE BUILDS?**

# ===================================================

## ❌ Single-Stage Build Problems:

1. **Large Image Size:**

   - Includes: Node.js runtime + npm/yarn + dev dependencies + build tools
   - Size: ~500MB - 1GB
   - Problem: Slow pull/push, waste storage

2. **Security Risks:**

   - Dev dependencies có thể chứa vulnerabilities
   - Build tools không cần trong production

3. **Unnecessary Files:**
   - Source code, test files, config files
   - Không cần trong production container

## ✅ Multi-Stage Build Benefits:

1. **Smaller Final Image:**

   - Only: nginx + built static files
   - Size: ~20-50MB (90% reduction)
   - Benefit: Fast pull/push, efficient storage

2. **Security:**

   - No dev dependencies in production
   - Minimal attack surface

3. **Separation of Concerns:**
   - Build stage: Development tools
   - Production stage: Only runtime needed
```

### **3.2. Build Arguments & Environment Variables**

```dockerfile
# ===================================================
# 🔧 **BUILD ARGUMENTS & ENV VARS**
# ===================================================

FROM node:20-alpine AS builder

WORKDIR /app

# ✅ Build arguments (build-time only) - Build arguments (chỉ khi build)
ARG NODE_ENV=production
ARG VITE_API_URL
ARG VITE_SENTRY_DSN
ARG BUILD_VERSION

# ✅ Environment variables (runtime) - Biến môi trường (runtime)
ENV NODE_ENV=$NODE_ENV
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_SENTRY_DSN=$VITE_SENTRY_DSN
ENV BUILD_VERSION=$BUILD_VERSION

COPY package*.json ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

# ✅ Build with arguments - Build với arguments
# docker build --build-arg VITE_API_URL=https://api.example.com -t myapp:latest .
```

```bash
# ===================================================
# 🚀 **BUILD COMMANDS** - Lệnh build
# ===================================================

# ✅ Basic build - Build cơ bản
docker build -t myapp:latest .

# ✅ Build with arguments - Build với arguments
docker build \
  --build-arg NODE_ENV=production \
  --build-arg VITE_API_URL=https://api.example.com \
  --build-arg BUILD_VERSION=1.0.0 \
  -t myapp:latest .

# ✅ Build specific stage - Build stage cụ thể
docker build --target builder -t myapp:builder .

# ✅ Build with cache - Build với cache
docker build --cache-from myapp:latest -t myapp:new .

# ✅ Multi-platform build - Build nhiều platform
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:latest \
  --push .
```

---

## 4. Docker Compose

### **4.1. Basic Docker Compose**

```yaml
# ===================================================
# 🐙 **DOCKER COMPOSE** (docker-compose.yml)
# ===================================================

version: '3.8'

services:
  # ✅ Frontend service - Service frontend
  frontend:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: development
        VITE_API_URL: http://backend:3000
    ports:
      - '3000:80' # host:container
    volumes:
      - ./src:/app/src # Hot reload trong dev
      - /app/node_modules # Anonymous volume (override)
    environment:
      - NODE_ENV=development
      - VITE_API_URL=http://backend:3000
    depends_on:
      - backend
    networks:
      - app-network

  # ✅ Backend service - Service backend
  backend:
    image: node:20-alpine
    working_dir: /app
    command: npm start
    ports:
      - '3001:3000'
    volumes:
      - ./backend:/app
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    networks:
      - app-network

  # ✅ Database service - Service database
  db:
    image: postgres:15-alpine
    ports:
      - '5432:5432'
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - app-network

  # ✅ Redis service (optional) - Service Redis (tùy chọn)
  redis:
    image: redis:7-alpine
    ports:
      - '6379:6379'
    networks:
      - app-network

# ✅ Networks - Networks
networks:
  app-network:
    driver: bridge

# ✅ Volumes - Volumes
volumes:
  postgres-data:
    driver: local
```

### **4.2. Production Docker Compose**

```yaml
# ===================================================
# 🚀 **PRODUCTION DOCKER COMPOSE** (docker-compose.prod.yml)
# ===================================================

version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
        VITE_API_URL: ${VITE_API_URL}
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - ./ssl:/etc/nginx/ssl:ro # SSL certificates
    environment:
      - NODE_ENV=production
    restart: unless-stopped
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost/']
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 10s
    networks:
      - app-network
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M

  # ✅ Nginx reverse proxy - Nginx reverse proxy
  nginx-proxy:
    image: nginx:alpine
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx-proxy.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - frontend
    restart: unless-stopped
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```

### **4.3. Docker Compose Commands**

```bash
# ===================================================
# 🛠️ **DOCKER COMPOSE COMMANDS** - Lệnh Docker Compose
# ===================================================

# ✅ Start services - Khởi động services
docker-compose up

# ✅ Start in background - Khởi động ở background
docker-compose up -d

# ✅ Build and start - Build và khởi động
docker-compose up --build

# ✅ Stop services - Dừng services
docker-compose stop

# ✅ Stop and remove - Dừng và xóa
docker-compose down

# ✅ View logs - Xem logs
docker-compose logs -f frontend

# ✅ Execute command - Chạy lệnh
docker-compose exec frontend sh

# ✅ Scale services - Scale services
docker-compose up --scale frontend=3

# ✅ Use specific file - Dùng file cụ thể
docker-compose -f docker-compose.prod.yml up
```

---

## 4.4. Docker Commands Reference - Cheat Sheet

### **4.4.1. Docker Commands - Lệnh Docker Cơ Bản**

```bash
# ===================================================
# 🐳 **DOCKER COMMANDS CHEAT SHEET** - Bảng Lệnh Docker
# ===================================================

# ┌─────────────────────────────────────────────────┐
# │ 📦 IMAGE COMMANDS - Lệnh Quản Lý Image         │
# └─────────────────────────────────────────────────┘

# ✅ Build image - Build image
docker build -t myapp:latest .
docker build -t myapp:v1.0.0 -f Dockerfile.prod .

# ✅ List images - Liệt kê images
docker images
docker image ls

# ✅ Remove image - Xóa image
docker rmi myapp:latest
docker image rm myapp:latest

# ✅ Remove all unused images - Xóa tất cả images không dùng
docker image prune -a

# ✅ Inspect image - Xem chi tiết image
docker inspect myapp:latest

# ✅ Tag image - Gắn tag cho image
docker tag myapp:latest myapp:v1.0.0

# ✅ Push image to registry - Đẩy image lên registry
docker push myorg/myapp:latest

# ✅ Pull image from registry - Kéo image từ registry
docker pull myorg/myapp:latest

# ┌─────────────────────────────────────────────────┐
# │ 🚀 CONTAINER COMMANDS - Lệnh Quản Lý Container │
# └─────────────────────────────────────────────────┘

# ✅ Run container - Chạy container
docker run myapp:latest
docker run -d -p 3000:80 --name myapp myapp:latest
docker run -it --rm node:20-alpine sh  # Interactive shell

# ✅ List containers - Liệt kê containers
docker ps              # Running containers
docker ps -a           # All containers (including stopped)
docker container ls    # Same as docker ps

# ✅ Start/Stop container - Khởi động/Dừng container
docker start myapp
docker stop myapp
docker restart myapp

# ✅ Remove container - Xóa container
docker rm myapp
docker container rm myapp

# ✅ Remove all stopped containers - Xóa tất cả containers đã dừng
docker container prune

# ✅ Execute command in container - Chạy lệnh trong container
docker exec -it myapp sh
docker exec myapp ls /app

# ✅ View logs - Xem logs
docker logs myapp
docker logs -f myapp        # Follow logs (real-time)
docker logs --tail 100 myapp # Last 100 lines

# ✅ Inspect container - Xem chi tiết container
docker inspect myapp

# ✅ Copy files - Copy files
docker cp myapp:/app/dist ./local-dist  # Container → Local
docker cp ./local-file myapp:/app/      # Local → Container

# ✅ Container stats - Thống kê container
docker stats myapp
docker stats              # All containers

# ┌─────────────────────────────────────────────────┐
# │ 🧹 CLEANUP COMMANDS - Lệnh Dọn Dẹp              │
# └─────────────────────────────────────────────────┘

# ✅ Remove all stopped containers - Xóa containers đã dừng
docker container prune

# ✅ Remove all unused images - Xóa images không dùng
docker image prune -a

# ✅ Remove all unused volumes - Xóa volumes không dùng
docker volume prune

# ✅ Remove all unused networks - Xóa networks không dùng
docker network prune

# ✅ Remove everything (nuclear option) - Xóa tất cả
docker system prune -a --volumes

# ┌─────────────────────────────────────────────────┐
# │ 🔍 INSPECT & DEBUG - Lệnh Kiểm Tra & Debug      │
# └─────────────────────────────────────────────────┘

# ✅ Container processes - Tiến trình trong container
docker top myapp

# ✅ Container resource usage - Sử dụng tài nguyên
docker stats myapp

# ✅ Container events - Sự kiện container
docker events

# ✅ Docker system info - Thông tin hệ thống Docker
docker info
docker version

# ✅ Build history - Lịch sử build
docker history myapp:latest

# ┌─────────────────────────────────────────────────┐
# │ 🌐 NETWORK COMMANDS - Lệnh Quản Lý Network     │
# └─────────────────────────────────────────────────┘

# ✅ List networks - Liệt kê networks
docker network ls

# ✅ Create network - Tạo network
docker network create my-network

# ✅ Inspect network - Xem chi tiết network
docker network inspect my-network

# ✅ Connect container to network - Kết nối container vào network
docker network connect my-network myapp

# ✅ Disconnect container from network - Ngắt kết nối
docker network disconnect my-network myapp

# ┌─────────────────────────────────────────────────┐
# │ 💾 VOLUME COMMANDS - Lệnh Quản Lý Volume        │
# └─────────────────────────────────────────────────┘

# ✅ List volumes - Liệt kê volumes
docker volume ls

# ✅ Create volume - Tạo volume
docker volume create my-volume

# ✅ Inspect volume - Xem chi tiết volume
docker volume inspect my-volume

# ✅ Remove volume - Xóa volume
docker volume rm my-volume
```

### **4.4.2. Docker Compose Commands - Lệnh Docker Compose**

```bash
# ===================================================
# 🐙 **DOCKER COMPOSE COMMANDS CHEAT SHEET** - Bảng Lệnh Compose
# ===================================================

# ┌─────────────────────────────────────────────────┐
# │ 🚀 LIFECYCLE COMMANDS - Lệnh Vòng Đời          │
# └─────────────────────────────────────────────────┘

# ✅ Start services - Khởi động services
docker-compose up                    # Foreground
docker-compose up -d                 # Background (detached)
docker-compose up --build            # Build và start
docker-compose up --build --force-recreate  # Force recreate

# ✅ Stop services - Dừng services
docker-compose stop                  # Stop (giữ containers)
docker-compose down                  # Stop và remove containers
docker-compose down -v               # Stop, remove containers + volumes

# ✅ Restart services - Khởi động lại services
docker-compose restart               # Restart tất cả
docker-compose restart frontend      # Restart service cụ thể

# ✅ Pause/Unpause - Tạm dừng/Tiếp tục
docker-compose pause
docker-compose unpause

# ┌─────────────────────────────────────────────────┐
# │ 🔨 BUILD COMMANDS - Lệnh Build                  │
# └─────────────────────────────────────────────────┘

# ✅ Build images - Build images
docker-compose build                 # Build tất cả services
docker-compose build frontend        # Build service cụ thể
docker-compose build --no-cache     # Build không dùng cache

# ✅ Rebuild specific service - Build lại service cụ thể
docker-compose up --build frontend

# ┌─────────────────────────────────────────────────┐
# │ 📊 STATUS & LOGS - Lệnh Trạng Thái & Logs       │
# └─────────────────────────────────────────────────┘

# ✅ List services - Liệt kê services
docker-compose ps                    # Running services
docker-compose ps -a                 # All services

# ✅ View logs - Xem logs
docker-compose logs                  # Tất cả services
docker-compose logs frontend         # Service cụ thể
docker-compose logs -f frontend      # Follow logs (real-time)
docker-compose logs --tail 100       # Last 100 lines

# ✅ Service status - Trạng thái services
docker-compose top                   # Processes trong services

# ┌─────────────────────────────────────────────────┐
# │ ⚙️ EXEC & RUN - Lệnh Thực Thi                   │
# └─────────────────────────────────────────────────┘

# ✅ Execute command - Chạy lệnh trong service
docker-compose exec frontend sh      # Shell trong container
docker-compose exec frontend ls /app # Chạy lệnh cụ thể

# ✅ Run one-off command - Chạy lệnh một lần
docker-compose run frontend npm test # Chạy test
docker-compose run --rm frontend sh  # Chạy và xóa sau khi xong

# ┌─────────────────────────────────────────────────┐
# │ 📁 FILE & CONFIG - Lệnh File & Cấu Hình         │
# └─────────────────────────────────────────────────┘

# ✅ Use specific file - Dùng file cụ thể
docker-compose -f docker-compose.prod.yml up
docker-compose -f docker-compose.yml -f docker-compose.override.yml up

# ✅ Validate config - Kiểm tra cấu hình
docker-compose config                # Hiển thị config đã merge
docker-compose config --services     # Liệt kê services

# ┌─────────────────────────────────────────────────┐
# │ 🔄 SCALE & UPDATE - Lệnh Scale & Cập Nhật       │
# └─────────────────────────────────────────────────┘

# ✅ Scale services - Scale services
docker-compose up --scale frontend=3 # Scale frontend lên 3 instances

# ✅ Pull latest images - Kéo images mới nhất
docker-compose pull                  # Pull tất cả
docker-compose pull frontend         # Pull service cụ thể

# ┌─────────────────────────────────────────────────┐
# │ 🧹 CLEANUP - Lệnh Dọn Dẹp                      │
# └─────────────────────────────────────────────────┘

# ✅ Remove stopped containers - Xóa containers đã dừng
docker-compose rm                    # Interactive
docker-compose rm -f                 # Force (không hỏi)

# ✅ Remove volumes - Xóa volumes
docker-compose down -v               # Xóa volumes khi down
```

### **4.4.3. Công Thức Docker Build Dễ Nhớ - Mnemonics**

```bash
# ===================================================
# 🧠 **DOCKER BUILD FORMULA - CÔNG THỨC DỄ NHỚ**
# ===================================================

# ┌─────────────────────────────────────────────────┐
# │ 📝 CÔNG THỨC CƠ BẢN - Basic Formula            │
# └─────────────────────────────────────────────────┘

# 💡 Công thức: docker build [OPTIONS] -t [IMAGE:TAG] [CONTEXT]
# 💡 Formula: docker build [OPTIONS] -t [IMAGE:TAG] [CONTEXT]

# ✅ Công thức đơn giản nhất - Simplest formula
docker build -t myapp:latest .

# 💡 Giải thích:
# - docker build: Lệnh build
# - -t myapp:latest: Tag image (tên:phiên bản)
# - . : Context (thư mục hiện tại)

# ┌─────────────────────────────────────────────────┐
# │ 🎯 CÔNG THỨC ĐẦY ĐỦ - Full Formula             │
# └─────────────────────────────────────────────────┘

# 💡 Công thức đầy đủ với các options phổ biến:
docker build \
  --file Dockerfile.prod \           # -f: Dockerfile cụ thể
  --tag myapp:v1.0.0 \               # -t: Tag image
  --build-arg NODE_ENV=production \  # --build-arg: Build arguments
  --build-arg VITE_API_URL=https://api.example.com \
  --target builder \                 # --target: Build stage cụ thể
  --cache-from myapp:latest \        # --cache-from: Cache từ image
  --progress=plain \                  # --progress: Hiển thị progress
  --no-cache \                       # --no-cache: Không dùng cache
  .

# ┌─────────────────────────────────────────────────┐
# │ 🧠 MNEMONICS - CÁCH NHỚ                        │
# └─────────────────────────────────────────────────┘

# 💡 Cách nhớ công thức Docker build:
#
# 1. "Build - Tag - Context" (BTC)
#    docker build -t [TAG] [CONTEXT]
#    → Build image, Tag nó, từ Context
#
# 2. "File - Tag - Args - Target - Context" (FTATC)
#    docker build -f [FILE] -t [TAG] --build-arg [ARGS] --target [STAGE] [CONTEXT]
#    → File Dockerfile, Tag image, Arguments, Target stage, Context
#
# 3. "Context là dấu chấm" (.)
#    → Luôn nhớ context là thư mục (thường là .)
#
# 4. "Tag = Name:Version"
#    → myapp:latest, myapp:v1.0.0, myapp:prod

# ┌─────────────────────────────────────────────────┐
# │ 📋 CÁC CÔNG THỨC THƯỜNG DÙNG - Common Formulas │
# └─────────────────────────────────────────────────┘

# ✅ 1. Build cơ bản - Basic build
docker build -t myapp:latest .

# ✅ 2. Build với Dockerfile cụ thể - Specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# ✅ 3. Build với build arguments - With build args
docker build \
  --build-arg NODE_ENV=production \
  --build-arg VITE_API_URL=https://api.example.com \
  -t myapp:latest .

# ✅ 4. Build stage cụ thể - Specific stage
docker build --target builder -t myapp:builder .

# ✅ 5. Build không cache - No cache
docker build --no-cache -t myapp:latest .

# ✅ 6. Build với cache từ image - Cache from image
docker build --cache-from myapp:latest -t myapp:new .

# ✅ 7. Build multi-platform - Multi-platform
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myapp:latest \
  --push .

# ✅ 8. Build với BuildKit - With BuildKit
DOCKER_BUILDKIT=1 docker build -t myapp:latest .

# ┌─────────────────────────────────────────────────┐
# │ 🎨 CÔNG THỨC THEO MỤC ĐÍCH - By Purpose        │
# └─────────────────────────────────────────────────┘

# 🎯 Development Build - Build cho development
docker build \
  --build-arg NODE_ENV=development \
  -t myapp:dev .

# 🎯 Production Build - Build cho production
docker build \
  --build-arg NODE_ENV=production \
  --build-arg VITE_API_URL=https://api.prod.com \
  -t myapp:prod .

# 🎯 Staging Build - Build cho staging
docker build \
  --build-arg NODE_ENV=staging \
  --build-arg VITE_API_URL=https://api.staging.com \
  -t myapp:staging .

# 🎯 Build với version - Build with version
docker build \
  --build-arg BUILD_VERSION=$(git rev-parse --short HEAD) \
  -t myapp:$(git rev-parse --short HEAD) .

# ┌─────────────────────────────────────────────────┐
# │ 💡 TIPS & TRICKS - Mẹo Vặt                      │
# └─────────────────────────────────────────────────┘

# ✅ Tip 1: Luôn dùng -t để tag (dễ quản lý)
docker build -t myapp:latest .

# ✅ Tip 2: Dùng --progress=plain để debug
docker build --progress=plain -t myapp:latest .

# ✅ Tip 3: Dùng --no-cache khi cần build lại từ đầu
docker build --no-cache -t myapp:latest .

# ✅ Tip 4: Dùng --target để build stage cụ thể (multi-stage)
docker build --target builder -t myapp:builder .

# ✅ Tip 5: Dùng BuildKit để build nhanh hơn
export DOCKER_BUILDKIT=1
docker build -t myapp:latest .

# ✅ Tip 6: Dùng docker buildx cho multi-platform
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# ┌─────────────────────────────────────────────────┐
# │ 🧮 CÔNG THỨC NHỚ LÂU - Long-term Memory        │
# └─────────────────────────────────────────────────┘

# 💡 Công thức "BTC" (Build - Tag - Context):
#    docker build -t [TAG] [CONTEXT]
#    → Nhớ: "Build Tag Context" = BTC (như Bitcoin 😄)

# 💡 Công thức "FTATC" (File - Tag - Args - Target - Context):
#    docker build -f [FILE] -t [TAG] --build-arg [ARGS] --target [STAGE] [CONTEXT]
#    → Nhớ: "File Tag Args Target Context" = FTATC

# 💡 Công thức "NAT" (Name - Args - Tag):
#    docker build --build-arg [ARGS] -t [NAME:TAG] [CONTEXT]
#    → Nhớ: "Name Args Tag" = NAT

# 💡 Công thức "PACT" (Platform - Args - Cache - Tag):
#    docker buildx build --platform [PLATFORM] --build-arg [ARGS] --cache-from [CACHE] -t [TAG] [CONTEXT]
#    → Nhớ: "Platform Args Cache Tag" = PACT
```

---

## 5. Security Hardening

### **5.1. Non-Root User**

```dockerfile
# ===================================================
# 🔒 **NON-ROOT USER** - User không phải root
# ===================================================

FROM nginx:1.25-alpine

# ✅ Create non-root user - Tạo user không phải root
RUN addgroup -g 1001 -S nginx-group && \
    adduser -S nginx-user -u 1001 -G nginx-group

# ✅ Copy files with proper ownership - Copy files với quyền sở hữu đúng
COPY --from=builder --chown=nginx-user:nginx-group /app/dist /usr/share/nginx/html

# ✅ Switch to non-root user - Chuyển sang user không phải root
USER nginx-user

# ✅ Verify user - Kiểm tra user
# RUN whoami  # Should output: nginx-user
```

### **5.2. Minimal Base Image**

```dockerfile
# ===================================================
# 🎯 **MINIMAL BASE IMAGE** - Base image tối thiểu
# ===================================================

# ✅ GOOD: Alpine Linux (5MB) - Alpine Linux (5MB)
FROM node:20-alpine

# ❌ BAD: Full Debian (150MB) - Full Debian (150MB)
# FROM node:20

# ✅ Benefits of Alpine:
# - Small size: 5MB vs 150MB
# - Security: Fewer packages = smaller attack surface
# - Fast: Quick pull/push
# - Production-ready: Used by major projects
```

### **5.3. Security Scanning**

```bash
# ===================================================
# 🔍 **SECURITY SCANNING** - Quét bảo mật
# ===================================================

# ✅ Docker Scout (built-in) - Docker Scout (tích hợp)
docker scout cves myapp:latest

# ✅ Trivy scanner - Trivy scanner
trivy image myapp:latest

# ✅ Snyk scanner - Snyk scanner
snyk test --docker myapp:latest

# ✅ Scan in CI/CD - Quét trong CI/CD
# .github/workflows/security.yml
- name: Scan image
  run: |
    docker build -t myapp:latest .
    trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest
```

### **5.4. Secrets Management**

```yaml
# ===================================================
# 🔐 **SECRETS MANAGEMENT** - Quản lý secrets
# ===================================================

# ✅ Docker Secrets (Docker Swarm) - Docker Secrets
version: '3.8'
services:
  frontend:
    secrets:
      - api_key
    environment:
      - API_KEY_FILE=/run/secrets/api_key

secrets:
  api_key:
    external: true
# ✅ Environment variables (not in Dockerfile) - Biến môi trường (không trong Dockerfile)
# ❌ BAD: ARG API_KEY=secret123  # Exposed in image layers
# ✅ GOOD: docker run -e API_KEY=secret123 myapp
```

---

## 6. Performance Optimization

### **6.1. Layer Caching Strategy**

```dockerfile
# ===================================================
# ⚡ **LAYER CACHING** - Cache layers
# ===================================================

# ✅ OPTIMAL ORDER - Thứ tự tối ưu
FROM node:20-alpine

WORKDIR /app

# ✅ Step 1: Copy package files (changes rarely) - Copy package files (ít thay đổi)
COPY package*.json yarn.lock ./

# ✅ Step 2: Install dependencies (cached if package.json unchanged) - Cài đặt dependencies (cache nếu package.json không đổi)
RUN yarn install --frozen-lockfile

# ✅ Step 3: Copy source code (changes frequently) - Copy mã nguồn (thay đổi thường xuyên)
COPY . .

# ✅ Step 4: Build (only runs if source changed) - Build (chỉ chạy nếu source thay đổi)
RUN yarn build

# ❌ BAD ORDER - Thứ tự sai
# COPY . .  # Changes every time → cache miss
# RUN yarn install  # Runs every time
```

### **6.2. BuildKit Optimization**

```bash
# ===================================================
# 🚀 **BUILDKIT** - Build engine mới
# ===================================================

# ✅ Enable BuildKit - Bật BuildKit
export DOCKER_BUILDKIT=1
docker build -t myapp:latest .

# ✅ Or in docker-compose - Hoặc trong docker-compose
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

# ✅ Benefits:
# - Parallel builds: Build stages in parallel
# - Better caching: More efficient cache
# - Mount cache: Share cache between builds
# - Secrets: Secure secret handling
```

### **6.3. Image Size Optimization**

```dockerfile
# ===================================================
# 📦 **IMAGE SIZE OPTIMIZATION** - Tối ưu kích thước image
# ===================================================

FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

# ✅ Production stage - Stage production
FROM nginx:1.25-alpine

# ✅ Remove unnecessary files - Xóa files không cần
RUN rm -rf /usr/share/nginx/html/*

# ✅ Copy only built files - Chỉ copy files đã build
COPY --from=builder /app/dist /usr/share/nginx/html

# ✅ Clean up - Dọn dẹp
RUN apk del --no-cache curl || true

# ✅ Result: ~20-30MB final image
```

---

## 7. CI/CD Integration

### **7.1. Complete CI/CD Pipeline with Docker**

```yaml
# ===================================================
# 🔄 **COMPLETE CI/CD PIPELINE WITH DOCKER**
# ===================================================

name: CI/CD Pipeline with Docker

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

# ✅ Pipeline stages với Docker
jobs:
  # Stage 1: Code Quality
  lint-and-format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci
      - run: npm run lint
      - run: npm run format:check
      - run: npm run type-check

  # Stage 2: Unit Tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - run: npm ci
      - run: npm run test:coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

  # Stage 3: Build Docker Image
  build-docker:
    runs-on: ubuntu-latest
    needs: [lint-and-format, test]
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            NODE_ENV=production
            VITE_API_URL=${{ secrets.VITE_API_URL }}

      - name: Save Docker image
        run: |
          docker save myapp:${{ github.sha }} | gzip > myapp-image.tar.gz

      - name: Upload Docker image artifact
        uses: actions/upload-artifact@v3
        with:
          name: docker-image
          path: myapp-image.tar.gz
          retention-days: 7

  # Stage 4: E2E Tests với Docker
  e2e:
    runs-on: ubuntu-latest
    needs: build-docker
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Download Docker image artifact
        uses: actions/download-artifact@v3
        with:
          name: docker-image
          path: ./

      - name: Load Docker image
        run: |
          gunzip -c myapp-image.tar.gz | docker load

      - name: Run container
        run: |
          docker run -d -p 3000:80 --name myapp-test myapp:${{ github.sha }}

      - name: Wait for container
        run: sleep 10

      - name: Run E2E tests
        run: |
          npm ci
          npx playwright install --with-deps
          npm run test:e2e -- --baseURL=http://localhost:3000

      - name: Cleanup
        if: always()
        run: docker rm -f myapp-test

  # Stage 5: Deploy to Staging (Docker)
  deploy-staging:
    runs-on: ubuntu-latest
    needs: [build-docker, e2e]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - uses: actions/checkout@v4

      - name: Download Docker image artifact
        uses: actions/download-artifact@v3
        with:
          name: docker-image
          path: ./

      - name: Load Docker image
        run: |
          gunzip -c myapp-image.tar.gz | docker load

      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Tag and push image
        run: |
          docker tag myapp:${{ github.sha }} ${{ secrets.REGISTRY_URL }}/myapp:staging
          docker push ${{ secrets.REGISTRY_URL }}/myapp:staging

      - name: Deploy to staging server
        run: |
          ssh ${{ secrets.STAGING_SSH_USER }}@${{ secrets.STAGING_HOST }} \
            "docker pull ${{ secrets.REGISTRY_URL }}/myapp:staging && \
             docker-compose -f /opt/app/docker-compose.staging.yml up -d"

  # Stage 6: Deploy to Production (Docker)
  deploy-production:
    runs-on: ubuntu-latest
    needs: [build-docker, e2e]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4

      - name: Download Docker image artifact
        uses: actions/download-artifact@v3
        with:
          name: docker-image
          path: ./

      - name: Load Docker image
        run: |
          gunzip -c myapp-image.tar.gz | docker load

      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Tag and push image
        run: |
          docker tag myapp:${{ github.sha }} ${{ secrets.REGISTRY_URL }}/myapp:latest
          docker tag myapp:${{ github.sha }} ${{ secrets.REGISTRY_URL }}/myapp:${{ github.sha }}
          docker push ${{ secrets.REGISTRY_URL }}/myapp:latest
          docker push ${{ secrets.REGISTRY_URL }}/myapp:${{ github.sha }}

      - name: Deploy to production (Blue-Green)
        run: |
          ssh ${{ secrets.PROD_SSH_USER }}@${{ secrets.PROD_HOST }} \
            "docker pull ${{ secrets.REGISTRY_URL }}/myapp:latest && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d --no-deps frontend"

      - name: Create Sentry release
        uses: getsentry/action-release@v1
        with:
          environment: production
          version: ${{ github.sha }}
```

### **7.2. GitHub Actions Docker Build & Push**

on:
push:
branches: [main]
tags: - 'v\*'

jobs:
build-and-push:
runs-on: ubuntu-latest
steps: - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: myorg/myapp
          tags: |
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=registry,ref=myorg/myapp:buildcache
          cache-to: type=registry,ref=myorg/myapp:buildcache,mode=max
          build-args: |
            NODE_ENV=production
            VITE_API_URL=${{ secrets.VITE_API_URL }}

````

### **7.3. Docker Layer Caching in CI**

```yaml
# ===================================================
# 💾 **DOCKER LAYER CACHING** - Cache layers trong CI
# ===================================================

- name: Build with cache
  uses: docker/build-push-action@v5
  with:
    context: .
    push: false
    tags: myapp:latest
    cache-from: |
      type=registry,ref=myorg/myapp:buildcache
      type=gha  # GitHub Actions cache
    cache-to: |
      type=registry,ref=myorg/myapp:buildcache,mode=max
      type=gha,mode=max
````

### **7.4. Deployment Strategies with Docker**

#### **7.4.1. Blue-Green Deployment với Docker**

```yaml
# ===================================================
# 🔵🟢 **BLUE-GREEN DEPLOYMENT WITH DOCKER**
# ===================================================

name: Blue-Green Deploy with Docker

on:
  workflow_dispatch:
    inputs:
      target:
        description: 'Deploy target (blue/green)'
        required: true
        type: choice
        options:
          - blue
          - green

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myorg/myapp:${{ inputs.target }}
            myorg/myapp:${{ github.sha }}
          cache-from: type=registry,ref=myorg/myapp:buildcache
          cache-to: type=registry,ref=myorg/myapp:buildcache,mode=max

      - name: Deploy to ${{ inputs.target }} environment
        run: |
          # Deploy to blue or green environment
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:${{ inputs.target }} && \
             docker-compose -f /opt/app/docker-compose.${{ inputs.target }}.yml up -d"

      - name: Run smoke tests
        run: |
          TARGET_URL="https://${{ inputs.target }}.example.com"
          curl -f $TARGET_URL/health || exit 1

      - name: Switch traffic to ${{ inputs.target }}
        run: |
          # Update load balancer to point to new environment
          ssh ${{ secrets.SSH_USER }}@${{ secrets.LB_HOST }} \
            "update-lb-config --target ${{ inputs.target }}"
```

#### **7.4.2. Canary Deployment với Docker**

```yaml
# ===================================================
# 🐤 **CANARY DEPLOYMENT WITH DOCKER** (Gradual rollout)
# ===================================================

name: Canary Deploy with Docker

on:
  workflow_dispatch:
    inputs:
      canary-percentage:
        description: 'Canary traffic percentage (10, 25, 50, 100)'
        required: true
        type: choice
        options: ['10', '25', '50', '100']

jobs:
  deploy-canary:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build and push canary image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: myorg/myapp:canary
          cache-from: type=registry,ref=myorg/myapp:buildcache

      - name: Deploy canary
        run: |
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:canary && \
             docker-compose -f /opt/app/docker-compose.canary.yml up -d"

      - name: Update traffic split
        run: |
          # Update load balancer traffic split
          curl -X POST ${{ secrets.LB_API }}/traffic-split \
            -H "Authorization: Bearer ${{ secrets.LB_TOKEN }}" \
            -d '{"canary": ${{ inputs.canary-percentage }}, "production": ${{ 100 - inputs.canary-percentage }}}'

      - name: Monitor canary for 10 minutes
        run: |
          sleep 600
          ERROR_RATE=$(curl -s ${{ secrets.MONITORING_API }}/metrics | jq '.error_rate')
          if [ "$ERROR_RATE" -gt "1" ]; then
            echo "Canary failed! Rolling back..."
            exit 1
          fi

      - name: Promote canary to production
        if: inputs.canary-percentage == '100'
        run: |
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker tag myorg/myapp:canary myorg/myapp:latest && \
             docker push myorg/myapp:latest && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d"
```

### **7.5. Environment Management với Docker**

```yaml
# ===================================================
# 🌍 **MULTI-ENVIRONMENT DOCKER BUILDS**
# ===================================================

name: Multi-Environment Docker Build

on:
  push:
    branches: [main, develop, staging]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [development, staging, production]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Set environment variables
        run: |
          if [ "${{ matrix.environment }}" == "production" ]; then
            echo "VITE_API_URL=https://api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_PROD }}" >> $GITHUB_ENV
            echo "IMAGE_TAG=prod" >> $GITHUB_ENV
          elif [ "${{ matrix.environment }}" == "staging" ]; then
            echo "VITE_API_URL=https://staging-api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_STAGING }}" >> $GITHUB_ENV
            echo "IMAGE_TAG=staging" >> $GITHUB_ENV
          else
            echo "VITE_API_URL=http://localhost:3000" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=" >> $GITHUB_ENV
            echo "IMAGE_TAG=dev" >> $GITHUB_ENV
          fi

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: myorg/myapp:${{ env.IMAGE_TAG }}
          build-args: |
            NODE_ENV=${{ matrix.environment }}
            VITE_API_URL=${{ env.VITE_API_URL }}
            VITE_SENTRY_DSN=${{ env.VITE_SENTRY_DSN }}
          cache-from: type=registry,ref=myorg/myapp:buildcache
          cache-to: type=registry,ref=myorg/myapp:buildcache,mode=max
```

### **7.6. Monitoring & Rollback với Docker**

```yaml
# ===================================================
# ⏪ **AUTOMATIC ROLLBACK WITH DOCKER**
# ===================================================

name: Deploy with Rollback

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Get previous deployment
        id: previous
        run: |
          PREV_VERSION=$(ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker images myorg/myapp --format '{{.Tag}}' | grep -v latest | head -1")
          echo "version=$PREV_VERSION" >> $GITHUB_OUTPUT
          echo "Previous version: $PREV_VERSION"

      - name: Build and push new version
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            myorg/myapp:${{ github.sha }}
            myorg/myapp:latest
          cache-from: type=registry,ref=myorg/myapp:buildcache

      - name: Deploy new version
        run: |
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:${{ github.sha }} && \
             docker tag myorg/myapp:${{ github.sha }} myorg/myapp:current && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d"

      - name: Wait for deployment
        run: sleep 60

      - name: Run health checks
        id: health
        continue-on-error: true
        run: |
          # Health check
          curl -f https://example.com/health || exit 1

          # Check error rate
          ERROR_RATE=$(curl -s ${{ secrets.MONITORING_API }}/metrics | jq '.error_rate')
          if (( $(echo "$ERROR_RATE > 0.05" | bc -l) )); then
            echo "Error rate too high: $ERROR_RATE"
            exit 1
          fi

      - name: Rollback on failure
        if: steps.health.outcome == 'failure'
        run: |
          echo "Health checks failed! Rolling back to ${{ steps.previous.outputs.version }}"

          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:${{ steps.previous.outputs.version }} && \
             docker tag myorg/myapp:${{ steps.previous.outputs.version }} myorg/myapp:current && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d"

          # Notify team
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"🚨 Deployment failed and rolled back to ${{ steps.previous.outputs.version }}"}'
```

### **7.7. Docker Compose trong CI/CD**

```yaml
# ===================================================
# 🐙 **DOCKER COMPOSE IN CI/CD**
# ===================================================

name: Test with Docker Compose

on: [push, pull_request]

jobs:
  test-with-compose:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Start services with Docker Compose
        run: |
          docker-compose -f docker-compose.test.yml up -d

      - name: Wait for services
        run: |
          timeout 60 bash -c 'until docker-compose -f docker-compose.test.yml ps | grep -q "Up"; do sleep 2; done'

      - name: Run tests
        run: |
          npm ci
          npm run test:integration
          npm run test:e2e

      - name: View logs
        if: always()
        run: |
          docker-compose -f docker-compose.test.yml logs

      - name: Stop services
        if: always()
        run: |
          docker-compose -f docker-compose.test.yml down -v
```

```yaml
# docker-compose.test.yml
version: '3.8'

services:
  frontend:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - '3000:80'
    environment:
      - NODE_ENV=test
      - VITE_API_URL=http://backend:3000
    depends_on:
      - backend
      - db

  backend:
    image: node:20-alpine
    working_dir: /app
    command: npm start
    ports:
      - '3001:3000'
    environment:
      - NODE_ENV=test
      - DATABASE_URL=postgresql://user:pass@db:5432/testdb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=testdb
    ports:
      - '5432:5432'
```

---

## 8. Kubernetes Basics

### **8.1. Kubernetes Deployment**

```yaml
# ===================================================
# ☸️ **KUBERNETES DEPLOYMENT** - Deployment Kubernetes
# ===================================================

apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: myorg/myapp:latest
          ports:
            - containerPort: 80
          env:
            - name: NODE_ENV
              value: 'production'
            - name: VITE_API_URL
              valueFrom:
                configMapKeyRef:
                  name: app-config
                  key: api-url
          resources:
            requests:
              memory: '256Mi'
              cpu: '250m'
            limits:
              memory: '512Mi'
              cpu: '500m'
          livenessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

### **8.2. Kubernetes vs Docker Compose**

```markdown
# ===================================================

# ⚖️ **KUBERNETES VS DOCKER COMPOSE**

# ===================================================

| Aspect                  | Docker Compose        | Kubernetes              |
| ----------------------- | --------------------- | ----------------------- |
| **Use Case**            | Local dev, small apps | Production, large scale |
| **Orchestration**       | Single host           | Multi-host cluster      |
| **Scaling**             | Manual                | Auto-scaling            |
| **High Availability**   | Limited               | Built-in                |
| **Service Discovery**   | DNS-based             | Built-in                |
| **Rolling Updates**     | Manual                | Automatic               |
| **Resource Management** | Basic                 | Advanced                |
| **Learning Curve**      | Easy                  | Steep                   |
```

---

## **🎯 Best Practices Summary**

### **✅ DO:**

1. **Multi-stage builds**: Separate build and production stages
2. **Layer caching**: Copy package.json before source code
3. **.dockerignore**: Exclude unnecessary files
4. **Non-root user**: Run containers as non-root
5. **Health checks**: Add HEALTHCHECK commands
6. **Minimal base images**: Use Alpine Linux
7. **Security scanning**: Scan images for vulnerabilities
8. **BuildKit**: Enable for better performance

### **❌ DON'T:**

1. **Single-stage builds**: Include dev dependencies in production
2. **Root user**: Don't run as root
3. **Hardcode secrets**: Don't put secrets in Dockerfile
4. **Large images**: Don't include unnecessary files
5. **No health checks**: Always add health checks
6. **Copy everything**: Use .dockerignore
7. **Outdated packages**: Keep base images updated

---

## **💡 Real-World Scenarios**

### **Scenario 1: Monorepo with Multiple Apps**

```dockerfile
# Build specific app in monorepo
FROM node:20-alpine AS builder
WORKDIR /app

# Copy root package files
COPY package.json yarn.lock ./
COPY nx.json tsconfig.base.json ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy app-specific code
COPY apps/my-app ./apps/my-app
COPY libs ./libs

# Build specific app
RUN npx nx build my-app --configuration=production

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist/apps/my-app /usr/share/nginx/html
```

### **Scenario 2: Environment-Specific Builds**

```bash
# Build for different environments
docker build \
  --build-arg NODE_ENV=production \
  --build-arg VITE_API_URL=https://api.prod.com \
  -t myapp:prod .

docker build \
  --build-arg NODE_ENV=staging \
  --build-arg VITE_API_URL=https://api.staging.com \
  -t myapp:staging .
```

---

**🎯 Remember:** "Docker containers should be lightweight, secure, and production-ready. Multi-stage builds + minimal base images + security hardening = best practices!"
