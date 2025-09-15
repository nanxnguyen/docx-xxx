# 🔍 ELK Stack Integration Guide

## Overview
Hướng dẫn tích hợp **ELK Stack** (Elasticsearch + Logstash + Kibana) để trace logs và debug lỗi cho ứng dụng NestJS.

## ⚡ Quick Start

### 1. Start ELK Stack
```bash
# Start ELK services
./elk.sh start

# Or manually
docker-compose -f docker-compose.elk.yml up -d
```

### 2. Start NestJS Application
```bash
npm run start:dev
```

### 3. Access Services
- **🚀 App**: http://localhost:3000
- **📊 Kibana**: http://localhost:5601
- **🔍 Elasticsearch**: http://localhost:9200
- **🔄 Logstash**: http://localhost:9600

## 📋 Setup Kibana Index Pattern

1. **Open Kibana**: http://localhost:5601
2. **Go to**: Stack Management > Index Patterns
3. **Create Pattern**: `learn-i-like-logs-*`
4. **Time Field**: `@timestamp`
5. **Save Pattern**

## 🧪 Test Logging

### Demo Endpoints
```bash
# Info log
curl http://localhost:3000/api/v1/common/logs/info

# Warning log  
curl http://localhost:3000/api/v1/common/logs/warning

# Error log
curl http://localhost:3000/api/v1/common/logs/error

# Business logic with random errors
curl -X POST http://localhost:3000/api/v1/common/logs/order/ORD123
```

## 📁 Log Files Structure

```
logs/
├── application-2025-09-04.log    # All application logs
├── error-2025-09-04.log          # Error logs only
├── exceptions.log                # Unhandled exceptions
└── rejections.log                # Promise rejections
```

## 🔍 Kibana Dashboard Features

### 1. **Discover Logs**
- View real-time logs
- Filter by log level: `level:error`
- Search by context: `context:CategoryService`
- Time-based filtering

### 2. **Create Visualizations**
- Error rate over time
- Log level distribution
- Service performance metrics

### 3. **Build Dashboards**
- System health overview
- Error tracking
- Performance monitoring

## 🛠️ Log Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| `error` | System errors, exceptions | Production issues |
| `warn` | Warning conditions | Potential problems |
| `info` | General information | Business events |
| `debug` | Debug information | Development |
| `verbose` | Detailed tracing | Deep debugging |

## 📊 Sample Kibana Queries

### Find Errors
```
level:error
```

### Filter by Service
```
context:KafkaService AND level:error
```

### Time Range Errors
```
level:error AND @timestamp:[now-1h TO now]
```

### Database Errors
```
message:*database* AND level:error
```

## 🔧 Configuration

### Environment Variables
```bash
# Log level (development)
LOG_LEVEL=debug

# Production
LOG_LEVEL=info
```

### Winston Configuration
- **Daily Rotation**: Auto-rotate log files
- **JSON Format**: Structured logging for ELK
- **Error Separation**: Separate error logs
- **Compression**: Gzip old log files

## 🚨 Production Tips

1. **Log Retention**: Set appropriate retention policies
2. **Index Management**: Use ILM (Index Lifecycle Management)
3. **Security**: Enable authentication in production
4. **Monitoring**: Set up alerts for error spikes
5. **Performance**: Monitor Elasticsearch resource usage

## 📈 Monitoring Checklist

- [ ] Application error rates
- [ ] Response time trends
- [ ] Database connection issues
- [ ] Kafka message failures
- [ ] Memory/CPU usage patterns
- [ ] API endpoint performance

## 🔄 Commands Reference

```bash
# ELK Management
./elk.sh start          # Start ELK Stack
./elk.sh stop           # Stop ELK Stack
./elk.sh restart        # Restart ELK Stack
./elk.sh status         # Check status
./elk.sh logs           # View logs
./elk.sh kibana         # Open Kibana
./elk.sh setup          # Setup Kibana
./elk.sh clean          # Remove all data

# Application
npm run start:dev       # Start with logging
npm run build          # Build for production
```

## 🐛 Troubleshooting

### Common Issues

1. **Elasticsearch won't start**
   ```bash
   # Check memory
   docker logs learn-i-like-elasticsearch
   # Increase Docker memory to 4GB+
   ```

2. **No logs in Kibana**
   ```bash
   # Check Logstash
   docker logs learn-i-like-logstash
   # Verify log files exist
   ls -la logs/
   ```

3. **Index pattern not found**
   - Generate some logs first
   - Wait 30 seconds for indexing
   - Refresh Kibana

### Log Verification
```bash
# Check if logs are being written
tail -f logs/application-*.log

# Check Elasticsearch indices
curl http://localhost:9200/_cat/indices

# Check Logstash pipeline
curl http://localhost:9600/_node/stats/pipeline
```

## 🎯 Next Steps

1. **Set up Alerts**: Configure Watcher for error thresholds
2. **Custom Dashboards**: Create business-specific dashboards  
3. **Log Parsing**: Add custom log patterns
4. **APM Integration**: Add Application Performance Monitoring
5. **Security**: Enable authentication and SSL

---

🔍 **Happy Debugging!** Your logs are now centralized and searchable in Kibana!
