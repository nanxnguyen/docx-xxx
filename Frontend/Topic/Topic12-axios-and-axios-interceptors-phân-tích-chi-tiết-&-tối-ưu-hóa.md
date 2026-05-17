# 🔌 Topic 12: Axios & Axios Interceptors

## ⭐ Senior/Staff Summary

Axios là HTTP client phổ biến cho frontend vì có API nhất quán cho `instance`, `timeout`, `AbortController`, `interceptors`, upload/download progress, `transform`, `validateStatus` và error handling.

`Axios interceptors` là middleware ở API boundary:

- Request interceptor chạy trước khi request đi ra ngoài.
- Response interceptor chạy sau khi response/error quay về.
- Interceptor nên xử lý cross-cutting concerns: auth header, refresh access token, retry policy, request id, timing, error normalization, telemetry.
- Interceptor không nên chứa business logic như điều hướng màn hình phức tạp, quyết định UI copy, hoặc mutation domain state.

> 💡 Senior mindset: hãy xem Axios instance như một `transport boundary`. Component/hook chỉ gọi service đã được chuẩn hóa; token, timeout, retry, cancellation, logging và error shape được kiểm soát ở một nơi.

## 🧠 Key Mental Model

| Thành phần | Chạy khi nào | Dùng để làm gì | Lưu ý production |
|---|---:|---|---|
| `axios.create()` | Lúc khởi tạo client | Tách config theo service/domain | Tránh mutate global `axios.defaults` |
| Request interceptor | Trước khi gửi request | Add token, locale, request id, metadata | Request interceptors chạy kiểu LIFO |
| Response interceptor | Khi nhận response/error | Refresh token, retry, normalize error, metrics | Response interceptors chạy kiểu FIFO |
| `AbortController` / `signal` | Khi cần hủy request | Cleanup React effect, search mới hủy search cũ | Không overwrite `signal` của caller |
| `timeout` | Request quá lâu | Fail fast, tránh UI treo | Timeout không thay thế cancellation |
| `validateStatus` | Trước nhánh success/error | Chọn status nào được coi là success | Coi `401` là success sẽ bypass refresh error interceptor |

### ✅ TypeScript augmentation dùng chung

Nếu thêm field custom như `_retry`, `retryCount`, `metadata.startTime`, `metadata.requestKey`, nên khai báo một lần thay vì ép kiểu rải rác.

```ts
// axios.d.ts hoặc file types được include bởi tsconfig
import "axios";

declare module "axios" {
  export interface InternalAxiosRequestConfig {
    _retry?: boolean;
    retryCount?: number;
    metadata?: {
      startTime?: number;
      requestKey?: string;
      dedupeId?: string;
      requestId?: string;
    };
  }
}
```

## 📚 Main Concepts

### 1. Axios instance

Tạo nhiều instance giúp config không leak giữa service:

| Instance | Mục đích | Config thường khác |
|---|---|---|
| `apiClient` | Business API | Auth header, refresh, error normalization |
| `authClient` | Login/refresh/logout | Không gắn refresh interceptor để tránh loop |
| `uploadClient` | Upload file | Timeout dài, progress |
| `publicClient` | Public API | Không token |
| `analyticsClient` | Tracking | Timeout ngắn, silent fail có kiểm soát |

```ts
import axios from "axios";

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10_000,
  headers: { Accept: "application/json" },
});

export const authClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10_000,
  withCredentials: true,
});
```

### 2. Request interceptor

Request interceptor phù hợp để gắn header và metadata kỹ thuật:

```ts
apiClient.interceptors.request.use((config) => {
  const accessToken = accessTokenStore.get();
  const requestId = crypto.randomUUID();

  if (accessToken) config.headers.Authorization = `Bearer ${accessToken}`;

  config.headers["X-Request-ID"] = requestId;
  config.metadata = {
    ...config.metadata,
    requestId,
    startTime: performance.now(),
  };

  return config;
});
```

### 3. Response interceptor

Response interceptor phù hợp để đo timing, normalize data/error, xử lý auth boundary và retry.

```ts
apiClient.interceptors.response.use(
  (response) => {
    const startTime = response.config.metadata?.startTime;
    const durationMs = startTime ? performance.now() - startTime : undefined;

    metrics.trackHttpSuccess({
      requestId: response.config.metadata?.requestId,
      url: response.config.url,
      status: response.status,
      durationMs,
    });

    return response;
  },
  (error) => Promise.reject(normalizeApiError(error)),
);
```

### 4. Error shape

Axios error có nhiều dạng; UI không nên tự parse raw `AxiosError` ở mọi component.

| Case | Dấu hiệu | UX nên làm |
|---|---|---|
| Server trả lỗi | `error.response` có status | Hiển thị theo status/domain error |
| Không nhận response | `error.request`, không có `response` | Báo network/server không phản hồi |
| Timeout | `error.code === "ECONNABORTED"` | Cho retry hoặc báo request quá lâu |
| Bị hủy | `error.code === "ERR_CANCELED"` | Thường im lặng, không toast |
| Config/setup error | Không có request hợp lệ | Log cho developer/debugging |

## 🛠️ Practical TypeScript/JavaScript Examples

### 1. Production auth client: access token in memory, refresh cookie HttpOnly

Trong production, refresh token không nên được dạy như mặc định đặt trong `localStorage` vì XSS có thể đọc được. Mô hình thường dùng hơn:

- Access token sống ngắn, giữ trong memory.
- Refresh token nằm trong cookie `HttpOnly; Secure; SameSite=Lax/Strict` nếu cùng site.
- Nếu cross-site cookie: cần `SameSite=None; Secure`, `withCredentials: true`, CORS chính xác và CSRF strategy.
- `localStorage` chỉ nên coi là demo đơn giản hoặc chấp nhận tradeoff rõ ràng.

```ts
import axios, { AxiosError, AxiosInstance } from "axios";

type RefreshResponse = {
  accessToken: string;
};

const accessTokenStore = {
  value: null as string | null,
  get() {
    return this.value;
  },
  set(token: string | null) {
    this.value = token;
  },
};

const authEvents = {
  emit(event: "session-expired") {
    window.dispatchEvent(new CustomEvent(event));
  },
};

const authClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10_000,
  withCredentials: true, // gửi HttpOnly refresh cookie
  xsrfCookieName: "XSRF-TOKEN",
  xsrfHeaderName: "X-XSRF-TOKEN",
});

export const apiClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10_000,
  withCredentials: true,
});

apiClient.interceptors.request.use((config) => {
  const token = accessTokenStore.get();
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

let refreshPromise: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  if (!refreshPromise) {
    refreshPromise = authClient
      .post<RefreshResponse>("/auth/refresh")
      .then((response) => {
        accessTokenStore.set(response.data.accessToken);
        return response.data.accessToken;
      })
      .finally(() => {
        refreshPromise = null;
      });
  }

  return refreshPromise;
}

apiClient.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config;

    if (error.response?.status !== 401 || !originalRequest || originalRequest._retry) {
      return Promise.reject(error);
    }

    originalRequest._retry = true;

    try {
      const newAccessToken = await refreshAccessToken();
      originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
      return apiClient(originalRequest);
    } catch (refreshError) {
      accessTokenStore.set(null);
      authEvents.emit("session-expired");
      return Promise.reject(refreshError);
    }
  },
);
```

🔥 Điểm quan trọng:

- Dùng `authClient` riêng để refresh request không tự đi vào refresh interceptor.
- Dùng `refreshPromise` để nhiều request `401` cùng lúc chỉ gọi refresh một lần.
- Dùng `_retry` để tránh infinite loop.
- Redirect login nên để auth/router layer xử lý qua event hoặc state, không hard-code ở interceptor nếu app lớn.
- Nếu dùng cookie auth, cần xử lý CSRF: `SameSite`, CSRF token, backend CORS và `withCredentials` phải khớp.

### 2. Error normalization có metadata/cause để debug

Normalize lỗi giúp UI đơn giản hơn, nhưng đừng làm mất raw error. Observability cần status, request id, URL, method, duration và `cause`.

```ts
import axios, { AxiosError } from "axios";

type ApiErrorCode =
  | "UNAUTHORIZED"
  | "FORBIDDEN"
  | "NETWORK"
  | "TIMEOUT"
  | "CANCELED"
  | "SERVER"
  | "UNKNOWN";

export class ApiClientError extends Error {
  code: ApiErrorCode;
  status?: number;
  metadata: {
    url?: string;
    method?: string;
    requestId?: string;
    durationMs?: number;
    axiosCode?: string;
  };

  constructor(params: {
    code: ApiErrorCode;
    message: string;
    status?: number;
    metadata?: ApiClientError["metadata"];
    cause?: unknown;
  }) {
    super(params.message, { cause: params.cause });
    this.name = "ApiClientError";
    this.code = params.code;
    this.status = params.status;
    this.metadata = params.metadata ?? {};
  }
}

export function normalizeApiError(error: unknown): ApiClientError {
  if (!axios.isAxiosError(error)) {
    return new ApiClientError({
      code: "UNKNOWN",
      message: "Unexpected error",
      cause: error,
    });
  }

  const startTime = error.config?.metadata?.startTime;
  const metadata = {
    url: error.config?.url,
    method: error.config?.method,
    requestId: error.config?.metadata?.requestId,
    durationMs: startTime ? performance.now() - startTime : undefined,
    axiosCode: error.code,
  };

  if (error.code === "ERR_CANCELED") {
    return new ApiClientError({
      code: "CANCELED",
      message: "Request canceled",
      metadata,
      cause: error,
    });
  }

  if (error.code === "ECONNABORTED") {
    return new ApiClientError({
      code: "TIMEOUT",
      message: "Request timed out",
      metadata,
      cause: error,
    });
  }

  if (!error.response) {
    return new ApiClientError({
      code: "NETWORK",
      message: "Network error",
      metadata,
      cause: error,
    });
  }

  const status = error.response.status;

  return new ApiClientError({
    code: status === 401 ? "UNAUTHORIZED" : status === 403 ? "FORBIDDEN" : "SERVER",
    status,
    message: getServerMessage(error) ?? "Request failed",
    metadata,
    cause: error,
  });
}

function getServerMessage(error: AxiosError): string | undefined {
  const data = error.response?.data;
  return typeof data === "object" && data !== null && "message" in data
    ? String(data.message)
    : undefined;
}
```

### 3. Retry với `Retry-After`, jitter, max cap và cancellation

Retry chỉ nên áp dụng cho lỗi tạm thời. Không retry vô điều kiện với `POST` tạo order/payment nếu backend không hỗ trợ `Idempotency-Key`.

```ts
import { AxiosError, InternalAxiosRequestConfig } from "axios";

const RETRYABLE_STATUS = new Set([408, 429, 500, 502, 503, 504]);
const IDEMPOTENT_METHODS = new Set(["get", "head", "options", "put", "delete"]);
const MAX_RETRIES = 2;
const BASE_DELAY_MS = 300;
const MAX_DELAY_MS = 5_000;

function parseRetryAfter(value: string | undefined): number | undefined {
  if (!value) return undefined;

  const seconds = Number(value);
  if (Number.isFinite(seconds)) return seconds * 1_000;

  const dateMs = Date.parse(value);
  return Number.isFinite(dateMs) ? Math.max(0, dateMs - Date.now()) : undefined;
}

function computeDelayMs(retryCount: number, retryAfter?: string) {
  const serverDelay = parseRetryAfter(retryAfter);
  if (serverDelay !== undefined) return Math.min(serverDelay, MAX_DELAY_MS);

  const exponential = BASE_DELAY_MS * 2 ** retryCount;
  const jitter = Math.random() * 150;
  return Math.min(exponential + jitter, MAX_DELAY_MS);
}

function sleep(ms: number, signal?: AbortSignal) {
  if (signal?.aborted) return Promise.reject(new DOMException("Aborted", "AbortError"));

  return new Promise<void>((resolve, reject) => {
    const timeoutId = window.setTimeout(resolve, ms);

    signal?.addEventListener(
      "abort",
      () => {
        window.clearTimeout(timeoutId);
        reject(new DOMException("Aborted", "AbortError"));
      },
      { once: true },
    );
  });
}

function isNetworkOrRetryableStatus(error: AxiosError) {
  const status = error.response?.status;
  return !status || RETRYABLE_STATUS.has(status);
}

function canRetry(config: InternalAxiosRequestConfig, error: AxiosError) {
  const method = config.method?.toLowerCase();
  const hasIdempotencyKey = Boolean(config.headers["Idempotency-Key"]);

  return (
    (config.retryCount ?? 0) < MAX_RETRIES &&
    isNetworkOrRetryableStatus(error) &&
    (Boolean(method && IDEMPOTENT_METHODS.has(method)) || hasIdempotencyKey)
  );
}

apiClient.interceptors.response.use(undefined, async (error: AxiosError) => {
  const config = error.config;
  if (!config || error.code === "ERR_CANCELED" || !canRetry(config, error)) {
    return Promise.reject(error);
  }

  config.retryCount = (config.retryCount ?? 0) + 1;

  const retryAfter = error.response?.headers["retry-after"];
  await sleep(computeDelayMs(config.retryCount, retryAfter), config.signal);

  return apiClient(config);
});
```

### 4. Cancellation trong React

Dùng `AbortController` để cleanup khi unmount hoặc khi `userId` đổi. Với UI, loading/error nên có accessible roles phù hợp.

```tsx
import axios from "axios";
import { useEffect, useState } from "react";

type User = {
  id: string;
  name: string;
};

export function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadUser() {
      try {
        setError(null);
        setUser(null);

        const response = await apiClient.get<User>(`/users/${userId}`, {
          signal: controller.signal,
        });

        setUser(response.data);
      } catch (error) {
        if (axios.isCancel(error)) return;
        setError("Cannot load user");
      }
    }

    loadUser();
    return () => controller.abort();
  }, [userId]);

  if (error) return <p role="alert">{error}</p>;
  if (!user) return <p role="status">Loading...</p>;

  return <h1>{user.name}</h1>;
}
```

✅ React implication: cancellation giảm stale update khi request cũ về sau request mới. Với app dùng React Query/SWR, nên để thư viện đó quản lý loading/cache/refetch, Axios chỉ lo transport.

### 5. Upload với progress

Khi gửi `FormData` trên browser, không tự set `Content-Type: multipart/form-data`; browser sẽ tự thêm boundary đúng.

```ts
const uploadClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 60_000,
});

export function uploadAvatar(file: File, onProgress: (percent: number) => void) {
  const formData = new FormData();
  formData.append("avatar", file);

  return uploadClient.post("/me/avatar", formData, {
    onUploadProgress: (event) => {
      if (!event.total) return;
      onProgress(Math.round((event.loaded * 100) / event.total));
    },
  });
}
```

### 6. Download file/blob an toàn hơn

Với download, cần append/click/remove link, delay `revokeObjectURL`, và sanitize filename nếu lấy từ server/user input.

```ts
function sanitizeFilename(filename: string) {
  return filename.replace(/[\\/:*?"<>|]/g, "_").replace(/\s+/g, " ").trim();
}

export async function downloadReport(reportId: string) {
  const response = await apiClient.get(`/reports/${reportId}/pdf`, {
    responseType: "blob",
    onDownloadProgress: (event) => {
      if (!event.total) return;
      const percent = Math.round((event.loaded * 100) / event.total);
      console.log(`Download ${percent}%`);
    },
  });

  const blob = new Blob([response.data], { type: "application/pdf" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");

  link.href = url;
  link.download = sanitizeFilename(`report-${reportId}.pdf`);
  link.style.display = "none";

  document.body.appendChild(link);
  link.click();
  link.remove();

  window.setTimeout(() => URL.revokeObjectURL(url), 1_000);
}
```

Với Excel/binary file:

```ts
export async function downloadExcel() {
  const response = await apiClient.get("/reports/export.xlsx", {
    responseType: "arraybuffer",
  });

  const blob = new Blob([response.data], {
    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  });

  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "export.xlsx";
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1_000);
}
```

### 7. Request dedupe không race và không overwrite caller signal

Dedupe thường dùng cho GET/search autocomplete: request mới có cùng key hủy request cũ. Bẫy hay gặp là:

- Overwrite `config.signal` làm mất cancellation của caller.
- Request cũ cleanup map và xóa nhầm entry của request mới.

```ts
import { InternalAxiosRequestConfig } from "axios";

const inFlight = new Map<string, { controller: AbortController; id: string }>();

function requestKey(config: InternalAxiosRequestConfig) {
  return `${config.method}:${config.baseURL ?? ""}${config.url}:${JSON.stringify(
    config.params ?? {},
  )}`;
}

function composeSignals(...signals: Array<AbortSignal | undefined>) {
  const activeSignals = signals.filter(Boolean) as AbortSignal[];
  if (activeSignals.length === 0) return undefined;
  if (activeSignals.length === 1) return activeSignals[0];

  const abortSignalWithAny = AbortSignal as typeof AbortSignal & {
    any?: (signals: AbortSignal[]) => AbortSignal;
  };

  if (abortSignalWithAny.any) return abortSignalWithAny.any(activeSignals);

  const controller = new AbortController();
  const abort = () => controller.abort();

  for (const signal of activeSignals) {
    if (signal.aborted) {
      controller.abort();
      break;
    }
    signal.addEventListener("abort", abort, { once: true });
  }

  return controller.signal;
}

apiClient.interceptors.request.use((config) => {
  if (config.method?.toLowerCase() !== "get") return config;

  const key = requestKey(config);
  const controller = new AbortController();
  const id = crypto.randomUUID();

  inFlight.get(key)?.controller.abort();
  inFlight.set(key, { controller, id });

  config.signal = composeSignals(config.signal, controller.signal);
  config.metadata = { ...config.metadata, requestKey: key, dedupeId: id };

  return config;
});

function cleanupDedupe(config?: InternalAxiosRequestConfig) {
  const key = config?.metadata?.requestKey;
  const id = config?.metadata?.dedupeId;
  if (!key || !id) return;

  const current = inFlight.get(key);
  if (current?.id === id) inFlight.delete(key);
}

apiClient.interceptors.response.use(
  (response) => {
    cleanupDedupe(response.config);
    return response;
  },
  (error) => {
    cleanupDedupe(error.config);
    return Promise.reject(error);
  },
);
```

> 💡 Với rate limiting nghiêm túc, dùng queue/concurrency limiter ở service layer hoặc thư viện chuyên dụng. Interceptor chỉ nên giữ logic mỏng.

### 8. Client factory cho SSR / micro-frontend

Trong SSR hoặc micro-frontend, tránh singleton global chứa token/user context. Tạo client theo request/remote để không leak config giữa user hoặc giữa remote apps.

```ts
type CreateHttpClientOptions = {
  baseURL: string;
  getAccessToken?: () => string | null | Promise<string | null>;
  getTenantId?: () => string | null;
  onUnauthorized?: () => void;
};

export function createHttpClient(options: CreateHttpClientOptions) {
  const client = axios.create({
    baseURL: options.baseURL,
    timeout: 10_000,
  });

  client.interceptors.request.use(async (config) => {
    const token = await options.getAccessToken?.();
    const tenantId = options.getTenantId?.();

    if (token) config.headers.Authorization = `Bearer ${token}`;
    if (tenantId) config.headers["X-Tenant-ID"] = tenantId;

    return config;
  });

  client.interceptors.response.use(undefined, (error) => {
    if (error.response?.status === 401) options.onUnauthorized?.();
    return Promise.reject(error);
  });

  return client;
}
```

### 9. `validateStatus`

`validateStatus` cho phép quyết định status nào đi vào nhánh success. Dùng khi API có contract rõ rằng `4xx` là business result mà UI cần xử lý.

```ts
const client = axios.create({
  validateStatus: (status) => status >= 200 && status < 500,
});
```

⚠️ Nếu `401` được coi là success, response error interceptor sẽ không chạy, nên flow refresh-token sẽ bị bypass. Với auth client chính, thường giữ mặc định `2xx` là success, hoặc xử lý `401` rõ trong success interceptor.

## 🚀 Production Notes / React Implications

| Chủ đề | Production note |
|---|---|
| Token storage | Prefer HttpOnly Secure SameSite refresh cookie + short-lived access token in memory; `localStorage` chỉ là demo/tradeoff rõ ràng. |
| Cookie auth / CSRF | Dùng `withCredentials`, CORS credentials, `SameSite`, CSRF token/header đúng contract backend. |
| Refresh token | Chống concurrent refresh, infinite loop, refresh endpoint bị interceptor đệ quy. |
| Error handling | Normalize lỗi nhưng giữ `cause`/metadata để debug và monitoring. UI quyết định toast/message. |
| Retry | Tôn trọng `Retry-After`, jitter, max cap, cancellation; chỉ retry idempotent hoặc có `Idempotency-Key`. |
| Cancellation | Dùng `AbortController`; khi interceptor thêm cancellation phải compose với signal của caller. |
| Download | Dùng `blob`/`arraybuffer`, sanitize filename, append/click/remove link, delay revoke URL. |
| Upload | Với browser `FormData`, không tự set multipart boundary. |
| React Query/SWR | Axios lo transport; data-fetching lib lo cache, dedupe, retry UI state, invalidation. |
| Accessibility | Loading dùng `role="status"` khi cần announce; error quan trọng dùng `role="alert"` hoặc focus management. |
| Logging | Không log token, password, cookie, PII; mask payload trước khi gửi monitoring. |
| Performance | Interceptor nên nhẹ; tránh deep transform lớn trên hot path nếu chưa đo profiling. |
| SSR | Không dùng singleton token store global cho nhiều user; tạo client theo request context. |
| Micro-frontend | Không mutate global defaults; mỗi remote/service dùng instance/factory riêng và cleanup interceptor runtime. |
| Service layer | Component gọi service/hook, không gọi raw Axios khắp nơi. API boundary dễ test và đổi transport hơn. |

## 🧪 Testing Notes

Nên test Axios boundary bằng MSW + Vitest/Jest thay vì mock từng component.

| Case nên test | Kỳ vọng |
|---|---|
| Concurrent `401` | Nhiều request chỉ gọi `/auth/refresh` một lần, rồi replay request thành công. |
| Refresh failure | Clear access token, emit session expired, không retry vô hạn. |
| Retry count | Retry đúng số lần, tôn trọng `Retry-After`, không retry non-idempotent `POST` thiếu `Idempotency-Key`. |
| Canceled request | Không toast lỗi, promise reject/cancel đúng, sleep retry cũng bị hủy. |
| Timeout | Normalize thành `TIMEOUT`, metadata còn URL/method/request id. |
| Dedupe race | Request cũ bị abort không xóa entry của request mới trong `inFlight`. |
| Caller `AbortSignal` | Caller abort vẫn hủy request dù interceptor có dedupe controller. |
| `validateStatus` | Khi `401` được success path, refresh error interceptor không chạy; test để tránh hiểu nhầm. |
| Upload/download | Upload không set multipart boundary thủ công; download remove link và revoke URL. |

Ví dụ hướng test ngắn:

```ts
import { http, HttpResponse } from "msw";
import { server } from "./testServer";

it("queues concurrent 401 refresh into one refresh call", async () => {
  let refreshCalls = 0;

  server.use(
    http.get("/users/me", ({ request }) => {
      return request.headers.get("authorization") === "Bearer new-token"
        ? HttpResponse.json({ id: "me" })
        : HttpResponse.json({}, { status: 401 });
    }),
    http.post("/auth/refresh", () => {
      refreshCalls += 1;
      return HttpResponse.json({ accessToken: "new-token" });
    }),
  );

  const results = await Promise.all([userService.me(), userService.me()]);

  expect(results).toEqual([{ id: "me" }, { id: "me" }]);
  expect(refreshCalls).toBe(1);
});
```

## ⚠️ Common Pitfalls

| Pitfall | Vì sao nguy hiểm | Cách xử lý |
|---|---|---|
| Lưu refresh token trong `localStorage` như production default | XSS đọc được token dài hạn | Dùng HttpOnly Secure SameSite cookie; label localStorage là demo/tradeoff |
| Dùng global `axios.defaults` khắp app | Config leak giữa service/test/user | Tạo `axios.create()` theo domain |
| Refresh token gọi bằng cùng `apiClient` | Dễ infinite loop `401` | Dùng `authClient` riêng |
| Không có `_retry` flag | Request retry vô hạn | Mark request đã retry |
| Nhiều `401` gọi nhiều refresh | Race condition, token ghi đè | Dùng shared `refreshPromise` hoặc queue |
| Retry mọi method | Có thể tạo duplicate order/payment | Chỉ retry idempotent hoặc request có idempotency key |
| Bỏ qua `Retry-After` | Làm backend quá tải hơn khi `429/503` | Parse header, thêm jitter và max cap |
| Overwrite `config.signal` | Caller không hủy được request nữa | Compose signal |
| Dedupe cleanup không kiểm tra identity | Request cũ xóa nhầm request mới | Lưu `id/controller` và cleanup có guard |
| Set multipart boundary thủ công | Browser gửi sai boundary | Để browser set `Content-Type` cho `FormData` |
| Revoke object URL ngay sau click | Một số browser chưa kịp bắt download | Remove link và delay revoke |
| Toast lỗi trong interceptor | Một lỗi có thể spam nhiều toast | Normalize lỗi, UI quyết định |
| Không eject interceptor setup động | Memory leak, duplicate handlers | Lưu id và `eject(id)` khi cleanup |
| Log raw request/response | Leak token/PII | Mask sensitive fields |
| Transform data quá sâu | Tốn CPU, khó debug | Transform ở boundary rõ ràng, có test |
| Cache GET trong interceptor tùy tiện | Dễ stale data, lệch React Query/SWR | Để data-fetching library quản lý cache |
| `validateStatus` quá rộng | Lỗi thật đi vào success path | Chỉ mở rộng status khi có contract rõ |

```ts
const id = apiClient.interceptors.response.use(onSuccess, onError);

// Khi interceptor được đăng ký trong lifecycle động:
apiClient.interceptors.response.eject(id);
```

## 🧭 Decision Guide / Checklist

### Khi nào nên dùng Axios?

| Nhu cầu | `fetch` | Axios |
|---|---:|---:|
| App nhỏ, request đơn giản | ✅ | ✅ |
| Timeout tiện lợi | Cần tự làm | ✅ |
| Interceptors | Cần wrapper | ✅ |
| Upload progress | Khó hơn | ✅ |
| Error shape thống nhất | Cần tự normalize | ✅ |
| Bundle size tối giản | ✅ | Cân nhắc |

### Production checklist

- ✅ Có `axios.create()` riêng cho từng API domain.
- ✅ Có timeout mặc định và timeout riêng cho upload/export.
- ✅ Auth model rõ: HttpOnly refresh cookie, access token memory, CSRF/CORS đúng nếu dùng cookie.
- ✅ Request interceptor chỉ gắn metadata/header/token, không chứa business logic.
- ✅ Response interceptor normalize lỗi, giữ `cause`/metadata và xử lý auth boundary.
- ✅ Refresh token chống concurrent refresh, có `_retry`, dùng `authClient` riêng.
- ✅ Retry có `Retry-After`, jitter, max cap, cancellation-aware sleep và idempotency policy.
- ✅ Cancellation dùng `AbortController`; interceptor không làm mất caller signal.
- ✅ Dedupe có guard chống race cleanup.
- ✅ Upload/download xử lý đúng browser behavior.
- ✅ Loading/error UI có role accessibility phù hợp.
- ✅ Không log secret/PII.
- ✅ Có test cho concurrent `401`, refresh fail, retry count, cancel, timeout, dedupe race, `validateStatus`.

## 💬 Short Interview Answer

Em nghĩ Axios interceptor là middleware ở API boundary. Request interceptor chạy trước khi gửi request, response interceptor chạy sau khi nhận response hoặc error. Em thường dùng nó để gắn access token, request id, locale, đo timing, normalize error, refresh access token và retry policy.

Theo em điểm quan trọng trong production là token storage và boundary phải rõ. Em không xem refresh token trong `localStorage` là default an toàn; nếu backend hỗ trợ, em ưu tiên refresh token trong cookie `HttpOnly; Secure; SameSite`, access token ngắn hạn giữ trong memory, kèm `withCredentials`, CORS và CSRF đúng. Refresh flow cần `authClient` riêng, `_retry`, và `refreshPromise` để nhiều request `401` chỉ refresh một lần.

Em thấy retry cũng phải có kỷ luật: tôn trọng `Retry-After`, có exponential backoff + jitter + max cap, không retry non-idempotent `POST` nếu không có `Idempotency-Key`, và sleep phải hủy được bằng `AbortSignal`. Với React, em thường để Axios lo transport, còn cache/loading/refetch thì dùng React Query hoặc SWR. Trong SSR hoặc micro-frontend, em tránh singleton global chứa token vì có nguy cơ leak context giữa user hoặc remote app.
