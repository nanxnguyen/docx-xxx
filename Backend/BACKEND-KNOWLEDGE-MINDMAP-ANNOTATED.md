# 🧠 BACKEND DEVELOPER (SENIOR) KNOWLEDGE MINDMAP - ANNOTATED VERSION
## Node.js | Express | NestJS | TypeScript
// 🇻🇳 Bản đồ kiến thức toàn diện cho Backend Developer cấp Senior - có chú thích đầy đủ

> **Specialized for Node.js Ecosystem**  
> Focus: Production-grade Node.js, Express patterns, NestJS architecture, TypeORM/Prisma

---

## 🎯 QUICK START - INLINE COMMENTS SECTION

// 🇻🇳 PHẦN CHÚ THÍCH INLINE CHO CÁC CODE EXAMPLES

### Node.js Event Loop - Blocking vs Non-blocking

```javascript
// =====================================================
// ❌ BAD EXAMPLE: Blocking Event Loop - KHÔNG NÊN DÙNG!
// =====================================================
const express = require('express');
const app = express();

app.get('/process', async (req, res) => {
  // Bước 1: Lấy 100k records từ database (async, không chặn)
  const data = await getData();
  
  // ⚠️ BẢ LỖI: expensiveSync() chạy SYNCHRONOUS, chặn event loop!
  // Mọi request khác phải chờ 1-2 giây để được xử lý
  // Điều này gây "thundering herd" effect - tất cả request chậm
  const result = data.map(item => expensiveSync(item));
  
  // Trả response chậm (1-2s thay vì 50ms)
  res.json(result);
});

app.listen(3000); // Server này sẽ RAM quá tải

// =====================================================
// ✅ GOOD EXAMPLE: Offload to Worker Thread - NÊN DÙNG!
// =====================================================
const { Worker } = require('worker_threads');
// Worker threads: chạy JavaScript trên thread riêng, không chặn main thread

app.get('/process', async (req, res) => {
  // Bước 1: Lấy data (async, không chặn main thread)
  const data = await getData();
  
  // Bước 2: Tạo worker thread để xử lý tác vụ nặng CPU
  // Main thread vẫn tiếp tục xử lý request khác
  // Worker thread chạy song song trên CPU core khác
  const worker = new Worker('./worker.js', { workerData: data });
  
  // Bước 3: Khi worker xong, gửi kết quả về
  // Cách này: latency vẫn ~100ms, nhưng throughput cao (1000 req/s)
  worker.on('message', result => {
    res.json(result); // Response gửi đi khi worker xong
  });
  
  // Bước 4: Main thread trở về handle request tiếp theo ngay lap tức
});

app.listen(3000); // Server này KHỎE: 1000 req/s ~100ms latency
```

### Circuit Breaker Pattern - Chống Cascading Failures

```javascript
// =====================================================
// PATTERN: Circuit Breaker - Bộ ngắt mạch
// =====================================================
// Mục đích: Khi downstream service fail (DB, API), ngửi/ấm khỏi request
// Danh theo: Chia cầu điện - khi quá tải, ngắt cầu để bảo vệ toàn bộ hệ thống

class CircuitBreaker {
  // Constructor nhận threshold (50% error rate = ngắt) và timeout (60s)
  constructor(threshold = 0.5, timeout = 60000) {
    // ✅ State 3 chiều: CLOSED (bình thường) → OPEN (ngắt) → HALF_OPEN (test lại)
    this.state = 'CLOSED'; // Trạng thái bình thường = circuit "thông"
    
    // Đếm số lần thất bại (để tính tỷ lệ error)
    this.failures = 0;
    
    // Đếm số lần thành công
    this.successes = 0;
    
    // Ngưỡng tỷ lệ lỗi (nếu failures/(failures+successes) > 50% → ngắt)
    this.threshold = threshold;
    
    // Thời gian chờ trước khi test lại (OPEN → HALF_OPEN)
    // Ví dụ: service fail, chờ 60s, rồi thử 1 request. Nếu OK thì trở về CLOSED
    this.timeout = timeout;
  }

  async execute(fn) {
    // ===== LOGIC KIỂM TRA STATE =====
    if (this.state === 'OPEN') {
      // Nếu ngắt, chờ timeout
      if (Date.now() - this.openedAt > this.timeout) {
        // Sau 60s, chuyển sang HALF_OPEN = thử test lại 1 request
        this.state = 'HALF_OPEN';
      } else {
        // Nếu chưa hết timeout, từ chối ngay (fail fast)
        // Lợi điểm: không lãng phí thời gian retry downstream service
        throw new Error('Circuit breaker is OPEN - service unavailable');
      }
    }

    // ===== THỰC THI HAM =====
    try {
      // Gọi function (VD: call DB, external API)
      const result = await fn();
      
      // Nếu thành công, ghi nhận
      this.onSuccess();
      
      return result;
      
    } catch (error) {
      // Nếu lỗi, ghi nhận
      this.onFailure();
      
      // Throw lại để caller biết lỗi
      throw error;
    }
  }

  onSuccess() {
    // Reset counter lỗi khi thành công
    // (cơ chế "forgetting" - không nhớ lỗi cũ)
    this.failures = 0;
    
    // Nếu đang test (HALF_OPEN) và request thành công → chuyển về CLOSED
    // Tức là service đã khỏe lại, tiếp tục bình thường
    if (this.state === 'HALF_OPEN') this.state = 'CLOSED';
  }

  onFailure() {
    // Tăng counter lỗi
    this.failures++;
    
    // Tính tổng = failures + successes
    const total = this.failures + this.successes;
    
    // Nếu tỷ lệ lỗi vượt threshold (50%) → ngắt mạch
    if (this.failures / total > this.threshold) {
      // Chuyển sang OPEN = ngắt không request
      this.state = 'OPEN';
      
      // Lưu thời điểm ngắt để countdown timeout
      this.openedAt = Date.now();
    }
  }
}

// ===== SỬ DỤNG CIRCUIT BREAKER =====
const breaker = new CircuitBreaker(0.5, 60000); // 50% error rate, 60s timeout

// VD: Gọi database
app.get('/users/:id', async (req, res) => {
  try {
    // Nếu DB fail 5 lần liên tiếp → breaker OPEN
    const user = await breaker.execute(() => 
      db.users.findOne(req.params.id)
    );
    
    res.json(user);
    
  } catch (error) {
    // Nếu circuit OPEN, return 503 ngay (không retry)
    // Điều này ngăn "cascading failure" - DB bị crush
    if (error.message.includes('OPEN')) {
      res.status(503).json({ error: 'Service temporarily unavailable' });
    } else {
      res.status(500).json({ error: error.message });
    }
  }
});
```

### NestJS Controller + Guard + Pipe (Full Execution Order)

```typescript
// =====================================================
// NestJS EXECUTION ORDER: Middleware → Guard → Pipe → Controller → Interceptor
// =====================================================

import { Controller, Get, Post, Body, Param, UseGuards, UsePipes } from '@nestjs/common';
import { JwtAuthGuard } from './auth.guard'; // Authentication: verify JWT token
import { RolesGuard } from './roles.guard'; // Authorization: check user.role
import { ValidationPipe } from '@nestjs/common'; // Validation: validate DTO
import { CreateUserDto } from './dtos/create-user.dto';

// Step 1️⃣: CONTROLLER DECORATOR
// @Controller('users') = tạo route `/users`
@Controller('users')
// Step 2️⃣: GUARD DECORATOR (apply to all routes in controller)
// JwtAuthGuard chạy TRƯỚC tất cả route handlers
// - Kiểm tra token = hợp lệ?
// - Nếu lỗi → throw UnauthorizedException → request bị reject
@UseGuards(JwtAuthGuard) 
export class UsersController {
  constructor(
    // Dependency Injection: inject UserService vào controller
    private userService: UserService
  ) {}

  // Route: GET /users/:id
  @Get(':id')
  // Step 3️⃣: GUARDS (specific route)
  // RolesGuard = kiểm tra user.role == 'admin'?
  @UseGuards(RolesGuard)
  // Step 4️⃣️: PIPES (transformation + validation)
  // ParseIntPipe = convert string 'id' → number (type: 123 thay vì "123")
  // @Param('id', ParseIntPipe) = tự động call pipe
  findOne(
    @Param('id', ParseIntPipe) id: number // ParseIntPipe giúp convert '123' → 123
  ) {
    // Bây giờ id là NUMBER, không phải STRING
    // Step 5️⃣: CONTROLLER HANDLER
    // - Gọi userService.findOne(id)
    // - Return user object
    return this.userService.findOne(id);
  }

  // Route: POST /users
  @Post()
  // Pipe: ValidationPipe = validate request body theo DTO
  // whitelist: true = bỏ các field ko định nghĩa trong DTO
  @UsePipes(new ValidationPipe({ whitelist: true }))
  // Step 5️⃣: CONTROLLER HANDLER (nhận request body)
  create(
    // @Body() = lấy request body
    // ValidationPipe tự động validate createUserDto ({name, email, password})
    // Nếu invalid → throw BadRequestException
    @Body() createUserDto: CreateUserDto
  ) {
    // Lúc này DTO đã validate + transform
    // Ví dụ: trim() whitespace, convert type
    return this.userService.create(createUserDto);
  }
}

// ===== EXECUTION FLOW EXAMPLE =====
/*
Request: POST /users
Content-Type: application/json
Authorization: Bearer <jwt_token>
Body: { name: "John", email: "john@example.com" }

Step 1: Middleware (express.json) → parse JSON body
Step 2: Guard (JwtAuthGuard) → verify JWT token
        - Extract token from header
        - Call jwt.verify()
        - Nếu invalid → throw UnauthorizedException → HTTP 401
        - Attach user to request: req.user = decoded_user

Step 3: Pipe (ValidationPipe) → validate DTO
        - Check required fields (name, email)
        - Check types (string, number, etc)
        - Run class-validator decorators (@IsEmail, @MinLength)
        - Nếu invalid → throw BadRequestException → HTTP 400
        
Step 4: Controller Handler → create(createUserDto)
        - Call userService.create()
        - Return user object

Step 5: Interceptor (if any) → transform response
        - Wrap response: { data: {...}, meta: {...} }
        
Step 6: Return response
        Response: HTTP 201 Created
        Body: { data: { id: 1, name: "John", email: "john@example.com" } }

❌ If any Guard/Pipe throw exception:
        → Jump to Exception Filter
        → Return error response
*/
```

### Caching Pattern: Cache-Aside vs Write-Through

```typescript
// =====================================================
// CACHING STRATEGY 1: CACHE-ASIDE (Lazy Loading)
// =====================================================
// Lợi: Chỉ cache dữ liệu được access
// Hại: Cache miss penalty (first access slow)

@Injectable()
export class ProductService {
  constructor(
    @InjectRepository(Product)
    private productRepo: Repository<Product>,
    private redis: Redis // Redis cache
  ) {}

  async getProduct(id: number) {
    // Bước 1: Check cache trước
    const cacheKey = `product:${id}`;
    const cached = await this.redis.get(cacheKey);
    
    // Nếu cache hit → return ngay (fast!)
    if (cached) {
      console.log(`Cache HIT: product ${id}`);
      return JSON.parse(cached);
    }

    // Bước 2: Cache MISS → query database
    console.log(`Cache MISS: product ${id} - query DB`);
    const product = await this.productRepo.findOne({ where: { id } });
    
    if (!product) throw new NotFoundException();

    // Bước 3: Save to cache (cho lần sau)
    // TTL = 3600 (1 hour) = cache sẽ tự xóa sau 1 giờ
    await this.redis.setex(cacheKey, 3600, JSON.stringify(product));

    return product;
  }

  async updateProduct(id: number, dto: UpdateProductDto) {
    // Bước 1: Update database
    const product = await this.productRepo.update({ id }, dto);

    // Bước 2: INVALIDATE cache
    // ⚠️ QUAN TRỌNG: Phải xóa cache khi data thay đổi
    // Nếu không xóa → client vẫn cache dữ liệu cũ (stale data)
    await this.redis.del(`product:${id}`);

    return product;
  }
}

// =====================================================
// CACHING STRATEGY 2: WRITE-THROUGH
// =====================================================
// Lợi: Cache luôn fresh (ko stale data)
// Hại: Write latency cao (update cache + DB đồng thời)

async updateProductWriteThrough(id: number, dto: UpdateProductDto) {
  // Bước 1: Update cache + database CÙNG LÚC
  // ⚠️ Chậm hơn vì phải update 2 nơi
  const [cacheResult, dbResult] = await Promise.all([
    // Update cache
    this.redis.setex(
      `product:${id}`,
      3600,
      JSON.stringify(dto)
    ),
    // Update database
    this.productRepo.update({ id }, dto)
  ]);

  return dbResult;
}

// =====================================================
// CACHE STAMPEDE PREVENTION: Distributed Lock
// =====================================================
// Problem: Cache expiration → 10000 requests hit DB simultaneously → crash
// Solution: Use distributed lock (Redlock) to serialize cache updates

async getProductWithLock(id: number) {
  const cacheKey = `product:${id}`;
  const lockKey = `lock:${cacheKey}`;

  // Bước 1: Check cache
  const cached = await this.redis.get(cacheKey);
  if (cached) return JSON.parse(cached);

  // Bước 2: Acquire distributed lock (5s timeout)
  // Nếu lock acquire fail → return toFileError (reduce load)
  const lock = await this.redlock.acquire([lockKey], 5000);

  try {
    // Bước 3: Double-check cache (race condition check)
    // Có thể request khác đã fill cache trong lúc chờ lock
    const cachedAgain = await this.redis.get(cacheKey);
    if (cachedAgain) return JSON.parse(cachedAgain);

    // Bước 4: Only ONE request queries DB (others are waiting)
    // Điều này ngăn "thundering herd" - 10k request → 1 DB query
    const product = await this.productRepo.findOne({ where: { id } });

    // Bước 5: Save to cache
    await this.redis.setex(cacheKey, 3600, JSON.stringify(product));

    return product;

  } finally {
    // Bước 6: Release lock
    // Các request khác đang chờ sẽ acquire lock và follow bước 4-5
    await lock.release();
  }
}
```

### TypeORM: N+1 Problem & Solutions

```typescript
// =====================================================
// PROBLEM: N+1 Query - Very Common Performance Bug!
// =====================================================

// ❌ BAD: N+1 queries (1 query get users + N queries get posts)
async getUsersWithPostsBad() {
  // Query 1: SELECT * FROM users (lấy 100 users)
  const users = await this.usersRepository.find();

  // Queries 2-101: SELECT * FROM posts WHERE author_id = ?
  // Vòng lặp này chạy N lần (100 lần)!
  // Total: 1 + 100 = 101 queries ❌ VERY SLOW
  for (const user of users) {
    user.posts = await this.postsRepository.find({
      where: { authorId: user.id }
    });
  }

  return users; // Đợi 101 queries mất ~2-5 giây
}

// ===== SOLUTION 1: EAGER LOADING (JOIN) =====
// ✅ GOOD: 1 query with JOIN
async getUsersWithPostsGood() {
  // JOIN query: SELECT users.*, posts.* FROM users LEFT JOIN posts
  // Total: 1 query ✅ FAST (10-50ms)
  return this.usersRepository.find({
    relations: ['posts', 'profile'] // Tự động JOIN
  });
}

// ===== SOLUTION 2: QueryBuilder (Complex Queries) =====
// ✅ Khi cần filter/sort/complex joins
async searchUsers(query: string) {
  return this.usersRepository
    .createQueryBuilder('user') // Alias 'user' → SELECT user.* FROM users user
    .leftJoinAndSelect('user.posts', 'posts') // LEFT JOIN posts ON posts.author_id = user.id
    .where('user.name ILIKE :query', { query: `%${query}%` }) // WHERE user.name LIKE '%query%'
    .orWhere('user.email ILIKE :query', { query: `%${query}%` }) // OR user.email LIKE '%query%'
    .orderBy('user.createdAt', 'DESC') // ORDER BY user.created_at DESC
    .take(20) // LIMIT 20
    .getMany(); // Execute query
}

// ===== SOLUTION 3: Batch Loading =====
// ✅ Khi không thể dùng JOIN
async getUsersWithPostsBatch() {
  // Query 1: Get all users
  const users = await this.usersRepository.find();

  // Query 2: Get posts for ALL users cùng lúc (1 query)
  // WHERE author_id IN (1, 2, 3, ..., 100)
  const authorIds = users.map(u => u.id);
  const allPosts = await this.postsRepository.find({
    where: { authorId: In(authorIds) }
  });

  // Map posts to users (in-memory)
  const postsMap = new Map<number, Post[]>();
  for (const post of allPosts) {
    if (!postsMap.has(post.authorId)) {
      postsMap.set(post.authorId, []);
    }
    postsMap.get(post.authorId)!.push(post);
  }

  // Attach posts to users
  for (const user of users) {
    user.posts = postsMap.get(user.id) || [];
  }

  // Total: 2 queries ✅ Better than N+1
  return users;
}
```

### Database Transactions: Pessimistic vs Optimistic Locking

```typescript
// =====================================================
// PROBLEM: Race Condition - Overselling
// =====================================================
// Scenario: Last item in stock (quantity = 1)
//          User A và User B cùng mua → stock = -1 (oversold!)

// ❌ BAD: No locking - Race condition
async checkoutBad(productId: number) {
  const product = await this.productRepo.findOne(productId);
  
  // User A: Check quantity = 1 (OK)
  // [User B: Check quantity = 1 (OK)]
  if (product.quantity < 1) throw new Error('Out of stock');
  
  // User A: quantity -= 1 = 0
  // [User B: quantity -= 1 = 0 WRONG! Should be -1 or reject]
  product.quantity -= 1;
  
  // Both save → final quantity = 0 (should be -1 or reject both)
  await this.productRepo.save(product);
}

// ===== SOLUTION 1: PESSIMISTIC LOCK =====
// ✅ Lock row before modifying (sequential)
async checkoutPessimistic(productId: number) {
  return this.productRepo.manager.transaction(async (tx) => {
    // SELECT ... FOR UPDATE = Lock row (block other transactions)
    const product = await tx.products.findOne({
      where: { id: productId },
      lock: { mode: 'pessimistic_write' } // Lock mode
    });

    // User A acquires lock, User B waits here
    // [User B blocked until User A commit/rollback]

    if (product.quantity < 1) throw new Error('Out of stock');

    product.quantity -= 1;
    await tx.save(product);

    // User A commits, User B now acquires lock
    // User B checks quantity = 0 → throw error (correct!)
  });
}

// ===== SOLUTION 2: OPTIMISTIC LOCK =====
// ✅ Use version column to detect conflict
@Entity()
class Product {
  @Column() quantity: number;
  
  @Version() // Auto-incremented on every save
  version: number;
}

async checkoutOptimistic(productId: number) {
  const product = await this.productRepo.findOne(productId);
  // product.version = 1

  // User A: Read version = 1
  // [User B: Read version = 1]

  if (product.quantity < 1) throw new Error('Out of stock');

  product.quantity -= 1;

  // User A saves with version check:
  // UPDATE products SET quantity = 0, version = 2 WHERE id = ? AND version = 1
  // ✅ Success (version matched)

  // User B tries to save with same version:
  // UPDATE products SET quantity = 0, version = 2 WHERE id = ? AND version = 1
  // ❌ Fail! (version mismatch - User A already incremented)
  // Throw OptimisticLockError → User B retries

  await this.productRepo.save(product); // Auto checks version
}

// ===== SOLUTION 3: ATOMIC UPDATE (Best) =====
// ✅ Atomic SQL operation (no locking overhead)
async checkoutAtomic(productId: number) {
  // SQL: UPDATE quantity = quantity - 1 WHERE id = ? AND quantity > 0
  // Pro: Atomic, no locks, fast
  // Con: complex business logic not possible
  
  const result = await this.productRepo.update(
    { id: productId, quantity: MoreThan(0) }, // WHERE quantity > 0
    { quantity: () => 'quantity - 1' } // UPDATE quantity = quantity - 1
  );

  if (result.affected === 0) throw new Error('Out of stock');

  return this.productRepo.findOne(productId);
}
```

### Idempotent Consumer Pattern (Event-Driven)

```typescript
// =====================================================
// PROBLEM: Message Broker delivers AT-LEAST-ONCE
// =====================================================
// means: Message có thể duplicated, received 2+ lần
// Solution: Idempotent consumer - process same message multiple times = same result

// ===== IDEMPOTENT CONSUMER PATTERN =====
@Injectable()
export class OrderConsumer {
  constructor(
    private orderService: OrderService,
    private redis: Redis // Store message IDs
  ) {}

  @EventPattern('order.created')
  async handleOrderCreated(event: OrderCreatedEvent) {
    // Sự kiện: đơn hàng được tạo
    // Event: { id: "uuid-123", data: { orderId: 1, userId: 1 } }

    const messageId = event.id; // Message ID = unique identifier
    const dedupKey = `processed:${messageId}`; // Deduplication key

    // Bước 1: Check if already processed
    const exists = await this.redis.exists(dedupKey);
    
    if (exists) {
      // Message đã xử lý trước đó
      // Return ngay (idempotent!) - kết quả giống hệt lần trước
      console.log(`Message ${messageId} already processed, skipping`);
      return;
    }

    try {
      // Bước 2: Process message
      // VD: Create order, reserve inventory, send email
      await this.orderService.createOrder(event.data);

      // Bước 3: Mark as processed (save to cache)
      // TTL = 7 days = message ID stored 7 days
      // (nếu message retry sau 7 days, treat as new)
      await this.redis.setex(dedupKey, 7 * 24 * 3600, '1');

    } catch (error) {
      // Message processing failed
      // Log error, then throw to trigger retry
      console.error(`Failed to process ${messageId}`, error);
      throw error; // Message Broker sẽ retry
    }
  }
}

// ===== SAGA PATTERN: Distributed Transaction =====
// =====================================================
// Problem: Multi-step transaction across multiple services
// Order → Inventory → Payment
// If Payment fails → Rollback Inventory & Order

@Injectable()
export class OrderSaga {
  constructor(
    private orderService: OrderService,
    private inventoryService: InventoryService,
    private paymentService: PaymentService,
    private eventBus: EventBus
  ) {}

  async createOrder(dto: CreateOrderDto) {
    // Step 1: Create order (status = PENDING)
    const order = await this.orderService.create({
      ...dto,
      status: 'PENDING'
    });

    try {
      // Step 2: Reserve inventory
      await this.inventoryService.reserve(order.id, dto.items);
      // Publish event: inventory.reserved

      // Step 3: Process payment
      await this.paymentService.charge(order.id, dto.totalAmount);
      // Publish event: payment.completed

      // Step 4: Update order status = CONFIRMED
      await this.orderService.update(order.id, { status: 'CONFIRMED' });
      // Publish event: order.confirmed

    } catch (error) {
      // COMPENSATING TRANSACTIONS (rollback)
      // Step 3a: Payment failed → Release inventory
      await this.inventoryService.release(order.id);
      
      // Step 3b: Update order = CANCELLED
      await this.orderService.update(order.id, { status: 'CANCELLED' });
      
      // Publish event: order.cancelled

      throw error; // Re-throw for caller
    }
  }
}
```

### Express Middleware: Full Stack Example

```typescript
// =====================================================
// EXPRESS MIDDLEWARE STACK - Complete Example
// =====================================================

import express, { Request, Response, NextFunction } from 'express';
import helmet from 'helmet'; // Security headers
import cors from 'cors'; // Cross-Origin Resource Sharing
import morgan from 'morgan'; // HTTP request logging
import compression from 'compression'; // gzip compression
import rateLimit from 'express-rate-limit'; // Rate limiting
import { v4 as uuid } from 'uuid'; // UUID generation

const app = express();

// ===== MIDDLEWARE STACK (Order Matters!) =====

// 1️⃣ REQUEST ID MIDDLEWARE
// Thêm unique ID cho mỗi request (để trace logs)
const requestIdMiddleware = (req: Request, res: Response, next: NextFunction) => {
  // Lấy ID từ header (nếu có) hoặc tạo mới
  req.id = (req.headers['x-request-id'] as string) || uuid();
  
  // Gắn ID vào response header
  res.setHeader('X-Request-ID', req.id);
  
  // Continue to next middleware
  next();
};

app.use(requestIdMiddleware);

// 2️⃣ SECURITY HEADERS
// helmet = set headers chống XSS, clickjacking, MIME sniffing, etc.
app.use(helmet());

// 3️⃣ CORS (Cross-Origin Resource Sharing)
// Allow frontend từ specific domains gọi API
app.use(cors({
  origin: ['https://app.example.com', 'https://admin.example.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true // Allow cookies
}));

// 4️⃣ COMPRESSION (gzip)
// Nén response body (giảm 70-80% size)
// VD: 1MB → 200KB (nhanh hơn 5x)
app.use(compression());

// 5️⃣ HTTP REQUEST LOGGER
// Log mỗi request: GET /api/users 200 15ms
app.use(morgan(':method :url :status :response-time ms'));

// 6️⃣ BODY PARSER (parse JSON)
// Parse request body từ JSON thành object
// VD: req.body = { name: "John" }
app.use(express.json({ limit: '10mb' })); // Max 10MB payload

// 7️⃣ RATE LIMITING
// Giới hạn số request: 100 request / 15 phút / IP
// Ngăn spam, DDoS
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Max 100 requests per window
  message: 'Too many requests, please try again later.',
  standardHeaders: true, // Return rate limit info in RateLimit-* headers
  legacyHeaders: false, // Disable X-RateLimit-* headers
});

app.use(limiter);

// ===== ROUTE HANDLERS =====

app.get('/api/users', (req: Request, res: Response) => {
  // Tại đây:
  // ✅ Request ID đã thêm (req.id)
  // ✅ Security headers đã set
  // ✅ CORS đã check
  // ✅ Body đã nén
  // ✅ Log đã ghi
  // ✅ Rate limit đã check

  res.json({
    requestId: req.id,
    data: [{ id: 1, name: 'John' }],
    timestamp: new Date()
  });
});

// ===== ERROR HANDLING MIDDLEWARE =====
// ⚠️ PHẢI CÓ 4 parameters để Express nhận diện là error handler!
// ⚠️ PHẢI ĐẶT SAU TẤT CẢ ROUTES!

app.use((
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // Log error với request ID để trace
  console.error('Error:', {
    requestId: req.id,
    message: err.message,
    stack: err.stack,
    url: req.url,
    method: req.method
  });

  // Return error response
  const statusCode = (err as any).statusCode || 500;
  res.status(statusCode).json({
    error: {
      requestId: req.id,
      message: err.message,
      code: (err as any).code || 'INTERNAL_ERROR',
      timestamp: new Date()
    }
  });
});

// ===== 404 HANDLER =====
app.use((req: Request, res: Response) => {
  res.status(404).json({
    error: {
      requestId: req.id,
      message: 'Not Found',
      path: req.url
    }
  });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

### Redis Caching with TTL and Invalidation

```typescript
// =====================================================
// REDIS CACHING - TTL & INVALIDATION PATTERNS
// =====================================================

import Redis from 'ioredis';

const redis = new Redis({
  host: 'localhost',
  port: 6379,
  retryStrategy: (times) => Math.min(times * 50, 2000) // Auto-reconnect
});

// ===== PATTERN 1: Simple KEY-VALUE Cache =====
async function cacheSimple(key: string, value: any, ttl: number) {
  // SETEX key = SET + expire in one command (atomic)
  // Format: SETEX product:123 3600 '{"id":123,"name":"...json...}'
  // TTL = 3600 seconds = 1 hour
  
  const serialized = JSON.stringify(value);
  await redis.setex(key, ttl, serialized);
  
  // After 3600 seconds, Redis auto-deletes key
  // ✅ Prevents memory leak (data always expires)
}

async function getCacheSimple(key: string) {
  const cached = await redis.get(key); // Returns string or null
  return cached ? JSON.parse(cached) : null;
}

// ===== PATTERN 2: HASH (for objects) =====
// Better than JSON serialization for large objects
async function cacheHash(key: string, obj: any, ttl: number) {
  // HMSET product:123 id 123 name "Product" price 99.99
  await redis.hmset(key, obj); // Set multiple fields
  
  // Set expiration
  await redis.expire(key, ttl);
}

async function getCacheHash(key: string) {
  // HGETALL product:123 = get all fields
  return redis.hgetall(key); // Returns object
}

// ===== PATTERN 3: CACHE INVALIDATION =====

async function invalidateCache(key: string) {
  // DEL key = delete immediately
  await redis.del(key);
}

async function invalidateCachePattern(pattern: string) {
  // KEYS product:* = find all keys matching pattern
  // ⚠️ SLOW on large datasets, use in background job only
  const keys = await redis.keys(pattern);
  
  if (keys.length > 0) {
    // DEL key1 key2 key3 ... = delete multiple
    await redis.del(...keys);
  }
}

// ===== PATTERN 4: TAG-BASED INVALIDATION =====
// Group related keys + invalidate together

async function cacheWithTag(key: string, value: any, tag: string, ttl: number) {
  // Save actual data
  await redis.setex(key, ttl, JSON.stringify(value));
  
  // Save tag reference: tags:user:123 = [key1, key2, key3]
  // SADD = add to set (unique, unordered)
  await redis.sadd(`tag:${tag}`, key);
  
  // Expire tag too
  await redis.expire(`tag:${tag}`, ttl);
}

async function invalidateByTag(tag: string) {
  // SMEMBERS = get all members of set
  // Get all keys with this tag: [product:123, product:456, ...]
  const keys = await redis.smembers(`tag:${tag}`);
  
  // Delete all keys in set
  if (keys.length > 0) {
    await redis.del(...keys);
  }
  
  // Delete tag itself
  await redis.del(`tag:${tag}`);
}

// Usage:
// Cache all products with tag 'inventory'
app.post('/admin/products/:id', async (req, res) => {
  const product = await updateProduct(req.params.id, req.body);
  
  // Invalidate all related caches
  await invalidateByTag('inventory'); // Deletes all product:* keys
  
  res.json(product);
});

// ===== PATTERN 5: PIPELINE (batch operations) =====
// Send multiple Redis commands in one round-trip

async function cacheBatch(items: Array<{key: string, value: any}>) {
  const pipeline = redis.pipeline(); // Create pipeline
  
  for (const item of items) {
    // Queue commands (not executed yet)
    pipeline.setex(item.key, 3600, JSON.stringify(item.value));
  }
  
  // Execute all commands at once (1 network round-trip)
  // Instead of N round-trips
  await pipeline.exec();
}

// ===== KEYS NAMING CONVENTION =====
// Namespace:Entity:Id = entity:user:123
// Good for: grouping, pattern matching

const keyFormats = {
  user: (id: number) => `user:profile:${id}`,
  product: (id: number) => `product:${id}`,
  cart: (userId: number) => `cart:${userId}`,
  session: (token: string) => `session:${token}`,
  rateLimit: (userId: number) => `ratelimit:${userId}`
};
```

---

## 📚 THAM KHẢO THÊM

Để chi tiết hơn, hãy xem file gốc: **BACKEND-KNOWLEDGE-MINDMAP.md**

File này chứa:
- ✅ Tất cả code examples với chú thích inline (tiếng Việt)
- ✅ Architecture patterns được giải thích rõ ràng
- ✅ Trade-offs và common mistakes
- ✅ Interview questions + answers
- ✅ Study guide & resources

---

**Bản cập nhật:** 2026-02-19  
**Format:** Markdown với inline comments (`//`)  
**Mục đích:** Học tập, chuẩn bị phỏng vấn Backend Senior Developer
