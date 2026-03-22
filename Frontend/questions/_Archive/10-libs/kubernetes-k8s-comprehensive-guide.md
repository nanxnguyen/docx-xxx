# 🐳 Kubernetes (K8s) - Hướng Dẫn Toàn Diện

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút)**

**"Kubernetes (K8s) là platform mã nguồn mở để orchestrate containers - tự động triển khai, mở rộng, và quản lý containerized applications."**

**🔑 Khái Niệm Cốt Lõi:**

1. **Container Orchestration**: 
   - Tự động scale pods lên/xuống theo demand
   - Self-healing: Restart failed containers
   - Rolling updates: Zero-downtime deployments
   - Load balancing: Distribute traffic giữa pods

2. **Architecture**:
   - **Master/Control Plane**: Quản lý cluster (API Server, etcd, Scheduler, Controller Manager)
   - **Worker Nodes**: Chạy containers (Kubelet, Container Runtime)
   - **etcd**: Distributed key-value store lưu trữ state toàn cluster

3. **Core Objects**:
   - **Pod**: Smallest deployable unit (usually 1 container)
   - **Deployment**: Manages replicas của pods (rolling updates)
   - **Service**: Network abstraction layer (internal/external communication)
   - **Namespace**: Virtual cluster (isolation)
   - **ConfigMap/Secret**: Configuration management
   - **PersistentVolume**: Storage management

4. **Workflow**:
   ```
   kubectl apply (manifest) → API Server → Store in etcd
   → Scheduler (tìm node phù hợp) → Kubelet (pull image, run container)
   → Controller Manager (monitor, reconcile)
   ```

5. **Advantages**:
   - ✅ High availability (multi-node, auto-failover)
   - ✅ Self-healing (auto-restart, reschedule)
   - ✅ Scalability (horizontal pod autoscaling)
   - ✅ Rolling updates (zero-downtime)
   - ✅ Resource management (CPU/memory limits)
   - ✅ Multi-cloud deployment (consistent API)

6. **Challenges**:
   - ⚠️ Steep learning curve
   - ⚠️ Complex networking
   - ⚠️ Requires infrastructure (not for simple apps)
   - ⚠️ Observability complexity (logging, monitoring, tracing)

**💼 Real-World Example:**
```
Deploy microservices:
- API Service: 3 replicas, auto-scale 2-10
- Database: 1 StatefulSet, persistent storage
- Cache: Redis, 2 replicas, RDB backup
- Frontend: 5 replicas, CDN + K8s Service

Kubernetes automatically:
→ Distributes pods across 5 nodes
→ Restarts failed pods
→ Updates services with 0 downtime
→ Auto-scales API to 8 replicas when CPU > 80%
→ Manages networking (DNS, load balancing)
```

---

## **📖 Table of Contents**

- [I. Kubernetes Fundamentals](#i-kubernetes-fundamentals)
- [II. Core Architecture](#ii-core-architecture)
- [III. Key Objects & Resources](#iii-key-objects--resources)
- [IV. Networking in K8s](#iv-networking-in-k8s)
- [V. Storage & Persistence](#v-storage--persistence)
- [VI. Scaling & Auto-scaling](#vi-scaling--auto-scaling)
- [VII. Best Practices](#vii-best-practices)
- [VIII. Deep Dive Questions](#viii-deep-dive-questions)

---

## **I. Kubernetes Fundamentals**

### **1.1 What is Kubernetes?**

```
┌─────────────────────────────────────────────────────────────┐
│                  KUBERNETES = K8S                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ Container Orchestration Platform:                          │
│                                                              │
│ ❌ BEFORE (Manual):                                         │
│   - Run docker containers manually                          │
│   - SSH to each server, start containers                    │
│   - Manual health checks, restarts                          │
│   - Manual load balancing                                   │
│   - Manual scaling (add/remove servers)                     │
│   - Nightmare for 100+ containers!                          │
│                                                              │
│ ✅ AFTER (K8s):                                             │
│   - Declare desired state (YAML manifest)                   │
│   - K8s handles the rest automatically                      │
│   - Self-healing, auto-scaling, auto-networking            │
│   - Consistent API across cloud providers                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### **1.2 Key Components**

```
┌──────────────────────────────────────────────────────────────────┐
│              KUBERNETES CLUSTER ARCHITECTURE                      │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────┐      ┌──────────────────────────┐  │
│  │  CONTROL PLANE          │      │  WORKER NODES (多個)    │  │
│  │  (Master Nodes)         │      │                          │  │
│  │                         │      │  ┌──────────────────┐   │  │
│  │ ┌─────────────────────┐ │      │  │ Node 1           │   │  │
│  │ │ API Server          │ │◄────┼──►├──────────────────┤   │  │
│  │ │ (REST API)          │ │      │  │ Kubelet (agent)  │   │  │
│  │ └─────────────────────┘ │      │  │ Container Runtime│   │  │
│  │                         │      │  │ (Docker/containerd)  │  │
│  │ ┌─────────────────────┐ │      │  │ ┌──┬──┬──────────┤   │  │
│  │ │ etcd (DB)           │ │      │  │ │P1│P2│P3...    │   │  │
│  │ │ Store state         │ │      │  │ └──┴──┴──────────┘   │  │
│  │ └─────────────────────┘ │      │  └──────────────────┘   │  │
│  │                         │      │                          │  │
│  │ ┌─────────────────────┐ │      │  ┌──────────────────┐   │  │
│  │ │ Scheduler           │ │      │  │ Node N           │   │  │
│  │ │ (assign pods)       │ │      │  │ (Similar...)    │   │  │
│  │ └─────────────────────┘ │      │  └──────────────────┘   │  │
│  │                         │      │                          │  │
│  │ ┌─────────────────────┐ │      └──────────────────────────┘  │
│  │ │Controller Manager   │ │                                    │
│  │ │ (reconcile state)   │ │      Network Layer:                │
│  │ └─────────────────────┘ │      • etcd links all nodes        │
│  │                         │      • Service networking          │
│  └─────────────────────────┘      • DNS (CoreDNS)              │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## **II. Core Architecture**

### **2.1 Control Plane Components**

| Component | Role | Responsibility |
|-----------|------|-----------------|
| **API Server** | Gateway | REST API, request validation, etcd write |
| **etcd** | Database | Distributed K/V store, cluster state |
| **Scheduler** | Assigner | Assign pods to nodes based on resources |
| **Controller Manager** | Monitor | Reconcile desired vs actual state |
| **Cloud Controller Manager** | Provider-specific | Cloud provider integration |

### **2.2 Worker Node Components**

| Component | Role | Responsibility |
|-----------|------|-----------------|
| **Kubelet** | Agent | Monitor pod health, communicate with API server |
| **Container Runtime** | Executor | Pull images, run containers (Docker/containerd) |
| **kube-proxy** | Network | Implement service networking, iptables rules |

### **2.3 Request Flow**

```
1️⃣ User applies manifest:
   kubectl apply -f deployment.yaml

2️⃣ API Server:
   - Validates manifest
   - Stores in etcd
   - Notifies watchers

3️⃣ Scheduler:
   - Watches for unassigned pods
   - Selects best node (CPU, memory, affinity)
   - Updates pod with node assignment

4️⃣ Kubelet (on target node):
   - Watches for pods assigned to it
   - Pulls container image
   - Runs container
   - Reports status

5️⃣ Controller Manager:
   - Monitors pod status continuously
   - If pod dies → reschedule
   - If replicas < desired → create new
   - If replicas > desired → delete

6️⃣ Service:
   - Routes traffic to healthy pods
   - kube-proxy updates iptables
   - DNS resolves service name
```

---

## **III. Key Objects & Resources**

### **3.1 Pod - Basic Building Block**

```yaml
# ❌ DON'T: Run pods directly
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app
    image: myapp:1.0
    ports:
    - containerPort: 8080

# ✅ DO: Use Deployment (manages pods)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
```

### **3.2 Service - Network Abstraction**

```yaml
# Service types:
# 1. ClusterIP (default) - Internal only
# 2. NodePort - External via node port
# 3. LoadBalancer - Cloud provider load balancer
# 4. ExternalName - Maps to external service

---
# ClusterIP - Internal communication
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - port: 8080
    targetPort: 8080

# Usage: curl http://app-service:8080 (from any pod)

---
# LoadBalancer - External access
apiVersion: v1
kind: Service
metadata:
  name: app-lb
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080

# Gets external IP from cloud provider (AWS, GCP, Azure)
# Usage: curl http://<external-ip>:80
```

### **3.3 ConfigMap & Secret**

```yaml
# ConfigMap - Non-sensitive configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "db.default.svc.cluster.local"
  LOG_LEVEL: "info"
  CACHE_TTL: "3600"

---
# Secret - Sensitive data (base64 encoded)
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQxMjM=  # base64 encoded
  API_KEY: YWJjZGVmZ2g=

---
# Use in Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
      - name: app
        image: myapp:1.0
        env:
        # From ConfigMap
        - name: DATABASE_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: DATABASE_HOST
        # From Secret
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secret
              key: DB_PASSWORD
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
      - name: config-volume
        configMap:
          name: app-config
```

### **3.4 StatefulSet - Stateful Applications**

```yaml
# StatefulSet: Databases, caches, message queues
# - Stable pod names (db-0, db-1, db-2)
# - Ordered deployment
# - Persistent storage per pod
# - Stable network identity

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: root-password
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 10Gi

# Access pattern:
# - mysql-0.mysql:3306 (stable network identity)
# - mysql-1.mysql:3306
# - mysql-2.mysql:3306
```

---

## **IV. Networking in K8s**

### **4.1 Pod-to-Pod Communication**

```
┌────────────────────────────────────────────────────┐
│         POD NETWORKING ARCHITECTURE                │
├────────────────────────────────────────────────────┤
│                                                    │
│ Same Node:                                        │
│ ┌─────────────────────────────────────────────┐  │
│ │ Pod A (10.0.1.1) ──┐                       │  │
│ │                    │ (via virtual bridge) │  │
│ │ Pod B (10.0.1.2) ──┤                       │  │
│ │                    ↓                       │  │
│ │             Node's eth0                   │  │
│ │         (10.244.0.0/24 network)          │  │
│ └─────────────────────────────────────────────┘  │
│                                                    │
│ Different Nodes:                                  │
│ ┌──────────────────────┐   ┌──────────────────┐  │
│ │ Node 1 (10.0.1.0/24) │   │ Node 2 (10.0.2) │  │
│ │ ┌────────────────┐   │   │ ┌────────────┐  │  │
│ │ │ Pod A          │   │   │ │ Pod C      │  │  │
│ │ │ (10.0.1.1)     │   │   │ │ (10.0.2.1) │  │  │
│ │ └────────────────┘   │   │ └────────────┘  │  │
│ │       │              │   │       ↑         │  │
│ │       └──────────────┼───┼───────┘         │  │
│ │      (tunnel/overlay)│   │                 │  │
│ └──────────────────────┘   └──────────────────┘  │
│                                                    │
│ Each pod gets routable IP (cluster-wide unique)  │
│ CNI plugin manages networking (Flannel, Calico)  │
│                                                    │
└────────────────────────────────────────────────────┘
```

### **4.2 Service Discovery & DNS**

```yaml
# Internal DNS (automatic):
# <service-name>.<namespace>.svc.cluster.local

# Example:
# Service: app-service in namespace: default
# DNS: app-service.default.svc.cluster.local

apiVersion: v1
kind: Service
metadata:
  name: api
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: api
  ports:
  - port: 8080

# From any pod in cluster:
curl http://api.production.svc.cluster.local:8080

# Shorter form (from same namespace):
curl http://api:8080
```

### **4.3 Ingress - External Access**

```yaml
# Ingress routes external traffic to services
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
  - host: web.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 3000

# Flow:
# api.example.com:443 → Ingress Controller → api-service:8080 → pods
```

---

## **V. Storage & Persistence**

### **5.1 PersistentVolume (PV) & PersistentVolumeClaim (PVC)**

```yaml
# PersistentVolume - Storage resource (cluster-level)
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-local
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce  # Only 1 pod can mount
  persistentVolumeReclaimPolicy: Retain  # Don't delete data
  storageClassName: fast-ssd
  hostPath:  # Local storage (development only!)
    path: /data

---
# PersistentVolumeClaim - Pod requests storage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 5Gi

---
# Use PVC in Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
      - name: app
        image: myapp:1.0
        volumeMounts:
        - name: data
          mountPath: /data
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: app-pvc
```

### **5.2 StorageClass - Dynamic Storage Provisioning**

```yaml
# StorageClass automates PV creation
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs  # Cloud provider
parameters:
  type: gp3  # General purpose SSD
  iops: "3000"
  throughput: "125"
allowVolumeExpansion: true

---
# PVC automatically creates matching PV
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
spec:
  storageClassName: fast-ssd  # ← Triggers provisioning
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi

# Kubernetes automatically:
# 1. Creates AWS EBS volume (50GB, gp3)
# 2. Creates PV pointing to it
# 3. Binds PVC to PV
```

---

## **VI. Scaling & Auto-scaling**

### **6.1 Manual Scaling**

```bash
# Scale deployment to 5 replicas
kubectl scale deployment myapp --replicas=5

# Check status
kubectl get pods -l app=myapp
```

### **6.2 Horizontal Pod Autoscaling (HPA)**

```yaml
# HPA scales pods based on metrics
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 2
  maxReplicas: 10
  metrics:
  # Scale based on CPU usage
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70  # Scale at 70% CPU
  # Scale based on custom metrics
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"

# Behavior (smooth scaling)
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait 5 min
      policies:
      - type: Percent
        value: 50  # Scale down max 50%
        periodSeconds: 15
    scaleUp:
      stabilizationWindowSeconds: 0  # Immediate
      policies:
      - type: Percent
        value: 100  # Double replicas
        periodSeconds: 15

# HPA automatically adjusts replicas based on CPU/custom metrics
```

### **6.3 Vertical Pod Autoscaling (VPA)**

```yaml
# VPA adjusts CPU/memory requests (requires downtime)
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: app-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Auto"  # Auto update or "Off" for recommendations only
  resourcePolicy:
    containerPolicies:
    - containerName: app
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
```

---

## **VII. Best Practices**

### **7.1 Resource Management**

```yaml
# ✅ Always set resource requests/limits
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
      - name: app
        image: myapp:1.0
        resources:
          # Minimum guaranteed (for scheduling)
          requests:
            cpu: 100m      # 0.1 core
            memory: 256Mi
          # Maximum allowed (hard limit)
          limits:
            cpu: 500m      # 0.5 core
            memory: 512Mi

# ❌ DON'T: No limits (can crash node!)
# ✅ DO: Set both requests and limits
```

### **7.2 Health Checks**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  template:
    spec:
      containers:
      - name: app
        image: myapp:1.0
        # Startup probe (initial delay)
        startupProbe:
          httpGet:
            path: /health
            port: 8080
          failureThreshold: 30  # 30 * 10 = 300s to start
          periodSeconds: 10
        # Liveness probe (is it alive?)
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3  # 3 failures → restart
        # Readiness probe (ready to serve?)
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
          failureThreshold: 1  # 1 failure → remove from service
```

### **7.3 Pod Disruption Budgets (PDB)**

```yaml
# Ensure minimum pods during voluntary disruption
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
spec:
  minAvailable: 2  # Keep at least 2 pods running
  selector:
    matchLabels:
      app: myapp

# During cluster upgrade:
# - kubectl drain node: respects PDB
# - Won't drain if leaves < 2 pods
# - Gracefully evicts pods (if safe)
```

### **7.4 Network Policies**

```yaml
# Restrict traffic (zero-trust networking)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-network-policy
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  - Egress
  ingress:
  # Allow from frontend only
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  # Allow to database
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  # Allow DNS
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
```

### **7.5 Security Best Practices**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-app
spec:
  template:
    spec:
      serviceAccountName: app-sa  # Custom service account
      securityContext:
        runAsNonRoot: true        # Don't run as root
        runAsUser: 1000
        fsReadOnlyRootFilesystem: true  # Read-only filesystem
      containers:
      - name: app
        image: myapp:1.0
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop:
            - ALL
          readOnlyRootFilesystem: true
        volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: var-cache
          mountPath: /var/cache
      volumes:
      - name: tmp
        emptyDir: {}
      - name: var-cache
        emptyDir: {}
```

### **7.6 Logging & Monitoring**

```yaml
# Add monitoring/observability
apiVersion: v1
kind: Pod
metadata:
  name: app
  labels:
    app: myapp
    version: v1
    team: platform
spec:
  containers:
  - name: app
    image: myapp:1.0
    ports:
    - name: metrics
      containerPort: 9090  # Prometheus metrics
    - name: http
      containerPort: 8080
    env:
    - name: LOG_LEVEL
      value: "info"

# Prometheus scrape config:
# scrape_configs:
# - job_name: 'kubernetes-pods'
#   kubernetes_sd_configs:
#   - role: pod
#   relabel_configs:
#   - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
#     action: keep
#     regex: true
```

---

## **VIII. Deep Dive Questions**

### **🔥 Q1: Pod Eviction vs Termination - Graceful Shutdown Flow**

```
❓ QUESTION: What happens when K8s evicts a pod?

GRACEFUL TERMINATION FLOW:
1. API Server receives delete request
2. Pod status → "Terminating"
3. kubelet sends SIGTERM to container
4. Container should cleanup (close DB connections, etc)
5. Wait terminationGracePeriodSeconds (default 30s)
6. If still running → SIGKILL (force kill)
7. Pod deleted

⚠️ PROBLEMS:
- Sometimes connection draining incomplete
- In-flight requests lost
- Stateful connections broken

✅ SOLUTION: PodDisruptionBudgets + terminationGracePeriodSeconds

apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  terminationGracePeriodSeconds: 60  # Give 60s to cleanup
  containers:
  - name: app
    image: myapp:1.0
    lifecycle:
      preStop:
        exec:
          command: ["/bin/sh", "-c", "sleep 15"]  # Allow k8s to remove from service

🎯 BEST PRACTICE:
- Set terminationGracePeriodSeconds to actual drain time
- Implement graceful shutdown in app
- Use preStop hook to remove from load balancer
- Set readinessProbe to fail during shutdown
```

---

### **🔥 Q2: StatefulSet vs Deployment - When to Use Each?**

```
❓ QUESTION: Why use StatefulSet for databases?

DEPLOYMENT (Stateless):
✅ Auto-restart on failure
✅ Fast scaling
✅ Rolling updates
❌ Pods are interchangeable
❌ No persistent identity
❌ Random DNS names

Examples: API servers, web frontends, microservices

STATEFULSET (Stateful):
✅ Stable pod names (mysql-0, mysql-1, mysql-2)
✅ Persistent storage per pod
✅ Ordered deployment/scaling
✅ DNS identity (mysql-0.mysql.default.svc.cluster.local)
❌ Slower scaling
❌ More complex

Examples: Databases, message queues, distributed systems

PROBLEM: If using Deployment for DB:
- Pod gets rescheduled to different node
- Data storage doesn't follow pod
- Pod gets new DNS name
- Old connections break

SOLUTION: Use StatefulSet
- Pod keeps same name on restart
- Storage keeps same volume
- DNS name stable
- Can reference specific pod (mysql-0 as primary, mysql-1,2 as replicas)

🎯 DECISION:
- Stateless service? → Deployment
- Stateful service (DB, cache)? → StatefulSet
- Need pod ordering/identity? → StatefulSet
```

---

### **🔥 Q3: Resource Requests vs Limits - Scheduling Impact**

```
❓ QUESTION: Why does my pod stay Pending?

SCENARIO:
Deployment: replicas: 5, requests: 1 CPU each (5 CPU total)
Nodes: 2 nodes with 3 CPU each (6 CPU total available)

PROBLEM:
Scheduler algorithm:
- Reserve space for system pods
- Can't split pods across nodes
- Pod 1-3: Node 1 (3 CPU) ✅
- Pod 4-5: Need 2 CPU, but only 3 available
- Pod 5 can't fit with Pod 4 (need 2 but have 3 max per node)
- Pod 5 → PENDING

SOLUTION:
1. Add more nodes
2. Reduce per-pod requests
3. Use node affinity to spread pods

REQUESTS vs LIMITS:

requests (guaranteed):
- Minimum resource required
- Scheduler uses for bin-packing
- Pod gets evicted if cluster memory low (but others too)

limits (ceiling):
- Maximum resource allowed
- OS enforces (container process killed if exceed)
- Pod never evicted just for exceeding (only on requests)

🎯 BEST PRACTICE:
- Set requests close to actual usage (for scheduling accuracy)
- Set limits ~20-30% higher than requests (allow spikes)
- Use VPA to recommend correct values
```

---

### **🔥 Q4: Init Containers & Sidecar Pattern**

```
❓ QUESTION: How to run setup tasks before main container?

Init Containers (run before app):
- Run sequentially to completion
- If init fails → pod keeps restarting
- Use for: Setup, migrations, permission fixes

Sidecar Containers (run alongside app):
- Run in parallel with main container
- Don't block if sidecars fail (pod may still work)
- Use for: Logging, monitoring, proxies

EXAMPLE: Database migration

apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  initContainers:
  - name: db-migrate
    image: myapp-migrate:1.0
    env:
    - name: DB_HOST
      value: db.default.svc
    # Wait for database
    - name: WAIT_FOR_DB
      value: "true"
  containers:
  - name: app
    image: myapp:1.0

FLOW:
1. db-migrate runs (waits for DB, runs migrations)
2. db-migrate succeeds ✅
3. app container starts
4. App connects to database (migrations already done)

SIDECAR EXAMPLE:

apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  # Main app
  - name: app
    image: myapp:1.0
    ports:
    - containerPort: 8080
  # Logging sidecar
  - name: logging-agent
    image: filebeat:latest
    volumeMounts:
    - name: logs
      mountPath: /logs
  volumes:
  - name: logs
    emptyDir: {}

🎯 USE CASES:
Init Containers: Database migrations, secret rotation, cache warming
Sidecars: Log shipping, monitoring agent, network proxy (istio)
```

---

### **🔥 Q5: Rolling Updates vs Blue-Green vs Canary**

```
❓ QUESTION: How to deploy v2 without downtime?

ROLLING UPDATE (default):
┌──────────────────────────────┐
│ Pod 1: v1 ──→ v2             │ Kill 1 old, start 1 new (one at a time)
│ Pod 2: v1 ──→ v2             │ Eventually all v2
│ Pod 3: v1 ──→ v2             │
└──────────────────────────────┘

maxSurge: 1      # Can have 1 extra pod during update
maxUnavailable: 0  # Never have 0 pods (zero-downtime)

⚠️ PROBLEM: Old and new code running together
- Database migrations can't be done safely
- Different behavior from new version
- Harder to rollback

BLUE-GREEN DEPLOYMENT:
┌──────────────────────────────┐
│ BLUE (v1): 3 pods → v1       │ All traffic here
│           ↓                  │
│ GREEN (v2): 3 pods → v2      │ Staging, no traffic
│           ↓                  │ Once tests pass:
│ Switch traffic BLUE → GREEN  │ Instant cutover
│                              │ All traffic here (instant)
└──────────────────────────────┘

✅ ADVANTAGES:
- Instant rollback (switch back to blue)
- Test v2 with real traffic before cutover
- Zero downtime

❌ DISADVANTAGES:
- 2x resources during deployment
- Need good monitoring (to detect issues)

CANARY DEPLOYMENT:
┌──────────────────────────────┐
│ v1: 9 pods (90% traffic)     │
│ v2: 1 pod (10% traffic)      │
│      ↓ (if no errors)        │
│ v1: 6 pods (60% traffic)     │
│ v2: 4 pods (40% traffic)     │
│      ↓ (if still good)       │
│ v2: 10 pods (100% traffic)   │
└──────────────────────────────┘

✅ ADVANTAGES:
- Slow rollout (detect issues early)
- Can rollback at any point
- Gradual customer impact

IMPLEMENTATION (using Istio):

apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: app
spec:
  hosts:
  - app
  http:
  - match:
    - headers:
        user-agent:
          regex: '.*Chrome.*'
    route:
    - destination:
        host: app
        subset: v2
    weight: 10  # 10% of Chrome users get v2
  - route:
    - destination:
        host: app
        subset: v1
      weight: 100
    - destination:
        host: app
        subset: v2
      weight: 0

🎯 DECISION:
- Simple apps? → Rolling update
- Critical apps? → Blue-green (instant rollback)
- Want gradual rollout? → Canary (detect issues slowly)
```

---

### **🔥 Q6: K8s Networking Models - CNI Deep Dive**

```
❓ QUESTION: How do pods communicate if each has different IP?

K8S NETWORKING REQUIREMENTS:
1. Container-to-Container: via localhost (same pod)
2. Pod-to-Pod: via pod IP (cross-node)
3. Pod-to-Service: via service ClusterIP (DNS routing)
4. External-to-Pod: via Ingress/LoadBalancer

PROBLEM: Pod IPs are not routable across nodes!
- Node 1 pod: 10.0.1.5
- Node 2 pod: 10.0.2.3
- How to route 10.0.1.5 traffic to Node 2?

SOLUTION: CNI Plugins create overlay networks

CNI OPTIONS:

1. Flannel (simple, performance good):
   - Creates VXLAN tunnels between nodes
   - Each node gets subnet (10.0.1.0/24, 10.0.2.0/24)
   - Traffic from 10.0.1.x → tunnel → Node 1

2. Calico (advanced, security):
   - Native IP routing (no tunneling)
   - Network policies support
   - Better performance
   - BGP-based

3. Weave (encrypted):
   - Auto-mesh networking
   - Encrypted by default
   - Good for multi-cloud

KUBE-PROXY (load balancer):
- Watches services
- Creates iptables/IPVS rules
- Example:
  Service IP: 10.0.0.1:8080
  Backend pods: 10.0.1.5:8080, 10.0.2.5:8080
  iptables rule: 10.0.0.1:8080 → {10.0.1.5, 10.0.2.5} (random)

DNS (CoreDNS):
- kubernetes.default.svc.cluster.local → 10.0.0.1 (API server)
- app-service.default.svc.cluster.local → 10.0.0.100 (service IP)
- app-pod-0.app-statefulset → 10.0.1.5 (pod IP)

🎯 SUMMARY:
Pod IP → CNI plugin routes cross-node → kube-proxy load balances
```

---

### **🔥 Q7: etcd - Why Data Loss Means Cluster Death**

```
❓ QUESTION: etcd is 'just' a database, right? Why so important?

etcd STORES:
- All cluster state
- Pod definitions
- Service endpoints
- ConfigMaps, Secrets
- PersistentVolume bindings
- RBAC policies
- Everything

SCENARIO: etcd corrupted:

Before:
- API server can't read/write
- Scheduler can't assign new pods
- Controllers can't reconcile
- Cluster becomes unresponsive

WORST CASE:
- Lose pod definitions
- Don't know where volumes should be
- Don't know which pods should exist
- Cluster becomes unrecoverable!

PROTECTION STRATEGIES:

1. Backup etcd regularly:
   ETCDCTL_API=3 etcdctl --endpoints=https://k8s-master:2379 \
     --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --cert=/etc/kubernetes/pki/etcd/server.crt \
     --key=/etc/kubernetes/pki/etcd/server.key \
     snapshot save /backups/etcd-snapshot.db

2. HA setup (multi-master):
   - 3 or 5 etcd nodes
   - Raft consensus
   - Survives 1-2 node failures

3. Storage class with backup:
   - Use managed etcd (AWS EKS, GCP GKE)
   - Auto backups
   - Disaster recovery built-in

4. Monitoring & Alerting:
   - Alert on etcd disk full
   - Alert on etcd latency
   - Alert on replication lag

🎯 LESSON: etcd is critical → treat like production database
```

---

### **🔥 Q8: Cluster Autoscaling vs Pod Autoscaling - Both Needed?**

```
❓ QUESTION: If I have HPA, why do I need Cluster Autoscaler?

HPA (Horizontal Pod Autoscaler):
- Scales number of pod replicas (2 → 10 pods)
- Requires existing nodes with capacity
- If no node has space → pods stay Pending

CLUSTER AUTOSCALER:
- Scales number of nodes
- Adds nodes when pods Pending
- Removes nodes when underutilized

SCENARIO:

Initial state:
- 2 nodes (3 CPU each, fully utilized)
- 10 pods running (each needs 0.5 CPU)

Traffic spike (50% increase):
1. HPA triggers: wants to scale to 15 pods
2. Scheduler tries to assign 5 new pods
3. No nodes have space! Pods → PENDING
4. Cluster Autoscaler sees PENDING pods
5. Cluster Autoscaler adds new node
6. Scheduler assigns pending pods to new node
7. All 15 pods running ✅

WITHOUT CLUSTER AUTOSCALER:
- HPA scales, but pods stay PENDING forever
- Traffic still not handled

WITHOUT HPA (only Cluster Autoscaler):
- Traffic spike → pods Pending
- Cluster Autoscaler adds nodes
- But every spike needs new node (wastes $$)
- Can't efficiently use existing nodes

✅ BOTH NEEDED:
- HPA: Optimize pod distribution (use 1 node efficiently)
- Cluster Autoscaler: Add nodes when all full

apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 2
  maxReplicas: 50  # Max before cluster autoscaler
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

### **🔥 Q9: RBAC & Network Policies - Defense in Depth**

```
❓ QUESTION: How to prevent unauthorized access in K8s cluster?

LAYER 1 - API Server Authentication/Authorization (RBAC):

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]  # Can read, not create/delete

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: pod-reader
subjects:
- kind: User
  name: "developer@example.com"
  apiGroup: rbac.authorization.k8s.io

LAYER 2 - Network Policies (Pod-to-Pod traffic):

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}  # Apply to all pods
  policyTypes:
  - Ingress
  - Egress
  # No ingress/egress rules = deny all

---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080

LAYER 3 - Pod Security Policies:

apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
  - ALL
  runAsUser:
    rule: 'MustRunAsNonRoot'
  fsGroup:
    rule: 'RunAsAny'
  readOnlyRootFilesystem: true

🎯 DEFENSE IN DEPTH:
1. RBAC: Who can do what in API
2. Network Policies: Which pods can talk
3. Pod Security: How containers run
4. Secrets: Encrypted sensitive data
```

---

### **🔥 Q10: Observability - Logging, Metrics, Tracing**

```
❓ QUESTION: How to debug pod crashes in production?

LOGGING:

kubectl logs pod-name  # Single pod
kubectl logs pod-name -c container  # Specific container
kubectl logs -f pod-name  # Stream logs
kubectl logs pod-name --previous  # Previous container (if crashed)

PROBLEM: Logs stored locally, lost when pod dies!

SOLUTION: Centralized logging (ELK, Splunk, etc):

apiVersion: v1
kind: Pod
metadata:
  name: app-with-logging
spec:
  containers:
  - name: app
    image: myapp:1.0
    volumeMounts:
    - name: log-volume
      mountPath: /var/log
  - name: log-forwarder
    image: filebeat:latest
    volumeMounts:
    - name: log-volume
      mountPath: /var/log
    # Filebeat ships logs to Elasticsearch
  volumes:
  - name: log-volume
    emptyDir: {}

METRICS:

kubectl top nodes       # Node CPU/memory
kubectl top pods        # Pod CPU/memory

PROBLEM: Only current metrics, no history!

SOLUTION: Prometheus + Grafana:
- Scrape metrics from /metrics endpoint
- Store timeseries in Prometheus
- Visualize in Grafana
- Alert on thresholds

TRACING:

Problem: Request goes through 10 microservices
- What caused latency?
- Where did it fail?
- How to debug?

Solution: Distributed tracing (Jaeger, Zipkin):

apiVersion: v1
kind: Pod
metadata:
  name: app-with-tracing
spec:
  containers:
  - name: app
    image: myapp:1.0
    env:
    - name: JAEGER_AGENT_HOST
      value: jaeger-agent.monitoring.svc
    - name: JAEGER_AGENT_PORT
      value: "6831"

🎯 OBSERVABILITY STACK:
- Logging: Centralized log aggregation (ELK/Splunk)
- Metrics: Prometheus + Grafana
- Tracing: Jaeger for request flow
- Monitoring: Prometheus Operator + AlertManager
```

---

## **📚 Quick Reference - Common Commands**

```bash
# Cluster info
kubectl cluster-info
kubectl nodes

# Deployments
kubectl create deployment app --image=myapp:1.0
kubectl scale deployment app --replicas=5
kubectl rollout status deployment app
kubectl rollout history deployment app
kubectl rollout undo deployment app

# Pods
kubectl get pods
kubectl get pods -A (all namespaces)
kubectl describe pod pod-name
kubectl logs pod-name
kubectl exec -it pod-name /bin/bash
kubectl port-forward pod-name 8080:8080

# Services
kubectl create service clusterip app --tcp=8080:8080
kubectl get svc
kubectl describe svc app-service

# Config
kubectl create configmap app-config --from-literal=KEY=VALUE
kubectl create secret generic app-secret --from-literal=PASSWORD=secret
kubectl get configmap
kubectl get secret

# Storage
kubectl get pvc
kubectl get pv
kubectl describe pvc pvc-name

# Resources
kubectl apply -f deployment.yaml
kubectl delete -f deployment.yaml
kubectl edit deployment app
kubectl patch deployment app -p '{"spec":{"replicas":3}}'

# Debugging
kubectl describe pod pod-name
kubectl logs pod-name
kubectl get events -A --sort-by='.lastTimestamp'
kubectl debug pod-name -it --image=busybox (interactive debugging)
```

---

## **🎓 Key Takeaways**

1. **Kubernetes solves scale problems** - Container orchestration for 100s/1000s of containers
2. **Declarative, not imperative** - Describe desired state, K8s ensures it
3. **Self-healing** - Auto restarts failed pods, reschedules to healthy nodes
4. **Resource efficient** - Bin-packing, auto-scaling, multi-tenancy
5. **Observability is hard** - Logging, metrics, tracing all needed
6. **Security layers** - RBAC, network policies, pod security policies
7. **Storage is complex** - Stateless vs stateful, PVs, backup strategy
8. **Monitoring critical** - etcd, kube-apiserver, scheduler, kubelet health

---

**Happy Learning! 🚀**

> "Kubernetes is the de facto standard for container orchestration - understanding it is essential for modern DevOps and platform engineering."
