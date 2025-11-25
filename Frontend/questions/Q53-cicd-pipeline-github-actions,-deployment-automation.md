# 🚀 Q53: CI/CD Pipeline - GitHub Actions, Deployment Automation

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CI/CD pipeline tự động hóa: Code quality (lint, test) → Build → Deploy. GitHub Actions: workflows YAML, matrix builds, caching. Deploy strategies: Blue-Green, Canary, Rolling. Secrets: GitHub Secrets + env variables."**

**🔑 CI/CD Stages:**

**1. Code Quality (on PR):**
- ESLint + Prettier check (formatting)
- TypeScript type check
- Unit tests (Jest/Vitest)
- Integration tests (React Testing Library)
- Bundle size check (fail if > budget)

**2. Build (on merge):**
- Install dependencies (npm ci với cache)
- Build production bundle (`npm run build`)
- Generate source maps
- Upload artifacts (S3, CDN)

**3. Deploy:**
- **Staging**: Auto-deploy on develop branch
- **Production**: Auto-deploy on main (or manual approval)
- Deployment strategies: Blue-Green, Canary, Rolling
- Health checks + smoke tests

**4. Post-Deploy:**
- Lighthouse CI (performance check)
- Sentry release tracking
- Slack/Discord notifications
- Rollback on failure

**🔑 GitHub Actions Best Practices:**

- **Matrix builds**: Test nhiều Node versions (18, 20, 22)
- **Caching**: `actions/cache` cho node_modules - save 2-5 phiMút
- **Secrets**: `${{ secrets.API_KEY }}` - không hardcode
- **Conditional runs**: `if: github.event_name == 'push'`
- **Reusable workflows**: Share common workflows

**⚠️ Lỗi Thường Gặp:**
- Không cache dependencies → mỗi build install lại (chậm)
- Hardcode secrets trong code → security risk
- Deploy thẳng production → không rollback, dùng Blue-Green
- Không test staging → bugs in production

**💡 Kiến Thức Senior:**
- **Docker multi-stage builds**: Build image nhỏ (Alpine base, remove dev deps)
- **Vercel/Netlify**: Zero-config CI/CD (auto-detect framework)
- **Deployment slots** (Azure): Test production environment trước swap
- **Feature flags**: Deploy code OFF, bật dần (LaunchDarkly)

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)  
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [CI/CD Pipeline Design](#1-cicd-pipeline-design)
2. [GitHub Actions Workflows](#2-github-actions-workflows)
3. [Build Optimization](#3-build-optimization)
4. [Deployment Strategies](#4-deployment-strategies)
5. [Environment Management](#5-environment-management)
6. [Secrets Management](#6-secrets-management)
7. [Docker for Frontend](#7-docker-for-frontend)
8. [Monitoring & Rollback](#8-monitoring--rollback)

---

## 1. CI/CD Pipeline Design

### **1.1. Complete CI/CD Flow**

```yaml
# ===================================================
# 🔄 **COMPLETE CI/CD PIPELINE**
# ===================================================

name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

# ✅ Pipeline stages
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

  # Stage 3: Build
  build:
    runs-on: ubuntu-latest
    needs: [lint-and-format, test]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      
      - run: npm ci
      - run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
          retention-days: 7

  # Stage 4: E2E Tests
  e2e:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      
      - run: npm ci
      - run: npx playwright install --with-deps
      
      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist/
      
      - run: npm run preview &
      - run: npm run test:e2e
      
      - name: Upload Playwright report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/

  # Stage 5: Deploy to Staging
  deploy-staging:
    runs-on: ubuntu-latest
    needs: [build, e2e]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - uses: actions/checkout@v4
      
      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist/
      
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          working-directory: ./

  # Stage 6: Deploy to Production
  deploy-production:
    runs-on: ubuntu-latest
    needs: [build, e2e]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/checkout@v4
      
      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: dist
          path: dist/
      
      - name: Deploy to Vercel Production
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
          working-directory: ./
      
      - name: Create Sentry release
        uses: getsentry/action-release@v1
        with:
          environment: production
          version: ${{ github.sha }}
```

---

## 2. GitHub Actions Workflows

### **2.1. Reusable Workflows**

```yaml
# ===================================================
# ♻️ **REUSABLE WORKFLOW** (.github/workflows/reusable-build.yml)
# ===================================================

name: Reusable Build

on:
  workflow_call:
    inputs:
      node-version:
        required: false
        type: string
        default: '20'
      environment:
        required: true
        type: string
    secrets:
      VITE_API_URL:
        required: true
      SENTRY_DSN:
        required: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build application
        env:
          VITE_API_URL: ${{ secrets.VITE_API_URL }}
          VITE_SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          NODE_ENV: ${{ inputs.environment }}
        run: npm run build
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: dist-${{ inputs.environment }}
          path: dist/

# ===================================================
# 🎯 **USAGE: Call reusable workflow**
# ===================================================

# .github/workflows/deploy-staging.yml
name: Deploy Staging

on:
  push:
    branches: [develop]

jobs:
  build-and-deploy:
    uses: ./.github/workflows/reusable-build.yml
    with:
      environment: staging
    secrets:
      VITE_API_URL: ${{ secrets.STAGING_API_URL }}
      SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
```

### **2.2. Matrix Strategy**

```yaml
# ===================================================
# 🔢 **MATRIX BUILDS** (Test across versions)
# ===================================================

name: Cross-Platform Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [18, 20, 22]
        exclude:
          # Exclude specific combinations
          - os: windows-latest
            node-version: 18
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      
      - run: npm ci
      - run: npm test
      
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: test-results-${{ matrix.os }}-node${{ matrix.node-version }}
          path: test-results/
```

---

## 3. Build Optimization

### **3.1. Caching Strategies**

```yaml
# ===================================================
# ⚡ **AGGRESSIVE CACHING**
# ===================================================

name: Optimized Build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      # ✅ Cache npm dependencies
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      
      # ✅ Cache node_modules explicitly
      - name: Cache node modules
        uses: actions/cache@v3
        id: cache-node-modules
        with:
          path: node_modules
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-
      
      - name: Install dependencies
        if: steps.cache-node-modules.outputs.cache-hit != 'true'
        run: npm ci
      
      # ✅ Cache Vite build cache
      - name: Cache Vite
        uses: actions/cache@v3
        with:
          path: |
            node_modules/.vite
            .vite
          key: ${{ runner.os }}-vite-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**/*.ts', '**/*.tsx') }}
      
      # ✅ Cache TypeScript build info
      - name: Cache TypeScript
        uses: actions/cache@v3
        with:
          path: '**/*.tsbuildinfo'
          key: ${{ runner.os }}-typescript-${{ hashFiles('**/package-lock.json') }}
      
      - run: npm run build
      
      # ✅ Cache build output for reuse
      - uses: actions/cache@v3
        with:
          path: dist/
          key: ${{ runner.os }}-build-${{ github.sha }}
```

### **3.2. Parallel Jobs**

```yaml
# ===================================================
# 🚀 **PARALLEL EXECUTION**
# ===================================================

name: Parallel Pipeline

on: [push]

jobs:
  install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - uses: actions/cache@v3
        with:
          path: node_modules
          key: ${{ runner.os }}-nm-${{ hashFiles('**/package-lock.json') }}

  lint:
    needs: install
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - uses: actions/cache@v3
        with:
          path: node_modules
          key: ${{ runner.os }}-nm-${{ hashFiles('**/package-lock.json') }}
      - run: npm run lint

  test-unit:
    needs: install
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - uses: actions/cache@v3
        with:
          path: node_modules
          key: ${{ runner.os }}-nm-${{ hashFiles('**/package-lock.json') }}
      - run: npm run test:unit

  test-integration:
    needs: install
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - uses: actions/cache@v3
        with:
          path: node_modules
          key: ${{ runner.os }}-nm-${{ hashFiles('**/package-lock.json') }}
      - run: npm run test:integration

  build:
    needs: [lint, test-unit, test-integration]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - uses: actions/cache@v3
        with:
          path: node_modules
          key: ${{ runner.os }}-nm-${{ hashFiles('**/package-lock.json') }}
      - run: npm run build
```

---

## 4. Deployment Strategies

### **4.1. Blue-Green Deployment**

```yaml
# ===================================================
# 🔵🟢 **BLUE-GREEN DEPLOYMENT**
# ===================================================

name: Blue-Green Deploy

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
      
      - name: Build application
        run: npm ci && npm run build
      
      - name: Deploy to ${{ inputs.target }} environment
        run: |
          if [ "${{ inputs.target }}" == "blue" ]; then
            echo "Deploying to BLUE environment"
            aws s3 sync dist/ s3://my-app-blue/ --delete
          else
            echo "Deploying to GREEN environment"
            aws s3 sync dist/ s3://my-app-green/ --delete
          fi
      
      - name: Run smoke tests
        run: npm run test:smoke -- --env=${{ inputs.target }}
      
      - name: Switch traffic to ${{ inputs.target }}
        run: |
          # Update load balancer to point to new environment
          aws elbv2 modify-rule \
            --rule-arn ${{ secrets.ALB_RULE_ARN }} \
            --actions Type=forward,TargetGroupArn=${{ secrets[format('TG_{0}_ARN', inputs.target)] }}
```

### **4.2. Canary Deployment**

```yaml
# ===================================================
# 🐤 **CANARY DEPLOYMENT** (Gradual rollout)
# ===================================================

name: Canary Deploy

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
      
      - name: Build and deploy canary
        run: |
          npm ci && npm run build
          aws s3 sync dist/ s3://my-app-canary/ --delete
      
      - name: Update traffic split
        run: |
          aws cloudfront update-distribution \
            --id ${{ secrets.CF_DISTRIBUTION_ID }} \
            --distribution-config file://canary-config.json \
            --if-match $ETAG
      
      - name: Monitor canary for 10 minutes
        run: |
          sleep 600
          ERROR_RATE=$(curl -s https://api.datadog.com/api/v1/metrics | jq '.error_rate')
          if [ "$ERROR_RATE" -gt "1" ]; then
            echo "Canary failed! Rolling back..."
            exit 1
          fi
      
      - name: Promote canary to production
        if: inputs.canary-percentage == '100'
        run: |
          aws s3 sync s3://my-app-canary/ s3://my-app-prod/ --delete
```

---

## 5. Environment Management

### **5.1. Environment Variables**

```yaml
# ===================================================
# 🌍 **ENVIRONMENT-SPECIFIC BUILDS**
# ===================================================

name: Multi-Environment Build

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
      
      - name: Set environment variables
        run: |
          if [ "${{ matrix.environment }}" == "production" ]; then
            echo "VITE_API_URL=https://api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_PROD }}" >> $GITHUB_ENV
          elif [ "${{ matrix.environment }}" == "staging" ]; then
            echo "VITE_API_URL=https://staging-api.example.com" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=${{ secrets.SENTRY_DSN_STAGING }}" >> $GITHUB_ENV
          else
            echo "VITE_API_URL=http://localhost:3000" >> $GITHUB_ENV
            echo "VITE_SENTRY_DSN=" >> $GITHUB_ENV
          fi
      
      - run: npm ci && npm run build
      
      - uses: actions/upload-artifact@v3
        with:
          name: dist-${{ matrix.environment }}
          path: dist/
```

---

## 6. Secrets Management

### **6.1. GitHub Secrets & Vault**

```yaml
# ===================================================
# 🔐 **SECRETS MANAGEMENT**
# ===================================================

name: Secure Deployment

on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      # ✅ Import secrets from Vault
      - name: Import Secrets from Vault
        uses: hashicorp/vault-action@v2
        with:
          url: https://vault.example.com
          token: ${{ secrets.VAULT_TOKEN }}
          secrets: |
            secret/data/production apiKey | API_KEY ;
            secret/data/production dbPassword | DB_PASSWORD
      
      # ✅ Use secrets in build
      - name: Build with secrets
        env:
          VITE_API_KEY: ${{ env.API_KEY }}
        run: npm ci && npm run build
      
      # ✅ Upload source maps to Sentry (with auth)
      - name: Upload source maps
        env:
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
        run: |
          npx @sentry/cli upload-sourcemaps \
            --org my-org \
            --project my-project \
            --release ${{ github.sha }} \
            ./dist
```

---

## 7. Docker for Frontend

### **7.1. Multi-Stage Dockerfile**

```dockerfile
# ===================================================
# 🐳 **OPTIMIZED DOCKERFILE**
# ===================================================

# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# ✅ Copy package files first (layer caching)
COPY package*.json ./
RUN npm ci --only=production

# ✅ Copy source code
COPY . .

# ✅ Build application
ENV NODE_ENV=production
RUN npm run build

# Stage 2: Production
FROM nginx:alpine

# ✅ Copy built assets
COPY --from=builder /app/dist /usr/share/nginx/html

# ✅ Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# ✅ Add health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

```yaml
# ===================================================
# 🚢 **DOCKER BUILD & PUSH WORKFLOW**
# ===================================================

name: Docker Build

on:
  push:
    tags:
      - 'v*'

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: myorg/my-app
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
          cache-from: type=registry,ref=myorg/my-app:buildcache
          cache-to: type=registry,ref=myorg/my-app:buildcache,mode=max
```

---

## 8. Monitoring & Rollback

### **8.1. Automated Rollback**

```yaml
# ===================================================
# ⏪ **AUTOMATIC ROLLBACK ON FAILURE**
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
      
      - name: Get previous deployment
        id: previous
        run: |
          PREV_VERSION=$(aws s3 cp s3://my-app-versions/current.txt -)
          echo "version=$PREV_VERSION" >> $GITHUB_OUTPUT
      
      - name: Build and deploy new version
        run: |
          npm ci && npm run build
          aws s3 sync dist/ s3://my-app-prod/
          echo "${{ github.sha }}" | aws s3 cp - s3://my-app-versions/current.txt
      
      - name: Wait for deployment
        run: sleep 60
      
      - name: Run health checks
        id: health
        continue-on-error: true
        run: |
          curl -f https://example.com/health || exit 1
          ERROR_RATE=$(curl -s https://api.datadog.com/api/v1/query?query=avg:error.rate | jq '.series[0].pointlist[-1][1]')
          if (( $(echo "$ERROR_RATE > 0.05" | bc -l) )); then
            echo "Error rate too high: $ERROR_RATE"
            exit 1
          fi
      
      - name: Rollback on failure
        if: steps.health.outcome == 'failure'
        run: |
          echo "Health checks failed! Rolling back to ${{ steps.previous.outputs.version }}"
          aws s3 sync s3://my-app-versions/${{ steps.previous.outputs.version }}/ s3://my-app-prod/
          
          # Notify team
          curl -X POST ${{ secrets.SLACK_WEBHOOK }} \
            -d '{"text":"🚨 Deployment failed and rolled back to ${{ steps.previous.outputs.version }}"}'
```

---

**🎯 Remember:** "A good CI/CD pipeline should be fast, reliable, and provide quick feedback. Automate everything that can be automated!"
