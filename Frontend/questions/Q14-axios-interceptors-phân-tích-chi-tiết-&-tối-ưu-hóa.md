# 🔌 Q14: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Interceptors là middleware functions chạy trước/sau mỗi request/response, giúp centralize authentication, error handling, logging, và data transformation."**

**🔑 4 Use Cases Chính:**

**1. Authentication & Token Management:**

- Request interceptor: **auto-add JWT token** vào headers
- Response interceptor: **auto-refresh expired tokens** (401 → refresh → retry)
- Pattern: Lưu refresh token, khi 401 → call refresh API → update token → retry failed request

**2. Global Error Handling:**

- **Centralized error processing** - không cần try/catch mọi nơi
- Handle network errors, timeouts, 401/403/500 uniformly
- Show toast notifications, log errors, redirect login

**3. Request/Response Transformation:**

- **Auto format** data: camelCase ↔ snake_case, date strings ↔ Date objects
- Add common headers: `Content-Type`, `Accept-Language`, device info
- Strip sensitive data trước khi log

**4. Performance Monitoring & Retry:**

- Track request **timing** (start time → duration)
- **Exponential backoff retry** cho failed requests
- Circuit breaker pattern (dừng requests sau N failures)

**⚠️ Lỗi Thường Gặp:**

- Không cleanup interceptor khi component unmount → **memory leak**
- Modify request config trực tiếp mà không clone → side effects
- Infinite loop khi retry logic không có **max attempts**
- Token refresh race condition (multiple 401s cùng lúc) → queue requests

**💡 Kiến Thức Senior:**

- **Execution order**: Request interceptors = **LIFO** (last added runs first), Response = **FIFO**
- Interceptor return Promise → có thể **async/await** bên trong
- Eject interceptor: `const id = axios.interceptors.request.use(...); axios.interceptors.request.eject(id)`
- Best practice: Tạo **separate axios instances** cho từng service (auth API, data API) với different interceptors

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
  baseURL: process.env.REACT_APP_API_URL || 'https://api.example.com', // 🌐 Base URL cho tất cả requests
  timeout: 10000, // ⏱️ 10 seconds timeout - Hủy request nếu quá 10s
  headers: {
    'Content-Type': 'application/json', // 📝 Default header cho JSON requests
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
    // 🔐 Add Authentication Token (Thêm token xác thực)
    const token = localStorage.getItem('accessToken'); // 📦 Lấy token từ localStorage
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`; // 🎫 Gắn token vào header
    }

    // 📝 Add Request ID for tracking (Thêm ID để tracking - hữu ích cho debugging)
    const requestId = `req_${Date.now()}_${Math.random()
      .toString(36)
      .substr(2, 9)}`; // 🎲 Tạo unique ID
    if (config.headers) {
      config.headers['X-Request-ID'] = requestId; // 🏷️ Gắn request ID vào header
    }

    // ⏱️ Add timestamp for performance monitoring (Thêm thời gian bắt đầu để đo performance)
    (config as any).metadata = { startTime: new Date().getTime() }; // ⏰ Lưu thời điểm bắt đầu

    // 📊 Logging (chỉ trong development - Chỉ log khi đang dev)
    if (process.env.NODE_ENV === 'development') {
      console.log(`🚀 [${config.method?.toUpperCase()}] ${config.url}`, {
        // 📡 Log request details
        headers: config.headers, // 📋 Headers
        params: config.params, // 🔍 Query params
        data: config.data, // 📦 Request body
      });
    }

    return config; // ✅ Trả về config đã modify
  },
  (error: AxiosError) => {
    // ❌ Handle request error (Xử lý lỗi request - VD: mạng đứt trước khi gửi)
    console.error('❌ Request Error:', error.message);
    return Promise.reject(error); // 🚫 Reject promise
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
    // ⏱️ Calculate request duration (Tính thời gian request)
    const duration =
      new Date().getTime() - (response.config as any).metadata?.startTime; // 📊 Thời gian = hiện tại - bắt đầu

    // 📊 Log response (development only - Chỉ log khi dev)
    if (process.env.NODE_ENV === 'development') {
      console.log(
        `✅ [${response.config.method?.toUpperCase()}] ${response.config.url}`,
        {
          status: response.status, // 🔢 HTTP status code
          duration: `${duration}ms`, // ⏱️ Thời gian request (ms)
          data: response.data, // 📦 Response data
        }
      );
    }

    // 📈 Send performance metrics to monitoring service (Gửi metrics nếu request chậm)
    if (duration > 3000) {
      // ⚠️ Nếu request > 3 giây
      // Alert if request takes > 3 seconds
      console.warn(
        `⚠️ Slow request detected: ${response.config.url} (${duration}ms)`
      );
      // sendToMonitoringService({ url: response.config.url, duration });  // 📡 Gửi lên monitoring service
    }

    // 🔄 Transform response data (e.g., snake_case → camelCase - Chuyển đổi format data)
    // response.data = transformKeys(response.data, 'camelCase');  // 🔤 VD: user_name → userName

    return response; // ✅ Trả về response
  },
  async (error: AxiosError) => {
    // ============================================
    // ERROR HANDLING - Comprehensive error management
    // ============================================
    const originalRequest = error.config as any;

    // 📊 Log error details (Ghi log chi tiết lỗi)
    console.error('❌ Response Error:', {
      url: originalRequest?.url, // 🌐 URL gặp lỗi
      method: originalRequest?.method, // 🔧 HTTP method (GET/POST/...)
      status: error.response?.status, // 🔢 Status code (401/403/500/...)
      message: error.message, // 📝 Error message
    });

    // 🔄 Case 1: RETRY LOGIC - Auto retry on network errors (Tự động thử lại khi lỗi mạng)
    if (!error.response && originalRequest && !originalRequest._retry) {
      // ⚠️ Không có response = lỗi mạng
      originalRequest._retry = true; // 🏷️ Đánh dấu đã retry
      originalRequest._retryCount = (originalRequest._retryCount || 0) + 1; // ➕ Tăng số lần retry

      if (originalRequest._retryCount <= 3) {
        // 3️⃣ Maximum 3 lần retry
        console.log(
          `🔄 Retrying request (${originalRequest._retryCount}/3)...`
        );
        await new Promise((resolve) =>
          setTimeout(resolve, 1000 * originalRequest._retryCount)
        ); // ⏱️ Exponential backoff: 1s, 2s, 3s
        return apiClient(originalRequest); // 🔁 Thử lại request
      }
    }

    // 🔐 Case 2: TOKEN REFRESH - 401 Unauthorized (Làm mới token khi hết hạn)
    if (
      error.response?.status === 401 &&
      originalRequest &&
      !originalRequest._retry
    ) {
      // 🔒 401 = Token hết hạn
      originalRequest._retry = true; // 🏷️ Đánh dấu đã refresh (tránh infinite loop)

      try {
        // 🔄 Attempt to refresh token (Thử làm mới token)
        const refreshToken = localStorage.getItem('refreshToken'); // 📦 Lấy refresh token
        const response = await axios.post('/auth/refresh', { refreshToken }); // 📡 Gọi API refresh

        const { accessToken, refreshToken: newRefreshToken } = response.data; // 🎫 Nhận tokens mới

        // 💾 Save new tokens (Lưu tokens mới)
        localStorage.setItem('accessToken', accessToken); // 💾 Lưu access token mới
        localStorage.setItem('refreshToken', newRefreshToken); // 💾 Lưu refresh token mới

        // 🔁 Retry original request with new token (Thử lại request với token mới)
        if (originalRequest.headers) {
          originalRequest.headers.Authorization = `Bearer ${accessToken}`; // 🎫 Gắn token mới vào header
        }

        console.log(
          '🔐 Token refreshed successfully, retrying original request...'
        );
        return apiClient(originalRequest); // ✅ Thử lại request ban đầu
      } catch (refreshError) {
        // ❌ Refresh failed → logout user (Refresh thất bại → đăng xuất)
        console.error('❌ Token refresh failed, logging out...');
        localStorage.clear(); // 🗑️ Xóa hết localStorage
        window.location.href = '/login'; // ↩️ Redirect về trang login
        return Promise.reject(refreshError);
      }
    }

    // 🚫 Case 3: FORBIDDEN - 403 (No permission - Không có quyền)
    if (error.response?.status === 403) {
      // 🔒 403 = Không có quyền truy cập
      console.error('🚫 Access Forbidden - You do not have permission');
      // 🔔 Show toast notification or redirect (Hiển thị thông báo hoặc redirect)
      // toast.error('You do not have permission to access this resource');
    }

    // ⚠️ Case 4: NOT FOUND - 404 (Không tìm thấy tài nguyên)
    if (error.response?.status === 404) {
      // 🔍 404 = URL không tồn tại
      console.error('⚠️ Resource not found');
      // 🎯 Handle 404 error (Xử lý lỗi 404 - VD: redirect to 404 page)
    }

    // 🔥 Case 5: SERVER ERROR - 500+ (Lỗi server nội bộ)
    if (error.response?.status && error.response.status >= 500) {
      // 💥 500+ = Lỗi server
      console.error('🔥 Server Error - Please try again later');
      // 🔔 Show user-friendly error message (Hiển thị thông báo thân thiện)
      // toast.error('Server error occurred. Please try again later.');
    }

    // 🌐 Case 6: NETWORK ERROR - No response from server (Lỗi mạng)
    if (error.code === 'ECONNABORTED' || error.message.includes('timeout')) {
      // ⏱️ Timeout hoặc mất kết nối
      console.error('⏱️ Request Timeout - Check your connection');
      // 📶 toast.error('Request timeout. Please check your internet connection.');
    }

    // 📦 Return formatted error (Trả về lỗi đã format)
    return Promise.reject({
      message: error.response?.data?.message || error.message, // 📝 Error message
      status: error.response?.status, // 🔢 Status code
      data: error.response?.data, // 📦 Error data (VD: validation errors)
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

// 📊 Request Interceptor 1 (will run SECOND - sẽ chạy thứ 2)
const reqInterceptor1 = apiClient.interceptors.request.use((config) => {
  console.log('Request Interceptor 1 - Add default headers'); // 📋 Thêm default headers
  config.headers['X-Custom-Header'] = 'value1'; // 🏷️ Custom header
  return config;
});

// 1️⃣ Request Interceptor 2 (will run FIRST - added last - sẽ chạy đầu tiên vì được add cuối)
const reqInterceptor2 = apiClient.interceptors.request.use((config) => {
  console.log('Request Interceptor 2 - Add timestamp'); // ⏱️ Thêm timestamp
  config.headers['X-Timestamp'] = Date.now().toString(); // ⏰ Unix timestamp
  return config;
});

// 📊 Response Interceptor 1 (will run FIRST - sẽ chạy đầu tiên)
const resInterceptor1 = apiClient.interceptors.response.use((response) => {
  console.log('Response Interceptor 1 - Transform data'); // 🔄 Transform data
  return response;
});

// 2️⃣ Response Interceptor 2 (will run SECOND - sẽ chạy thứ 2)
const resInterceptor2 = apiClient.interceptors.response.use((response) => {
  console.log('Response Interceptor 2 - Cache response'); // 💾 Cache response
  return response;
});

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
  apiClient.interceptors.request.eject(reqInterceptor1); // 🗑️ Xóa request interceptor 1
  apiClient.interceptors.request.eject(reqInterceptor2); // 🗑️ Xóa request interceptor 2
  apiClient.interceptors.response.eject(resInterceptor1); // 🗑️ Xóa response interceptor 1
  apiClient.interceptors.response.eject(resInterceptor2); // 🗑️ Xóa response interceptor 2
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
  private queue: Array<() => Promise<any>> = []; // 📊 Hàng đợi chứa các requests
  private activeRequests = 0; // 📊 Số requests đang chạy
  private maxConcurrent = 5; // 5️⃣ Maximum 5 concurrent requests - Tối đa 5 requests cùng lúc

  async add<T>(requestFn: () => Promise<T>): Promise<T> {
    // ⚠️ Nếu đã đạt max concurrent, đợi trong queue (Chờ đến lượt)
    if (this.activeRequests >= this.maxConcurrent) {
      await new Promise<void>((resolve) => {
        this.queue.push(() => {
          // 📥 Thêm vào hàng đợi
          resolve();
          return Promise.resolve();
        });
      });
    }

    this.activeRequests++; // ➡️ Tăng số requests đang chạy

    try {
      const result = await requestFn(); // ▶️ Thực thi request
      return result;
    } finally {
      this.activeRequests--; // ⬇️ Giảm số requests đang chạy

      // 🔁 Process next request in queue (Xử lý request tiếp theo trong hàng đợi)
      const nextRequest = this.queue.shift(); // 📤 Lấy request đầu hàng đợi
      if (nextRequest) {
        nextRequest(); // ▶️ Chạy request tiếp theo
      }
    }
  }
}

const requestQueue = new RequestQueue();

// Add queuing interceptor
apiClient.interceptors.request.use(async (config) => {
  await requestQueue.add(() => Promise.resolve());
  return config;
});

// ============================================
// 7. ADVANCED: Request Deduplication
// ============================================
/**
 * Vietnamese Explanation:
 * - Ngăn chặn duplicate requests (cùng URL + method + params)
 * - Nếu có request đang pending, return kết quả của request đó
 * - Useful khi user click nhiều lần hoặc component re-render
 */
const pendingRequests = new Map<string, Promise<any>>(); // 📋 Map lưu các pending requests

apiClient.interceptors.request.use(
  (config) => {
    // 🔑 Create unique key for this request (Tạo key duy nhất cho request)
    const requestKey = `${config.method}:${config.url}:${JSON.stringify(
      config.params
    )}`;

    // ❓ Nếu đã có request pending với key này (Request trùng lặp)
    if (pendingRequests.has(requestKey)) {
      console.log('🔄 Duplicate request detected, using pending request...');
      // 🔁 Return pending promise (sẽ reject này để reuse pending request)
      throw {
        __DUPLICATE__: true, // 🏷️ Đánh dấu là duplicate
        promise: pendingRequests.get(requestKey), // 📦 Trả về promise đang pending
      };
    }

    // 💾 Store request key in config for later cleanup (Lưu key để cleanup sau)
    (config as any).__requestKey = requestKey;

    return config;
  },
  (error) => {
    // ✅ Nếu là duplicate request, return pending promise (Trả về pending promise)
    if (error.__DUPLICATE__) {
      return error.promise; // 🔁 Reuse kết quả của request đang chạy
    }
    return Promise.reject(error);
  }
);

apiClient.interceptors.response.use(
  (response) => {
    // 🗑️ Remove from pending requests (Xóa khỏi pending requests khi hoàn thành)
    const requestKey = (response.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey); // 🗑️ Xóa request key
    }
    return response;
  },
  (error) => {
    // 🗑️ Remove from pending requests even on error (Xóa ngay cả khi lỗi)
    const requestKey = (error.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey); // 🗑️ Xóa request key
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
    // 🔧 Setup interceptors (Cài đặt interceptors)
    const requestInterceptor = apiClient.interceptors.request.use((config) => {
      // ➕ Add logic here (Thêm logic ở đây)
      return config;
    });

    const responseInterceptor = apiClient.interceptors.response.use(
      (response) => {
        // ➕ Add logic here (Thêm logic ở đây)
        return response;
      }
    );

    // 🧹 Cleanup function (Hàm dọn dẹp)
    return () => {
      apiClient.interceptors.request.eject(requestInterceptor); // 🗑️ Xóa request interceptor
      apiClient.interceptors.response.eject(responseInterceptor); // 🗑️ Xóa response interceptor
    };
  }, []); // 🎯 Empty dependency array = run once on mount (Chỉ chạy 1 lần khi mount)
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
// ❌ Sai: Không cleanup interceptors (Memory leak!)
useEffect(() => {
  axios.interceptors.request.use((config) => config);
  // ⚠️ Missing cleanup - Sẽ tạo memory leak!
}, []);

// ✅ Đúng: Always cleanup (Luôn dọn dẹp)
useEffect(() => {
  const interceptor = axios.interceptors.request.use((config) => config); // 🔧 Setup
  return () => axios.interceptors.request.eject(interceptor); // 🧹 Cleanup
}, []);

// ❌ Sai: Forget to return config/response (Quên return!)
axios.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer token';
  // ⚠️ Forgot to return config - Request sẽ bị undefined!
});

// ✅ Đúng: Always return (Luôn phải return)
axios.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer token'; // 🔐 Gắn token
  return config; // ✅ TRẢ VỀ config!
});

// ❌ Sai: Infinite loop trong token refresh (Vòng lặp vô hạn!)
axios.interceptors.response.use(
  (res) => res,
  async (error) => {
    if (error.response?.status === 401) {
      await axios.post('/auth/refresh'); // ⚠️ Uses same instance → infinite loop!
      return axios(error.config);
    }
  }
);

// ✅ Đúng: Use separate instance for refresh (Dùng instance riêng để refresh)
const refreshClient = axios.create(); // 🆕 Instance riêng cho refresh
axios.interceptors.response.use(
  (res) => res,
  async (error) => {
    if (error.response?.status === 401 && !error.config._retry) {
      // 🏷️ Kiểm tra _retry flag
      error.config._retry = true; // ⚠️ Ngăn infinite loop
      await refreshClient.post('/auth/refresh'); // 🔄 Dùng instance khác!
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

## **PHẦN 2: Axios Instance - Deep Dive & Best Practices**

---

## **📚 TẠI SAO CẦN AXIOS INSTANCE?**

### **❌ Problem: Dùng Default Axios**

```typescript
// ❌ BAD: Global axios - shared interceptors, config cho TẤT CẢ requests
import axios from 'axios';

// ⚠️ Problem 1: Tất cả requests dùng chung config
axios.defaults.baseURL = 'https://api.example.com'; // 🌐 Ảnh hưởng GLOBAL - Tất cả requests!
axios.defaults.timeout = 5000; // ⏱️ Ảnh hưởng GLOBAL - Tất cả requests!

// ⚠️ Problem 2: Interceptors apply cho TẤT CẢ
axios.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer token'; // 🔐 Cả auth API và public API đều có token!
  return config; // 😱 Cả auth API và public API đều có token!
});

// ⚠️ Problem 3: Không thể config riêng cho từng service
await axios.get('/users'); // 🔍 Uses global config
await axios.post('https://upload.api.com/files', file); // 😱 Cũng dùng config trên!
```

**Hậu quả:**

- ❌ Conflict config giữa các services (timeout khác nhau)
- ❌ Interceptors apply cho cả requests không cần (auth token ở public API)
- ❌ Khó debug (không biết request nào dùng config gì)
- ❌ Khó test (global state affects tests)
- ❌ Memory leak khi không cleanup interceptors

---

### **✅ Solution: Separate Axios Instances**

```typescript
// ✅ GOOD: Mỗi service có instance riêng
const mainAPI = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
}); // 🌐 Main API - 10s timeout
const authAPI = axios.create({
  baseURL: 'https://auth.example.com',
  timeout: 5000,
}); // 🔐 Auth API - 5s timeout (nhanh hơn)
const uploadAPI = axios.create({
  baseURL: 'https://upload.example.com',
  timeout: 60000,
}); // 📤 Upload API - 60s timeout (file lớn)

// ✅ Mỗi instance có interceptors riêng, không ảnh hưởng lẫn nhau
mainAPI.interceptors.request.use((config) => {
  /* 🎯 Only for mainAPI */
});
authAPI.interceptors.request.use((config) => {
  /* 🔐 Only for authAPI */
});
```

---

## **🏗️ AXIOS INSTANCE - ARCHITECTURE**

```
┌─────────────────────────────────────────────────────────────┐
│                     APPLICATION                              │
│                                                              │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│   │  mainAPI     │  │  authAPI     │  │  uploadAPI   │    │
│   │  Instance    │  │  Instance    │  │  Instance    │    │
│   └──────────────┘  └──────────────┘  └──────────────┘    │
│         │                  │                  │             │
│         ├─ config         ├─ config         ├─ config      │
│         ├─ interceptors   ├─ interceptors   ├─ interceptors│
│         └─ methods        └─ methods        └─ methods      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND SERVICES                           │
│   api.example.com  │  auth.example.com  │  upload.api.com  │
└─────────────────────────────────────────────────────────────┘
```

---

## **🎯 BEST PRACTICES - PRODUCTION-READY SETUP**

### **1. Service-Based Organization (Recommended)**

```typescript
// ═══════════════════════════════════════════════════════════
// src/services/api/index.ts
// ═══════════════════════════════════════════════════════════

import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

// ────────────────────────────────────────────────────────────
// BASE CONFIGURATION (Cấu hình cơ bản chung)
// ────────────────────────────────────────────────────────────

const BASE_CONFIG: AxiosRequestConfig = {
  headers: {
    'Content-Type': 'application/json', // 📝 Default JSON content type
  },
  withCredentials: true, // 🔐 CSRF cookies - Gửi cookies trong cross-origin requests
};

// ────────────────────────────────────────────────────────────
// 1️⃣ MAIN API - Business logic, data CRUD (CRUD dữ liệu chính)
// ────────────────────────────────────────────────────────────

export const mainAPI = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'https://api.example.com', // 🌐 Base URL
  timeout: 10000, // ⏱️ 10s - Standard timeout (Thời gian chờ chuẩn)
  ...BASE_CONFIG, // 📦 Spread base config
});

// 🔧 Interceptors riêng cho mainAPI (Interceptors cụ thể cho main API)
mainAPI.interceptors.request.use(
  (config) => {
    // ✅ Auto-add auth token (Tự động thêm token)
    const token = localStorage.getItem('accessToken'); // 📦 Lấy token
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`; // 🔐 Gắn token vào header
    }

    // ✅ Add request metadata (Thêm metadata để tracking)
    (config as any).metadata = { startTime: Date.now() }; // ⏰ Lưu thời điểm bắt đầu

    return config;
  },
  (error) => Promise.reject(error) // ❌ Reject lỗi
);

mainAPI.interceptors.response.use(
  (response) => {
    // ✅ Log slow requests (Cảnh báo requests chậm)
    const duration = Date.now() - (response.config as any).metadata?.startTime; // 📊 Tính duration
    if (duration > 3000) {
      // ⚠️ Nếu > 3 giây
      console.warn(`⚠️ Slow API: ${response.config.url} (${duration}ms)`);
    }
    return response;
  },
  async (error) => {
    // ✅ Handle 401 - Token refresh (Xử lý token hết hạn)
    if (error.response?.status === 401 && !error.config._retry) {
      // 🔐 401 = Token expired
      error.config._retry = true; // 🏷️ Đánh dấu đã retry

      try {
        const refreshToken = localStorage.getItem('refreshToken'); // 📦 Lấy refresh token
        const { data } = await authAPI.post('/refresh', { refreshToken }); // 🔄 Gọi API refresh

        localStorage.setItem('accessToken', data.accessToken); // 💾 Lưu token mới
        error.config.headers.Authorization = `Bearer ${data.accessToken}`; // 🔐 Update header

        return mainAPI.request(error.config); // ✅ Retry with new token (Thử lại với token mới)
      } catch (refreshError) {
        localStorage.clear(); // 🗑️ Xóa hết data
        window.location.href = '/login'; // ↩️ Redirect login
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// ────────────────────────────────────────────────────────────
// 2️⃣ AUTH API - Login, Register, Refresh Token (Xác thực người dùng)
// ────────────────────────────────────────────────────────────

export const authAPI = axios.create({
  baseURL: process.env.REACT_APP_AUTH_URL || 'https://auth.example.com', // 🌐 Auth server URL
  timeout: 5000, // ⏱️ 5s - Nhanh hơn (Auth requests should be fast)
  ...BASE_CONFIG, // 📦 Spread base config
});

// ⚠️ AUTH API KHÔNG CÓ token interceptor (để tránh infinite loop)
// ⚠️ KHÔNG retry 401 ở authAPI (Login không cần retry token)

authAPI.interceptors.request.use((config) => {
  // ✅ Add device fingerprint (Đánh dấu thiết bị để chống fraud)
  config.headers['X-Device-ID'] = getDeviceId(); // 📱 Device ID duy nhất
  return config;
});

authAPI.interceptors.response.use(
  (response) => response,
  (error) => {
    // ✅ Auth-specific error handling (Xử lý lỗi cụ thể cho auth)
    if (error.response?.status === 429) {
      // 🚫 429 = Quá nhiều requests
      // Rate limited (Bị giới hạn tốc độ)
      console.error('⚠️ Too many login attempts. Please try again later.');
    }
    return Promise.reject(error);
  }
);

// ────────────────────────────────────────────────────────────
// 3️⃣ UPLOAD API - Large files, images, documents (Tải file lên)
// ────────────────────────────────────────────────────────────

export const uploadAPI = axios.create({
  baseURL: process.env.REACT_APP_UPLOAD_URL || 'https://upload.example.com', // 🌐 Upload server
  timeout: 60000, // ⏱️ 60s - File lớn cần nhiều thời gian (Large files need more time)
  headers: {
    'Content-Type': 'multipart/form-data', // ✅ Dành cho file uploads (For file uploads)
  },
  withCredentials: true, // 🔐 Gửi cookies
  maxContentLength: 100 * 1024 * 1024, // 📦 100MB max (Giới hạn kích thước file)
  maxBodyLength: 100 * 1024 * 1024, // 📦 100MB max body
});

uploadAPI.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken'); // 📦 Lấy token
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`; // 🔐 Gắn token
  }

  // ✅ Track upload progress (Theo dõi tiến độ upload)
  config.onUploadProgress = (progressEvent) => {
    const percent = Math.round(
      (progressEvent.loaded * 100) / progressEvent.total!
    ); // 📊 Tính %
    console.log(`📤 Upload: ${percent}%`);
    // Dispatch to Redux/Zustand: setUploadProgress(percent);  // 📢 Cập nhật UI
  };

  return config;
});

// ────────────────────────────────────────────────────────────
// 4️⃣ PUBLIC API - No auth required (Không cần xác thực: blog, landing page)
// ────────────────────────────────────────────────────────────

export const publicAPI = axios.create({
  baseURL: process.env.REACT_APP_PUBLIC_API || 'https://public.example.com', // 🌐 Public API URL
  timeout: 8000, // ⏱️ 8s timeout
  ...BASE_CONFIG, // 📦 Spread base config
});

// ⚠️ PUBLIC API không có Authorization header (Không cần token)
publicAPI.interceptors.request.use((config) => {
  // ✅ Only add tracking/analytics headers (Chỉ thêm tracking headers)
  config.headers['X-Client-Version'] = process.env.REACT_APP_VERSION; // 🏷️ Phiên bản app
  return config;
});

// ────────────────────────────────────────────────────────────
// 5️⃣ ANALYTICS API - Tracking, metrics (Theo dõi hành vi: fire and forget)
// ────────────────────────────────────────────────────────────

export const analyticsAPI = axios.create({
  baseURL: 'https://analytics.example.com', // 🌐 Analytics server
  timeout: 2000, // ⏱️ Timeout nhanh - Không chặn user actions (Fast timeout - don't block user actions)
  ...BASE_CONFIG, // 📦 Spread base config
});

// ✅ Fire and forget - không cần error handling (Gửi đi và quên - Không ảnh hưởng app)
analyticsAPI.interceptors.response.use(
  (response) => response,
  (error) => {
    // 🔇 Silent fail - analytics không nên block app (Lỗi analytics không quan trọng)
    console.debug('Analytics error (ignored):', error.message); // 📝 Chỉ log debug
    return Promise.resolve(); // ⚠️ Không propagate error - Don't propagate error
  }
);
```

---

### **2. Centralized API Service Layer**

```typescript
// ═══════════════════════════════════════════════════════════
// src/services/api/users.ts
// ═══════════════════════════════════════════════════════════

import { mainAPI } from './index';

export interface User {
  id: string;
  name: string;
  email: string;
  role: 'user' | 'admin';
}

export interface CreateUserDTO {
  name: string;
  email: string;
  password: string;
}

// ✅ Type-safe API methods (Các method có type an toàn)
export const userService = {
  // GET /users (Lấy danh sách tất cả users)
  getAll: async (): Promise<User[]> => {
    const { data } = await mainAPI.get<User[]>('/users'); // 📡 Gọi GET request
    return data; // 📦 Trả về array of users
  },

  // GET /users/:id (Lấy 1 user theo ID)
  getById: async (id: string): Promise<User> => {
    const { data } = await mainAPI.get<User>(`/users/${id}`); // 🔍 Tìm user theo ID
    return data; // 👤 Trả về user object
  },

  // POST /users (Tạo user mới)
  create: async (dto: CreateUserDTO): Promise<User> => {
    const { data } = await mainAPI.post<User>('/users', dto); // ➕ Tạo user
    return data; // 🆕 Trả về user mới tạo
  },

  // PUT /users/:id (Cập nhật user)
  update: async (id: string, updates: Partial<User>): Promise<User> => {
    const { data } = await mainAPI.put<User>(`/users/${id}`, updates); // ✏️ Cập nhật
    return data; // 📦 Trả về user đã cập nhật
  },

  // DELETE /users/:id (Xóa user)
  delete: async (id: string): Promise<void> => {
    await mainAPI.delete(`/users/${id}`); // 🗑️ Xóa user
  },

  // GET /users?search=...&page=... (Tìm kiếm users)
  search: async (
    query: string,
    page = 1
  ): Promise<{ users: User[]; total: number }> => {
    const { data } = await mainAPI.get('/users', {
      params: { search: query, page, limit: 10 }, // 🔎 Query params: search, page, limit
    });
    return data; // 📊 Trả về danh sách users + tổng số
  },
};

// ═══════════════════════════════════════════════════════════
// src/services/api/auth.ts
// ═══════════════════════════════════════════════════════════

import { authAPI } from './index';

export interface LoginDTO {
  email: string;
  password: string;
}

export interface AuthResponse {
  accessToken: string;
  refreshToken: string;
  user: User;
}

export const authService = {
  login: async (credentials: LoginDTO): Promise<AuthResponse> => {
    const { data } = await authAPI.post<AuthResponse>('/login', credentials); // 🔐 Gọi API login

    // ✅ Auto-save tokens (Tự động lưu tokens vào localStorage)
    localStorage.setItem('accessToken', data.accessToken); // 💾 Lưu access token
    localStorage.setItem('refreshToken', data.refreshToken); // 💾 Lưu refresh token

    return data; // 👤 Trả về user info + tokens
  },

  register: async (dto: CreateUserDTO): Promise<AuthResponse> => {
    const { data } = await authAPI.post<AuthResponse>('/register', dto); // ✏️ Đăng ký tài khoản mới
    localStorage.setItem('accessToken', data.accessToken); // 💾 Lưu access token
    localStorage.setItem('refreshToken', data.refreshToken); // 💾 Lưu refresh token
    return data; // 🆕 Trả về user + tokens
  },

  logout: async (): Promise<void> => {
    const refreshToken = localStorage.getItem('refreshToken'); // 📦 Lấy refresh token
    await authAPI.post('/logout', { refreshToken }); // 🚪 Gọi API logout
    localStorage.clear(); // 🗑️ Xóa hết localStorage
  },

  refreshToken: async (): Promise<AuthResponse> => {
    const refreshToken = localStorage.getItem('refreshToken'); // 📦 Lấy refresh token
    const { data } = await authAPI.post<AuthResponse>('/refresh', {
      refreshToken,
    }); // 🔄 Lấy tokens mới

    localStorage.setItem('accessToken', data.accessToken); // 💾 Lưu access token mới
    localStorage.setItem('refreshToken', data.refreshToken); // 💾 Lưu refresh token mới

    return data; // 🆕 Trả về tokens mới
  },
};

// ═══════════════════════════════════════════════════════════
// src/services/api/upload.ts
// ═══════════════════════════════════════════════════════════

import { uploadAPI } from './index';

export interface UploadResponse {
  url: string;
  filename: string;
  size: number;
}

export const uploadService = {
  uploadFile: async (
    file: File,
    onProgress?: (percent: number) => void // 📊 Callback cập nhật tiến độ
  ): Promise<UploadResponse> => {
    const formData = new FormData(); // 📦 Tạo FormData
    formData.append('file', file); // 📄 Thêm file vào FormData

    const { data } = await uploadAPI.post<UploadResponse>('/upload', formData, {
      onUploadProgress: (e) => {
        // 📊 Theo dõi progress
        const percent = Math.round((e.loaded * 100) / e.total!); // 📊 Tính %
        onProgress?.(percent); // 📢 Gọi callback
      },
    });

    return data; // 🔗 Trả về URL, filename, size
  },

  uploadMultiple: async (files: File[]): Promise<UploadResponse[]> => {
    const formData = new FormData(); // 📦 Tạo FormData
    files.forEach((file) => formData.append('files', file)); // 📄 Thêm nhiều files

    const { data } = await uploadAPI.post<UploadResponse[]>(
      '/upload/batch',
      formData
    ); // 📤 Upload batch
    return data; // 📦 Trả về array của UploadResponse
  },
};
```

---

### **3. React Integration - Custom Hooks**

```typescript
// ═══════════════════════════════════════════════════════════
// src/hooks/useAPI.ts
// ═══════════════════════════════════════════════════════════

import { useState, useEffect } from 'react';
import { AxiosInstance, AxiosRequestConfig } from 'axios';

interface UseAPIOptions<T> extends AxiosRequestConfig {
  instance?: AxiosInstance;
  onSuccess?: (data: T) => void;
  onError?: (error: any) => void;
}

export function useAPI<T>(options: UseAPIOptions<T>) {
  const [data, setData] = useState<T | null>(null); // 📦 Data state
  const [loading, setLoading] = useState(false); // ⏳ Loading state
  const [error, setError] = useState<any>(null); // ❌ Error state

  const execute = async () => {
    setLoading(true); // ⏳ Bắt đầu loading
    setError(null); // 🧹 Clear lỗi cũ

    try {
      const instance = options.instance || mainAPI; // 🌐 Dùng instance nào? (Default: mainAPI)
      const response = await instance.request<T>(options); // 📡 Gọi API

      setData(response.data); // 💾 Lưu data vào state
      options.onSuccess?.(response.data); // ✅ Gọi callback success
    } catch (err) {
      setError(err); // ❌ Lưu error vào state
      options.onError?.(err); // ❌ Gọi callback error
    } finally {
      setLoading(false); // ⏹️ Kết thúc loading
    }
  };

  return { data, loading, error, execute }; // 📦 Trả về states + execute function
}

// ═══════════════════════════════════════════════════════════
// USAGE IN COMPONENTS
// ═══════════════════════════════════════════════════════════

function UserList() {
  const {
    data: users,
    loading,
    error,
    execute,
  } = useAPI<User[]>({
    method: 'get', // 🔍 HTTP method
    url: '/users', // 🌐 API endpoint
  });

  useEffect(() => {
    execute(); // 🚀 Chạy API khi component mount
  }, []);

  if (loading) return <div>Loading...</div>; // ⏳ Hiển thị loading
  if (error) return <div>Error: {error.message}</div>; // ❌ Hiển thị lỗi

  return (
    <ul>
      {users?.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  ); // 📋 Hiển thị danh sách users
}
```

---

### **4. Environment-Based Configuration**

```typescript
// ═══════════════════════════════════════════════════════════
// src/services/api/config.ts
// ═══════════════════════════════════════════════════════════

interface APIConfig {
  baseURL: string;
  timeout: number;
}

const ENV_CONFIGS: Record<string, APIConfig> = {
  development: {
    baseURL: 'http://localhost:3000/api', // 💻 Local development
    timeout: 30000, // ⏱️ 30s - Dài hơn để debug (Longer for debugging)
  },
  staging: {
    baseURL: 'https://staging-api.example.com', // 🏗️ Staging server
    timeout: 10000, // ⏱️ 10s - Timeout chuẩn
  },
  production: {
    baseURL: 'https://api.example.com', // 🌐 Production server
    timeout: 8000, // ⏱️ 8s - Nhanh hơn cho production (Faster for production)
  },
};

export const getAPIConfig = (): APIConfig => {
  const env = process.env.NODE_ENV || 'development'; // 🎯 Lấy môi trường hiện tại
  return ENV_CONFIGS[env]; // 📦 Trả về config tương ứng
};

// Usage (Sử dụng)
const config = getAPIConfig(); // ⚙️ Lấy config theo environment
const mainAPI = axios.create(config); // 🆕 Tạo instance với config
```

---

### **5. Request Queue & Rate Limiting**

```typescript
// ═══════════════════════════════════════════════════════════
// src/services/api/requestQueue.ts
// ═══════════════════════════════════════════════════════════

class RequestQueue {
  private queue: Array<() => Promise<any>> = []; // 📋 Hàng đợi chứa requests
  private activeCount = 0; // 📊 Số requests đang chạy
  private readonly maxConcurrent: number; // 5️⃣ Số requests đồng thời tối đa

  constructor(maxConcurrent = 5) {
    this.maxConcurrent = maxConcurrent; // 5️⃣ Mặc định: 5 requests cùng lúc
  }

  async add<T>(requestFn: () => Promise<T>): Promise<T> {
    // ⚠️ Wait if max concurrent reached (Chờ nếu đã đạt giới hạn)
    if (this.activeCount >= this.maxConcurrent) {
      await new Promise<void>((resolve) => {
        this.queue.push(() => {
          // 📍 Thêm vào queue
          resolve(); // ✅ Resolve khi đến lượt
          return Promise.resolve();
        });
      });
    }

    this.activeCount++; // ➕ Tăng số requests đang chạy

    try {
      return await requestFn(); // ▶️ Thực thi request
    } finally {
      this.activeCount--; // ➖ Giảm số requests đang chạy

      // 🔁 Process next in queue (Xử lý request tiếp theo)
      const next = this.queue.shift(); // 📤 Lấy request đầu hàng đợi
      if (next) next(); // ▶️ Chạy request tiếp theo
    }
  }
}

// Apply to instance (Gắn vào axios instance)
const queue = new RequestQueue(5); // 5️⃣ Tối đa 5 requests đồng thời

mainAPI.interceptors.request.use(async (config) => {
  await queue.add(() => Promise.resolve()); // ⏳ Chờ đến lượt trong queue
  return config; // ✅ Tiếp tục request
});
```

---

## **🎯 BEST PRACTICES SUMMARY**

```typescript
// ✅ 1. ONE INSTANCE PER SERVICE (Mỗi service 1 instance riêng)
const mainAPI = axios.create({ baseURL: '/api' });      // 🌐 Main API
const authAPI = axios.create({ baseURL: '/auth' });     // 🔐 Auth API

// ✅ 2. SEPARATE AUTH API (avoid infinite loop) (Tách auth API để tránh vòng lặp)
// authAPI không có token refresh interceptor

// ✅ 3. TYPE-SAFE SERVICE LAYER (Service layer có type an toàn)
export const userService = {
  getAll: (): Promise<User[]> => mainAPI.get('/users').then(r => r.data),  // 📦 Type-safe
};

// ✅ 4. ENVIRONMENT-BASED CONFIG (Config theo môi trường)
const config = getAPIConfig(); // ⚙️ dev/staging/prod

// ✅ 5. CLEANUP INTERCEPTORS (React) (Dọn dẹp interceptors)
useEffect(() => {
  const id = mainAPI.interceptors.request.use(...);  // 🔧 Setup
  return () => mainAPI.interceptors.request.eject(id);  // 🧹 Cleanup
}, []);

// ✅ 6. CANCEL REQUESTS ON UNMOUNT (Hủy requests khi unmount)
useEffect(() => {
  const controller = new AbortController();  // 🚫 Abort controller
  mainAPI.get('/users', { signal: controller.signal });  // 📡 Request có signal
  return () => controller.abort();  // 🚫 Hủy request khi unmount
}, []);

// ✅ 7. DIFFERENT TIMEOUTS PER SERVICE (Mỗi service timeout khác nhau)
const uploadAPI = axios.create({ timeout: 60000 }); // 📤 60s - File lớn (Large files)
const mainAPI = axios.create({ timeout: 10000 });   // ⏱️ 10s - Chuẩn (Standard)

// ✅ 8. RATE LIMITING (Giới hạn số requests đồng thời)
const queue = new RequestQueue(5); // 5️⃣ Tối đa 5 concurrent (Max 5 concurrent)

// ✅ 9. ERROR HANDLING PER INSTANCE (Xử lý lỗi riêng cho từng instance)
mainAPI.interceptors.response.use(null, handleMainAPIError);  // ❌ Main API errors
authAPI.interceptors.response.use(null, handleAuthAPIError);  // ❌ Auth API errors

// ✅ 10. LOGGING (dev only) (Chỉ log ở development)
if (process.env.NODE_ENV === 'development') {  // 💻 Dev mode only
  mainAPI.interceptors.request.use(logRequest);  // 📝 Log tất cả requests
}
```

---

## **⚠️ COMMON MISTAKES**

```typescript
// ❌ 1. Using global axios
import axios from 'axios';
axios.get('/users'); // BAD - uses global config

// ✅ Fix: Use instance
const api = axios.create({});
api.get('/users');

// ❌ 2. Token refresh với same instance
mainAPI.interceptors.response.use(null, async (error) => {
  if (error.response?.status === 401) {
    await mainAPI.post('/refresh'); // ❌ Infinite loop!
  }
});

// ✅ Fix: Use separate authAPI
if (error.response?.status === 401) {
  await authAPI.post('/refresh'); // ✅ Separate instance
}

// ❌ 3. Not cleaning up interceptors
useEffect(() => {
  mainAPI.interceptors.request.use(...);
  // ❌ Missing cleanup
}, []);

// ✅ Fix: Always eject
useEffect(() => {
  const id = mainAPI.interceptors.request.use(...);
  return () => mainAPI.interceptors.request.eject(id);
}, []);

// ❌ 4. Hardcoded baseURL (Hard-code URL trong code)
const api = axios.create({ baseURL: 'https://api.example.com' });  // ❌ SAI - Không linh hoạt!

// ✅ Fix: Environment variables (Dùng biến môi trường)
const api = axios.create({ baseURL: process.env.REACT_APP_API_URL });  // ✅ Đúng - Linh hoạt theo env

// ❌ 5. Same timeout for all requests (Cùng 1 timeout cho mọi requests)
const api = axios.create({ timeout: 5000 });  // ⏱️ 5s cho tất cả
api.post('/upload', largeFile); // ❌ Timeout sau 5s! (File lớn sẽ timeout!)

// ✅ Fix: Different instances (Mỗi instance timeout riêng)
const uploadAPI = axios.create({ timeout: 60000 });  // ⏱️ 60s cho upload
uploadAPI.post('/upload', largeFile);  // ✅ Đủ thời gian cho file lớn
```

---

## **📊 PERFORMANCE CONSIDERATIONS (Cân Nhắc Hiệu Năng)**

```typescript
// ✅ 1. Connection Pooling (automatic in axios) (Tái sử dụng kết nối - Tự động)
// Reuse connections for same baseURL (Tái sử dụng kết nối cho cùng baseURL)
// 💡 Axios tự động reuse HTTP connections cho cùng baseURL
// 💡 Lợi ích: Giảm overhead của việc tạo connection mới (TCP handshake...)
// 💡 VD: 10 requests đến api.example.com → Chỉ tạo 1 connection, reuse 9 lần

// ✅ 2. Request Deduplication (Loại bỏ requests trùng lặp)
const pendingRequests = new Map<string, Promise<any>>(); // 📋 Map lưu requests đang chạy
mainAPI.interceptors.request.use((config) => {
  const key = `${config.method}:${config.url}`; // 🔑 Tạo unique key
  // 💡 Key = method + URL để identify request giống nhau

  if (pendingRequests.has(key)) {
    // ❓ Nếu đang có request giống vậy đang chạy
    console.log('🔄 Reusing pending request'); // 📝 Log khi reuse
    return Promise.reject({
      __DUPLICATE__: true,
      promise: pendingRequests.get(key),
    }); // 🔁 Trả về promise đang chạy (không tạo request mới)
  }

  // 📡 Tạo request mới và lưu vào pending
  const promise = mainAPI.request(config).finally(() => {
    pendingRequests.delete(key); // 🗑️ Xóa khi hoàn thành
  });
  pendingRequests.set(key, promise); // 💾 Lưu vào pending
  return config; // ✅ Tiếp tục request
});
// 💡 Lợi ích: Tránh spam requests (VD: User click nhiều lần button)

// ✅ 3. Response Caching (GET only) (Cache kết quả - Chỉ GET)
const cache = new Map<string, { data: any; timestamp: number }>(); // 💾 Map lưu cache
mainAPI.interceptors.request.use((config) => {
  if (config.method === 'get' && cache.has(config.url)) {
    // 🔍 Nếu đã có cache
    const cached = cache.get(config.url)!;
    const ttl = 5 * 60 * 1000; // ⏱️ 5 phút TTL

    if (Date.now() - cached.timestamp < ttl) {
      // ✅ Cache chưa hết hạn
      console.log('💾 Returning cached response'); // 📝 Log khi dùng cache
      return Promise.resolve({ data: cached.data } as any); // 📦 Trả về cache
    } else {
      cache.delete(config.url); // 🗑️ Xóa cache hết hạn
    }
  }
  return config; // ✅ Tiếp tục request bình thường
});
// 💡 Lợi ích: Giảm số lượng requests, tăng tốc độ
// ⚠️ Lưu ý: Chỉ cache GET requests, không cache POST/PUT/DELETE

// ✅ 4. Compression (gzip) (Nén dữ liệu)
mainAPI.defaults.headers['Accept-Encoding'] = 'gzip, deflate'; // 📦 Yêu cầu server nén response
// 💡 Accept-Encoding: Browser yêu cầu server nén response
// 💡 Server sẽ nén response (gzip) → Giảm kích thước 70-90%
// 💡 Browser tự động giải nén → Không cần code gì thêm
// 💡 Lợi ích: Giảm bandwidth, tăng tốc độ load

// ✅ 5. Parallel Requests (Gọi nhiều requests đồng thời)
await Promise.all([
  // 🚀 Chạy song song, không chờ nhau
  mainAPI.get('/users'), // 👥 Users
  mainAPI.get('/posts'), // 📝 Posts
  mainAPI.get('/comments'), // 💬 Comments
]); // ✅ Nhanh hơn chạy tuần tự!
// 💡 Promise.all(): Chờ TẤT CẢ promises hoàn thành
// 💡 Nếu 1 request mất 1s → Tổng thời gian = 1s (song song)
// 💡 Nếu chạy tuần tự → Tổng thời gian = 3s (chậm hơn 3 lần!)
```

---

## **🔒 SECURITY BEST PRACTICES (Thực Hành Bảo Mật Tốt Nhất)**

```typescript
// ✅ 1. HTTPS Only (production) (Chỉ dùng HTTPS ở production)
const api = axios.create({
  baseURL:
    process.env.NODE_ENV === 'production' // 🌐 Kiểm tra environment
      ? 'https://api.example.com' // 🔒 HTTPS ở production (bảo mật)
      : 'http://localhost:3000', // 💻 HTTP ở local (OK for dev)
});
// 💡 HTTPS: Mã hóa dữ liệu giữa client và server
// 💡 Tránh: Man-in-the-middle attacks, data interception
// ⚠️ Lưu ý: Luôn dùng HTTPS ở production!

// ✅ 2. CSRF Protection (Chống CSRF attacks)
const api = axios.create({
  withCredentials: true, // 🔐 Gửi cookies trong cross-origin requests
  // 💡 withCredentials: Cho phép gửi cookies (cần cho CSRF protection)
  xsrfCookieName: 'XSRF-TOKEN', // 🍪 Tên cookie chứa CSRF token
  // 💡 Server set cookie này khi user login
  xsrfHeaderName: 'X-XSRF-TOKEN', // 🏷️ Tên header gửi CSRF token
  // 💡 Axios tự động đọc cookie và gửi vào header này
});
// 💡 CSRF: Cross-Site Request Forgery - Tấn công giả mạo request
// 💡 Cách chống: Server gửi CSRF token trong cookie → Client gửi lại trong header
// 💡 Server verify token → Chỉ request hợp lệ mới được xử lý

// ✅ 3. Sanitize Sensitive Data (don't log) (Không log dữ liệu nhạy cảm)
mainAPI.interceptors.request.use((config) => {
  const sanitized = { ...config }; // 📦 Copy config để không ảnh hưởng config gốc
  delete sanitized.headers?.Authorization; // 🗑️ Xóa token trước khi log
  delete sanitized.headers?.['X-API-Key']; // 🗑️ Xóa API key (nếu có)
  delete sanitized.data?.password; // 🗑️ Xóa password từ request body
  console.log('📡 Request:', sanitized); // ✅ An toàn để log (Safe to log)
  return config; // ✅ Trả về config gốc có token (không bị ảnh hưởng)
});
// 💡 Tại sao: Logs có thể bị leak (console, file logs, monitoring tools...)
// 💡 Tránh: Token, password, credit card... bị expose trong logs

// ✅ 4. Token Storage (httpOnly cookies > localStorage) (Lưu token an toàn)
// Prefer backend setting httpOnly cookie over localStorage (httpOnly cookies an toàn hơn localStorage)
// 💡 httpOnly cookies: JavaScript không thể đọc → Tránh XSS attacks
// 💡 localStorage: JavaScript có thể đọc → Dễ bị XSS attacks
// 💡 Best practice: Backend set httpOnly cookie → Không cần lưu token ở frontend

// ✅ 5. Content Security Policy (Chính sách bảo mật nội dung)
mainAPI.defaults.headers['Content-Security-Policy'] = "default-src 'self'";
// 🚫 Chỉ load resources từ chính domain
// 💡 CSP: Ngăn chặn XSS attacks, code injection
// 💡 'self': Chỉ cho phép load từ cùng origin
// 💡 Có thể config chi tiết hơn: script-src, style-src, img-src...
```

---

## **📝 MINDMAP: Axios Instance Architecture**

```
AXIOS INSTANCE STRATEGY
├── mainAPI (Business Logic)
│   ├── baseURL: /api
│   ├── timeout: 10s
│   ├── Auth Token Interceptor
│   ├── Token Refresh (401)
│   └── Error Handling
│
├── authAPI (Authentication)
│   ├── baseURL: /auth
│   ├── timeout: 5s
│   ├── NO auth interceptor (avoid loop)
│   └── Rate limit handling (429)
│
├── uploadAPI (File Uploads)
│   ├── baseURL: /upload
│   ├── timeout: 60s
│   ├── multipart/form-data
│   ├── Progress tracking
│   └── Large file support (100MB)
│
├── publicAPI (No Auth)
│   ├── baseURL: /public
│   ├── timeout: 8s
│   └── Analytics headers only
│
└── analyticsAPI (Tracking)
    ├── baseURL: /analytics
    ├── timeout: 2s
    ├── Fire and forget
    └── Silent fail (no error propagation)
```

---

### **3. Request Cancellation (Hủy Request)**

```typescript
// ═══════════════════════════════════════════════════════════
// ABORT CONTROLLER (Modern - Cách hiện đại để hủy request)
// ═══════════════════════════════════════════════════════════

const controller = new AbortController(); // 🚫 Tạo AbortController để điều khiển việc hủy request
// 💡 AbortController: Cho phép hủy request bất cứ lúc nào
// 💡 Signal: Đối tượng để truyền vào axios config

axios
  .get('/api/users', { signal: controller.signal }) // 📡 Gửi request với signal
  .catch((error) => {
    if (axios.isCancel(error)) {
      // ✅ Kiểm tra xem request có bị hủy không
      console.log('Request canceled'); // 📝 Log khi request bị hủy
      // 💡 axios.isCancel(): Kiểm tra error có phải do cancel không
    }
  });

controller.abort(); // 🚫 Hủy request ngay lập tức
// 💡 abort(): Dừng request đang chạy, trigger catch với CancelError

// ═══════════════════════════════════════════════════════════
// USE CASE: Cancel on unmount (React - Hủy khi component unmount)
// ═══════════════════════════════════════════════════════════

useEffect(() => {
  const controller = new AbortController(); // 🚫 Tạo controller trong useEffect

  axios
    .get('/api/users', { signal: controller.signal }) // 📡 Request có signal
    .then(({ data }) => setUsers(data)) // ✅ Lưu data nếu thành công
    .catch((error) => !axios.isCancel(error) && console.error(error)); // ❌ Chỉ log lỗi thật (không phải cancel)
  // 💡 !axios.isCancel(): Bỏ qua lỗi do cancel (không phải lỗi thật)

  return () => controller.abort(); // 🧹 Cleanup: Hủy request khi component unmount
  // 💡 Quan trọng: Tránh memory leak, tránh update state sau khi unmount
}, []);
```

---

### **4. File Upload & Download (Tải File Lên & Xuống)**

```typescript
// ═══════════════════════════════════════════════════════════
// UPLOAD với Progress (Tải file lên với theo dõi tiến độ)
// ═══════════════════════════════════════════════════════════

const uploadFile = async (file: File) => {
  const formData = new FormData(); // 📦 Tạo FormData để gửi file
  // 💡 FormData: Cho phép gửi file qua HTTP POST
  formData.append('file', file); // 📄 Thêm file vào FormData
  // 💡 append(): Thêm field vào FormData (key: 'file', value: File object)

  const { data } = await axios.post('/api/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }, // 📝 Header cho file upload
    // 💡 multipart/form-data: Content-Type dành cho file uploads
    // ⚠️ Lưu ý: KHÔNG set Content-Type manually, để browser tự set (có boundary)
    onUploadProgress: (e) => {
      // 📊 Callback theo dõi tiến độ upload
      const percent = Math.round((e.loaded * 100) / e.total!); // 📊 Tính % đã upload
      // 💡 e.loaded: Số bytes đã upload
      // 💡 e.total: Tổng số bytes cần upload
      console.log(`📤 Upload: ${percent}%`); // 📝 Log tiến độ
      // 💡 Có thể dispatch vào Redux/Zustand để update UI progress bar
      // setUploadProgress(percent);  // 📢 Cập nhật state
    },
  });

  return data; // 📦 Trả về response data (VD: { url: '...', filename: '...' })
};

// ═══════════════════════════════════════════════════════════
// DOWNLOAD File (Tải file xuống)
// ═══════════════════════════════════════════════════════════

const downloadFile = async (fileId: string) => {
  const response = await axios.get(`/api/files/${fileId}`, {
    responseType: 'blob', // ⚠️ QUAN TRỌNG: Phải set blob để nhận binary data
    // 💡 blob: Binary Large Object - Dữ liệu nhị phân (file, image, PDF...)
    // 💡 Không set responseType: Nhận về JSON string (sai!)
  });

  // 🔗 Tạo URL từ blob để download
  const url = window.URL.createObjectURL(new Blob([response.data])); // 🌐 Tạo object URL từ blob
  // 💡 createObjectURL(): Tạo URL tạm thời từ blob (VD: blob:http://localhost:3000/abc123)
  // 💡 new Blob(): Tạo blob object từ response data

  const link = document.createElement('a'); // 🔗 Tạo thẻ <a> để trigger download
  link.href = url; // 🔗 Gán URL vào href
  link.download = 'filename.pdf'; // 📄 Tên file khi download
  // 💡 download attribute: Browser sẽ download thay vì navigate
  link.click(); // 🖱️ Click programmatically để trigger download

  window.URL.revokeObjectURL(url); // 🗑️ Xóa object URL để giải phóng memory
  // 💡 revokeObjectURL(): Quan trọng để tránh memory leak!
  // 💡 Object URL chiếm memory, phải revoke sau khi dùng xong
};
```

---

### **5. Error Handling (Xử Lý Lỗi)**

```typescript
// ═══════════════════════════════════════════════════════════
// TYPE-SAFE ERROR HANDLING (Xử lý lỗi an toàn với TypeScript)
// ═══════════════════════════════════════════════════════════

try {
  const response = await axios.get('/api/users'); // 📡 Gọi API
} catch (error) {
  // ✅ Kiểm tra xem có phải AxiosError không (Type-safe)
  if (axios.isAxiosError(error)) {
    // 💡 axios.isAxiosError(): Type guard để TypeScript biết đây là AxiosError

    if (error.response) {
      // ✅ Server đã phản hồi với error status (4xx, 5xx)
      // 💡 error.response: Server đã nhận request và trả về error
      const { status, data } = error.response; // 📦 Lấy status code và error data

      switch (status) {
        case 400:
          console.error('❌ Bad Request - Dữ liệu không hợp lệ');
          // 💡 400: Client gửi request sai format
          break;
        case 401:
          window.location.href = '/login'; // ↩️ Redirect về login
          // 💡 401: Chưa đăng nhập hoặc token hết hạn
          break;
        case 403:
          console.error('🚫 Forbidden - Không có quyền truy cập');
          // 💡 403: Đã đăng nhập nhưng không có quyền
          break;
        case 404:
          console.error('⚠️ Not Found - Tài nguyên không tồn tại');
          // 💡 404: URL không tồn tại
          break;
        case 422:
          console.error('📝 Validation Error:', data.errors);
          // 💡 422: Dữ liệu không hợp lệ (validation errors)
          // 💡 data.errors: Thường là object chứa lỗi validation
          break;
        case 500:
          console.error('🔥 Server Error - Lỗi server nội bộ');
          // 💡 500: Lỗi server (database, code...)
          break;
      }
    } else if (error.request) {
      // ⚠️ Request đã gửi nhưng không nhận được response (network error, timeout)
      // 💡 error.request: Request đã được gửi nhưng server không phản hồi
      console.error('🌐 Network error or timeout - Kiểm tra kết nối mạng');
      // 💡 Có thể là: Mất mạng, server down, timeout
    } else {
      // ❌ Lỗi khi setup request (trước khi gửi)
      // 💡 Lỗi này xảy ra trước khi request được gửi đi
      console.error('🚨 Request setup error:', error.message);
      // 💡 VD: URL không hợp lệ, config sai...
    }
  } else {
    // ⚠️ Không phải AxiosError (lỗi khác)
    console.error('❓ Unknown error:', error);
  }
}

// ═══════════════════════════════════════════════════════════
// CUSTOM ERROR HANDLER (Hàm xử lý lỗi tùy chỉnh)
// ═══════════════════════════════════════════════════════════

const handleError = (error: unknown) => {
  // ✅ Kiểm tra xem có phải AxiosError không
  if (axios.isAxiosError(error)) {
    return {
      success: false, // ❌ Đánh dấu thất bại
      message: error.response?.data?.message || error.message, // 📝 Error message
      // 💡 Ưu tiên message từ server, nếu không có thì dùng error.message
      status: error.response?.status, // 🔢 HTTP status code (VD: 400, 401, 500...)
      errors: error.response?.data?.errors, // 📋 Validation errors (nếu có)
      // 💡 errors: Thường là object chứa các lỗi validation
      // 💡 VD: { email: ['Email không hợp lệ'], password: ['Mật khẩu quá ngắn'] }
    };
  }
  // ⚠️ Không phải AxiosError → Trả về error mặc định
  return {
    success: false,
    message: 'Unexpected error - Lỗi không xác định',
  };
};
```

---

### **6. Advanced Patterns (Các Mẫu Nâng Cao)**

```typescript
// ═══════════════════════════════════════════════════════════
// RETRY LOGIC với Exponential Backoff (Thử lại với tăng dần thời gian chờ)
// ═══════════════════════════════════════════════════════════

const axiosRetry = async (config: any, retries = 3) => {
  // 💡 Exponential Backoff: Tăng thời gian chờ theo cấp số nhân
  // 💡 VD: Lần 1 chờ 1s, lần 2 chờ 2s, lần 3 chờ 4s...
  // 💡 Giúp server có thời gian recover khi bị quá tải

  for (let i = 0; i < retries; i++) {
    try {
      return await axios(config); // 📡 Thử gọi API
    } catch (error) {
      if (i === retries - 1) throw error; // ❌ Đã hết số lần retry → throw error
      // 💡 retries - 1: Lần cuối cùng, không retry nữa

      // ⏱️ Chờ trước khi retry (exponential: 1s, 2s, 4s...)
      await new Promise((r) => setTimeout(r, 1000 * Math.pow(2, i)));
      // 💡 Math.pow(2, i): 2^0=1, 2^1=2, 2^2=4...
      // 💡 1000 * Math.pow(2, i): 1000ms, 2000ms, 4000ms...
    }
  }
};

// ═══════════════════════════════════════════════════════════
// REQUEST DEDUPLICATION (Loại bỏ requests trùng lặp)
// ═══════════════════════════════════════════════════════════

const pending = new Map<string, Promise<any>>(); // 📋 Map lưu các requests đang chạy
// 💡 Key: `${method}:${url}` (VD: 'GET:/api/users')
// 💡 Value: Promise của request đó

const dedupeRequest = async (config: any) => {
  const key = `${config.method}:${config.url}`; // 🔑 Tạo unique key cho request
  // 💡 Key = method + URL để identify request giống nhau

  // ✅ Nếu đã có request giống vậy đang chạy → Reuse kết quả
  if (pending.has(key)) {
    console.log('🔄 Duplicate request detected, reusing pending request...');
    return pending.get(key); // 🔁 Trả về promise đang chạy (không tạo request mới)
  }

  // 📡 Tạo request mới và lưu vào pending
  const promise = axios(config).finally(() => {
    pending.delete(key); // 🗑️ Xóa khỏi pending khi hoàn thành (success hoặc error)
  });
  pending.set(key, promise); // 💾 Lưu promise vào pending
  return promise; // 📦 Trả về promise
};
// 💡 Lợi ích: Tránh gọi API nhiều lần giống nhau (VD: User click nhiều lần)

// ═══════════════════════════════════════════════════════════
// RESPONSE CACHING (Cache kết quả response)
// ═══════════════════════════════════════════════════════════

const cache = new Map<string, { data: any; timestamp: number }>(); // 💾 Map lưu cache
// 💡 Key: URL của request
// 💡 Value: { data: response data, timestamp: thời điểm cache }

const cachedRequest = async (url: string, ttl = 5 * 60 * 1000) => {
  // 💡 ttl: Time To Live - Thời gian cache hợp lệ (mặc định: 5 phút)
  // 💡 5 * 60 * 1000 = 300,000ms = 5 phút

  const cached = cache.get(url); // 🔍 Kiểm tra xem đã có cache chưa

  // ✅ Nếu có cache và chưa hết hạn → Trả về cache
  if (cached && Date.now() - cached.timestamp < ttl) {
    console.log('💾 Returning cached data'); // 📝 Log khi dùng cache
    return cached.data; // 📦 Trả về data từ cache (không gọi API)
  }

  // 📡 Chưa có cache hoặc đã hết hạn → Gọi API
  const { data } = await axios.get(url); // 📡 Gọi API để lấy data mới

  // 💾 Lưu vào cache
  cache.set(url, {
    data, // 📦 Response data
    timestamp: Date.now(), // ⏰ Thời điểm cache (để tính TTL)
  });

  return data; // 📦 Trả về data mới
};
// 💡 Lợi ích: Giảm số lượng requests, tăng tốc độ (đặc biệt với GET requests)
// ⚠️ Lưu ý: Chỉ cache GET requests, không cache POST/PUT/DELETE
```

---

### **💡 Best Practices (Thực Hành Tốt Nhất)**

```typescript
// ✅ 1. Dùng instance thay vì default axios (Tạo instance riêng thay vì dùng global)
const api = axios.create({ baseURL: '/api' });
// 💡 Tại sao: Tránh conflict config, dễ test, dễ quản lý
// ❌ Tránh: axios.defaults.baseURL = '/api' (ảnh hưởng global)

// ✅ 2. TypeScript types (Sử dụng TypeScript để type-safe)
interface User {
  id: string;
  name: string;
}
const getUser = async (id: string): Promise<User> => {
  const { data } = await api.get<User>(`/users/${id}`); // 📦 Type-safe response
  // 💡 <User>: Generic type cho response data
  return data; // ✅ TypeScript biết data là User type
};

// ✅ 3. Centralize error handling trong interceptors (Tập trung xử lý lỗi)
api.interceptors.response.use(
  (response) => response, // ✅ Success: Trả về response như bình thường
  (error) => {
    handleError(error); // 🔧 Xử lý lỗi tập trung (toast, log, redirect...)
    return Promise.reject(error); // 🚫 Reject để caller có thể catch
    // 💡 Luôn reject để caller biết request failed
  }
);

// ✅ 4. Cancel requests on unmount (Hủy requests khi component unmount)
useEffect(() => {
  const controller = new AbortController(); // 🚫 Tạo AbortController
  // ... fetch data với signal
  api.get('/users', { signal: controller.signal }); // 📡 Request có signal
  return () => controller.abort(); // 🧹 Cleanup: Hủy request khi unmount
  // 💡 Quan trọng: Tránh memory leak, tránh update state sau khi unmount
}, []);

// ✅ 5. Set timeout để tránh hung requests (Đặt timeout để tránh request treo)
axios.create({ timeout: 10000 }); // ⏱️ 10 giây timeout
// 💡 Timeout: Hủy request nếu không nhận response sau X giây
// 💡 Tránh: Request treo mãi mãi, tốn tài nguyên

// ✅ 6. Separate auth instance (Tách instance cho auth để tránh infinite loop)
const authAPI = axios.create({ baseURL: '/auth' });
// 💡 Tại sao: Token refresh không dùng cùng instance → Tránh infinite loop
// 💡 VD: mainAPI gặp 401 → gọi authAPI.post('/refresh') → Không trigger lại interceptor
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
