# 🔌 Q20: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa




**⚡ Quick Summary:**
> Interceptors = middleware cho request/response. Transform data, add headers, handle errors

**💡 Ghi Nhớ:**
- 📤 **Request**: Transform request trước khi gửi (add token, headers)
- 📥 **Response**: Process response/error trước khi return
- 🔄 **Chain**: Multiple interceptors chạy theo thứ tự LIFO

**Trả lời:**

**🔥 Core Concepts:**

- **Interceptors**: Middleware functions được execute trước/sau mỗi HTTP request/response
- **Request Interceptors**: Transform/modify requests trước khi gửi đến server (add headers, auth tokens, logging)
- **Response Interceptors**: Process responses hoặc handle errors trước khi return về caller
- **Execution Order**: Request interceptors chạy theo thứ tự LIFO (Last In First Out), Response interceptors chạy theo FIFO (First In First Out)
- **Chain of Responsibility Pattern**: Mỗi interceptor có thể modify data và pass sang interceptor tiếp theo

**✅ Ưu điểm:**

- **Centralized Logic**: Authentication, logging, error handling ở một nơi duy nhất
- **Code Reusability**: Không cần lặp lại logic cho mỗi request
- **Separation of Concerns**: Tách logic infrastructure ra khỏi business logic
- **Global Error Handling**: Xử lý errors thống nhất (401, 403, 500, network errors)
- **Request/Response Transformation**: Format data tự động (camelCase ↔ snake_case)
- **Performance Monitoring**: Track request timing, add metrics
- **Retry Logic**: Tự động retry failed requests với exponential backoff
- **Token Refresh**: Automatically refresh expired tokens trước khi request

**⚠️ Nhược điểm:**

- **Side Effects**: Có thể gây unexpected behaviors nếu không careful
- **Debugging Complexity**: Khó debug khi có nhiều interceptors chained
- **Performance Overhead**: Mỗi interceptor adds processing time
- **Memory Leaks**: Nếu không cleanup properly khi component unmount

**🎯 Use Cases & Hoạt Động Tối Ưu:**

**Code Example - Comprehensive Implementation:**

```typescript
import axios, {
  AxiosInstance,
  AxiosRequestConfig,
  AxiosResponse,
  AxiosError,
  InternalAxiosRequestConfig,
} from 'axios';

// ============================================
// 1. BASE CONFIGURATION - Tạo axios instance
// ============================================
const apiClient: AxiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'https://api.example.com',
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// ============================================
// 2. REQUEST INTERCEPTOR - Authentication & Logging
// ============================================
/**
 * Vietnamese Explanation:
 * - Request interceptor chạy TRƯỚC KHI request được gửi đi
 * - Thứ tự: Interceptor được add SAU CÙNG sẽ chạy TRƯỚC (LIFO)
 * - Có thể modify config: headers, params, data, timeout...
 */
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 🔐 Add Authentication Token
    const token = localStorage.getItem('accessToken');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // 📝 Add Request ID for tracking (useful for debugging)
    const requestId = `req_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    if (config.headers) {
      config.headers['X-Request-ID'] = requestId;
    }

    // ⏱️ Add timestamp for performance monitoring
    (config as any).metadata = { startTime: new Date().getTime() };

    // 📊 Logging (chỉ trong development)
    if (process.env.NODE_ENV === 'development') {
      console.log(`🚀 [${config.method?.toUpperCase()}] ${config.url}`, {
        headers: config.headers,
        params: config.params,
        data: config.data,
      });
    }

    return config;
  },
  (error: AxiosError) => {
    // Handle request error (e.g., network down before request sent)
    console.error('❌ Request Error:', error.message);
    return Promise.reject(error);
  }
);

// ============================================
// 3. RESPONSE INTERCEPTOR - Success Handling
// ============================================
/**
 * Vietnamese Explanation:
 * - Response interceptor chạy SAU KHI nhận response từ server
 * - Thứ tự: Interceptor được add TRƯỚC sẽ chạy TRƯỚC (FIFO)
 * - Có thể transform response data trước khi return về caller
 */
apiClient.interceptors.response.use(
  (response: AxiosResponse) => {
    // ⏱️ Calculate request duration
    const duration = new Date().getTime() - (response.config as any).metadata?.startTime;

    // 📊 Log response (development only)
    if (process.env.NODE_ENV === 'development') {
      console.log(`✅ [${response.config.method?.toUpperCase()}] ${response.config.url}`, {
        status: response.status,
        duration: `${duration}ms`,
        data: response.data,
      });
    }

    // 📈 Send performance metrics to monitoring service
    if (duration > 3000) {
      // Alert if request takes > 3 seconds
      console.warn(`⚠️ Slow request detected: ${response.config.url} (${duration}ms)`);
      // sendToMonitoringService({ url: response.config.url, duration });
    }

    // 🔄 Transform response data (e.g., snake_case → camelCase)
    // response.data = transformKeys(response.data, 'camelCase');

    return response;
  },
  async (error: AxiosError) => {
    // ============================================
    // ERROR HANDLING - Comprehensive error management
    // ============================================
    const originalRequest = error.config as any;

    // 📊 Log error details
    console.error('❌ Response Error:', {
      url: originalRequest?.url,
      method: originalRequest?.method,
      status: error.response?.status,
      message: error.message,
    });

    // 🔄 Case 1: RETRY LOGIC - Auto retry on network errors
    if (!error.response && originalRequest && !originalRequest._retry) {
      originalRequest._retry = true;
      originalRequest._retryCount = (originalRequest._retryCount || 0) + 1;

      if (originalRequest._retryCount <= 3) {
        // Maximum 3 retries
        console.log(`🔄 Retrying request (${originalRequest._retryCount}/3)...`);
        await new Promise((resolve) => setTimeout(resolve, 1000 * originalRequest._retryCount)); // Exponential backoff
        return apiClient(originalRequest);
      }
    }

    // 🔐 Case 2: TOKEN REFRESH - 401 Unauthorized
    if (error.response?.status === 401 && originalRequest && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        // Attempt to refresh token
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('/auth/refresh', { refreshToken });

        const { accessToken, refreshToken: newRefreshToken } = response.data;

        // Save new tokens
        localStorage.setItem('accessToken', accessToken);
        localStorage.setItem('refreshToken', newRefreshToken);

        // Retry original request with new token
        if (originalRequest.headers) {
          originalRequest.headers.Authorization = `Bearer ${accessToken}`;
        }

        console.log('🔐 Token refreshed successfully, retrying original request...');
        return apiClient(originalRequest);
      } catch (refreshError) {
        // Refresh failed → logout user
        console.error('❌ Token refresh failed, logging out...');
        localStorage.clear();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    // 🚫 Case 3: FORBIDDEN - 403 (No permission)
    if (error.response?.status === 403) {
      console.error('🚫 Access Forbidden - You do not have permission');
      // Show toast notification or redirect
      // toast.error('You do not have permission to access this resource');
    }

    // ⚠️ Case 4: NOT FOUND - 404
    if (error.response?.status === 404) {
      console.error('⚠️ Resource not found');
      // Handle 404 error (e.g., redirect to 404 page)
    }

    // 🔥 Case 5: SERVER ERROR - 500+
    if (error.response?.status && error.response.status >= 500) {
      console.error('🔥 Server Error - Please try again later');
      // Show user-friendly error message
      // toast.error('Server error occurred. Please try again later.');
    }

    // 🌐 Case 6: NETWORK ERROR - No response from server
    if (error.code === 'ECONNABORTED' || error.message.includes('timeout')) {
      console.error('⏱️ Request Timeout - Check your connection');
      // toast.error('Request timeout. Please check your internet connection.');
    }

    // Return formatted error
    return Promise.reject({
      message: error.response?.data?.message || error.message,
      status: error.response?.status,
      data: error.response?.data,
    });
  }
);

// ============================================
// 4. ADVANCED: MULTIPLE INTERCEPTORS - Execution Order
// ============================================
/**
 * Vietnamese Explanation về thứ tự execution:
 * 
 * Request Interceptors (LIFO - Last In First Out):
 * - Interceptor được add SAU CÙNG chạy TRƯỚC
 * - Example: Add interceptor 1 → Add interceptor 2 → Add interceptor 3
 * - Execution: 3 → 2 → 1 → Request sent
 * 
 * Response Interceptors (FIFO - First In First Out):
 * - Interceptor được add TRƯỚC chạy TRƯỚC
 * - Example: Add interceptor 1 → Add interceptor 2 → Add interceptor 3
 * - Execution: Response received → 1 → 2 → 3
 */

// Request Interceptor 1 (will run SECOND)
const reqInterceptor1 = apiClient.interceptors.request.use(
  (config) => {
    console.log('Request Interceptor 1 - Add default headers');
    config.headers['X-Custom-Header'] = 'value1';
    return config;
  }
);

// Request Interceptor 2 (will run FIRST - added last)
const reqInterceptor2 = apiClient.interceptors.request.use(
  (config) => {
    console.log('Request Interceptor 2 - Add timestamp');
    config.headers['X-Timestamp'] = Date.now().toString();
    return config;
  }
);

// Response Interceptor 1 (will run FIRST)
const resInterceptor1 = apiClient.interceptors.response.use(
  (response) => {
    console.log('Response Interceptor 1 - Transform data');
    return response;
  }
);

// Response Interceptor 2 (will run SECOND)
const resInterceptor2 = apiClient.interceptors.response.use(
  (response) => {
    console.log('Response Interceptor 2 - Cache response');
    return response;
  }
);

// ============================================
// 5. CLEANUP - Remove interceptors when needed
// ============================================
/**
 * Vietnamese Explanation:
 * - Quan trọng: PHẢI remove interceptors khi component unmount
 * - Tránh memory leaks và duplicate interceptors
 * - Use trong useEffect cleanup hoặc componentWillUnmount
 */
export const cleanupInterceptors = () => {
  apiClient.interceptors.request.eject(reqInterceptor1);
  apiClient.interceptors.request.eject(reqInterceptor2);
  apiClient.interceptors.response.eject(resInterceptor1);
  apiClient.interceptors.response.eject(resInterceptor2);
};

// ============================================
// 6. ADVANCED USE CASE: Request Queuing & Throttling
// ============================================
/**
 * Vietnamese Explanation:
 * - Giới hạn số lượng concurrent requests
 * - Prevent overwhelming server với too many requests cùng lúc
 * - Useful cho rate-limited APIs
 */
class RequestQueue {
  private queue: Array<() => Promise<any>> = [];
  private activeRequests = 0;
  private maxConcurrent = 5; // Maximum 5 concurrent requests

  async add<T>(requestFn: () => Promise<T>): Promise<T> {
    // Nếu đã đạt max concurrent, đợi trong queue
    if (this.activeRequests >= this.maxConcurrent) {
      await new Promise<void>((resolve) => {
        this.queue.push(() => {
          resolve();
          return Promise.resolve();
        });
      });
    }

    this.activeRequests++;

    try {
      const result = await requestFn();
      return result;
    } finally {
      this.activeRequests--;

      // Process next request in queue
      const nextRequest = this.queue.shift();
      if (nextRequest) {
        nextRequest();
      }
    }
  }
}

const requestQueue = new RequestQueue();

// Add queuing interceptor
apiClient.interceptors.request.use(
  async (config) => {
    await requestQueue.add(() => Promise.resolve());
    return config;
  }
);

// ============================================
// 7. ADVANCED: Request Deduplication
// ============================================
/**
 * Vietnamese Explanation:
 * - Ngăn chặn duplicate requests (cùng URL + method + params)
 * - Nếu có request đang pending, return kết quả của request đó
 * - Useful khi user click nhiều lần hoặc component re-render
 */
const pendingRequests = new Map<string, Promise<any>>();

apiClient.interceptors.request.use(
  (config) => {
    // Create unique key for this request
    const requestKey = `${config.method}:${config.url}:${JSON.stringify(config.params)}`;

    // Nếu đã có request pending với key này
    if (pendingRequests.has(requestKey)) {
      console.log('🔄 Duplicate request detected, using pending request...');
      // Return pending promise (sẽ reject này để reuse pending request)
      throw {
        __DUPLICATE__: true,
        promise: pendingRequests.get(requestKey),
      };
    }

    // Store request key in config for later cleanup
    (config as any).__requestKey = requestKey;

    return config;
  },
  (error) => {
    // Nếu là duplicate request, return pending promise
    if (error.__DUPLICATE__) {
      return error.promise;
    }
    return Promise.reject(error);
  }
);

apiClient.interceptors.response.use(
  (response) => {
    // Remove from pending requests
    const requestKey = (response.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey);
    }
    return response;
  },
  (error) => {
    // Remove from pending requests even on error
    const requestKey = (error.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey);
    }
    return Promise.reject(error);
  }
);

// ============================================
// 8. USAGE EXAMPLES
// ============================================
export const exampleUsage = async () => {
  try {
    // Tất cả requests sẽ tự động có:
    // - Auth token header
    // - Request ID
    // - Performance monitoring
    // - Error handling
    // - Auto retry on network errors
    // - Token refresh on 401
    const response = await apiClient.get('/users');
    console.log('Users:', response.data);

    const user = await apiClient.post('/users', {
      name: 'John Doe',
      email: 'john@example.com',
    });
    console.log('Created user:', user.data);
  } catch (error) {
    console.error('Error:', error);
  }
};

// ============================================
// 9. REACT HOOK INTEGRATION
// ============================================
/**
 * Vietnamese Explanation:
 * - Integrate interceptors với React lifecycle
 * - Cleanup khi component unmount
 */
import { useEffect } from 'react';

export const useAxiosInterceptors = () => {
  useEffect(() => {
    // Setup interceptors
    const requestInterceptor = apiClient.interceptors.request.use(
      (config) => {
        // Add logic here
        return config;
      }
    );

    const responseInterceptor = apiClient.interceptors.response.use(
      (response) => {
        // Add logic here
        return response;
      }
    );

    // Cleanup function
    return () => {
      apiClient.interceptors.request.eject(requestInterceptor);
      apiClient.interceptors.response.eject(responseInterceptor);
    };
  }, []); // Empty dependency array = run once on mount
};
```

**🎯 Best Practices - Tối Ưu Hóa:**

1. **Always Cleanup Interceptors**: Eject interceptors khi component unmount để tránh memory leaks
2. **Use Separate Axios Instances**: Tạo riêng instance cho từng API (auth API, data API, analytics API)
3. **Avoid Heavy Computation**: Interceptors should be fast, avoid blocking operations
4. **Proper Error Handling**: Always return Promise.reject() trong error handler
5. **Token Refresh Strategy**: Implement queue cho multiple requests khi token expired
6. **Development vs Production**: Use different logging levels (verbose in dev, minimal in prod)
7. **Request/Response Transformation**: Centralize data transformation logic (camelCase ↔ snake_case)
8. **Performance Monitoring**: Track slow requests and send metrics to monitoring service
9. **Request Deduplication**: Prevent duplicate identical requests
10. **Rate Limiting**: Implement request queuing to respect API rate limits
11. **Retry Strategy**: Use exponential backoff for failed requests
12. **Timeout Configuration**: Set appropriate timeouts based on endpoint type

**⚠️ Common Mistakes - Lỗi Thường Gặp:**

```typescript
// ❌ Sai: Không cleanup interceptors
useEffect(() => {
  axios.interceptors.request.use(config => config);
  // Missing cleanup!
}, []);

// ✅ Đúng: Always cleanup
useEffect(() => {
  const interceptor = axios.interceptors.request.use(config => config);
  return () => axios.interceptors.request.eject(interceptor);
}, []);

// ❌ Sai: Forget to return config/response
axios.interceptors.request.use(config => {
  config.headers.Authorization = 'Bearer token';
  // Forgot to return config!
});

// ✅ Đúng: Always return
axios.interceptors.request.use(config => {
  config.headers.Authorization = 'Bearer token';
  return config;
});

// ❌ Sai: Infinite loop trong token refresh
axios.interceptors.response.use(
  res => res,
  async (error) => {
    if (error.response?.status === 401) {
      await axios.post('/auth/refresh'); // Uses same instance → infinite loop!
      return axios(error.config);
    }
  }
);

// ✅ Đúng: Use separate instance for refresh
const refreshClient = axios.create();
axios.interceptors.response.use(
  res => res,
  async (error) => {
    if (error.response?.status === 401 && !error.config._retry) {
      error.config._retry = true;
      await refreshClient.post('/auth/refresh');
      return axios(error.config);
    }
  }
);
```

**📊 Performance Considerations:**

- **Interceptor Overhead**: Mỗi interceptor adds ~0.1-1ms processing time
- **Memory Usage**: Pending requests map cần cleanup để avoid memory leaks
- **Request Queueing**: Limit concurrent requests to 5-10 tùy server capacity
- **Token Refresh**: Queue all requests khi refreshing để avoid multiple refresh calls
- **Caching**: Cache GET requests trong interceptors để reduce server load

## **PHẦN 2: Axios - Core Features & Advanced Patterns**

### **1. Axios Basics & Comparison**

```typescript
// ═══════════════════════════════════════════════════════════
// BASIC USAGE
// ═══════════════════════════════════════════════════════════

import axios from 'axios';

// GET, POST, PUT, DELETE
const { data } = await axios.get('/api/users');
await axios.post('/api/users', userData); // ✅ Auto JSON stringify
await axios.put(`/api/users/${id}`, updates);
await axios.delete(`/api/users/${id}`);

// ═══════════════════════════════════════════════════════════
// AXIOS vs FETCH - So sánh
// ═══════════════════════════════════════════════════════════

// ❌ Fetch: Manual JSON parse + error checking
const response = await fetch('/api/users');
if (!response.ok) throw new Error('Failed');
const data = await response.json();

// ✅ Axios: Automatic
const { data } = await axios.get('/api/users');
// Auto parse JSON, auto throw error nếu status >= 400

/**
 * Axios Advantages:
 * ✅ Auto JSON transform (request & response)
 * ✅ Auto error handling (throw on 4xx, 5xx)
 * ✅ Built-in timeout, interceptors, CSRF protection
 * ✅ Request/response transformation
 * ✅ Progress events, request cancellation
 * 
 * Fetch Advantages:
 * ✅ Native browser API (no dependencies)
 * ✅ Smaller bundle size
 */
```

---

### **2. Configuration & Instances**

```typescript
// ═══════════════════════════════════════════════════════════
// CREATE AXIOS INSTANCE - Best Practice
// ═══════════════════════════════════════════════════════════

const apiClient = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true, // CSRF cookies
});

// Multiple instances cho different APIs
const authAPI = axios.create({ baseURL: 'https://auth.example.com' });
const uploadAPI = axios.create({ 
  baseURL: 'https://upload.example.com',
  timeout: 60000, // Large files
});

// ═══════════════════════════════════════════════════════════
// FULL CONFIG OPTIONS (common ones)
// ═══════════════════════════════════════════════════════════

await axios({
  url: '/users',
  method: 'get',
  headers: { Authorization: 'Bearer token' },
  params: { page: 1, limit: 10 }, // Query string
  data: { name: 'John' }, // Request body
  timeout: 5000,
  responseType: 'json', // 'blob' | 'arraybuffer' | 'text'
  onUploadProgress: (e) => console.log(`${(e.loaded / e.total!) * 100}%`),
  onDownloadProgress: (e) => console.log(`${(e.loaded / e.total!) * 100}%`),
});
```

---

### **3. Request Cancellation**

```typescript
// ═══════════════════════════════════════════════════════════
// ABORT CONTROLLER (Modern)
// ═══════════════════════════════════════════════════════════

const controller = new AbortController();

axios.get('/api/users', { signal: controller.signal })
  .catch(error => {
    if (axios.isCancel(error)) {
      console.log('Request canceled');
    }
  });

controller.abort(); // Cancel request

// ═══════════════════════════════════════════════════════════
// USE CASE: Cancel on unmount (React)
// ═══════════════════════════════════════════════════════════

useEffect(() => {
  const controller = new AbortController();
  
  axios.get('/api/users', { signal: controller.signal })
    .then(({ data }) => setUsers(data))
    .catch(error => !axios.isCancel(error) && console.error(error));
  
  return () => controller.abort(); // Cleanup
}, []);
```

---

### **4. File Upload & Download**

```typescript
// ═══════════════════════════════════════════════════════════
// UPLOAD với Progress
// ═══════════════════════════════════════════════════════════

const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);
  
  const { data } = await axios.post('/api/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    onUploadProgress: (e) => {
      const percent = Math.round((e.loaded * 100) / e.total!);
      console.log(`Upload: ${percent}%`);
    },
  });
  
  return data;
};

// ═══════════════════════════════════════════════════════════
// DOWNLOAD File
// ═══════════════════════════════════════════════════════════

const downloadFile = async (fileId: string) => {
  const response = await axios.get(`/api/files/${fileId}`, {
    responseType: 'blob', // Important!
  });
  
  // Trigger download
  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.download = 'filename.pdf';
  link.click();
  window.URL.revokeObjectURL(url);
};
```

---

### **5. Error Handling**

```typescript
// ═══════════════════════════════════════════════════════════
// TYPE-SAFE ERROR HANDLING
// ═══════════════════════════════════════════════════════════

try {
  const response = await axios.get('/api/users');
} catch (error) {
  if (axios.isAxiosError(error)) {
    if (error.response) {
      // Server responded với error status
      const { status, data } = error.response;
      
      switch (status) {
        case 400: console.error('Bad Request'); break;
        case 401: window.location.href = '/login'; break;
        case 403: console.error('Forbidden'); break;
        case 404: console.error('Not Found'); break;
        case 422: console.error('Validation:', data.errors); break;
        case 500: console.error('Server Error'); break;
      }
      
    } else if (error.request) {
      // Request sent nhưng no response (network error, timeout)
      console.error('Network error or timeout');
      
    } else {
      // Error setting up request
      console.error('Request setup error:', error.message);
    }
  }
}

// ═══════════════════════════════════════════════════════════
// CUSTOM ERROR HANDLER
// ═══════════════════════════════════════════════════════════

const handleError = (error: unknown) => {
  if (axios.isAxiosError(error)) {
    return {
      success: false,
      message: error.response?.data?.message || error.message,
      status: error.response?.status,
      errors: error.response?.data?.errors, // Validation errors
    };
  }
  return { success: false, message: 'Unexpected error' };
};
```

---

### **6. Advanced Patterns**

```typescript
// ═══════════════════════════════════════════════════════════
// RETRY LOGIC với Exponential Backoff
// ═══════════════════════════════════════════════════════════

const axiosRetry = async (config: any, retries = 3) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await axios(config);
    } catch (error) {
      if (i === retries - 1) throw error;
      await new Promise(r => setTimeout(r, 1000 * Math.pow(2, i))); // 1s, 2s, 4s
    }
  }
};

// ═══════════════════════════════════════════════════════════
// REQUEST DEDUPLICATION
// ═══════════════════════════════════════════════════════════

const pending = new Map<string, Promise<any>>();

const dedupeRequest = async (config: any) => {
  const key = `${config.method}:${config.url}`;
  
  if (pending.has(key)) return pending.get(key); // Reuse pending
  
  const promise = axios(config).finally(() => pending.delete(key));
  pending.set(key, promise);
  return promise;
};

// ═══════════════════════════════════════════════════════════
// RESPONSE CACHING
// ═══════════════════════════════════════════════════════════

const cache = new Map<string, { data: any; timestamp: number }>();

const cachedRequest = async (url: string, ttl = 5 * 60 * 1000) => {
  const cached = cache.get(url);
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data; // Return cached
  }
  
  const { data } = await axios.get(url);
  cache.set(url, { data, timestamp: Date.now() });
  return data;
};
```

---

### **💡 Best Practices**

```typescript
// ✅ 1. Dùng instance thay vì default axios
const api = axios.create({ baseURL: '/api' });

// ✅ 2. TypeScript types
interface User { id: string; name: string; }
const getUser = async (id: string): Promise<User> => {
  const { data } = await api.get<User>(`/users/${id}`);
  return data;
};

// ✅ 3. Centralize error handling trong interceptors
api.interceptors.response.use(
  response => response,
  error => {
    handleError(error);
    return Promise.reject(error);
  }
);

// ✅ 4. Cancel requests on unmount
useEffect(() => {
  const controller = new AbortController();
  // ... fetch data với signal
  return () => controller.abort();
}, []);

// ✅ 5. Set timeout để tránh hung requests
axios.create({ timeout: 10000 });

// ✅ 6. Separate auth instance (tránh infinite loop trong token refresh)
const authAPI = axios.create({ baseURL: '/auth' });
```

---






---

# 🌐 **Mindmap: Axios Interceptors (Chuẩn Senior)**

```
                    AXIOS INTERCEPTORS
                           │
 ┌─────────────────────────┴──────────────────────────┐
 │                                                    │
 │                                                    │
 Request Interceptor                           Response Interceptor
 (Chạy trước request)                           (Chạy trước return)
 │                                                    │
 │                                                    │
- Add Token (Auth)                               - Transform response
- Add headers                                    - Global error handling
- Logging                                        - Retry logic
- Add request ID                                 - Token refresh (401)
- Modify params/data                             - Redirect login
- Throttle / queue requests                      - Format API error
- Start timer (measure duration)                 - Detect slow API
 │                                                    │
 │                                                    │
 LIFO (Last In First Out)                        FIFO (First In First Out)
```

---

## 🔥 **1. Request Interceptor – Những gì thường làm**

```
Request Interceptor:
   ├── Add Authorization Token
   ├── Add X-Request-ID
   ├── Start performance timer
   ├── Add Content-Type
   ├── Logging (dev only)
   ├── Dedupe request
   ├── Queue requests (max concurrent)
   └── Transform camelCase → snake_case
```

---

## 🔥 **2. Response Interceptor – Những gì thường làm**

```
Response Interceptor:
   ├── Transform response.data
   ├── Remove pending request from dedupe map
   ├── Check slow API (duration > 3s)
   ├── Global error handling:
   │       ├── 400 Validation
   │       ├── 401 Refresh token
   │       ├── 403 Forbidden
   │       ├── 404 Not Found
   │       └── 500 Server error
   ├── Retry logic (network error)
   ├── Auto redirect login
   └── camelCase response
```

---

# ⚡ **3. Token Refresh – Mindmap**

```
Token Refresh Flow:
  1. Call API → 401?
  2. Check _retry flag
  3. Pause all requests (queue)
  4. Call /refresh-token
  5. If success:
       - Update accessToken
       - Retry all queued requests
  6. If fail:
       - logout()
       - redirect("/login")
```

---

# ⚙️ **4. Execution Order – Mindmap**

```
Request:
   Add R1
   Add R2
   Add R3
 → Execution: R3 → R2 → R1

Response:
   Add S1
   Add S2
   Add S3
 → Execution: S1 → S2 → S3
```

---

# 🛑 **5. Cleanup (React) – Mindmap**

```
useEffect:
  ├── Setup request interceptor → idReq
  ├── Setup response interceptor → idRes
  └── Cleanup:
         eject(idReq)
         eject(idRes)
```

---

# 🧠 **6. Best Practices – Mindmap**

```
Best Practices:
  ├── Always eject interceptors (React cleanup)
  ├── Use Axios instances (avoid global)
  ├── Use separate instance for refresh token
  ├── Centralize error handling
  ├── Use request dedupe for spam click
  ├── Use retry with exponential backoff
  ├── Add request timing
  ├── Don't modify config deeply (avoid side effects)
  └── Avoid heavy logic inside interceptors
```
