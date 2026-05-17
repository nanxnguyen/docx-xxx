# 🔌 Topic 35: WebSocket & Real-time Streaming - WebSocket, Socket.IO, Centrifuge/Centrifugo

## 1. ⭐ Senior/Staff Summary

Real-time frontend không chỉ là “mở WebSocket rồi nghe message”. Production real-time cần xử lý **connection lifecycle**, **authentication**, **reconnect**, **resubscribe**, **message ordering**, **duplicate events**, **backpressure**, **rate limit**, **visibility/tab behavior**, **scaling nhiều server** và **React cleanup**.

Tóm tắt lựa chọn:

- ✅ **Native WebSocket**: low-level, nhẹ, chuẩn browser, phù hợp khi protocol đơn giản và team tự kiểm soát reconnect/auth/message contract.
- ✅ **Socket.IO**: high-level hơn WebSocket, có event API, reconnect, rooms, namespaces, acknowledgements, fallback transport. Đổi lại nặng hơn và cần Socket.IO server/protocol riêng.
- ✅ **Centrifuge/Centrifugo**: realtime pub/sub platform. Server là **Centrifugo**, JS client thường gọi là **centrifuge-js**. Hợp app cần channels, presence, history, recovery, JWT auth và scale ngang qua broker như Redis/NATS.
- ✅ **SSE**: tốt cho server → client only, đơn giản hơn WebSocket khi không cần bidirectional realtime.

> 💡 Mental model: **WebSocket là đường ống**, Socket.IO là **framework event realtime**, Centrifugo là **realtime pub/sub infrastructure**.

## 2. 🧠 Key Mental Model

### 2.1. Polling vs SSE vs WebSocket

| Cơ chế | Chiều dữ liệu | Ưu điểm | Nhược điểm | Hợp khi |
|---|---|---|---|---|
| Polling | Client hỏi server định kỳ | Dễ làm, chạy mọi nơi | Tốn request, latency theo interval | Data ít thay đổi |
| Long polling | Client giữ request lâu | Gần realtime hơn polling | Server giữ request, phức tạp hơn | Fallback realtime |
| SSE | Server → client | Đơn giản, tự reconnect, dùng HTTP | Không bidirectional | Notifications, live feed |
| WebSocket | 2 chiều | Low latency, server push, client push | Tự lo reconnect/auth/protocol | Chat, trading, collaboration |
| Socket.IO | 2 chiều + event API | Reconnect, rooms, ack, fallback | Không tương thích raw WS server | App realtime cần DX nhanh |
| Centrifugo | Pub/sub realtime | Channels, presence, history, recovery, scale | Cần server/broker/config | Enterprise realtime platform |

### 2.2. Lifecycle đúng của một realtime client

```text
connect
  ↓
authenticate
  ↓
subscribe channels / join rooms
  ↓
receive messages
  ↓
batch/throttle update UI
  ↓
disconnect or reconnect
  ↓
resubscribe + recover missed messages
```

### 2.3. Ba câu hỏi senior phải hỏi

1. **Delivery guarantee là gì?** Có cần at-most-once, at-least-once, exactly-once-like bằng idempotency không?
2. **Missed messages xử lý sao?** Refetch snapshot, dùng history/recovery, hay chấp nhận mất?
3. **Scale ra nhiều server thế nào?** Sticky session, Redis adapter, broker, channel permissions, backpressure?

## 3. 📚 Main Concepts

### 3.1. Native WebSocket

WebSocket là browser API tạo kết nối lâu dài giữa client và server:

- `ws://` không mã hóa.
- `wss://` có TLS, nên dùng trong production.
- Sau HTTP Upgrade handshake, client/server có thể gửi message 2 chiều.
- Browser WebSocket không cho set custom headers tùy ý; auth thường qua cookie, query token ngắn hạn, subprotocol hoặc message auth sau connect.

```ts
const socket = new WebSocket('wss://api.example.com/realtime');

socket.addEventListener('open', () => {
  socket.send(JSON.stringify({ type: 'subscribe', channel: 'prices:BTC' }));
});

socket.addEventListener('message', (event) => {
  const message = JSON.parse(event.data);
  console.log(message);
});

socket.addEventListener('close', (event) => {
  console.log(event.code, event.reason, event.wasClean);
});
```

### 3.2. WebSocket readyState và close codes

| State | Giá trị | Ý nghĩa |
|---|---:|---|
| `CONNECTING` | `0` | Đang handshake, chưa gửi được |
| `OPEN` | `1` | Có thể gửi/nhận message |
| `CLOSING` | `2` | Đang đóng |
| `CLOSED` | `3` | Đã đóng |

Close codes hay gặp:

| Code | Ý nghĩa | Reconnect? |
|---:|---|---|
| `1000` | Normal closure | Không, trừ khi user cần reconnect |
| `1001` | Going away, tab/page/server rời đi | Tùy ngữ cảnh |
| `1006` | Abnormal closure, không nhận close frame | Có |
| `1008` | Policy violation, thường auth/permission | Không tự loop, cần refresh auth |
| `1011` | Server error | Có backoff |
| `1012` | Service restart | Có backoff |

### 3.3. Reconnection: exponential backoff + jitter

Reconnect không nên retry liên tục. Nếu 10k clients cùng reconnect mỗi giây, server sẽ bị “reconnect storm”.

```ts
function getReconnectDelay(attempt: number) {
  const base = 1000;
  const max = 30000;
  const exponential = Math.min(max, base * 2 ** attempt);
  const jitter = Math.random() * 500;
  return exponential + jitter;
}

function shouldReconnect(code: number) {
  return ![1000, 1008].includes(code);
}
```

Best practice:

- giới hạn số lần retry
- thêm jitter
- hiển thị trạng thái reconnect cho user
- resubscribe sau khi reconnect
- refresh token nếu close vì auth/session expired

### 3.4. Heartbeat / ping-pong

Connection có thể “chết im lặng” khi mobile đổi mạng, laptop sleep, proxy timeout. Heartbeat giúp phát hiện.

Native WebSocket trong browser không expose WebSocket-level ping frame. Bạn thường phải dùng application-level heartbeat:

```ts
socket.send(JSON.stringify({ type: 'ping', ts: Date.now() }));
```

Server trả:

```json
{ "type": "pong", "ts": 1710000000000 }
```

Nếu quá lâu không nhận `pong`, đóng connection và reconnect.

### 3.5. Message contract

Đừng gửi object tùy hứng. Real-time app cần message envelope rõ:

```ts
type RealtimeMessage<T> = {
  id: string;
  type: string;
  channel: string;
  version: number;
  timestamp: number;
  data: T;
};
```

Các field quan trọng:

- `id`: chống duplicate, idempotency
- `type`: route handler
- `channel`: biết message thuộc stream nào
- `version`: migrate schema
- `timestamp` hoặc `sequence`: ordering/recovery
- `data`: payload thật

### 3.6. Ordering, duplicate và idempotency

Realtime không nên giả định message luôn đến đúng thứ tự hoặc chỉ đến một lần.

Ví dụ xử lý update theo sequence:

```ts
type PriceUpdate = {
  symbol: string;
  price: number;
  sequence: number;
};

const lastSequenceBySymbol = new Map<string, number>();

function applyPriceUpdate(update: PriceUpdate) {
  const lastSequence = lastSequenceBySymbol.get(update.symbol) ?? 0;

  if (update.sequence <= lastSequence) {
    return;
  }

  lastSequenceBySymbol.set(update.symbol, update.sequence);
  updatePriceInStore(update);
}
```

### 3.7. Backpressure

Backpressure xảy ra khi server gửi nhanh hơn client xử lý. Dấu hiệu:

- UI lag
- memory tăng
- message queue dài
- tab crash
- state update quá nhiều

Cách xử lý:

- server gửi snapshot + delta thay vì từng event nhỏ
- throttle/batch ở client
- drop message cũ nếu chỉ cần latest value
- dùng binary/protobuf nếu payload lớn
- giảm subscription scope
- pause stream khi tab hidden nếu nghiệp vụ cho phép

### 3.8. React integration

Trong React, WebSocket nên được quản lý ở một layer ổn định:

- singleton manager hoặc provider ở app shell
- hook subscribe/unsubscribe theo channel
- cleanup khi component unmount
- tránh tạo nhiều socket cho cùng một stream
- dùng `useRef` cho socket instance, không để socket trong state nếu không cần render

```tsx
import { useEffect, useRef, useState } from 'react';

export function useWebSocket(url: string) {
  const socketRef = useRef<WebSocket | null>(null);
  const [status, setStatus] = useState<'connecting' | 'open' | 'closed'>(
    'connecting'
  );

  useEffect(() => {
    const socket = new WebSocket(url);
    socketRef.current = socket;

    socket.addEventListener('open', () => setStatus('open'));
    socket.addEventListener('close', () => setStatus('closed'));

    return () => {
      socket.close(1000, 'component unmounted');
      socketRef.current = null;
    };
  }, [url]);

  return { socketRef, status };
}
```

### 3.9. Shared subscription manager

Nếu 5 component cùng cần `prices:BTC`, không nên tạo 5 WebSocket/subscription riêng. Dùng reference counting:

```ts
class SubscriptionManager {
  private counts = new Map<string, number>();

  subscribe(channel: string) {
    const count = this.counts.get(channel) ?? 0;
    this.counts.set(channel, count + 1);

    if (count === 0) {
      this.send({ type: 'subscribe', channel });
    }

    return () => this.unsubscribe(channel);
  }

  private unsubscribe(channel: string) {
    const nextCount = (this.counts.get(channel) ?? 1) - 1;

    if (nextCount <= 0) {
      this.counts.delete(channel);
      this.send({ type: 'unsubscribe', channel });
      return;
    }

    this.counts.set(channel, nextCount);
  }

  private send(message: unknown) {
    // send through shared socket
  }
}
```

### 3.10. UI batching

Nếu nhận 1000 messages/s, không nên `setState` 1000 lần/s. Batch theo animation frame:

```tsx
function useBatchedMessages<T>(onBatch: (messages: T[]) => void) {
  const queueRef = useRef<T[]>([]);
  const frameRef = useRef<number | null>(null);

  return (message: T) => {
    queueRef.current.push(message);

    if (frameRef.current !== null) return;

    frameRef.current = requestAnimationFrame(() => {
      const batch = queueRef.current;
      queueRef.current = [];
      frameRef.current = null;
      onBatch(batch);
    });
  };
}
```

### 3.11. Socket.IO

Socket.IO không phải “raw WebSocket”. Nó dùng protocol riêng trên Engine.IO, có thể dùng polling rồi upgrade lên WebSocket.

Socket.IO mạnh ở:

- event API: `emit`, `on`
- auto reconnect
- rooms
- namespaces
- acknowledgements
- binary support
- adapters để scale nhiều server
- fallback transport

Client:

```ts
import { io } from 'socket.io-client';

const socket = io('https://api.example.com/orders', {
  auth: { token: accessToken },
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 1000,
  transports: ['websocket', 'polling'],
});

socket.on('connect', () => {
  socket.emit('join-room', 'orders:me');
});

socket.on('order-updated', (event) => {
  console.log(event);
});
```

### 3.12. Socket.IO rooms vs namespaces

| Khái niệm | Ý nghĩa | Ví dụ |
|---|---|---|
| Namespace | Tách endpoint logic trên cùng server | `/chat`, `/admin`, `/orders` |
| Room | Nhóm socket bên trong namespace | `room:123`, `user:42`, `project:abc` |

Server:

```ts
io.of('/chat').on('connection', (socket) => {
  socket.on('join-room', (roomId: string) => {
    socket.join(roomId);
  });

  socket.on('message', ({ roomId, text }) => {
    io.of('/chat').to(roomId).emit('message', {
      id: crypto.randomUUID(),
      text,
    });
  });
});
```

Rule thực tế:

- dùng **namespace** để tách domain hoặc middleware lớn
- dùng **room** cho dynamic grouping: chat room, user-specific room, project room
- tránh tạo namespace động quá nhiều nếu room là đủ

### 3.13. Acknowledgements và timeout

Ack dùng khi client cần biết server đã xử lý event.

```ts
socket.timeout(5000).emit('place-order', order, (error, response) => {
  if (error) {
    showError('Order timeout');
    return;
  }

  showSuccess(`Order accepted: ${response.orderId}`);
});
```

Ack không thay thế database transaction. Nó chỉ là application-level response cho một event.

### 3.14. Centrifuge/Centrifugo

Tên dễ nhầm:

- **Centrifugo**: realtime server.
- **centrifuge-js / Centrifuge client**: JavaScript SDK dùng ở frontend.

Centrifugo phù hợp khi app cần:

- channel-based pub/sub
- private channels
- JWT auth
- presence
- history
- recovery sau reconnect
- scale ngang qua broker
- nhiều client cùng subscribe stream

```ts
import { Centrifuge } from 'centrifuge';

const centrifuge = new Centrifuge('wss://realtime.example.com/connection/websocket', {
  token: connectionToken,
});

const sub = centrifuge.newSubscription('market:BTC');

sub.on('publication', (ctx) => {
  console.log(ctx.data);
});

sub.subscribe();
centrifuge.connect();
```

### 3.15. Centrifugo presence, history, recovery

| Feature | Ý nghĩa | Khi dùng |
|---|---|---|
| Presence | Biết ai đang online trong channel | Chat, collaborative editing |
| History | Lấy lại message gần đây | Feed, missed notifications |
| Recovery | Client reconnect và recover từ offset/stream position | Market feed, collaboration |
| Private channel token | Token riêng cho channel nhạy cảm | Portfolio/user-specific data |

Ví dụ private channel:

```ts
const sub = centrifuge.newSubscription(`portfolio:${userId}`, {
  getToken: async () => {
    const response = await fetch('/api/realtime/channel-token', {
      method: 'POST',
      body: JSON.stringify({ channel: `portfolio:${userId}` }),
    });

    const { token } = await response.json();
    return token;
  },
});
```

### 3.16. Scaling realtime

Scaling realtime khác REST:

- mỗi connection giữ memory/file descriptor
- load balancer phải hiểu WebSocket upgrade
- nếu dùng nhiều server, cần chia sẻ pub/sub state
- room/channel membership phải đồng bộ qua adapter/broker
- cần rate limit connect/message/subscription

Chiến lược:

- **Socket.IO**: Redis adapter hoặc compatible adapter.
- **Centrifugo**: dùng broker/engine như Redis, NATS tùy setup.
- **Native WebSocket**: tự build registry, broker, sticky session hoặc pub/sub layer.

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Native WebSocket client có reconnect

```ts
type MessageHandler = (message: unknown) => void;

export class RealtimeSocket {
  private socket: WebSocket | null = null;
  private attempts = 0;
  private subscriptions = new Set<string>();

  constructor(
    private readonly url: string,
    private readonly onMessage: MessageHandler
  ) {}

  connect() {
    this.socket = new WebSocket(this.url);

    this.socket.addEventListener('open', () => {
      this.attempts = 0;
      for (const channel of this.subscriptions) {
        this.send({ type: 'subscribe', channel });
      }
    });

    this.socket.addEventListener('message', (event) => {
      this.onMessage(JSON.parse(event.data));
    });

    this.socket.addEventListener('close', (event) => {
      if (!shouldReconnect(event.code)) return;
      window.setTimeout(() => this.connect(), getReconnectDelay(this.attempts++));
    });
  }

  subscribe(channel: string) {
    this.subscriptions.add(channel);
    this.send({ type: 'subscribe', channel });
  }

  close() {
    this.socket?.close(1000, 'client close');
  }

  private send(payload: unknown) {
    if (this.socket?.readyState !== WebSocket.OPEN) return;
    this.socket.send(JSON.stringify(payload));
  }
}
```

### 4.2. React hook subscribe channel

```tsx
import { useEffect, useState } from 'react';

type Price = {
  symbol: string;
  value: number;
};

export function usePrice(symbol: string) {
  const [price, setPrice] = useState<Price | null>(null);

  useEffect(() => {
    const unsubscribe = realtimeManager.subscribe<Price>(
      `prices:${symbol}`,
      (message) => setPrice(message)
    );

    return unsubscribe;
  }, [symbol]);

  return price;
}
```

### 4.3. Socket.IO emit with acknowledgement

```ts
type PlaceOrderResponse =
  | { ok: true; orderId: string }
  | { ok: false; reason: string };

function placeOrder(order: unknown) {
  socket.timeout(5000).emit(
    'place-order',
    order,
    (error: Error | null, response: PlaceOrderResponse) => {
      if (error) {
        showError('Server did not acknowledge the order');
        return;
      }

      if (!response.ok) {
        showError(response.reason);
        return;
      }

      showSuccess(`Order ${response.orderId} accepted`);
    }
  );
}
```

### 4.4. Centrifuge subscription hook

```tsx
import { useEffect, useState } from 'react';
import type { Subscription } from 'centrifuge';

export function useCentrifugeChannel<T>(channel: string) {
  const [data, setData] = useState<T | null>(null);

  useEffect(() => {
    const subscription: Subscription = centrifuge.newSubscription(channel);

    subscription.on('publication', (ctx) => {
      setData(ctx.data as T);
    });

    subscription.subscribe();

    return () => {
      subscription.unsubscribe();
      subscription.removeAllListeners();
    };
  }, [channel]);

  return data;
}
```

### 4.5. Page visibility: giảm tải khi tab hidden

```ts
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    realtimeManager.pauseLowPriorityChannels();
    return;
  }

  realtimeManager.resumeLowPriorityChannels();
  realtimeManager.refetchSnapshot();
});
```

## 5. 🏗️ Production Notes / React Implications

### 5.1. React rendering

Realtime message có thể đến rất nhanh. Nếu mỗi message gọi `setState`, React sẽ render quá nhiều.

Nên:

- batch messages
- update store theo map/entity
- chỉ subscribe component vào phần state cần dùng
- dùng `requestAnimationFrame` cho UI ticker/chart
- dùng virtualization cho list nhiều events
- cleanup listener/socket/subscription khi unmount

### 5.2. Security

Realtime connection vẫn cần security như API thường:

- chỉ dùng `wss://` trong production
- authenticate connection
- authorize từng channel/room
- token ngắn hạn cho private channel
- rate limit connect/message/subscribe
- validate schema message server-side
- không tin client event như `join-admin-room`
- tránh gửi PII không cần thiết qua broadcast

### 5.3. Delivery guarantees

WebSocket tự nó không cho “exactly once delivery” ở tầng business. App cần tự thiết kế:

- message ID để dedupe
- sequence number để bỏ message cũ
- snapshot + delta
- ack cho command quan trọng
- retry idempotent
- refetch snapshot sau reconnect

### 5.4. Offline và reconnect

Khi mất mạng:

- show trạng thái offline/reconnecting
- queue command nếu nghiệp vụ cho phép
- expire queue nếu quá lâu
- resubscribe sau reconnect
- recover history hoặc refetch snapshot
- tránh replay action nguy hiểm như thanh toán/order nếu không idempotent

### 5.5. Observability

Realtime cần metrics riêng:

- connection count
- reconnect count
- message rate
- average payload size
- dropped messages
- ack timeout
- latency p50/p95/p99
- subscription count
- server fanout lag
- client render cost

### 5.6. SSR / Next.js

WebSocket chỉ chạy client-side:

- không tạo WebSocket trong Server Component
- đặt connection trong Client Component/provider
- tránh dùng token server-only trong JS bundle
- nếu dùng cookie auth, cấu hình same-site/CORS/proxy đúng
- cleanup khi route/app unmount

## 6. ⚠️ Common Pitfalls

### 6.1. Tạo nhiều WebSocket cho cùng dữ liệu

Nhiều component mount → nhiều connection → server tốn tài nguyên, message duplicate. Dùng shared manager/provider.

### 6.2. Không reconnect hoặc reconnect quá agresive

Không reconnect thì app “chết” sau mất mạng. Reconnect không backoff thì gây storm. Dùng exponential backoff + jitter.

### 6.3. Không resubscribe sau reconnect

Connection mới không tự biết channel cũ. Sau reconnect cần subscribe lại rooms/channels hoặc dùng SDK hỗ trợ recovery.

### 6.4. Không authenticate/authorize channel

Auth ở connection chưa đủ nếu user có thể tự gửi `subscribe: "admin:*"`. Server phải authorize từng channel/room.

### 6.5. Dùng WebSocket cho server state bình thường

Nếu dữ liệu không cần realtime, dùng HTTP + cache đơn giản hơn. WebSocket làm tăng chi phí vận hành.

### 6.6. Không xử lý duplicate/out-of-order

Realtime stream có thể duplicate khi retry/reconnect. Dùng message ID hoặc sequence.

### 6.7. Gửi payload quá lớn

Payload lớn làm lag UI và nghẽn network. Dùng diff/delta, compression, pagination hoặc binary format nếu thật sự cần.

### 6.8. Memory leak listener

Không remove listener/subscription khi component unmount sẽ gây update vào component đã chết và duplicate handlers.

### 6.9. Không kiểm soát backpressure

Nếu client không xử lý kịp, queue phình ra. Cần throttle, batch hoặc drop event cũ theo nghiệp vụ.

### 6.10. Log token/message nhạy cảm

Realtime message thường chứa user data. Không log token, PII, private channel payload vào console/analytics.

## 7. ✅ Decision Guide / Checklist

### 7.1. Chọn công nghệ nào?

| Nhu cầu | Chọn |
|---|---|
| Realtime 2 chiều đơn giản, team muốn control protocol | Native WebSocket |
| Chat/collaboration cần rooms, ack, reconnect nhanh | Socket.IO |
| Enterprise pub/sub nhiều channels, presence, history, recovery | Centrifugo + centrifuge-js |
| Server chỉ push updates, client không cần gửi nhiều | SSE |
| Data không cần realtime | HTTP + React Query/SWR cache |
| Multi-server Socket.IO | Socket.IO + adapter/broker |
| Private per-user stream quy mô lớn | Centrifugo private channels/JWT |

### 7.2. Checklist trước khi merge realtime feature

- [ ] Dùng `wss://` ở production.
- [ ] Có auth và channel/room authorization.
- [ ] Có reconnect với backoff + jitter.
- [ ] Có resubscribe/recover sau reconnect.
- [ ] Có cleanup socket/listener/subscription khi unmount.
- [ ] Có message schema/version.
- [ ] Có message ID hoặc sequence nếu cần dedupe/order.
- [ ] Có backpressure strategy.
- [ ] Có UI trạng thái connecting/reconnecting/offline.
- [ ] Có rate limit server-side.
- [ ] Có metrics: reconnect, latency, message rate, errors.
- [ ] Có fallback/refetch snapshot sau reconnect.

### 7.3. Checklist React

- [ ] Không tạo socket trong render.
- [ ] Không tạo socket trong mỗi component nhỏ.
- [ ] Dùng provider/manager cho connection shared.
- [ ] Dùng `useRef` cho socket instance.
- [ ] Batch state updates nếu message rate cao.
- [ ] Cleanup trong `useEffect`.
- [ ] Không set state sau unmount.

## 8. 🎤 Short Interview Answer

Theo em, WebSocket là protocol tốt khi cần realtime 2 chiều như chat, trading, collaboration hoặc live dashboard. Nhưng dùng production thì không chỉ mở `new WebSocket()` là xong. Em sẽ thiết kế message contract rõ, auth connection, authorize theo channel, xử lý reconnect bằng exponential backoff, resubscribe sau reconnect và có cách recover missed messages bằng history hoặc refetch snapshot.

Nếu app chỉ cần realtime đơn giản và muốn control protocol, em dùng native WebSocket. Nếu cần rooms, acknowledgements, auto reconnect và fallback transport nhanh, em cân nhắc Socket.IO. Nếu hệ thống lớn cần pub/sub, presence, history, recovery và scale ngang, em sẽ cân nhắc Centrifugo với client Centrifuge.

Điểm quan trọng trong React là không tạo nhiều connection theo từng component. Em thường đặt connection ở provider/manager, component chỉ subscribe channel cần dùng, cleanup khi unmount và batch update UI nếu message đến nhanh. Với realtime, em cũng luôn hỏi về ordering, duplicate messages, backpressure và security trước khi chọn giải pháp.

## 9. 🧾 Ghi nhớ nhanh

- **WebSocket**: raw, nhẹ, bidirectional, tự lo reconnect/protocol.
- **Socket.IO**: event API, rooms, namespaces, ack, reconnect, fallback.
- **Centrifugo**: pub/sub server, channels, presence, history, recovery, scale.
- **SSE**: server → client, đơn giản hơn nếu không cần 2 chiều.
- **Reconnect**: dùng exponential backoff + jitter.
- **Resubscribe**: bắt buộc sau reconnect nếu SDK không tự recover.
- **Backpressure**: batch/throttle/drop theo nghiệp vụ.
- **Security**: auth connection chưa đủ, phải authorize channel/room.
- **React**: shared manager/provider, cleanup listener, batch state updates.
- **Delivery**: dùng message ID/sequence/snapshot để chống duplicate/missed messages.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| WebSocket | Protocol giao tiếp 2 chiều qua một connection lâu dài |
| `ws://` | WebSocket không mã hóa |
| `wss://` | WebSocket qua TLS, nên dùng ở production |
| HTTP Upgrade | Cơ chế nâng HTTP connection thành WebSocket |
| Polling | Client gọi server định kỳ để hỏi data mới |
| Long polling | Client giữ request mở cho đến khi server có data |
| SSE | Server-Sent Events, server push một chiều qua HTTP |
| Socket.IO | Realtime framework dùng protocol riêng, hỗ trợ rooms/reconnect/fallback |
| Engine.IO | Tầng transport bên dưới Socket.IO |
| Namespace | Không gian logic trong Socket.IO như `/chat`, `/orders` |
| Room | Nhóm socket để broadcast trong Socket.IO |
| Acknowledgement | Callback/response xác nhận event đã được server xử lý |
| Centrifugo | Realtime pub/sub server |
| Centrifuge client | SDK kết nối frontend tới Centrifugo |
| Channel | Stream pub/sub mà client subscribe |
| Presence | Thông tin ai đang online trong channel |
| History | Lưu message gần đây để client lấy lại |
| Recovery | Khôi phục message bị miss sau reconnect |
| Backpressure | Khi producer gửi nhanh hơn consumer xử lý |
| Heartbeat | Ping/pong định kỳ để phát hiện dead connection |
| Exponential backoff | Retry với delay tăng dần |
| Jitter | Random delay nhỏ để tránh nhiều client reconnect cùng lúc |
| Idempotency | Xử lý lặp lại cùng message mà không gây sai state |
| Sticky session | Load balancer giữ client về cùng server |
| Broker | Hệ thống trung gian pub/sub như Redis/NATS |

## 11. 📚 Nguồn chính thức đã đối chiếu

- MDN WebSocket API: <https://developer.mozilla.org/en-US/docs/Web/API/WebSocket>
- Socket.IO client options: <https://socket.io/docs/v4/client-options/>
- Socket.IO rooms: <https://socket.io/docs/v4/rooms/>
- Socket.IO namespaces: <https://socket.io/docs/v4/namespaces/>
- Socket.IO emitting events / acknowledgements: <https://socket.io/docs/v4/emitting-events/>
- Centrifugo client SDK API: <https://centrifugal.dev/docs/transports/client_api>
- Centrifugo channels/namespaces: <https://centrifugal.dev/docs/server/channels>
