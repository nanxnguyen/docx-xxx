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
# ✅ FROM: Chọn base image (node:20-alpine = Node.js 20 trên Alpine Linux)
# ✅ AS builder: Đặt tên stage là "builder" để dùng ở stage sau
FROM node:20-alpine AS builder

# ✅ Set working directory - Thư mục làm việc trong container
# ✅ Tất cả lệnh sau sẽ chạy trong thư mục /app
WORKDIR /app

# ✅ Copy package files first (layer caching) - Copy package.json trước
# ✅ Tại sao copy package.json trước? → Để tận dụng Docker layer caching
# ✅ package.json ít thay đổi → cache hit → không cần install lại dependencies mỗi lần code thay đổi
COPY package*.json ./  # ✅ Copy package.json và package-lock.json
COPY yarn.lock ./      # ✅ Copy yarn.lock (nếu dùng yarn)

# ✅ Install dependencies - Cài đặt dependencies
# ✅ --frozen-lockfile: Không update lockfile, đảm bảo version chính xác
RUN yarn install --frozen-lockfile

# ✅ Copy source code - Copy mã nguồn
# ✅ Copy sau khi install deps → chỉ chạy lại build khi code thay đổi
COPY . .

# ✅ Build application - Build ứng dụng
# ✅ Tạo production bundle (dist folder)
RUN yarn build

# ✅ Stage 2: Production stage - Stage production
# ✅ FROM: Bắt đầu stage mới với base image nhẹ (nginx:alpine)
# ✅ Chỉ cần nginx để serve static files, không cần Node.js
FROM nginx:1.25-alpine

# ✅ Copy built files from builder - Copy files đã build từ stage builder
# ✅ --from=builder: Copy từ stage "builder" đã định nghĩa ở trên
# ✅ /app/dist: Thư mục build output từ stage builder
# ✅ /usr/share/nginx/html: Thư mục nginx serve static files
COPY --from=builder /app/dist /usr/share/nginx/html

# ✅ Copy nginx configuration - Copy cấu hình nginx
# ✅ nginx.conf: File cấu hình nginx (routing, headers, ...)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ✅ Expose port - Mở port 80 để truy cập từ bên ngoài
EXPOSE 80

# ✅ Health check - Kiểm tra sức khỏe container
# ✅ --interval=30s: Kiểm tra mỗi 30 giây
# ✅ --timeout=3s: Timeout sau 3 giây nếu không response
# ✅ --start-period=5s: Đợi 5 giây sau khi container start trước khi check
# ✅ --retries=3: Retry 3 lần trước khi đánh dấu unhealthy
# ✅ CMD: Lệnh kiểm tra (wget check HTTP response)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

# ✅ Start nginx - Khởi động nginx
# ✅ CMD: Lệnh mặc định khi container start
# ✅ ["nginx", "-g", "daemon off;"]: Chạy nginx ở foreground (không chạy background)
CMD ["nginx", "-g", "daemon off;"]
```

### **2.2. Advanced Multi-Stage Build**

```dockerfile
# ===================================================
# 🚀 **ADVANCED MULTI-STAGE BUILD** - Build nâng cao
# ===================================================

# ✅ Stage 1: Dependencies stage - Stage cài đặt dependencies
# ✅ Tách riêng stage install deps để cache tốt hơn
FROM node:20-alpine AS deps

WORKDIR /app

# ✅ Copy only package files - Chỉ copy package files
# ✅ Chỉ copy package.json, yarn.lock → layer này ít thay đổi → cache tốt
COPY package*.json yarn.lock ./

# ✅ Install dependencies (cached layer) - Cài đặt dependencies (cache layer)
# ✅ --frozen-lockfile: Không update lockfile
# ✅ --production=false: Cài cả dev dependencies (cần cho build)
RUN yarn install --frozen-lockfile --production=false

# ✅ Stage 2: Builder stage - Stage build
# ✅ Stage này chỉ copy node_modules từ stage deps → không cần install lại
FROM node:20-alpine AS builder

WORKDIR /app

# ✅ Copy dependencies from deps stage - Copy dependencies từ stage deps
# ✅ Copy node_modules từ stage deps → tiết kiệm thời gian (không cần install lại)
COPY --from=deps /app/node_modules ./node_modules

# ✅ Copy source code - Copy mã nguồn
# ✅ Copy source code sau khi đã có node_modules → chỉ rebuild khi code thay đổi
COPY . .

# ✅ Build arguments - Build arguments (truyền vào khi build)
# ✅ ARG: Chỉ tồn tại trong quá trình build, không có trong runtime
ARG VITE_API_URL        # ✅ API URL cho Vite build
ARG VITE_SENTRY_DSN     # ✅ Sentry DSN cho error tracking
ARG NODE_ENV=production # ✅ Environment (default: production)

# ✅ Set environment variables - Đặt biến môi trường (tồn tại trong runtime)
# ✅ ENV: Tồn tại trong container khi chạy
# ✅ $NODE_ENV: Lấy giá trị từ ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_SENTRY_DSN=$VITE_SENTRY_DSN

# ✅ Build application - Build ứng dụng
# ✅ Build với environment variables đã set ở trên
RUN yarn build

# ✅ Stage 3: Production stage - Stage production
FROM nginx:1.25-alpine

# ✅ Security: Update packages - Cập nhật packages
# ✅ apk update: Cập nhật danh sách packages
# ✅ apk upgrade: Upgrade packages lên version mới nhất (fix security vulnerabilities)
# ✅ apk add --no-cache curl: Cài curl (cần cho health check) nhưng không cache package index
# ✅ rm -rf /var/cache/apk/*: Xóa cache để giảm image size
RUN apk update && apk upgrade && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# ✅ Security: Create non-root user - Tạo user không phải root
# ✅ addgroup: Tạo group "nginx-group" với GID 1001 (system group -S)
# ✅ adduser: Tạo user "nginx-user" với UID 1001, thuộc group nginx-group
# ✅ Tại sao? → Chạy container với non-root user → giảm security risk
RUN addgroup -g 1001 -S nginx-group && \
    adduser -S nginx-user -u 1001 -G nginx-group

# ✅ Copy built files with proper ownership - Copy files với quyền sở hữu đúng
# ✅ --chown=nginx-user:nginx-group: Set ownership cho files → user nginx-user có quyền đọc
COPY --from=builder --chown=nginx-user:nginx-group /app/dist /usr/share/nginx/html

# ✅ Copy nginx configuration - Copy cấu hình nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ✅ Health check - Kiểm tra sức khỏe container
# ✅ curl -f: Fail nếu HTTP status code >= 400
# ✅ http://localhost/: Check root endpoint
# ✅ || exit 1: Exit với code 1 nếu fail → container đánh dấu unhealthy
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# ✅ Switch to non-root user - Chuyển sang user không phải root
# ✅ USER: Tất cả lệnh sau sẽ chạy với user nginx-user (không phải root)
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
# ✅ ARG: Chỉ tồn tại trong quá trình build, không có trong image layers
# ✅ Có thể truyền từ command line: docker build --build-arg VITE_API_URL=...
ARG NODE_ENV=production      # ✅ Environment (có default value)
ARG VITE_API_URL             # ✅ API URL (không có default, phải truyền)
ARG VITE_SENTRY_DSN          # ✅ Sentry DSN cho error tracking
ARG BUILD_VERSION            # ✅ Version của build (git commit hash, ...)

# ✅ Environment variables (runtime) - Biến môi trường (runtime)
# ✅ ENV: Tồn tại trong container khi chạy, có thể override khi docker run
# ✅ $NODE_ENV: Lấy giá trị từ ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_SENTRY_DSN=$VITE_SENTRY_DSN
ENV BUILD_VERSION=$BUILD_VERSION

COPY package*.json ./
RUN yarn install --frozen-lockfile

COPY . .
RUN yarn build

# ✅ Build with arguments - Build với arguments
# ✅ --build-arg: Truyền giá trị cho ARG trong Dockerfile
# ✅ Ví dụ: docker build --build-arg VITE_API_URL=https://api.example.com -t myapp:latest .
```

```bash
# ===================================================
# 🚀 **BUILD COMMANDS** - Lệnh build
# ===================================================

# ✅ Basic build - Build cơ bản
# ✅ -t myapp:latest: Tag image với tên "myapp" và tag "latest"
# ✅ . : Context (thư mục hiện tại) - Docker sẽ tìm Dockerfile trong thư mục này
docker build -t myapp:latest .

# ✅ Build with arguments - Build với arguments
# ✅ --build-arg: Truyền giá trị cho ARG trong Dockerfile
# ✅ NODE_ENV=production: Set ARG NODE_ENV = production
# ✅ VITE_API_URL=...: Set ARG VITE_API_URL
# ✅ BUILD_VERSION=1.0.0: Set ARG BUILD_VERSION
docker build \
  --build-arg NODE_ENV=production \
  --build-arg VITE_API_URL=https://api.example.com \
  --build-arg BUILD_VERSION=1.0.0 \
  -t myapp:latest .

# ✅ Build specific stage - Build stage cụ thể (multi-stage build)
# ✅ --target builder: Chỉ build đến stage "builder", không build stage production
# ✅ Dùng khi chỉ cần build stage để test hoặc debug
docker build --target builder -t myapp:builder .

# ✅ Build with cache - Build với cache từ image khác
# ✅ --cache-from: Sử dụng layers từ image myapp:latest làm cache
# ✅ Giúp build nhanh hơn nếu có layers giống nhau
docker build --cache-from myapp:latest -t myapp:new .

# ✅ Multi-platform build - Build cho nhiều platform (ARM64 + AMD64)
# ✅ docker buildx: Build cho nhiều architectures cùng lúc
# ✅ --platform linux/amd64,linux/arm64: Build cho cả x86_64 và ARM64
# ✅ --push: Push image lên registry sau khi build xong
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
      context: . # ✅ Context: Thư mục chứa Dockerfile
      dockerfile: Dockerfile # ✅ Dockerfile: Tên file Dockerfile (mặc định là Dockerfile)
      args: # ✅ Build arguments: Truyền vào Dockerfile khi build
        NODE_ENV: development # ✅ ARG NODE_ENV = development
        VITE_API_URL: http://backend:3000 # ✅ ARG VITE_API_URL
    ports:
      # ✅ Port mapping: host:container
      # ✅ 3000:80 = Expose port 80 của container ra port 3000 của host
      # ✅ Truy cập: http://localhost:3000 → container port 80
      - '3000:80'
    volumes:
      # ✅ Volume mapping: host:container
      # ✅ ./src:/app/src = Mount thư mục ./src (local) vào /app/src (container)
      # ✅ Hot reload: Code thay đổi trong ./src → tự động reload trong container
      - ./src:/app/src
      # ✅ Anonymous volume: Tạo volume ẩn danh cho /app/node_modules
      # ✅ Override mount ./src:/app/src → node_modules không bị ghi đè bởi local
      - /app/node_modules
    environment:
      # ✅ Environment variables: Biến môi trường trong container
      - NODE_ENV=development
      - VITE_API_URL=http://backend:3000 # ✅ backend = service name (Docker Compose DNS)
    depends_on:
      # ✅ depends_on: Đợi service "backend" start trước khi start frontend
      - backend
    networks:
      # ✅ networks: Kết nối vào network "app-network"
      # ✅ Các services trong cùng network có thể giao tiếp qua service name
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
    restart: unless-stopped # ✅ Restart policy: Tự động restart nếu container stop (trừ khi manually stop)
    healthcheck:
      # ✅ Health check: Kiểm tra container có healthy không
      test: ['CMD', 'curl', '-f', 'http://localhost/'] # ✅ Lệnh kiểm tra: curl check HTTP
      interval: 30s # ✅ Kiểm tra mỗi 30 giây
      timeout: 3s # ✅ Timeout sau 3 giây
      retries: 3 # ✅ Retry 3 lần trước khi đánh dấu unhealthy
      start_period: 10s # ✅ Đợi 10 giây sau khi start trước khi check
    networks:
      - app-network
    deploy:
      # ✅ Deploy configuration (Docker Swarm mode)
      replicas: 3 # ✅ Chạy 3 instances của service
      resources:
        limits: # ✅ Giới hạn tài nguyên tối đa
          cpus: '0.5' # ✅ Tối đa 0.5 CPU cores
          memory: 512M # ✅ Tối đa 512MB RAM
        reservations: # ✅ Tài nguyên đảm bảo (reserved)
          cpus: '0.25' # ✅ Đảm bảo 0.25 CPU cores
          memory: 256M # ✅ Đảm bảo 256MB RAM

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

# ✅ Build image - Build image từ Dockerfile
# ✅ -t myapp:latest: Tag image với tên "myapp" và tag "latest"
# ✅ . : Context (thư mục hiện tại)
docker build -t myapp:latest .
# ✅ -f Dockerfile.prod: Dùng Dockerfile.prod thay vì Dockerfile mặc định
docker build -t myapp:v1.0.0 -f Dockerfile.prod .

# ✅ List images - Liệt kê tất cả images trên máy
docker images        # ✅ Hiển thị: REPOSITORY, TAG, IMAGE ID, SIZE, CREATED
docker image ls      # ✅ Tương tự docker images

# ✅ Remove image - Xóa image
docker rmi myapp:latest           # ✅ rmi = remove image
docker image rm myapp:latest      # ✅ Tương tự docker rmi

# ✅ Remove all unused images - Xóa tất cả images không dùng
# ✅ -a: Xóa cả images không có tag (dangling images)
docker image prune -a

# ✅ Inspect image - Xem chi tiết image (metadata, config, layers, ...)
docker inspect myapp:latest

# ✅ Tag image - Gắn tag mới cho image
# ✅ Tạo tag "v1.0.0" cho image myapp:latest (không tạo image mới)
docker tag myapp:latest myapp:v1.0.0

# ✅ Push image to registry - Đẩy image lên registry (Docker Hub, ECR, ...)
# ✅ myorg/myapp:latest: Format: registry/username/image:tag
docker push myorg/myapp:latest

# ✅ Pull image from registry - Kéo image từ registry về máy
docker pull myorg/myapp:latest

# ┌─────────────────────────────────────────────────┐
# │ 🚀 CONTAINER COMMANDS - Lệnh Quản Lý Container │
# └─────────────────────────────────────────────────┘

# ✅ Run container - Chạy container từ image
docker run myapp:latest  # ✅ Chạy container ở foreground
# ✅ -d: Detached mode (chạy ở background)
# ✅ -p 3000:80: Port mapping (host:container)
# ✅ --name myapp: Đặt tên container là "myapp"
docker run -d -p 3000:80 --name myapp myapp:latest
# ✅ -it: Interactive + TTY (cho phép tương tác)
# ✅ --rm: Tự động xóa container khi exit
# ✅ sh: Chạy shell trong container
docker run -it --rm node:20-alpine sh

# ✅ List containers - Liệt kê containers
docker ps              # ✅ Chỉ hiển thị containers đang chạy
docker ps -a           # ✅ Hiển thị tất cả containers (bao gồm đã stop)
docker container ls    # ✅ Tương tự docker ps

# ✅ Start/Stop container - Khởi động/Dừng container
docker start myapp     # ✅ Start container đã tồn tại
docker stop myapp      # ✅ Stop container (graceful shutdown)
docker restart myapp   # ✅ Restart container (stop + start)

# ✅ Remove container - Xóa container
docker rm myapp        # ✅ Xóa container (phải stop trước)
docker container rm myapp  # ✅ Tương tự docker rm

# ✅ Remove all stopped containers - Xóa tất cả containers đã dừng
docker container prune

# ✅ Execute command in container - Chạy lệnh trong container đang chạy
# ✅ -it: Interactive + TTY
# ✅ sh: Chạy shell
docker exec -it myapp sh
# ✅ Chạy lệnh ls /app trong container
docker exec myapp ls /app

# ✅ View logs - Xem logs của container
docker logs myapp              # ✅ Xem tất cả logs
docker logs -f myapp            # ✅ -f: Follow logs (real-time, như tail -f)
docker logs --tail 100 myapp   # ✅ --tail 100: Chỉ hiển thị 100 dòng cuối

# ✅ Inspect container - Xem chi tiết container
docker inspect myapp

# ✅ Copy files - Copy files giữa container và host
# ✅ Container → Local: Copy từ container ra máy local
docker cp myapp:/app/dist ./local-dist
# ✅ Local → Container: Copy từ máy local vào container
docker cp ./local-file myapp:/app/

# ✅ Container stats - Thống kê tài nguyên container (CPU, Memory, Network, I/O)
docker stats myapp       # ✅ Stats của container "myapp"
docker stats             # ✅ Stats của tất cả containers đang chạy

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
docker-compose up                    # ✅ Foreground: Hiển thị logs, Ctrl+C để stop
docker-compose up -d                 # ✅ Background (detached): Chạy ở background
docker-compose up --build            # ✅ Build images trước khi start
docker-compose up --build --force-recreate  # ✅ Force recreate: Tạo containers mới (không dùng cũ)

# ✅ Stop services - Dừng services
docker-compose stop                  # ✅ Stop containers nhưng không xóa (có thể start lại)
docker-compose down                  # ✅ Stop và remove containers (không xóa volumes)
docker-compose down -v               # ✅ Stop, remove containers + volumes (xóa cả data)

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

# ✅ Execute command - Chạy lệnh trong service đang chạy
docker-compose exec frontend sh      # ✅ Chạy shell trong container "frontend"
docker-compose exec frontend ls /app # ✅ Chạy lệnh ls /app trong container

# ✅ Run one-off command - Chạy lệnh một lần (tạo container mới, chạy lệnh, xóa)
docker-compose run frontend npm test # ✅ Tạo container mới, chạy npm test, xóa container
docker-compose run --rm frontend sh  # ✅ --rm: Tự động xóa container sau khi exit

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

# ✅ Scale services - Scale services (chạy nhiều instances)
# ✅ --scale frontend=3: Chạy 3 containers của service "frontend"
docker-compose up --scale frontend=3

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
# - docker build: Lệnh build image từ Dockerfile
# - -t myapp:latest: Tag image với tên "myapp" và tag "latest" (tên:phiên bản)
# - . : Context (thư mục hiện tại) - Docker sẽ tìm Dockerfile trong thư mục này

# ┌─────────────────────────────────────────────────┐
# │ 🎯 CÔNG THỨC ĐẦY ĐỦ - Full Formula             │
# └─────────────────────────────────────────────────┘

# 💡 Công thức đầy đủ với các options phổ biến:
docker build \
  --file Dockerfile.prod \           # ✅ -f: Dùng Dockerfile.prod thay vì Dockerfile mặc định
  --tag myapp:v1.0.0 \               # ✅ -t: Tag image với tên và version
  --build-arg NODE_ENV=production \  # ✅ --build-arg: Truyền giá trị cho ARG trong Dockerfile
  --build-arg VITE_API_URL=https://api.example.com \
  --target builder \                 # ✅ --target: Chỉ build đến stage "builder" (multi-stage)
  --cache-from myapp:latest \        # ✅ --cache-from: Dùng layers từ image này làm cache
  --progress=plain \                  # ✅ --progress: Hiển thị progress chi tiết (dễ debug)
  --no-cache \                       # ✅ --no-cache: Không dùng cache (build từ đầu)
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

# ✅ Docker Scout (built-in) - Docker Scout (tích hợp trong Docker Desktop)
# ✅ Quét vulnerabilities trong image
docker scout cves myapp:latest  # ✅ cves = Common Vulnerabilities and Exposures

# ✅ Trivy scanner - Trivy scanner (open-source, phổ biến)
# ✅ Quét vulnerabilities, misconfigurations, secrets
trivy image myapp:latest

# ✅ Snyk scanner - Snyk scanner (commercial, có free tier)
# ✅ Quét vulnerabilities và suggest fixes
snyk test --docker myapp:latest

# ✅ Scan in CI/CD - Quét trong CI/CD pipeline
# ✅ Tự động quét image sau khi build → fail build nếu có HIGH/CRITICAL vulnerabilities
# .github/workflows/security.yml
- name: Scan image
  run: |
    docker build -t myapp:latest .
    # ✅ --exit-code 1: Exit với code 1 nếu có vulnerabilities
    # ✅ --severity HIGH,CRITICAL: Chỉ fail nếu có HIGH hoặc CRITICAL vulnerabilities
    trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest
```

### **5.4. Secrets Management**

```yaml
# ===================================================
# 🔐 **SECRETS MANAGEMENT** - Quản lý secrets
# ===================================================

# ✅ Docker Secrets (Docker Swarm) - Docker Secrets
# ✅ Quản lý secrets an toàn trong Docker Swarm
version: '3.8'
services:
  frontend:
    secrets:
      - api_key # ✅ Mount secret "api_key" vào container
    environment:
      - API_KEY_FILE=/run/secrets/api_key # ✅ Secret được mount tại /run/secrets/api_key

secrets:
  api_key:
    external: true # ✅ Secret được tạo bên ngoài (docker secret create)

# ✅ Environment variables (not in Dockerfile) - Biến môi trường (không trong Dockerfile)
# ❌ BAD: ARG API_KEY=secret123
# ❌ Vấn đề: ARG được lưu trong image layers → có thể xem bằng docker history
# ❌ → Security risk: Secrets bị expose trong image

# ✅ GOOD: docker run -e API_KEY=secret123 myapp
# ✅ Environment variables được truyền khi chạy container → không lưu trong image
# ✅ → An toàn hơn: Secrets không có trong image layers
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
# ✅ Tại sao copy package.json trước?
# ✅ → package.json ít thay đổi → Docker cache layer này → không cần install lại deps mỗi lần code thay đổi
COPY package*.json yarn.lock ./

# ✅ Step 2: Install dependencies (cached if package.json unchanged) - Cài đặt dependencies
# ✅ Nếu package.json không đổi → Docker dùng cache layer này → không chạy lại yarn install
# ✅ → Tiết kiệm thời gian build (install deps mất 2-5 phút)
RUN yarn install --frozen-lockfile

# ✅ Step 3: Copy source code (changes frequently) - Copy mã nguồn (thay đổi thường xuyên)
# ✅ Copy source code sau khi install deps → chỉ rebuild khi code thay đổi
COPY . .

# ✅ Step 4: Build (only runs if source changed) - Build (chỉ chạy nếu source thay đổi)
# ✅ Nếu source code không đổi → Docker dùng cache → không chạy lại yarn build
RUN yarn build

# ❌ BAD ORDER - Thứ tự sai
# COPY . .  # ❌ Copy toàn bộ code trước → mỗi lần code thay đổi → cache miss
# RUN yarn install  # ❌ Phải chạy lại yarn install mỗi lần → chậm
```

### **6.2. BuildKit Optimization**

```bash
# ===================================================
# 🚀 **BUILDKIT** - Build engine mới
# ===================================================

# ✅ Enable BuildKit - Bật BuildKit
# ✅ DOCKER_BUILDKIT=1: Bật BuildKit (build engine mới, nhanh hơn)
export DOCKER_BUILDKIT=1
docker build -t myapp:latest .

# ✅ Or in docker-compose - Hoặc trong docker-compose
# ✅ COMPOSE_DOCKER_CLI_BUILD=1: Dùng Docker CLI build thay vì docker-compose build
# ✅ DOCKER_BUILDKIT=1: Bật BuildKit
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

# ✅ Benefits (Lợi ích của BuildKit):
# - Parallel builds: Build các stages song song (nhanh hơn)
# - Better caching: Cache hiệu quả hơn (cache mount, inline cache, ...)
# - Mount cache: Share cache giữa các builds (cache mount)
# - Secrets: Xử lý secrets an toàn hơn (không lưu trong image layers)
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
        # ✅ Setup Docker Buildx: Build engine mới với nhiều tính năng hơn
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        # ✅ Build và push Docker image
        uses: docker/build-push-action@v5
        with:
          context: . # ✅ Context: Thư mục chứa Dockerfile
          push: false # ✅ Không push lên registry (chỉ build)
          tags: myapp:${{ github.sha }} # ✅ Tag image với git commit SHA
          cache-from: type=gha # ✅ Cache từ GitHub Actions cache
          cache-to: type=gha,mode=max # ✅ Lưu cache vào GitHub Actions (mode=max = lưu tất cả layers)
          build-args: | # ✅ Build arguments: Truyền vào Dockerfile
            NODE_ENV=production
            VITE_API_URL=${{ secrets.VITE_API_URL }}  # ✅ Lấy từ GitHub Secrets

      - name: Save Docker image
        # ✅ Save image thành file tar.gz để lưu làm artifact
        # ✅ docker save: Export image thành tar file
        # ✅ gzip: Nén file để giảm kích thước
        run: |
          docker save myapp:${{ github.sha }} | gzip > myapp-image.tar.gz

      - name: Upload Docker image artifact
        # ✅ Upload image file lên GitHub Actions artifacts
        # ✅ Artifacts có thể download và sử dụng ở jobs khác
        uses: actions/upload-artifact@v3
        with:
          name: docker-image # ✅ Tên artifact
          path: myapp-image.tar.gz # ✅ File cần upload
          retention-days: 7 # ✅ Giữ artifact trong 7 ngày

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
        # ✅ Load image từ file tar.gz đã download
        # ✅ gunzip: Giải nén file
        # ✅ docker load: Import image từ tar file
        run: |
          gunzip -c myapp-image.tar.gz | docker load

      - name: Run container
        # ✅ Chạy container từ image đã load
        # ✅ -d: Detached mode (background)
        # ✅ -p 3000:80: Port mapping (host:container)
        # ✅ --name myapp-test: Đặt tên container
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
        # ✅ Tag image với registry URL và push lên registry
        # ✅ docker tag: Tạo tag mới cho image (không tạo image mới)
        # ✅ docker push: Đẩy image lên registry (Docker Hub, ECR, GCR, ...)
        run: |
          docker tag myapp:${{ github.sha }} ${{ secrets.REGISTRY_URL }}/myapp:staging
          docker push ${{ secrets.REGISTRY_URL }}/myapp:staging

      - name: Deploy to staging server
        # ✅ Deploy lên staging server qua SSH
        # ✅ docker pull: Kéo image mới nhất từ registry
        # ✅ docker-compose up -d: Start services với docker-compose
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

```yaml
# ===================================================
# 🚀 **GITHUB ACTIONS DOCKER BUILD & PUSH**
# ===================================================

name: Docker Build and Push

on:
  push:
    branches: [main] # ✅ Trigger khi push vào branch main
    tags: # ✅ Trigger khi push tag
      - 'v*' # ✅ Tag bắt đầu bằng "v" (v1.0.0, v2.1.3, ...)

jobs:
  build-and-push:
    runs-on: ubuntu-latest # ✅ Chạy trên Ubuntu runner
    steps:
      - uses: actions/checkout@v4 # ✅ Checkout code từ repository

      - name: Set up Docker Buildx
        # ✅ Setup Docker Buildx: Build engine mới với nhiều tính năng
        uses: docker/setup-buildx-action@v3

      - name: Login to Docker Hub
        # ✅ Login vào Docker Hub để push image
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }} # ✅ Username từ GitHub Secrets
          password: ${{ secrets.DOCKER_PASSWORD }} # ✅ Password từ GitHub Secrets

      - name: Extract metadata
        # ✅ Extract metadata từ git (tags, labels, ...)
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: myorg/myapp # ✅ Image name
          tags: |
            type=semver,pattern={{version}}        # ✅ Tag: v1.0.0 → myorg/myapp:v1.0.0
            type=semver,pattern={{major}}.{{minor}} # ✅ Tag: v1.0.0 → myorg/myapp:v1.0
            type=sha                                # ✅ Tag: myorg/myapp:abc1234 (git commit SHA)

      - name: Build and push
        # ✅ Build và push image lên registry
        uses: docker/build-push-action@v5
        with:
          context: . # ✅ Context: Thư mục chứa Dockerfile
          push: true # ✅ Push image lên registry sau khi build
          tags: ${{ steps.meta.outputs.tags }} # ✅ Tags từ metadata action
          labels: ${{ steps.meta.outputs.labels }} # ✅ Labels từ metadata action
          cache-from: type=registry,ref=myorg/myapp:buildcache # ✅ Cache từ registry
          cache-to: type=registry,ref=myorg/myapp:buildcache,mode=max # ✅ Lưu cache vào registry
          build-args: | # ✅ Build arguments
            NODE_ENV=production
            VITE_API_URL=${{ secrets.VITE_API_URL }}  # ✅ Lấy từ GitHub Secrets
```

### **7.3. Docker Layer Caching in CI**

```yaml
# ===================================================
# 💾 **DOCKER LAYER CACHING** - Cache layers trong CI
# ===================================================

- name: Build with cache
  # ✅ Build với cache để tăng tốc độ build
  uses: docker/build-push-action@v5
  with:
    context: .
    push: false # ✅ Không push image (chỉ build)
    tags: myapp:latest
    cache-from: |
      # ✅ Cache từ 2 nguồn:
      type=registry,ref=myorg/myapp:buildcache  # ✅ Cache từ registry (image buildcache)
      type=gha                                   # ✅ Cache từ GitHub Actions cache
    cache-to: |
      # ✅ Lưu cache vào 2 nơi:
      type=registry,ref=myorg/myapp:buildcache,mode=max  # ✅ Lưu vào registry
      type=gha,mode=max                                    # ✅ Lưu vào GitHub Actions cache
      # ✅ mode=max: Lưu tất cả layers (kể cả intermediate layers)
```

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
        # ✅ Deploy lên blue hoặc green environment
        # ✅ inputs.target: "blue" hoặc "green" (từ workflow_dispatch)
        run: |
          # ✅ SSH vào server và deploy
          # ✅ docker pull: Kéo image mới từ registry
          # ✅ docker-compose up -d: Start services với docker-compose
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:${{ inputs.target }} && \
             docker-compose -f /opt/app/docker-compose.${{ inputs.target }}.yml up -d"

      - name: Run smoke tests
        # ✅ Chạy smoke tests để đảm bảo deployment thành công
        # ✅ curl -f: Fail nếu HTTP status >= 400
        run: |
          TARGET_URL="https://${{ inputs.target }}.example.com"
          curl -f $TARGET_URL/health || exit 1  # ✅ Check health endpoint

      - name: Switch traffic to ${{ inputs.target }}
        # ✅ Switch traffic từ environment cũ sang environment mới
        # ✅ Update load balancer config để route traffic đến environment mới
        run: |
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
        # ✅ Update traffic split: Chia traffic giữa canary và production
        # ✅ Ví dụ: canary-percentage = 10 → 10% traffic đến canary, 90% đến production
        run: |
          curl -X POST ${{ secrets.LB_API }}/traffic-split \
            -H "Authorization: Bearer ${{ secrets.LB_TOKEN }}" \
            -d '{"canary": ${{ inputs.canary-percentage }}, "production": ${{ 100 - inputs.canary-percentage }}}'
            # ✅ Gửi request đến Load Balancer API để update traffic split

      - name: Monitor canary for 10 minutes
        # ✅ Monitor canary deployment trong 10 phút
        # ✅ Kiểm tra error rate → nếu quá cao thì rollback
        run: |
          sleep 600  # ✅ Đợi 10 phút (600 giây)
          # ✅ Lấy error rate từ monitoring API
          ERROR_RATE=$(curl -s ${{ secrets.MONITORING_API }}/metrics | jq '.error_rate')
          if [ "$ERROR_RATE" -gt "1" ]; then  # ✅ Nếu error rate > 1%
            echo "Canary failed! Rolling back..."
            exit 1  # ✅ Exit với code 1 → workflow fail → trigger rollback
          fi

      - name: Promote canary to production
        # ✅ Promote canary lên production khi canary-percentage = 100%
        # ✅ Chỉ chạy khi đã chuyển 100% traffic sang canary
        if: inputs.canary-percentage == '100'
        run: |
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker tag myorg/myapp:canary myorg/myapp:latest && \
             docker push myorg/myapp:latest && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d"
          # ✅ docker tag: Tag canary image thành latest
          # ✅ docker push: Push latest image lên registry
          # ✅ docker-compose up -d: Deploy production với image mới
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
        # ✅ Set environment variables dựa trên matrix.environment
        # ✅ $GITHUB_ENV: File để set environment variables cho các steps sau
        run: |
          if [ "${{ matrix.environment }}" == "production" ]; then
            # ✅ Production environment
            echo "VITE_API_URL=https://api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_PROD }}" >> $GITHUB_ENV
            echo "IMAGE_TAG=prod" >> $GITHUB_ENV
          elif [ "${{ matrix.environment }}" == "staging" ]; then
            # ✅ Staging environment
            echo "VITE_API_URL=https://staging-api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_STAGING }}" >> $GITHUB_ENV
            echo "IMAGE_TAG=staging" >> $GITHUB_ENV
          else
            # ✅ Development environment
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
        # ✅ Lấy version của deployment trước đó để rollback nếu cần
        id: previous
        run: |
          # ✅ SSH vào server và lấy tag của image (trừ "latest")
          # ✅ docker images: Liệt kê images
          # ✅ --format '{{.Tag}}': Chỉ hiển thị tag
          # ✅ grep -v latest: Loại bỏ tag "latest"
          # ✅ head -1: Lấy tag đầu tiên (version mới nhất)
          PREV_VERSION=$(ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker images myorg/myapp --format '{{.Tag}}' | grep -v latest | head -1")
          echo "version=$PREV_VERSION" >> $GITHUB_OUTPUT  # ✅ Lưu vào output để dùng ở step sau
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
        # ✅ Chạy health checks sau khi deploy
        id: health
        continue-on-error: true # ✅ Tiếp tục workflow ngay cả khi step này fail
        run: |
          # ✅ Health check: Kiểm tra endpoint /health
          curl -f https://example.com/health || exit 1  # ✅ -f: Fail nếu HTTP status >= 400

          # ✅ Check error rate: Kiểm tra error rate từ monitoring API
          ERROR_RATE=$(curl -s ${{ secrets.MONITORING_API }}/metrics | jq '.error_rate')
          if (( $(echo "$ERROR_RATE > 0.05" | bc -l) )); then  # ✅ Nếu error rate > 5%
            echo "Error rate too high: $ERROR_RATE"
            exit 1  # ✅ Exit với code 1 → step fail
          fi

      - name: Rollback on failure
        # ✅ Rollback nếu health checks fail
        # ✅ Chỉ chạy khi step "health" có outcome = 'failure'
        if: steps.health.outcome == 'failure'
        run: |
          echo "Health checks failed! Rolling back to ${{ steps.previous.outputs.version }}"

          # ✅ Rollback: Deploy lại version trước đó
          ssh ${{ secrets.SSH_USER }}@${{ secrets.HOST }} \
            "docker pull myorg/myapp:${{ steps.previous.outputs.version }} && \
             docker tag myorg/myapp:${{ steps.previous.outputs.version }} myorg/myapp:current && \
             docker-compose -f /opt/app/docker-compose.prod.yml up -d"
          # ✅ docker pull: Kéo image version cũ từ registry
          # ✅ docker tag: Tag thành "current"
          # ✅ docker-compose up -d: Deploy lại với image cũ

          # ✅ Notify team: Gửi thông báo đến Slack
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
        # ✅ Start services với docker-compose.test.yml
        # ✅ -f: Dùng file docker-compose.test.yml (thay vì docker-compose.yml mặc định)
        # ✅ up -d: Start ở background (detached)
        run: |
          docker-compose -f docker-compose.test.yml up -d

      - name: Wait for services
        # ✅ Đợi services start xong trước khi chạy tests
        # ✅ timeout 60: Timeout sau 60 giây
        # ✅ until ... grep -q "Up": Đợi đến khi có service status "Up"
        # ✅ sleep 2: Đợi 2 giây giữa mỗi lần check
        run: |
          timeout 60 bash -c 'until docker-compose -f docker-compose.test.yml ps | grep -q "Up"; do sleep 2; done'

      - name: Run tests
        # ✅ Chạy integration tests và E2E tests
        run: |
          npm ci                    # ✅ Install dependencies
          npm run test:integration  # ✅ Chạy integration tests
          npm run test:e2e          # ✅ Chạy E2E tests

      - name: View logs
        # ✅ Xem logs của services (dùng để debug nếu tests fail)
        # ✅ if: always(): Chạy ngay cả khi tests fail
        if: always()
        run: |
          docker-compose -f docker-compose.test.yml logs

      - name: Stop services
        # ✅ Stop và xóa services sau khi tests xong
        # ✅ down -v: Stop containers và xóa volumes
        # ✅ if: always(): Chạy ngay cả khi tests fail (cleanup)
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

apiVersion: apps/v1 # ✅ API version của Kubernetes
kind: Deployment # ✅ Loại resource: Deployment (quản lý pods)
metadata:
  name: frontend # ✅ Tên deployment
  labels:
    app: frontend # ✅ Label để selector pods
spec:
  replicas: 3 # ✅ Số lượng pods cần chạy (3 instances)
  selector:
    matchLabels:
      app: frontend # ✅ Select pods có label app=frontend
  template:
    metadata:
      labels:
        app: frontend # ✅ Label cho pods được tạo
    spec:
      containers:
        - name: frontend
          image: myorg/myapp:latest # ✅ Docker image để chạy
          ports:
            - containerPort: 80 # ✅ Port container expose (80)
          env:
            # ✅ Environment variables
            - name: NODE_ENV
              value: 'production' # ✅ Giá trị trực tiếp
            - name: VITE_API_URL
              valueFrom:
                configMapKeyRef: # ✅ Lấy từ ConfigMap
                  name: app-config # ✅ Tên ConfigMap
                  key: api-url # ✅ Key trong ConfigMap
          resources:
            requests: # ✅ Tài nguyên đảm bảo (reserved)
              memory: '256Mi' # ✅ Đảm bảo 256MB RAM
              cpu: '250m' # ✅ Đảm bảo 0.25 CPU cores (250 millicores)
            limits: # ✅ Giới hạn tài nguyên tối đa
              memory: '512Mi' # ✅ Tối đa 512MB RAM
              cpu: '500m' # ✅ Tối đa 0.5 CPU cores
          livenessProbe:
            # ✅ Liveness probe: Kiểm tra container có còn sống không
            # ✅ Nếu fail → Kubernetes kill và restart container
            httpGet:
              path: / # ✅ Check endpoint /
              port: 80
            initialDelaySeconds: 30 # ✅ Đợi 30 giây sau khi start trước khi check
            periodSeconds: 10 # ✅ Check mỗi 10 giây
          readinessProbe:
            # ✅ Readiness probe: Kiểm tra container đã sẵn sàng nhận traffic chưa
            # ✅ Nếu fail → Kubernetes không route traffic đến pod này
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5 # ✅ Đợi 5 giây sau khi start
            periodSeconds: 5 # ✅ Check mỗi 5 giây
---
apiVersion: v1
kind: Service # ✅ Loại resource: Service (expose pods ra ngoài)
metadata:
  name: frontend-service # ✅ Tên service
spec:
  selector:
    app: frontend # ✅ Select pods có label app=frontend
  ports:
    - protocol: TCP
      port: 80 # ✅ Port của service (port bên ngoài)
      targetPort: 80 # ✅ Port của container (port bên trong)
  type:
    LoadBalancer # ✅ LoadBalancer: Expose service ra ngoài cluster (có external IP)
    # ✅ Các loại khác: ClusterIP (internal), NodePort (expose qua node port)
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
