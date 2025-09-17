# 🐳 Docker & Docker Compose Best Practices

## 📋 Mục Lục
1. [Docker Cơ Bản](#docker-cơ-bản)
2. [Dockerfile Best Practices](#dockerfile-best-practices)
3. [Docker Compose Best Practices](#docker-compose-best-practices)
4. [Bảo Mật Docker](#bảo-mật-docker)
5. [Performance Optimization](#performance-optimization)
6. [Production Deployment](#production-deployment)
7. [Monitoring & Logging](#monitoring--logging)
8. [Troubleshooting](#troubleshooting)

---

## 🐳 Docker Cơ Bản

### Docker Là Gì?
Docker là platform containerization cho phép đóng gói ứng dụng và dependencies vào container lightweight, portable.

### Khái Niệm Cốt Lõi
```typescript
interface DockerConcepts {
  image: {
    definition: "Template để tạo containers";
    analogy: "Như blueprint/khuôn mẫu";
    example: "node:18, nginx:alpine";
  };

  container: {
    definition: "Running instance của image";
    analogy: "Như virtual machine nhẹ";
    example: "Web server đang chạy từ nginx image";
  };

  dockerfile: {
    definition: "Script để build image";
    analogy: "Như recipe/công thức nấu ăn";
    example: "FROM node:18 + COPY + RUN commands";
  };

  volume: {
    definition: "Persistent storage cho containers";
    analogy: "Như external hard drive";
    example: "Database data, log files";
  };
}
```

### Lợi Ích Chính
- **Portability**: Chạy được ở đâu cũng giống nhau
- **Consistency**: Môi trường nhất quán từ dev đến production
- **Efficiency**: Nhẹ hơn Virtual Machine
- **Scalability**: Dễ dàng scale horizontal
- **Isolation**: Cô lập process và resource

---

## 📝 Dockerfile Best Practices

### 1. Multi-Stage Builds

```dockerfile
# ✅ GOOD: Multi-stage build cho Node.js app
FROM node:18-alpine AS builder
WORKDIR /app

# Copy package files first (better caching)
COPY package*.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy source code
COPY . .
RUN yarn build

# Production stage
FROM nginx:1.25-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

```dockerfile
# ❌ BAD: Single stage với dev dependencies
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install  # Includes dev dependencies
RUN yarn build
EXPOSE 3000
CMD ["yarn", "start"]
```

### 2. Security Best Practices

```dockerfile
# ✅ SECURE Dockerfile
FROM node:18.10.0-alpine AS builder

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001 -G nodejs

WORKDIR /app

# Copy package files with proper ownership
COPY --chown=nextjs:nodejs package*.json ./
RUN yarn install --frozen-lockfile --production=false

# Copy source with proper ownership
COPY --chown=nextjs:nodejs . .
RUN yarn build

# Production stage
FROM nginx:1.25-alpine

# Update packages and install security updates
RUN apk update && apk upgrade && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# Create non-root user for nginx
RUN addgroup -g 1001 -S nginx-group && \
    adduser -S nginx-user -u 1001 -G nginx-group

# Copy built app with proper ownership
COPY --from=builder --chown=nginx-user:nginx-group /app/dist /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

USER nginx-user
EXPOSE 80
```

### 3. Layer Optimization

```dockerfile
# ✅ OPTIMIZED: Minimize layers and improve caching
FROM node:18-alpine

# Combine RUN commands to reduce layers
RUN apk update && apk upgrade && \
    apk add --no-cache \
    curl \
    dumb-init && \
    rm -rf /var/cache/apk/*

# Copy dependency files first (changes less frequently)
COPY package*.json yarn.lock ./
RUN yarn install --frozen-lockfile --production && \
    yarn cache clean

# Copy source code last (changes frequently)
COPY . .

# Use .dockerignore to exclude unnecessary files
```

### 4. .dockerignore File

```dockerignore
# .dockerignore
node_modules
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.git
.gitignore
README.md
.env
.nyc_output
coverage
.DS_Store
.vscode
dist
build
*.md
```

### 5. Image Tagging Strategy

```bash
# ✅ GOOD: Specific version tags
docker build -t myapp:1.2.3 .
docker build -t myapp:latest .
docker build -t myapp:stable .

# ❌ BAD: Only using latest
docker build -t myapp .
```

---

## 🐙 Docker Compose Best Practices

### 1. Service Organization

```yaml
# ✅ GOOD: Well-structured docker-compose.yml
version: '3.8'

services:
  # Frontend service
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      args:
        - NODE_ENV=production
    ports:
      - "3000:80"
    environment:
      - API_URL=http://backend:8080
    depends_on:
      - backend
    networks:
      - frontend
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:80/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Backend service
  backend:
    build: ./backend
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://user:password@database:5432/myapp
      - REDIS_URL=redis://redis:6379
    depends_on:
      database:
        condition: service_healthy
      redis:
        condition: service_started
    networks:
      - frontend
      - backend
    volumes:
      - ./backend/uploads:/app/uploads
    restart: unless-stopped

  # Database service
  database:
    image: postgres:14-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d myapp"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - backend
    restart: unless-stopped

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
```

### 2. Environment-Specific Configurations

```yaml
# docker-compose.yml (base)
version: '3.8'
services:
  app:
    build: .
    environment:
      - NODE_ENV=production

# docker-compose.override.yml (development - automatically loaded)
version: '3.8'
services:
  app:
    volumes:
      - ./src:/app/src
    environment:
      - NODE_ENV=development
    ports:
      - "3000:3000"

# docker-compose.prod.yml (production)
version: '3.8'
services:
  app:
    image: myapp:latest
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
```

### 3. Secrets Management

```yaml
# ✅ GOOD: Using Docker secrets
version: '3.8'

services:
  app:
    image: myapp
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password
      - API_KEY_FILE=/run/secrets/api_key

secrets:
  db_password:
    file: ./secrets/db_password.txt
  api_key:
    file: ./secrets/api_key.txt
```

```yaml
# ❌ BAD: Hardcoded secrets
version: '3.8'
services:
  app:
    image: myapp
    environment:
      - DB_PASSWORD=mysecretpassword123
      - API_KEY=sk-1234567890abcdef
```

### 4. Resource Management

```yaml
# Resource limits and reservations
services:
  app:
    image: myapp
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
        reservations:
          memory: 256M
          cpus: '0.25'
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

---

## 🔒 Bảo Mật Docker

### 1. Container Security

```bash
# ✅ SECURE: Container runtime options
docker run \
  --user 1001:1001 \                    # Non-root user
  --read-only \                         # Read-only filesystem
  --tmpfs /tmp \                        # Writable tmp
  --tmpfs /var/run \                    # Writable var/run
  --no-new-privileges \                 # Prevent privilege escalation
  --cap-drop ALL \                      # Drop all capabilities
  --cap-add NET_BIND_SERVICE \          # Add only needed capabilities
  --security-opt no-new-privileges \    # Security options
  --security-opt apparmor:docker-default \
  --memory 512m \                       # Memory limits
  --cpus 1.0 \                         # CPU limits
  --pids-limit 100 \                   # Process limits
  myapp:latest
```

### 2. Image Security

```bash
# Security scanning
docker scan myapp:latest              # Docker native scanning
trivy image myapp:latest              # Alternative scanner
dive myapp:latest                     # Image layer analysis

# Image signing
docker trust sign myapp:latest
docker trust inspect myapp:latest
```

### 3. Network Security

```yaml
# Secure network configuration
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # Backend network isolated from external
  database:
    driver: bridge
    internal: true  # Database only accessible from backend
```

### 4. Secrets Management

```bash
# Create secrets
echo "mysecretpassword" | docker secret create db_password -
echo "myapikey" | docker secret create api_key -

# Use secrets in compose
version: '3.8'
services:
  app:
    image: myapp
    secrets:
      - db_password
      - api_key
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password
```

---

## ⚡ Performance Optimization

### 1. Image Size Optimization

```dockerfile
# ✅ OPTIMIZED: Smaller image size
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

### 2. Build Optimization

```bash
# Build with cache
docker build --cache-from myapp:latest -t myapp:new .

# Multi-stage build with specific target
docker build --target builder -t myapp:builder .

# Build with build args
docker build --build-arg NODE_ENV=production -t myapp:prod .
```

### 3. Resource Monitoring

```bash
# Monitor resource usage
docker stats
docker exec container_name top
docker exec container_name free -h
docker exec container_name df -h

# System cleanup
docker system prune -a
docker volume prune
docker network prune
```

### 4. Caching Strategies

```dockerfile
# Optimize layer caching
FROM node:18-alpine

# Copy package files first (changes less frequently)
COPY package*.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy source code last (changes frequently)
COPY . .
RUN yarn build
```

---

## 🚀 Production Deployment

### 1. Production Dockerfile

```dockerfile
# Production-ready Dockerfile
FROM node:18.10.0-alpine AS builder

# Security: Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001 -G nodejs

WORKDIR /app

# Copy package files with proper ownership
COPY --chown=nextjs:nodejs package*.json yarn.lock ./
RUN yarn install --frozen-lockfile --production=false

# Copy source with proper ownership
COPY --chown=nextjs:nodejs . .
RUN yarn build

# Production stage
FROM nginx:1.25-alpine

# Update packages and install security updates
RUN apk update && apk upgrade && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# Create non-root user for nginx
RUN addgroup -g 1001 -S nginx-group && \
    adduser -S nginx-user -u 1001 -G nginx-group

# Copy built app with proper ownership
COPY --from=builder --chown=nginx-user:nginx-group /app/dist /usr/share/nginx/html

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

USER nginx-user
EXPOSE 80
```

### 2. Production Compose

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  app:
    image: myapp:latest
    ports:
      - "80:80"
    environment:
      - NODE_ENV=production
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'
        reservations:
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

### 3. Deployment Scripts

```bash
#!/bin/bash
# deploy.sh

set -e

# Build and tag image
docker build -t myapp:latest .
docker tag myapp:latest myapp:$(date +%Y%m%d-%H%M%S)

# Deploy with compose
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Health check
sleep 30
curl -f http://localhost/health || exit 1

echo "Deployment successful!"
```

---

## 📊 Monitoring & Logging

### 1. Logging Configuration

```yaml
# Logging setup
services:
  app:
    image: myapp
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    labels:
      - "prometheus.io/scrape=true"
      - "prometheus.io/port=3000"
      - "prometheus.io/path=/metrics"
```

### 2. Monitoring Stack

```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  # Prometheus monitoring
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus

  # Grafana dashboards
  grafana:
    image: grafana/grafana
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana

  # Log aggregation
  elasticsearch:
    image: elasticsearch:7.15.0
    environment:
      - discovery.type=single-node
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  kibana:
    image: kibana:7.15.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

volumes:
  prometheus_data:
  grafana_data:
  elasticsearch_data:
```

### 3. Health Checks

```yaml
# Health check configuration
services:
  app:
    image: myapp
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

---

## 🔧 Troubleshooting

### 1. Common Issues

```bash
# Container won't start
docker logs container_name
docker events --filter container=container_name

# Performance issues
docker stats
docker exec container_name top
docker exec container_name free -h
docker exec container_name df -h

# Network connectivity
docker exec container_name ping google.com
docker exec container_name nslookup google.com
docker exec container_name netstat -tlnp

# Storage issues
docker system df
docker volume ls
docker exec container_name du -sh /*

# Image build issues
docker build --no-cache .
docker build --progress=plain .
```

### 2. Debug Commands

```bash
# Debug container
docker exec -it container_name bash
docker exec -it container_name sh  # For Alpine

# Inspect container
docker inspect container_name
docker inspect --format='{{.NetworkSettings.IPAddress}}' container_name

# Check logs
docker logs container_name
docker logs -f container_name
docker logs --tail 100 container_name
docker logs --since 2h container_name

# Monitor resources
docker stats
docker exec container_name top
docker exec container_name ps aux
```

### 3. Cleanup Commands

```bash
# Clean up resources
docker system prune -a
docker volume prune
docker network prune
docker image prune -a

# Remove specific resources
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
docker volume rm $(docker volume ls -q)
```

---

## 📋 Checklist Best Practices

### ✅ Dockerfile Checklist
- [ ] Use specific base image versions (not `latest`)
- [ ] Implement multi-stage builds
- [ ] Create non-root user
- [ ] Use `.dockerignore` file
- [ ] Optimize layer caching
- [ ] Add health checks
- [ ] Update packages for security
- [ ] Minimize image size

### ✅ Docker Compose Checklist
- [ ] Use specific image versions
- [ ] Implement proper networking
- [ ] Use secrets for sensitive data
- [ ] Add resource limits
- [ ] Configure health checks
- [ ] Set up proper logging
- [ ] Use environment-specific configs
- [ ] Implement proper dependencies

### ✅ Security Checklist
- [ ] Run containers as non-root
- [ ] Use read-only filesystems
- [ ] Drop unnecessary capabilities
- [ ] Implement network segmentation
- [ ] Use secrets management
- [ ] Scan images for vulnerabilities
- [ ] Update base images regularly
- [ ] Implement proper access controls

### ✅ Production Checklist
- [ ] Use production-ready base images
- [ ] Implement monitoring and logging
- [ ] Configure proper health checks
- [ ] Set up resource limits
- [ ] Implement backup strategies
- [ ] Use orchestration tools (Kubernetes)
- [ ] Implement CI/CD pipelines
- [ ] Regular security updates

---

## 🎯 Kết Luận

Docker và Docker Compose là công cụ mạnh mẽ cho containerization, nhưng cần tuân thủ best practices để đảm bảo:

1. **Security**: Bảo mật container và data
2. **Performance**: Tối ưu hóa resource usage
3. **Maintainability**: Dễ dàng maintain và scale
4. **Reliability**: Ổn định trong production

### Key Takeaways:
- Luôn sử dụng specific versions thay vì `latest`
- Implement multi-stage builds để giảm image size
- Tạo non-root user cho security
- Sử dụng secrets management cho sensitive data
- Implement proper monitoring và logging
- Regular security scanning và updates

---

*Tài liệu này được tạo dựa trên best practices từ cộng đồng Docker và kinh nghiệm thực tế trong các dự án production.*
