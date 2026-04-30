# 🔌 Q14: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Interceptors là middleware functions (hàm trung gian) chạy trước/sau mỗi request/response, giúp tập trung hóa (centralize) authentication, error handling, logging, và data transformation."**

**💡 Giải thích đơn giản:**

- **Middleware**: Là các hàm chạy giữa chừng, không phải điểm đầu hay điểm cuối
- **Request Interceptor**: Chạy TRƯỚC khi request được gửi đi → Có thể sửa đổi request
- **Response Interceptor**: Chạy SAU khi nhận response → Có thể xử lý response hoặc lỗi
- **Centralize**: Tập trung logic vào một nơi → Không cần lặp lại code ở mọi nơi

**🔑 4 Use Cases Chính - 4 Trường Hợp Sử Dụng Chính:**

**1. Authentication & Token Management - Xác Thực & Quản Lý Token:**

- **Request interceptor**: **Tự động thêm JWT token** vào headers

  - Mỗi request tự động có token → Không cần thêm thủ công mỗi lần
  - Ví dụ: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`

- **Response interceptor**: **Tự động làm mới token hết hạn** (401 → refresh → retry)

  - Khi gặp lỗi 401 (Unauthorized) → Tự động gọi API refresh token
  - Lấy token mới → Cập nhật → Thử lại request ban đầu

- **Pattern (Mẫu)**: Lưu refresh token, khi 401 → call refresh API → update token → retry failed request
  - Flow: Request → 401 → Refresh token → Update token → Retry request → Success

**2. Global Error Handling - Xử Lý Lỗi Toàn Cục:**

- **Centralized error processing** - Xử lý lỗi tập trung, không cần try/catch mọi nơi

  - Tất cả lỗi được xử lý ở một chỗ → Code sạch hơn, dễ maintain
  - Không cần `try/catch` ở mỗi API call

- Handle network errors, timeouts, 401/403/500 uniformly - Xử lý thống nhất các lỗi

  - Network error (mất mạng) → Hiển thị thông báo "Kiểm tra kết nối"
  - Timeout (quá thời gian) → Hiển thị "Request quá lâu, vui lòng thử lại"
  - 401 (Unauthorized) → Tự động refresh token hoặc redirect login
  - 403 (Forbidden) → Hiển thị "Không có quyền truy cập"
  - 500 (Server Error) → Hiển thị "Lỗi server, vui lòng thử lại sau"

- Show toast notifications, log errors, redirect login - Hiển thị thông báo, ghi log, chuyển hướng
  - Toast: Thông báo popup cho user (VD: "Đăng nhập thành công!")
  - Log: Ghi lại lỗi để developer debug
  - Redirect: Tự động chuyển về trang login khi hết phiên

**3. Request/Response Transformation - Chuyển Đổi Dữ Liệu:**

- **Auto format** data: camelCase ↔ snake_case, date strings ↔ Date objects

  - **camelCase**: `userName`, `firstName` (JavaScript style)
  - **snake_case**: `user_name`, `first_name` (Python/Backend style)
  - Tự động chuyển đổi giữa 2 format → Frontend dùng camelCase, Backend dùng snake_case
  - Date strings: `"2024-01-01"` → `new Date("2024-01-01")` (Object Date)

- Add common headers: `Content-Type`, `Accept-Language`, device info

  - `Content-Type: application/json` → Báo server gửi JSON
  - `Accept-Language: vi-VN` → Báo server trả về tiếng Việt
  - Device info: `X-Device-ID`, `X-Platform` → Theo dõi thiết bị user

- Strip sensitive data trước khi log - Xóa dữ liệu nhạy cảm trước khi ghi log
  - Token, password, credit card → Không được log ra console/file
  - Tránh leak thông tin nhạy cảm trong logs

**4. Performance Monitoring & Retry - Theo Dõi Hiệu Năng & Thử Lại:**

- Track request **timing** (start time → duration) - Theo dõi thời gian request

  - Lưu thời điểm bắt đầu → Tính thời gian kết thúc → Duration
  - Ví dụ: Request bắt đầu lúc 10:00:00, kết thúc lúc 10:00:02 → Duration = 2 giây

- **Exponential backoff retry** cho failed requests - Thử lại với thời gian chờ tăng dần

  - Lần 1 fail → Đợi 1 giây → Thử lại
  - Lần 2 fail → Đợi 2 giây → Thử lại
  - Lần 3 fail → Đợi 4 giây → Thử lại
  - → Tăng gấp đôi mỗi lần (1s → 2s → 4s → 8s...)

- Circuit breaker pattern (dừng requests sau N failures) - Mẫu cầu chì
  - Nếu fail quá nhiều lần (VD: 5 lần) → Tự động ngắt (không gọi API nữa)
  - Sau một thời gian (VD: 60 giây) → Thử lại 1 lần
  - Nếu thành công → Mở lại (cho phép gọi API bình thường)
  - → Bảo vệ server khỏi quá tải khi server đang down

**💡 Kiến Thức Senior - Advanced Knowledge:**

- **Interceptor return Promise → có thể async/await bên trong**

  - Interceptor có thể là async function → Dùng `await` để chờ async operations
  - Ví dụ: `async (config) => { await refreshToken(); return config; }`

- **Eject interceptor - Xóa interceptor**:

  - `const id = axios.interceptors.request.use(...)` → Lưu ID
  - `axios.interceptors.request.eject(id)` → Xóa interceptor bằng ID
  - → Quan trọng để cleanup, tránh memory leak

- **Best practice: Tạo separate axios instances cho từng service**
  - `mainAPI` cho business logic (có token interceptor)
  - `authAPI` cho authentication (KHÔNG có token interceptor → Tránh infinite loop)
  - `uploadAPI` cho file uploads (timeout dài hơn, có progress tracking)
  - → Mỗi service có config và interceptors riêng → Không ảnh hưởng lẫn nhau

**⚡ Quick Summary:**

> Interceptors = middleware cho request/response. Transform data, add headers, handle errors

**💡 Ghi Nhớ:**

- 📤 **Request**: Transform request trước khi gửi (add token, headers)
- 📥 **Response**: Process response/error trước khi return
- 🔄 **Chain**: Multiple interceptors chạy theo thứ tự LIFO

**Trả lời:**

**🔥 Core Concepts - Khái Niệm Cốt Lõi:**

- **Interceptors - Bộ chặn**:

  - Middleware functions (hàm trung gian) được execute (thực thi) trước/sau mỗi HTTP request/response
  - Giống như "cửa kiểm soát" → Mọi request/response đều phải đi qua
  - Có thể sửa đổi, kiểm tra, xử lý request/response trước khi tiếp tục

- **Request Interceptors - Bộ chặn Request**:

  - Transform/modify (chuyển đổi/sửa đổi) requests trước khi gửi đến server
  - Có thể: add headers (thêm tiêu đề), auth tokens (token xác thực), logging (ghi log)
  - Ví dụ: Tự động thêm `Authorization: Bearer token` vào mọi request

- **Response Interceptors - Bộ chặn Response**:

  - Process responses (xử lý phản hồi) hoặc handle errors (xử lý lỗi) trước khi return về caller (người gọi)
  - Có thể: transform data (chuyển đổi dữ liệu), catch errors (bắt lỗi), retry (thử lại)
  - Ví dụ: Tự động refresh token khi gặp lỗi 401

- **Execution Order - Thứ Tự Thực Thi**:

  - **Request interceptors**: Chạy theo thứ tự **LIFO** (Last In First Out - Vào sau chạy trước)
    - Interceptor được add cuối cùng → Chạy đầu tiên
    - Ví dụ: Add 1 → Add 2 → Add 3 → Execution: 3 → 2 → 1
  - **Response interceptors**: Chạy theo thứ tự **FIFO** (First In First Out - Vào trước chạy trước)
    - Interceptor được add đầu tiên → Chạy đầu tiên
    - Ví dụ: Add 1 → Add 2 → Add 3 → Execution: 1 → 2 → 3

- **Chain of Responsibility Pattern - Mẫu Chuỗi Trách Nhiệm**:
  - Mỗi interceptor có thể modify (sửa đổi) data và pass (chuyển) sang interceptor tiếp theo
  - Giống như "dây chuyền" → Mỗi interceptor xử lý một phần → Chuyển tiếp
  - Ví dụ: Interceptor 1 thêm token → Interceptor 2 thêm header → Interceptor 3 log → Request sent

**✅ Ưu điểm - Advantages:**

- **Centralized Logic - Logic Tập Trung**:

  - Authentication (xác thực), logging (ghi log), error handling (xử lý lỗi) ở một nơi duy nhất
  - → Dễ maintain (bảo trì), dễ thay đổi, không cần sửa nhiều nơi

- **Code Reusability - Tái Sử Dụng Code**:

  - Không cần lặp lại logic cho mỗi request
  - → Viết 1 lần, dùng cho tất cả requests

- **Separation of Concerns - Tách Biệt Mối Quan Tâm**:

  - Tách logic infrastructure (cơ sở hạ tầng) ra khỏi business logic (logic nghiệp vụ)
  - → Code rõ ràng hơn, dễ test hơn

- **Global Error Handling - Xử Lý Lỗi Toàn Cục**:

  - Xử lý errors thống nhất (401, 403, 500, network errors)
  - → User experience tốt hơn, không cần xử lý lỗi ở mọi nơi

- **Request/Response Transformation - Chuyển Đổi Dữ Liệu**:

  - Format data tự động (camelCase ↔ snake_case)
  - → Frontend và Backend có thể dùng format khác nhau, tự động chuyển đổi

- **Performance Monitoring - Theo Dõi Hiệu Năng**:

  - Track request timing (theo dõi thời gian), add metrics (thêm số liệu)
  - → Phát hiện requests chậm, tối ưu hóa performance

- **Retry Logic - Logic Thử Lại**:

  - Tự động retry failed requests với exponential backoff
  - → Tăng khả năng thành công khi có lỗi tạm thời (network hiccup)

- **Token Refresh - Làm Mới Token**:
  - Automatically refresh expired tokens trước khi request
  - → User không bị logout đột ngột, trải nghiệm mượt mà hơn

**⚠️ Nhược điểm - Disadvantages:**

- **Side Effects - Tác Động Phụ**:

  - Có thể gây unexpected behaviors (hành vi không mong muốn) nếu không careful (cẩn thận)
  - → Phải test kỹ, đảm bảo không ảnh hưởng đến các requests khác

- **Debugging Complexity - Độ Phức Tạp Debug**:

  - Khó debug khi có nhiều interceptors chained (chuỗi)
  - → Khó biết interceptor nào gây lỗi, cần log chi tiết

- **Performance Overhead - Chi Phí Hiệu Năng**:

  - Mỗi interceptor adds processing time (thêm thời gian xử lý)
  - → Mỗi interceptor thêm ~0.1-1ms, nhiều interceptors → chậm hơn

- **Memory Leaks - Rò Rỉ Bộ Nhớ**:
  - Nếu không cleanup properly (dọn dẹp đúng cách) khi component unmount
  - → Interceptors vẫn còn trong memory → Chiếm RAM, có thể crash app

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
    // Kiểm tra: Không có response = lỗi mạng (network error, timeout, server down...)
    if (!error.response && originalRequest && !originalRequest._retry) {
      // ⚠️ Không có response = lỗi mạng (không phải lỗi từ server)
      // 💡 error.response = undefined → Server không phản hồi (mất mạng, timeout...)
      // 💡 originalRequest = Request ban đầu (để retry)
      // 💡 !originalRequest._retry = Chưa retry lần nào (tránh retry mãi mãi)

      originalRequest._retry = true; // 🏷️ Đánh dấu đã retry (tránh infinite loop)
      originalRequest._retryCount = (originalRequest._retryCount || 0) + 1; // ➕ Tăng số lần retry
      // 💡 _retryCount: Đếm số lần đã retry (0 → 1 → 2 → 3)

      if (originalRequest._retryCount <= 3) {
        // 3️⃣ Maximum 3 lần retry (tổng 4 lần: 1 lần đầu + 3 lần retry)
        console.log(
          `🔄 Retrying request (${originalRequest._retryCount}/3)...`
        );

        // ⏱️ Exponential backoff: Thời gian chờ tăng dần (1s, 2s, 3s)
        // 💡 Lần 1: 1000ms (1 giây)
        // 💡 Lần 2: 2000ms (2 giây)
        // 💡 Lần 3: 3000ms (3 giây)
        // → Cho server thời gian recover khi bị quá tải
        await new Promise((resolve) =>
          setTimeout(resolve, 1000 * originalRequest._retryCount)
        );

        return apiClient(originalRequest); // 🔁 Thử lại request ban đầu
        // 💡 Gọi lại request với config gốc → Có thể thành công lần này
      }
      // ⚠️ Nếu đã retry 3 lần vẫn fail → Không retry nữa, throw error
    }

    // 🔐 Case 2: TOKEN REFRESH - 401 Unauthorized (Làm mới token khi hết hạn)
    // Kiểm tra: 401 = Token hết hạn hoặc không hợp lệ
    if (
      error.response?.status === 401 &&
      originalRequest &&
      !originalRequest._retry
    ) {
      // 🔒 401 = Unauthorized (Token hết hạn hoặc không hợp lệ)
      // 💡 error.response?.status === 401 → Server trả về lỗi 401
      // 💡 originalRequest = Request ban đầu (để retry sau khi refresh)
      // 💡 !originalRequest._retry = Chưa refresh (tránh infinite loop)

      originalRequest._retry = true; // 🏷️ Đánh dấu đã refresh (tránh infinite loop)
      // 💡 Quan trọng: Đánh dấu ngay để tránh nhiều requests cùng refresh token

      try {
        // 🔄 Attempt to refresh token (Thử làm mới token)
        const refreshToken = localStorage.getItem('refreshToken'); // 📦 Lấy refresh token từ localStorage
        // 💡 Refresh token: Token dùng để lấy access token mới (thường có thời hạn dài hơn)

        // ⚠️ QUAN TRỌNG: Dùng axios riêng (KHÔNG dùng apiClient) để tránh infinite loop
        // 💡 Nếu dùng apiClient → Sẽ trigger lại interceptor → Infinite loop!
        const response = await axios.post('/auth/refresh', { refreshToken }); // 📡 Gọi API refresh
        // 💡 axios: Default axios instance (không có interceptors) hoặc authAPI riêng

        const { accessToken, refreshToken: newRefreshToken } = response.data; // 🎫 Nhận tokens mới từ server
        // 💡 Server trả về: { accessToken: '...', refreshToken: '...' }

        // 💾 Save new tokens (Lưu tokens mới vào localStorage)
        localStorage.setItem('accessToken', accessToken); // 💾 Lưu access token mới
        localStorage.setItem('refreshToken', newRefreshToken); // 💾 Lưu refresh token mới
        // 💡 Cập nhật tokens mới → Các requests sau sẽ dùng token mới

        // 🔁 Retry original request with new token (Thử lại request với token mới)
        if (originalRequest.headers) {
          originalRequest.headers.Authorization = `Bearer ${accessToken}`; // 🎫 Gắn token mới vào header
          // 💡 Cập nhật header với token mới → Request sẽ thành công
        }

        console.log(
          '🔐 Token refreshed successfully, retrying original request...'
        );
        return apiClient(originalRequest); // ✅ Thử lại request ban đầu với token mới
        // 💡 Request ban đầu sẽ thành công vì đã có token mới
      } catch (refreshError) {
        // ❌ Refresh failed → logout user (Refresh thất bại → đăng xuất)
        // 💡 Refresh token cũng hết hạn hoặc không hợp lệ → Phải đăng nhập lại
        console.error('❌ Token refresh failed, logging out...');
        localStorage.clear(); // 🗑️ Xóa hết localStorage (tokens, user data...)
        window.location.href = '/login'; // ↩️ Redirect về trang login
        return Promise.reject(refreshError); // 🚫 Reject error để caller biết
      }
    }

    // 🚫 Case 3: FORBIDDEN - 403 (No permission - Không có quyền)
    if (error.response?.status === 403) {
      // 🔒 403 = Forbidden (Không có quyền truy cập)
      // 💡 Khác với 401: 401 = Chưa đăng nhập, 403 = Đã đăng nhập nhưng không có quyền
      // 💡 Ví dụ: User thường cố truy cập trang admin → 403
      console.error('🚫 Access Forbidden - You do not have permission');
      // 🔔 Show toast notification or redirect (Hiển thị thông báo hoặc redirect)
      // toast.error('You do not have permission to access this resource');
      // 💡 Có thể redirect về trang chủ hoặc hiển thị thông báo lỗi
    }

    // ⚠️ Case 4: NOT FOUND - 404 (Không tìm thấy tài nguyên)
    if (error.response?.status === 404) {
      // 🔍 404 = Not Found (URL không tồn tại)
      // 💡 Ví dụ: GET /api/users/999 → User không tồn tại → 404
      console.error('⚠️ Resource not found');
      // 🎯 Handle 404 error (Xử lý lỗi 404 - VD: redirect to 404 page)
      // 💡 Có thể redirect về trang 404 hoặc hiển thị thông báo "Không tìm thấy"
    }

    // 🔥 Case 5: SERVER ERROR - 500+ (Lỗi server nội bộ)
    if (error.response?.status && error.response.status >= 500) {
      // 💥 500+ = Server Error (Lỗi server nội bộ)
      // 💡 500 = Internal Server Error (Lỗi code, database...)
      // 💡 502 = Bad Gateway (Server proxy lỗi)
      // 💡 503 = Service Unavailable (Server quá tải)
      console.error('🔥 Server Error - Please try again later');
      // 🔔 Show user-friendly error message (Hiển thị thông báo thân thiện)
      // toast.error('Server error occurred. Please try again later.');
      // 💡 Không nên hiển thị chi tiết lỗi cho user (bảo mật)
    }

    // 🌐 Case 6: NETWORK ERROR - No response from server (Lỗi mạng)
    if (error.code === 'ECONNABORTED' || error.message.includes('timeout')) {
      // ⏱️ Timeout hoặc mất kết nối
      // 💡 error.code === 'ECONNABORTED' → Request bị hủy (timeout hoặc abort)
      // 💡 error.message.includes('timeout') → Request quá thời gian chờ
      console.error('⏱️ Request Timeout - Check your connection');
      // 📶 toast.error('Request timeout. Please check your internet connection.');
      // 💡 User nên kiểm tra kết nối mạng hoặc thử lại sau
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
// 7. ADVANCED: Request Deduplication - Loại Bỏ Requests Trùng Lặp
// ============================================
/**
 * Vietnamese Explanation - Giải Thích Tiếng Việt:
 * - Ngăn chặn duplicate requests (cùng URL + method + params)
 *   → Tránh gọi API nhiều lần giống nhau (VD: User click nhiều lần button)
 * - Nếu có request đang pending (đang chạy), return kết quả của request đó
 *   → Reuse (tái sử dụng) kết quả thay vì tạo request mới
 * - Useful khi user click nhiều lần hoặc component re-render
 *   → Tránh spam server, tiết kiệm bandwidth
 */
const pendingRequests = new Map<string, Promise<any>>(); // 📋 Map lưu các pending requests
// 💡 Key: `${method}:${url}:${params}` (VD: 'GET:/api/users:{"page":1}')
// 💡 Value: Promise của request đó (đang chạy)

apiClient.interceptors.request.use(
  (config) => {
    // 🔑 Create unique key for this request (Tạo key duy nhất cho request)
    // 💡 Key = method + URL + params → Identify request giống nhau
    const requestKey = `${config.method}:${config.url}:${JSON.stringify(
      config.params
    )}`;
    // 💡 Ví dụ: 'GET:/api/users:{"page":1,"limit":10}'
    // 💡 2 requests giống nhau → Cùng key → Detect duplicate

    // ❓ Nếu đã có request pending với key này (Request trùng lặp)
    if (pendingRequests.has(requestKey)) {
      console.log('🔄 Duplicate request detected, using pending request...');
      // 🔁 Return pending promise (sẽ reject này để reuse pending request)
      // 💡 Throw error đặc biệt với flag __DUPLICATE__ để error handler biết
      throw {
        __DUPLICATE__: true, // 🏷️ Đánh dấu là duplicate (không phải lỗi thật)
        promise: pendingRequests.get(requestKey), // 📦 Trả về promise đang pending
        // 💡 Promise này sẽ resolve/reject khi request đầu tiên xong
      };
    }

    // 💾 Store request key in config for later cleanup (Lưu key để cleanup sau)
    (config as any).__requestKey = requestKey;
    // 💡 Lưu key vào config → Response interceptor sẽ xóa khỏi pendingRequests

    return config; // ✅ Tiếp tục request bình thường (không duplicate)
  },
  (error) => {
    // ✅ Nếu là duplicate request, return pending promise (Trả về pending promise)
    // 💡 Error handler: Bắt error từ request interceptor
    if (error.__DUPLICATE__) {
      return error.promise; // 🔁 Reuse kết quả của request đang chạy
      // 💡 Không tạo request mới → Tiết kiệm bandwidth, tránh spam server
    }
    return Promise.reject(error); // ❌ Lỗi thật → Reject bình thường
  }
);

apiClient.interceptors.response.use(
  (response) => {
    // 🗑️ Remove from pending requests (Xóa khỏi pending requests khi hoàn thành)
    // 💡 Quan trọng: Cleanup để tránh memory leak và cho phép request mới
    const requestKey = (response.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey); // 🗑️ Xóa request key khỏi Map
      // 💡 Sau khi xóa → Request mới với cùng key có thể được tạo lại
    }
    return response; // ✅ Trả về response bình thường
  },
  (error) => {
    // 🗑️ Remove from pending requests even on error (Xóa ngay cả khi lỗi)
    // 💡 Quan trọng: Phải cleanup cả khi lỗi (không chỉ khi thành công)
    const requestKey = (error.config as any).__requestKey;
    if (requestKey) {
      pendingRequests.delete(requestKey); // 🗑️ Xóa request key khỏi Map
      // 💡 Nếu không xóa → Request key vẫn còn → Không thể tạo request mới
    }
    return Promise.reject(error); // ❌ Reject error để caller xử lý
  }
);
// 💡 Tại sao cleanup quan trọng?
// - Nếu không xóa → pendingRequests Map sẽ lớn dần → Memory leak
// - Nếu không xóa → Request mới với cùng key sẽ bị block (vì Map vẫn có key cũ)

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

### **❌ Problem: Dùng Default Axios - Vấn Đề Khi Dùng Axios Mặc Định**

```typescript
// ❌ BAD: Global axios - shared interceptors, config cho TẤT CẢ requests
// 💡 Vấn đề: Dùng axios mặc định → Tất cả requests dùng chung config và interceptors
import axios from 'axios';

// ⚠️ Problem 1: Tất cả requests dùng chung config
axios.defaults.baseURL = 'https://api.example.com'; // 🌐 Ảnh hưởng GLOBAL - Tất cả requests!
// 💡 Tất cả requests (kể cả upload, auth, public API) đều dùng baseURL này
axios.defaults.timeout = 5000; // ⏱️ Ảnh hưởng GLOBAL - Tất cả requests!
// 💡 Upload file lớn cũng chỉ có 5s timeout → Sẽ timeout!

// ⚠️ Problem 2: Interceptors apply cho TẤT CẢ
axios.interceptors.request.use((config) => {
  config.headers.Authorization = 'Bearer token'; // 🔐 Cả auth API và public API đều có token!
  return config; // 😱 Cả auth API và public API đều có token!
  // 💡 Vấn đề: Public API (blog, landing page) không cần token → Lãng phí, có thể gây lỗi
});

// ⚠️ Problem 3: Không thể config riêng cho từng service
await axios.get('/users'); // 🔍 Uses global config
await axios.post('https://upload.api.com/files', file); // 😱 Cũng dùng config trên!
// 💡 Upload API cần timeout dài hơn (60s) nhưng chỉ có 5s → Timeout!
```

**Hậu quả - Consequences:**

- ❌ **Conflict config giữa các services** (timeout khác nhau)

  - Upload API cần 60s timeout nhưng chỉ có 5s → Timeout!
  - Auth API cần 5s timeout nhưng có thể bị ảnh hưởng bởi config khác

- ❌ **Interceptors apply cho cả requests không cần** (auth token ở public API)

  - Public API (blog, landing page) không cần token → Lãng phí, có thể gây lỗi
  - Analytics API không cần token → Không cần thiết

- ❌ **Khó debug** (không biết request nào dùng config gì)

  - Tất cả requests dùng chung config → Khó biết request nào có vấn đề
  - Khó trace lỗi vì không biết interceptor nào ảnh hưởng

- ❌ **Khó test** (global state affects tests)

  - Global config ảnh hưởng đến tất cả tests → Tests có thể fail không rõ lý do
  - Khó mock vì phải mock global axios

- ❌ **Memory leak khi không cleanup interceptors**
  - Interceptors được add vào global axios → Không cleanup được dễ dàng
  - Component unmount nhưng interceptors vẫn còn → Memory leak

---

### **✅ Solution: Separate Axios Instances - Giải Pháp: Tách Axios Instances**

```typescript
// ✅ GOOD: Mỗi service có instance riêng
// 💡 Mỗi instance độc lập → Config và interceptors riêng → Không ảnh hưởng lẫn nhau

const mainAPI = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
}); // 🌐 Main API - 10s timeout
// 💡 Dùng cho: Business logic (users, posts, comments...)
// 💡 Có token interceptor, error handling, logging

const authAPI = axios.create({
  baseURL: 'https://auth.example.com',
  timeout: 5000,
}); // 🔐 Auth API - 5s timeout (nhanh hơn)
// 💡 Dùng cho: Authentication (login, register, refresh token...)
// 💡 KHÔNG có token interceptor (tránh infinite loop khi refresh token)
// 💡 Timeout ngắn hơn vì auth requests nên nhanh

const uploadAPI = axios.create({
  baseURL: 'https://upload.example.com',
  timeout: 60000,
}); // 📤 Upload API - 60s timeout (file lớn)
// 💡 Dùng cho: File uploads (images, documents...)
// 💡 Timeout dài hơn vì file lớn cần nhiều thời gian
// 💡 Có progress tracking interceptor

// ✅ Mỗi instance có interceptors riêng, không ảnh hưởng lẫn nhau
mainAPI.interceptors.request.use((config) => {
  /* 🎯 Only for mainAPI - Chỉ ảnh hưởng mainAPI */
  // 💡 Thêm token, logging, request ID...
});
authAPI.interceptors.request.use((config) => {
  /* 🔐 Only for authAPI - Chỉ ảnh hưởng authAPI */
  // 💡 KHÔNG thêm token (tránh infinite loop)
  // 💡 Chỉ thêm device fingerprint, rate limit handling...
});
// 💡 Upload API có interceptors riêng cho progress tracking
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

### **5. Micro-Frontend Case - Dùng Axios Instance Trong Micro FE**

Trong kiến trúc **micro-frontend (MFE)**, mỗi remote app có lifecycle, domain nghiệp vụ và release cycle riêng. Vì vậy **không nên dùng global axios/default axios** cho toàn hệ thống, vì interceptor/config của remote này có thể ảnh hưởng remote khác.

**Nguyên tắc senior:**

- **Shell/host quản lý context chung**: auth token provider, tenant, locale, correlation id, environment config.
- **Mỗi remote tạo axios instance riêng** bằng factory, không mutate global `axios.defaults`.
- **Interceptor phải scoped theo instance** và cleanup khi remote unmount nếu interceptor được đăng ký trong runtime lifecycle.
- **Auth/refresh dùng instance riêng** để tránh infinite loop.
- **Không share mutable singleton bừa bãi** giữa các remote, vì dễ gây coupling, duplicate interceptor và khó debug.

```typescript
// shared/http/createHttpClient.ts
import axios, { AxiosInstance, InternalAxiosRequestConfig } from 'axios';

type HttpClientOptions = {
  baseURL: string;
  getAccessToken?: () => string | null | Promise<string | null>;
  getTenantId?: () => string | null;
  onUnauthorized?: () => void;
};

export function createHttpClient(options: HttpClientOptions): AxiosInstance {
  const client = axios.create({
    baseURL: options.baseURL,
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json',
    },
  });

  client.interceptors.request.use(async (config: InternalAxiosRequestConfig) => {
    const token = await options.getAccessToken?.();
    const tenantId = options.getTenantId?.();

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    if (tenantId) {
      config.headers['X-Tenant-ID'] = tenantId;
    }

    return config;
  });

  client.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        options.onUnauthorized?.();
      }

      return Promise.reject(error);
    }
  );

  return client;
}
```

Remote app tạo instance riêng từ context do shell truyền vào:

```typescript
// remote-order/bootstrap.ts
import { createHttpClient } from '@shared/http/createHttpClient';

type ShellContext = {
  apiBaseUrls: {
    order: string;
  };
  auth: {
    getAccessToken: () => Promise<string | null>;
    logout: () => void;
  };
  tenant: {
    getTenantId: () => string | null;
  };
};

export function createOrderApi(shellContext: ShellContext) {
  return createHttpClient({
    baseURL: shellContext.apiBaseUrls.order,
    getAccessToken: shellContext.auth.getAccessToken,
    getTenantId: shellContext.tenant.getTenantId,
    onUnauthorized: shellContext.auth.logout,
  });
}
```

Nếu remote cần interceptor tạm thời theo màn hình/component, phải eject khi unmount:

```typescript
useEffect(() => {
  const requestId = orderAPI.interceptors.request.use((config) => {
    config.headers['X-Feature-Name'] = 'order-ticket';
    return config;
  });

  return () => {
    orderAPI.interceptors.request.eject(requestId);
  };
}, [orderAPI]);
```

**Pattern nên dùng trong Micro FE:**

| Case | Nên làm |
| --- | --- |
| Nhiều remote gọi nhiều backend khác nhau | Mỗi remote/service có axios instance riêng |
| Auth token dùng chung | Shell expose `getAccessToken()`, remote không tự đọc storage nếu không cần |
| Refresh token | Dùng `authAPI` riêng hoặc để shell/auth module xử lý |
| Remote mount/unmount nhiều lần | Eject interceptors runtime để tránh duplicate |
| Multi-tenant/locale/correlation id | Inject qua request interceptor từ shell context |
| Debug production | Thêm `X-Request-ID`/correlation id per request |

**Anti-patterns trong Micro FE:**

```typescript
// ❌ Remote mutate global axios: ảnh hưởng shell và remote khác
axios.defaults.baseURL = '/order-api';
axios.interceptors.request.use(addOrderHeaders);

// ❌ Remote tự đọc token từ localStorage ở nhiều nơi: coupling với auth implementation
const token = localStorage.getItem('accessToken');

// ❌ Mỗi lần mount lại add interceptor nhưng không eject
orderAPI.interceptors.request.use(addFeatureHeader);
```

**Cách trả lời phỏng vấn:**

> Trong micro-frontend, tôi không dùng global axios vì interceptor là global side effect. Tôi tạo axios instance bằng factory cho từng remote/service, inject auth/env/tenant từ shell context, tách auth refresh bằng instance riêng, và cleanup interceptor khi remote/component unmount. Cách này tránh cross-remote pollution, duplicate interceptors và giúp debug request rõ hơn.

---

### **6. Request Queue & Rate Limiting**

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

// ✅ 2. Response Caching (GET only) (Cache kết quả - Chỉ GET)
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

### **2. Axios Instance & Configuration**

#### **2.1. Create Custom Instance**

```typescript
// ═══════════════════════════════════════════════════════════
// CREATE AXIOS INSTANCE - Best Practice
// ═══════════════════════════════════════════════════════════

import axios, { AxiosInstance } from 'axios';

// Tạo instance với base config
const apiClient: AxiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'https://api.example.com',
  timeout: 10000, // 10 seconds
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },

  // Credentials & CSRF
  withCredentials: true, // Send cookies với cross-origin requests
  xsrfCookieName: 'XSRF-TOKEN', // CSRF token cookie name
  xsrfHeaderName: 'X-XSRF-TOKEN', // CSRF token header name

  // Validate status
  validateStatus: (status) => status >= 200 && status < 500,
});

// ═══════════════════════════════════════════════════════════
// MULTIPLE INSTANCES - Cho different APIs
// ═══════════════════════════════════════════════════════════

// Main API
const mainAPI = axios.create({
  baseURL: 'https://api.main.com',
  timeout: 5000,
});

// Auth API (separate instance để tránh infinite loop trong token refresh)
const authAPI = axios.create({
  baseURL: 'https://auth.main.com',
  timeout: 3000,
});

// Analytics API
const analyticsAPI = axios.create({
  baseURL: 'https://analytics.main.com',
  timeout: 15000,
});

// File Upload API
const uploadAPI = axios.create({
  baseURL: 'https://upload.main.com',
  timeout: 60000, // 1 minute for large files
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

// Sử dụng
mainAPI.get('/users');
authAPI.post('/login', credentials);
analyticsAPI.post('/track', event);
uploadAPI.post('/files', formData);
```

---

### **3. Request Cancellation - Hủy Request**

```typescript
// ═══════════════════════════════════════════════════════════
// ABORT CONTROLLER (Modern - Axios 0.22+)
// ═══════════════════════════════════════════════════════════

// 🚫 AbortController - Công cụ để hủy request
const controller = new AbortController();
// 💡 AbortController: Cho phép hủy request bất cứ lúc nào
// 💡 Signal: Đối tượng để truyền vào axios config

// 📡 Gửi request với signal → Có thể hủy được
axios
  .get('/api/users', {
    signal: controller.signal, // 🔗 Gắn signal vào request
  })
  .then((response) => {
    console.log(response.data); // ✅ Nhận dữ liệu nếu thành công
  })
  .catch((error) => {
    // ❌ Xử lý lỗi (có thể là lỗi thật hoặc do cancel)
    if (axios.isCancel(error)) {
      // ✅ Kiểm tra xem có phải do cancel không
      console.log('Request canceled:', error.message);
      // 💡 axios.isCancel(): Kiểm tra error có phải do cancel không
      // 💡 Nếu là cancel → Không phải lỗi thật, không cần xử lý
    }
  });

// 🚫 Cancel request - Hủy request ngay lập tức
controller.abort('User canceled the request');
// 💡 abort(): Dừng request đang chạy, trigger catch với CancelError
// 💡 Message: Thông điệp giải thích lý do hủy

// ═══════════════════════════════════════════════════════════
// USE CASE 1: Cancel on Component Unmount (React)
// ═══════════════════════════════════════════════════════════

import { useEffect, useState } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // 🚫 Tạo AbortController trong useEffect
    const controller = new AbortController();
    // 💡 Mỗi lần component mount → Tạo controller mới

    const fetchUsers = async () => {
      try {
        // 📡 Gửi request với signal → Có thể hủy được
        const { data } = await axios.get('/api/users', {
          signal: controller.signal, // 🔗 Gắn signal vào request
        });
        setUsers(data); // ✅ Lưu data vào state nếu thành công
      } catch (error) {
        // ❌ Xử lý lỗi (chỉ log lỗi thật, không log cancel)
        if (!axios.isCancel(error)) {
          // 💡 !axios.isCancel(): Chỉ log lỗi thật (không phải do cancel)
          console.error('Error fetching users:', error);
        }
        // 💡 Nếu là cancel → Không log (bình thường, không phải lỗi)
      }
    };

    fetchUsers(); // 🚀 Gọi hàm fetch users

    // 🧹 Cleanup: Cancel request khi component unmount
    return () => {
      controller.abort(); // 🚫 Hủy request khi component unmount
      // 💡 Quan trọng: Tránh memory leak, tránh update state sau khi unmount
      // 💡 Nếu không cleanup → Request vẫn chạy → Có thể update state sau khi unmount → Error
    };
  }, []); // 💡 Empty dependency array = Chỉ chạy 1 lần khi mount

  return <div>...</div>;
}

// ═══════════════════════════════════════════════════════════
// USE CASE 2: Cancel Previous Search Request
// ═══════════════════════════════════════════════════════════

function SearchComponent() {
  const [query, setQuery] = useState('');
  const controllerRef = useRef<AbortController | null>(null);

  const handleSearch = async (searchQuery: string) => {
    // 🚫 Cancel previous request nếu có - Hủy request cũ trước khi gửi mới
    if (controllerRef.current) {
      controllerRef.current.abort(); // Hủy request cũ
      // 💡 Quan trọng: Tránh race condition (request cũ về sau → ghi đè kết quả mới)
    }

    // 🆕 Create new controller - Tạo controller mới cho request này
    controllerRef.current = new AbortController();

    try {
      // 📡 Gửi request search với signal → Có thể hủy được
      const { data } = await axios.get('/api/search', {
        params: { q: searchQuery }, // 🔍 Query params: search term
        signal: controllerRef.current.signal, // 🔗 Gắn signal để có thể hủy
      });
      setResults(data); // ✅ Lưu kết quả vào state
    } catch (error) {
      // ❌ Xử lý lỗi (chỉ log lỗi thật, không log cancel)
      if (!axios.isCancel(error)) {
        console.error('Search error:', error);
      }
      // 💡 Nếu là cancel → Không log (bình thường khi user gõ tiếp)
    }
  };

  // ⏱️ Debounce search - Chờ user ngừng gõ 500ms mới search
  useEffect(() => {
    // 💡 Debounce: Mỗi lần query thay đổi → Reset timer → Đợi 500ms
    const timer = setTimeout(() => {
      if (query) {
        // ✅ Chỉ search nếu có query (không search khi query rỗng)
        handleSearch(query);
      }
    }, 500); // ⏱️ Đợi 500ms sau khi user ngừng gõ

    // 🧹 Cleanup: Clear timer khi query thay đổi hoặc unmount
    return () => clearTimeout(timer);
    // 💡 Quan trọng: Clear timer để tránh memory leak
    // 💡 Nếu không clear → Timer vẫn chạy → Có thể search với query cũ
  }, [query]); // 💡 Chạy lại mỗi khi query thay đổi
}

// ═══════════════════════════════════════════════════════════
// CANCEL TOKEN (Legacy - Deprecated nhưng vẫn hoạt động)
// ═══════════════════════════════════════════════════════════

const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios
  .get('/api/users', {
    cancelToken: source.token,
  })
  .catch((error) => {
    if (axios.isCancel(error)) {
      console.log('Request canceled:', error.message);
    }
  });

// Cancel
source.cancel('Operation canceled by user');
```

---

### **4. File Upload & Download**

#### **4.1. File Upload with Progress**

```typescript
// ═══════════════════════════════════════════════════════════
// UPLOAD SINGLE FILE
// ═══════════════════════════════════════════════════════════

const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('userId', '123');

  try {
    const { data } = await axios.post('/api/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        const percentCompleted = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total!
        );
        console.log(`Upload progress: ${percentCompleted}%`);
        // Update UI progress bar
      },
    });

    return data;
  } catch (error) {
    console.error('Upload failed:', error);
    throw error;
  }
};

// ═══════════════════════════════════════════════════════════
// UPLOAD MULTIPLE FILES
// ═══════════════════════════════════════════════════════════

const uploadMultipleFiles = async (files: File[]) => {
  const formData = new FormData();

  files.forEach((file, index) => {
    formData.append(`file${index}`, file);
  });

  const { data } = await axios.post('/api/upload-multiple', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    onUploadProgress: (progressEvent) => {
      const percentCompleted = Math.round(
        (progressEvent.loaded * 100) / progressEvent.total!
      );
      console.log(`Total upload progress: ${percentCompleted}%`);
    },
  });

  return data;
};

// ═══════════════════════════════════════════════════════════
// REACT COMPONENT - File Upload với Progress Bar
// ═══════════════════════════════════════════════════════════

function FileUploader() {
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploading, setUploading] = useState(false);

  const handleFileUpload = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    setUploading(true);

    try {
      await axios.post('/api/upload', formData, {
        onUploadProgress: (progressEvent) => {
          const progress = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total!
          );
          setUploadProgress(progress);
        },
      });

      alert('Upload successful!');
    } catch (error) {
      console.error('Upload failed:', error);
    } finally {
      setUploading(false);
      setUploadProgress(0);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileUpload} disabled={uploading} />
      {uploading && (
        <div className="progress-bar">
          <div style={{ width: `${uploadProgress}%` }}>{uploadProgress}%</div>
        </div>
      )}
    </div>
  );
}
```

#### **4.2. File Download**

```typescript
// ═══════════════════════════════════════════════════════════
// DOWNLOAD FILE
// ═══════════════════════════════════════════════════════════

const downloadFile = async (fileId: string) => {
  try {
    const response = await axios.get(`/api/files/${fileId}`, {
      responseType: 'blob', // ✅ Important cho files
      onDownloadProgress: (progressEvent) => {
        const percentCompleted = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total!
        );
        console.log(`Download progress: ${percentCompleted}%`);
      },
    });

    // Create blob URL và trigger download
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'filename.pdf'); // Filename
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Download failed:', error);
  }
};

// ═══════════════════════════════════════════════════════════
// DOWNLOAD DIFFERENT FILE TYPES
// ═══════════════════════════════════════════════════════════

const downloadPDF = async () => {
  const response = await axios.get('/api/report.pdf', {
    responseType: 'blob',
  });

  const blob = new Blob([response.data], { type: 'application/pdf' });
  const url = window.URL.createObjectURL(blob);
  window.open(url); // Open in new tab
};

const downloadExcel = async () => {
  const response = await axios.get('/api/export.xlsx', {
    responseType: 'arraybuffer', // For Excel files
  });

  const blob = new Blob([response.data], {
    type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  });

  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'export.xlsx';
  link.click();
};
```

---

### **5. Error Handling - Xử Lý Lỗi Chi Tiết**

```typescript
// ═══════════════════════════════════════════════════════════
// ERROR STRUCTURE
// ═══════════════════════════════════════════════════════════

try {
  const response = await axios.get('/api/users');
} catch (error) {
  if (axios.isAxiosError(error)) {
    // ✅ Type-safe error handling

    if (error.response) {
      // ❌ Server responded với status code ngoài 2xx
      console.error('Response error:');
      console.error('Status:', error.response.status);
      console.error('Data:', error.response.data);
      console.error('Headers:', error.response.headers);

      // Handle specific status codes
      switch (error.response.status) {
        case 400:
          console.error('Bad Request - Invalid data');
          break;
        case 401:
          console.error('Unauthorized - Please login');
          // Redirect to login
          window.location.href = '/login';
          break;
        case 403:
          console.error('Forbidden - No permission');
          break;
        case 404:
          console.error('Not Found');
          break;
        case 422:
          console.error('Validation Error');
          // Show validation errors
          const validationErrors = error.response.data.errors;
          break;
        case 429:
          console.error('Too Many Requests - Rate limited');
          break;
        case 500:
          console.error('Server Error');
          break;
        case 503:
          console.error('Service Unavailable');
          break;
      }
    } else if (error.request) {
      // ❌ Request sent nhưng không nhận được response
      console.error('Request error - No response received');
      console.error('Possible causes:');
      console.error('- Network error');
      console.error('- CORS issue');
      console.error('- Request timeout');
      console.error('- Server not responding');
    } else {
      // ❌ Lỗi khi setup request
      console.error('Setup error:', error.message);
    }

    console.error('Config:', error.config);
  } else {
    // Lỗi khác (không phải Axios error)
    console.error('Unexpected error:', error);
  }
}

// ═══════════════════════════════════════════════════════════
// CUSTOM ERROR HANDLER
// ═══════════════════════════════════════════════════════════

interface ApiErrorResponse {
  success: boolean;
  message: string;
  status: number | null;
  data: any;
  errors?: Record<string, string[]>; // Validation errors
}

const handleAxiosError = (error: unknown): ApiErrorResponse => {
  if (axios.isAxiosError(error)) {
    const message = error.response?.data?.message || error.message;
    const status = error.response?.status || null;
    const errors = error.response?.data?.errors;

    return {
      success: false,
      message,
      status,
      data: error.response?.data,
      errors,
    };
  }

  return {
    success: false,
    message: 'An unexpected error occurred',
    status: null,
    data: null,
  };
};

// Usage
try {
  const response = await axios.post('/api/users', userData);
  return {
    success: true,
    data: response.data,
    message: 'Success',
    status: 200,
  };
} catch (error) {
  return handleAxiosError(error);
}
```

---

### **6. Advanced Features**

#### **6.1. Response Caching**

```typescript
// ═══════════════════════════════════════════════════════════
// SIMPLE CACHE IMPLEMENTATION
// ═══════════════════════════════════════════════════════════

interface CacheEntry {
  data: any;
  timestamp: number;
}

const cache = new Map<string, CacheEntry>();

const cachedRequest = async (
  url: string,
  config = {},
  ttl = 5 * 60 * 1000 // 5 minutes
) => {
  const cacheKey = `${url}:${JSON.stringify(config)}`;

  // Check cache
  const cached = cache.get(cacheKey);
  if (cached && Date.now() - cached.timestamp < ttl) {
    console.log('✅ Returning cached data');
    return cached.data;
  }

  // Fetch fresh data
  const response = await axios.get(url, config);
  cache.set(cacheKey, {
    data: response.data,
    timestamp: Date.now(),
  });

  return response.data;
};
```

---

### **💡 Best Practices**

```typescript
// ✅ 1. Luôn dùng axios instance thay vì default axios
const api = axios.create({ baseURL: '/api' });

// ✅ 2. TypeScript types cho responses
interface User {
  id: string;
  name: string;
}

const getUser = async (id: string): Promise<User> => {
  const { data } = await api.get<User>(`/users/${id}`);
  return data;
};

// ✅ 3. Centralize error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Handle globally
    handleAxiosError(error);
    return Promise.reject(error);
  }
);

// ✅ 4. Cancel requests on component unmount
useEffect(() => {
  const controller = new AbortController();
  // ... fetch data
  return () => controller.abort();
}, []);

// ✅ 5. Use timeout để avoid hung requests
axios.create({ timeout: 10000 });
```
