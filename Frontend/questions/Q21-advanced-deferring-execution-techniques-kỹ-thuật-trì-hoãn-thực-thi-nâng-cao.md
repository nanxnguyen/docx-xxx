# ⏱️ Q21: Advanced Deferring Execution Techniques - Kỹ Thuật Trì Hoãn Thực Thi Nâng Cao




```typescript
// ═══════════════════════════════════════════════════════════
// INSTALLATION
// ═══════════════════════════════════════════════════════════

// npm install axios
// yarn add axios
// pnpm add axios

import axios from 'axios';

// ═══════════════════════════════════════════════════════════
// BASIC REQUESTS
// ═══════════════════════════════════════════════════════════

// GET request
const getUsers = async () => {
  try {
    const response = await axios.get('/api/users');
    console.log(response.data); // ✅ Auto JSON parsing
    console.log(response.status); // 200
    console.log(response.headers); // Headers object
    console.log(response.config); // Request config
  } catch (error) {
    console.error(error);
  }
};

// POST request
const createUser = async (userData: any) => {
  const response = await axios.post('/api/users', userData);
  // ✅ Auto JSON stringify - không cần JSON.stringify()
  return response.data;
};

// PUT/PATCH/DELETE
const updateUser = (id: string, data: any) => axios.put(`/api/users/${id}`, data);
const patchUser = (id: string, data: any) => axios.patch(`/api/users/${id}`, data);
const deleteUser = (id: string) => axios.delete(`/api/users/${id}`);
```

#### **1.2. Axios vs Fetch API - So Sánh Chi Tiết**

```typescript
// ═══════════════════════════════════════════════════════════
// FETCH API - Nhiều bước thủ công
// ═══════════════════════════════════════════════════════════

// ❌ Fetch: Manual JSON parsing + error checking
const fetchUsers = async () => {
  try {
    const response = await fetch('/api/users');
    
    // ❌ Phải check response.ok manually
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    // ❌ Phải parse JSON manually
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
};

// POST với fetch - verbose
const createUserFetch = async (userData: any) => {
  const response = await fetch('/api/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // ❌ Manual header
    },
    body: JSON.stringify(userData), // ❌ Manual stringify
  });
  
  if (!response.ok) throw new Error('Failed');
  return await response.json(); // ❌ Manual parse
};

// ═══════════════════════════════════════════════════════════
// AXIOS - Tự động & ngắn gọn
// ═══════════════════════════════════════════════════════════

// ✅ Axios: Clean & automatic
const axiosUsers = async () => {
  const { data } = await axios.get('/api/users');
  // ✅ Auto JSON parse
  // ✅ Auto throw error nếu status >= 400
  return data;
};

// POST với axios - simple
const createUserAxios = async (userData: any) => {
  const { data } = await axios.post('/api/users', userData);
  // ✅ Auto set Content-Type: application/json
  // ✅ Auto JSON.stringify()
  return data;
};

// ═══════════════════════════════════════════════════════════
// COMPARISON TABLE
// ═══════════════════════════════════════════════════════════

/**
 * ┌────────────────────┬──────────────────┬──────────────────┐
 * │ Feature            │ Fetch            │ Axios            │
 * ├────────────────────┼──────────────────┼──────────────────┤
 * │ JSON Transform     │ ❌ Manual        │ ✅ Automatic     │
 * │ Error Handling     │ ❌ Manual check  │ ✅ Auto throw    │
 * │ Timeout            │ ❌ AbortControl  │ ✅ Built-in      │
 * │ Interceptors       │ ❌ None          │ ✅ Built-in      │
 * │ Progress Events    │ ❌ Complex       │ ✅ Easy          │
 * │ Cancel Requests    │ ⚠️ AbortControl  │ ✅ Multiple ways │
 * │ Browser Support    │ ✅ Native        │ ⚠️ +13KB bundle  │
 * │ CSRF Protection    │ ❌ Manual        │ ✅ Built-in      │
 * │ Base URL           │ ❌ Manual        │ ✅ Config        │
 * │ Request/Response   │ ❌ None          │ ✅ Transform     │
 * └────────────────────┴──────────────────┴──────────────────┘
 */
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
    'Accept': 'application/json',
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

#### **2.2. Full Request Configuration**

```typescript
// ═══════════════════════════════════════════════════════════
// COMPLETE CONFIG OPTIONS
// ═══════════════════════════════════════════════════════════

const config = {
  // URL
  url: '/users',
  baseURL: 'https://api.example.com',
  
  // Method
  method: 'get', // 'get' | 'post' | 'put' | 'delete' | 'patch' | 'head' | 'options'
  
  // Headers
  headers: {
    'Authorization': 'Bearer token',
    'X-Custom-Header': 'value',
  },
  
  // Query params (?key=value)
  params: {
    page: 1,
    limit: 10,
    sort: 'createdAt:desc',
  },
  
  // Params serializer
  paramsSerializer: {
    serialize: (params) => {
      // Custom serialization
      return Object.entries(params)
        .map(([key, val]) => `${key}=${encodeURIComponent(val)}`)
        .join('&');
    },
  },
  
  // Request body
  data: {
    name: 'John',
    age: 30,
  },
  
  // Timeout
  timeout: 5000, // 5 seconds
  
  // Response type
  responseType: 'json', // 'json' | 'blob' | 'arraybuffer' | 'document' | 'text' | 'stream'
  
  // Response encoding
  responseEncoding: 'utf8',
  
  // Max content length
  maxContentLength: 2000,
  maxBodyLength: 2000,
  
  // Validate status
  validateStatus: (status) => status >= 200 && status < 300,
  
  // Max redirects
  maxRedirects: 5,
  
  // HTTP Auth
  auth: {
    username: 'user',
    password: 'pass',
  },
  
  // Proxy
  proxy: {
    protocol: 'http',
    host: '127.0.0.1',
    port: 9000,
    auth: {
      username: 'proxy-user',
      password: 'proxy-pass',
    },
  },
  
  // Progress events
  onUploadProgress: (progressEvent) => {
    const percentCompleted = Math.round(
      (progressEvent.loaded * 100) / progressEvent.total!
    );
    console.log(`Upload: ${percentCompleted}%`);
  },
  
  onDownloadProgress: (progressEvent) => {
    const percentCompleted = Math.round(
      (progressEvent.loaded * 100) / progressEvent.total!
    );
    console.log(`Download: ${percentCompleted}%`);
  },
  
  // Decompress response
  decompress: true,
};

const response = await axios(config);
```

---

### **3. Request Cancellation - Hủy Request**

```typescript
// ═══════════════════════════════════════════════════════════
// ABORT CONTROLLER (Modern - Axios 0.22+)
// ═══════════════════════════════════════════════════════════

const controller = new AbortController();

axios.get('/api/users', {
  signal: controller.signal
}).then(response => {
  console.log(response.data);
}).catch(error => {
  if (axios.isCancel(error)) {
    console.log('Request canceled:', error.message);
  }
});

// Cancel request
controller.abort('User canceled the request');

// ═══════════════════════════════════════════════════════════
// USE CASE 1: Cancel on Component Unmount (React)
// ═══════════════════════════════════════════════════════════

import { useEffect, useState } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    const controller = new AbortController();
    
    const fetchUsers = async () => {
      try {
        const { data } = await axios.get('/api/users', {
          signal: controller.signal
        });
        setUsers(data);
      } catch (error) {
        if (!axios.isCancel(error)) {
          console.error('Error fetching users:', error);
        }
      }
    };
    
    fetchUsers();
    
    // Cleanup: Cancel request khi unmount
    return () => {
      controller.abort();
    };
  }, []);
  
  return <div>...</div>;
}

// ═══════════════════════════════════════════════════════════
// USE CASE 2: Cancel Previous Search Request
// ═══════════════════════════════════════════════════════════

function SearchComponent() {
  const [query, setQuery] = useState('');
  const controllerRef = useRef<AbortController | null>(null);
  
  const handleSearch = async (searchQuery: string) => {
    // Cancel previous request nếu có
    if (controllerRef.current) {
      controllerRef.current.abort();
    }
    
    // Create new controller
    controllerRef.current = new AbortController();
    
    try {
      const { data } = await axios.get('/api/search', {
        params: { q: searchQuery },
        signal: controllerRef.current.signal
      });
      setResults(data);
    } catch (error) {
      if (!axios.isCancel(error)) {
        console.error('Search error:', error);
      }
    }
  };
  
  // Debounce search
  useEffect(() => {
    const timer = setTimeout(() => {
      if (query) {
        handleSearch(query);
      }
    }, 500);
    
    return () => clearTimeout(timer);
  }, [query]);
}

// ═══════════════════════════════════════════════════════════
// CANCEL TOKEN (Legacy - Deprecated nhưng vẫn hoạt động)
// ═══════════════════════════════════════════════════════════

const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('/api/users', {
  cancelToken: source.token
}).catch(error => {
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
  
  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
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
          <div style={{ width: `${uploadProgress}%` }}>
            {uploadProgress}%
          </div>
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
  return { success: true, data: response.data, message: 'Success', status: 200 };
} catch (error) {
  return handleAxiosError(error);
}
```

---

### **6. Advanced Features**

#### **6.1. Retry Logic**

```typescript
// ═══════════════════════════════════════════════════════════
// AUTO RETRY với Exponential Backoff
// ═══════════════════════════════════════════════════════════

const axiosRetry = async (config: any, retries = 3, delay = 1000) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await axios(config);
    } catch (error) {
      if (i === retries - 1) throw error;
      
      // Exponential backoff
      const waitTime = delay * Math.pow(2, i);
      console.log(`Retry ${i + 1}/${retries} after ${waitTime}ms...`);
      await new Promise(resolve => setTimeout(resolve, waitTime));
    }
  }
};

// Usage
const data = await axiosRetry({
  method: 'get',
  url: '/api/users',
}, 3, 1000);
```

#### **6.2. Request Deduplication**

```typescript
// ═══════════════════════════════════════════════════════════
// PREVENT DUPLICATE REQUESTS
// ═══════════════════════════════════════════════════════════

const pendingRequests = new Map<string, Promise<any>>();

const dedupeRequest = async (config: any) => {
  const key = `${config.method}:${config.url}:${JSON.stringify(config.params)}`;
  
  // Nếu có request pending
  if (pendingRequests.has(key)) {
    console.log('🔄 Reusing pending request...');
    return pendingRequests.get(key);
  }
  
  // Create new request
  const promise = axios(config).finally(() => {
    pendingRequests.delete(key);
  });
  
  pendingRequests.set(key, promise);
  return promise;
};
```

#### **6.3. Response Caching**

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
  response => response,
  error => {
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

---
