# 🔑 Q52: Hashing, Encryption & Digital Signatures - Phân Biệt & Ứng Dụng Thực Tế

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔑 Q52: Hashing, Encryption & Digital Signatures - Phân Biệt & Ứng Dụng Thực Tế</span></summary>


**❓ Câu Hỏi:**
Phân biệt Hashing, Encryption và Digital Signature. Khi nào dùng từng loại? Giải thích cơ chế hoạt động và ví dụ thực tế với bcrypt, AES, RSA, JWT signing.



#### **📊 So Sánh Tổng Quan: Hash vs Encryption vs Digital Signature**

| Tiêu Chí            | **Hashing**                    | **Encryption**                     | **Digital Signature**               |
| ------------------- | ------------------------------ | ---------------------------------- | ----------------------------------- |
| **Cơ Chế**          | One-way (không đảo ngược)      | Two-way (mã hóa ↔ giải mã)         | Sign & Verify (ký & xác thực)       |
| **Mục Đích**        | Verify integrity, checksum     | Protect confidentiality            | Verify authenticity & integrity     |
| **Reversible?**     | ❌ KHÔNG (cannot decrypt)      | ✅ CÓ (with key)                   | ✅ CÓ (verify only, not decrypt)    |
| **Input → Output**  | Bất kỳ độ dài → Fixed length   | Bất kỳ độ dài → Variable ciphertext | Data → Signature                   |
| **Key Required?**   | ❌ KHÔNG (salt optional)       | ✅ CÓ (symmetric/asymmetric)       | ✅ CÓ (private key sign, public verify) |
| **Use Cases**       | Password storage, checksums    | Data encryption, HTTPS             | JWT tokens, API authentication      |
| **Algorithms**      | bcrypt, SHA-256, MD5 (legacy)  | AES, RSA, ChaCha20                 | RSA, ECDSA, EdDSA                   |
| **Performance**     | Slow (bcrypt: 10 rounds)       | Fast (AES: hardware accelerated)   | Medium (RSA slower than ECDSA)      |

---

#### **🔍 Cơ Chế Hoạt Động Chi Tiết**

Trước khi đi vào code, hãy hiểu rõ **CƠ CHẾ** hoạt động của từng loại để biết **KHI NÀO** dùng **CÁI GÌ**.

---

#### **🔐 A. HASHING - Hàm Băm Một Chiều**

**📌 Cơ Chế Hoạt Động:**

```
INPUT (bất kỳ độ dài) → HASH FUNCTION → OUTPUT (fixed length)

"password123"     →  bcrypt  →  "$2b$10$N9qo8uLO..."  (60 chars)
"myfile.pdf"      →  SHA-256 →  "e3b0c44298fc1c..." (64 hex chars)
"Hello World"     →  SHA-256 →  "a591a6d40bf420..." (64 hex chars)
```

**🔑 Đặc Điểm Quan Trọng:**

1. **One-Way (Một chiều)**: 
   - ✅ Có thể: Password → Hash
   - ❌ KHÔNG thể: Hash → Password
   - Lý do: Hash function loại bỏ thông tin (many-to-one mapping)

2. **Deterministic (Cố định)**:
   ```typescript
   hash("password123") === hash("password123")  // ✅ Luôn giống nhau
   ```

3. **Avalanche Effect (Hiệu ứng tuyết lở)**:
   ```typescript
   hash("password123")  → "e3b0c44298fc1c..."
   hash("password124")  → "92cf3b8ec0a8d7..."  // Hoàn toàn khác!
   // Chỉ thay đổi 1 ký tự → hash hoàn toàn khác
   ```

4. **Fixed Output Length (Độ dài cố định)**:
   ```typescript
   hash("Hi")           → 64 hex chars (SHA-256)
   hash("Very long...") → 64 hex chars (SHA-256)
   // Input bất kỳ → output luôn 64 chars
   ```

**🎯 Tại Sao Dùng cho Passwords?**

```typescript
// ❌ VẤN ĐỀ: Lưu plaintext password
Database: { email: "user@example.com", password: "mypassword123" }
// Nếu hacker hack database → biết ngay password!

// ✅ GIẢI PHÁP: Hash password
Database: { email: "user@example.com", password: "$2b$10$N9qo8uLO..." }
// Hacker chỉ thấy hash, KHÔNG thể reverse về password!

// KHI LOGIN:
const userInput = "mypassword123";
const storedHash = "$2b$10$N9qo8uLO...";

// So sánh: hash(userInput) === storedHash?
const isValid = bcrypt.compare(userInput, storedHash);  // ✅ true nếu đúng
```

**💡 Salt - Ngăn Rainbow Table Attack:**

```typescript
// ❌ KHÔNG DÙNG SALT:
hash("password123") → "e3b0c44298fc1c..."  // Luôn giống nhau
// Hacker tạo Rainbow Table (bảng hash sẵn của triệu passwords phổ biến)
// Tra ngược: "e3b0c44298fc1c..." → "password123"  ✅ Tìm được!

// ✅ DÙNG SALT:
hash("password123" + "randomSalt1") → "$2b$10$abc..."
hash("password123" + "randomSalt2") → "$2b$10$xyz..."
// Mỗi user có salt khác nhau → cùng password cũng khác hash
// Rainbow Table KHÔNG dùng được! (vì phải tạo bảng cho mỗi salt)
```

---

#### **🔐 B. ENCRYPTION - Mã Hóa Hai Chiều**

Có 2 loại: **Symmetric** (Đối xứng) và **Asymmetric** (Bất đối xứng).

---

#### **🔐 B.1. SYMMETRIC ENCRYPTION - Mã Hóa Đối Xứng (1 Key)**

**📌 Cơ Chế Hoạt Động:**

```
PLAINTEXT + KEY → [ENCRYPT] → CIPHERTEXT
CIPHERTEXT + KEY → [DECRYPT] → PLAINTEXT

Ví dụ:
"Hello World" + key123 → [AES Encrypt] → "6Kq8z3Xp..."
"6Kq8z3Xp..." + key123 → [AES Decrypt] → "Hello World"
```

**🔑 Đặc Điểm:**
- **1 key duy nhất**: Dùng cho cả encrypt VÀ decrypt
- **Fast**: AES-256 rất nhanh (hardware accelerated)
- **Problem**: Làm sao gửi key an toàn cho receiver?

**🎯 Ví Dụ Thực Tế - Alice gửi message cho Bob:**

```typescript
// ALICE (Sender):
const message = "Meet me at 3pm";
const secretKey = "shared-secret-key-123";  // ⚠️ Alice và Bob đều biết key này

const encrypted = AES.encrypt(message, secretKey);  // "6Kq8z3Xp..."
// Alice gửi encrypted message cho Bob

// BOB (Receiver):
const received = "6Kq8z3Xp...";
const secretKey = "shared-secret-key-123";  // ⚠️ Bob phải có CÙNG key

const decrypted = AES.decrypt(received, secretKey);  // "Meet me at 3pm"
console.log(decrypted);  // ✅ Bob đọc được message
```

**⚠️ VẤN ĐỀ: Key Distribution Problem**

```
Alice và Bob cách nhau 1000km, làm sao chia sẻ secretKey an toàn?
- Gửi qua email? ❌ Email có thể bị intercept
- Gửi qua SMS? ❌ SMS không mã hóa
- Nói điện thoại? ❌ Điện thoại có thể bị nghe lén

→ Giải pháp: Dùng ASYMMETRIC ENCRYPTION để trao đổi symmetric key!
```

**🎯 Use Cases:**
- **Database Encryption**: Encrypt PII (email, phone, SSN)
- **File Encryption**: Encrypt files trước khi upload cloud
- **HTTPS Data**: Sau khi handshake, dùng AES encrypt data
- **Disk Encryption**: BitLocker, FileVault dùng AES

**💡 Tại Sao HTTPS Dùng AES (Không Dùng RSA)?**

```
AES-256:  Encrypt 1GB file trong ~1 giây
RSA-2048: Encrypt 1GB file trong ~10 phút!

→ HTTPS flow:
1. Handshake: Dùng RSA trao đổi AES key (chỉ ~32 bytes)
2. Data Transfer: Dùng AES encrypt data (nhanh!)
```

---

#### **🔐 B.2. ASYMMETRIC ENCRYPTION - Mã Hóa Bất Đối Xứng (2 Keys)**

**📌 Cơ Chế Hoạt Động:**

```
2 KEYS: Public Key (công khai) + Private Key (bí mật)

ENCRYPT với PUBLIC KEY → Decrypt với PRIVATE KEY
PLAINTEXT + Public Key  → [ENCRYPT] → CIPHERTEXT
CIPHERTEXT + Private Key → [DECRYPT] → PLAINTEXT
```

**🔑 Đặc Điểm:**
- **2 keys khác nhau**: Public (share freely) + Private (keep secret)
- **Math Magic**: Dựa trên số học (factorization, discrete logarithm)
- **Slow**: RSA chậm hơn AES 10-100x

**🎯 Ví Dụ Thực Tế - Alice gửi message cho Bob:**

```typescript
// BOB tạo key pair:
const bobKeys = generateRSAKeyPair();
// bobKeys.publicKey  = "-----BEGIN PUBLIC KEY-----..."  (Share freely)
// bobKeys.privateKey = "-----BEGIN PRIVATE KEY-----..." (Keep secret!)

// Bob gửi PUBLIC KEY cho Alice (qua email, website, anywhere)
// ⚠️ Public key KHÔNG sợ bị lộ! Ai cũng biết được!

// ALICE (Sender):
const message = "Meet me at 3pm";
const encrypted = RSA.encrypt(message, bobKeys.publicKey);  // Dùng Bob's PUBLIC KEY
// encrypted = "f8Kq3z..."

// ⚠️ Chỉ Bob mới decrypt được (vì chỉ Bob có PRIVATE KEY)
// Alice KHÔNG thể decrypt (dù Alice là người encrypt!)

// BOB (Receiver):
const decrypted = RSA.decrypt(encrypted, bobKeys.privateKey);  // Dùng Bob's PRIVATE KEY
console.log(decrypted);  // "Meet me at 3pm" ✅
```

**💡 Giải Quyết Key Distribution Problem:**

```
Alice muốn gửi message cho Bob:

CÁCH CŨ (Symmetric):
1. Alice và Bob phải gặp nhau để trao đổi secret key  ❌ Không tiện
2. Hoặc gửi key qua kênh không an toàn  ❌ Nguy hiểm

CÁCH MỚI (Asymmetric):
1. Bob tạo key pair (public + private)
2. Bob share public key lên website/email (KHÔNG sợ lộ!)
3. Alice lấy Bob's public key
4. Alice encrypt message với Bob's public key
5. Gửi encrypted message cho Bob
6. Bob decrypt với private key (chỉ Bob có!)

✅ KHÔNG cần gặp nhau!
✅ KHÔNG cần trao đổi secret key!
✅ Public key bị lộ cũng KHÔNG sao!
```

**🎯 Use Cases:**
- **HTTPS Handshake**: Server gửi public key, client encrypt AES key
- **SSH Authentication**: Client có private key, server có public key
- **PGP Email**: Encrypt email với recipient's public key
- **Digital Signatures**: Sign với private key, verify với public key (đảo ngược!)

**🔐 Public Key vs Private Key - Ai Dùng Cái Gì?**

```typescript
// ENCRYPTION (Mã hóa - Protect Confidentiality):
Sender   encrypt với RECEIVER's PUBLIC KEY
Receiver decrypt với RECEIVER's PRIVATE KEY

Ví dụ: Alice gửi message cho Bob
Alice:  encrypt(message, Bob's PUBLIC KEY)   → ciphertext
Bob:    decrypt(ciphertext, Bob's PRIVATE KEY) → message

// DIGITAL SIGNATURE (Chữ ký số - Prove Authenticity):
Signer  sign với SIGNER's PRIVATE KEY
Verifier verify với SIGNER's PUBLIC KEY

Ví dụ: Alice ký document
Alice:  sign(document, Alice's PRIVATE KEY)   → signature
Bob:    verify(document, signature, Alice's PUBLIC KEY) → ✅ valid
```

---

#### **🔐 C. DIGITAL SIGNATURE - Chữ Ký Số**

**📌 Cơ Chế Hoạt Động:**

```
SIGN (Ký):
1. Hash document với SHA-256 → hash
2. Encrypt hash với PRIVATE KEY → signature
3. Gửi document + signature

VERIFY (Xác thực):
1. Hash received document → hash1
2. Decrypt signature với PUBLIC KEY → hash2
3. Compare hash1 === hash2 ?
   - ✅ Match → Document valid, không bị tamper
   - ❌ Not match → Document bị thay đổi hoặc signature giả
```

**🔑 Đặc Điểm:**
- **Prove Authenticity**: Chứng minh document từ đúng người (chỉ họ có private key)
- **Prove Integrity**: Chứng minh document không bị thay đổi (hash khớp)
- **Non-repudiation**: Signer không thể chối bỏ đã ký (vì chỉ họ có private key)

**🎯 Ví Dụ Thực Tế - Alice Ký Contract:**

```typescript
// ALICE tạo key pair:
const aliceKeys = generateRSAKeyPair();
// aliceKeys.publicKey  = "-----BEGIN PUBLIC KEY-----..."  (Share)
// aliceKeys.privateKey = "-----BEGIN PRIVATE KEY-----..." (Secret)

// ALICE KÝ CONTRACT:
const contract = "I agree to pay $10000 to Bob";

// Bước 1: Hash contract
const hash = SHA256(contract);  // "e3b0c44298fc1c..."

// Bước 2: Encrypt hash với PRIVATE KEY
const signature = RSA.encrypt(hash, aliceKeys.privateKey);  // "f8Kq3z..."

// Alice gửi cho Bob: contract + signature + Alice's public key

// BOB VERIFY SIGNATURE:
const receivedContract = "I agree to pay $10000 to Bob";
const receivedSignature = "f8Kq3z...";
const alicePublicKey = "-----BEGIN PUBLIC KEY-----...";

// Bước 1: Hash received contract
const hash1 = SHA256(receivedContract);  // "e3b0c44298fc1c..."

// Bước 2: Decrypt signature với PUBLIC KEY
const hash2 = RSA.decrypt(receivedSignature, alicePublicKey);  // "e3b0c44298fc1c..."

// Bước 3: Compare
if (hash1 === hash2) {
  console.log("✅ Signature valid!");
  console.log("✅ Contract từ Alice (vì chỉ Alice có private key)");
  console.log("✅ Contract không bị thay đổi (vì hash khớp)");
} else {
  console.log("❌ Signature invalid!");
  console.log("❌ Contract bị tamper hoặc signature giả!");
}
```

**💡 Tại Sao KHÔNG Encrypt Toàn Bộ Document?**

```
RSA SLOW:
- Sign toàn bộ contract (10 pages) → 10 giây
- Sign hash của contract (64 chars)  → 0.01 giây

Hash UNIQUE:
- 2 documents khác nhau → 2 hashes khác nhau
- 1 document thay đổi 1 ký tự → hash hoàn toàn khác
→ Verify hash = verify toàn bộ document!
```

**🎯 Use Cases:**
- **JWT Tokens**: Server sign JWT với private key, client verify với public key
- **Code Signing**: Software developers sign apps (macOS, Windows)
- **SSL Certificates**: Certificate Authority (CA) sign certificates
- **Blockchain**: Sign transactions với private key
- **Email (PGP)**: Sign emails để prove authenticity

**🔐 Digital Signature vs Encryption - Khác Nhau Thế Nào?**

```typescript
// ENCRYPTION (Mã hóa):
Mục đích: Protect CONFIDENTIALITY (bảo mật)
Encrypt với: RECEIVER's PUBLIC KEY
Decrypt với: RECEIVER's PRIVATE KEY
Result: Chỉ receiver đọc được message

Ví dụ: Alice gửi secret message cho Bob
Alice:  encrypt(message, Bob's PUBLIC)    → Bob decrypt với Bob's PRIVATE
        ↑ Dùng Bob's keys!

// DIGITAL SIGNATURE (Chữ ký số):
Mục đích: Prove AUTHENTICITY & INTEGRITY (xác thực & toàn vẹn)
Sign với: SIGNER's PRIVATE KEY
Verify với: SIGNER's PUBLIC KEY
Result: Mọi người verify được message từ signer

Ví dụ: Alice ký contract
Alice:  sign(contract, Alice's PRIVATE)   → Bob verify với Alice's PUBLIC
        ↑ Dùng Alice's keys!
```

**🎯 JWT Example - Kết Hợp Cả Hai:**

```typescript
// SERVER (Sign JWT):
const payload = { userId: "123", role: "admin" };
const privateKey = "-----BEGIN PRIVATE KEY-----...";

// Hash payload + sign với PRIVATE KEY
const token = jwt.sign(payload, privateKey, { algorithm: 'RS256' });
// "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMjMifQ.signature"

// CLIENT/API (Verify JWT):
const publicKey = "-----BEGIN PUBLIC KEY-----...";

try {
  const verified = jwt.verify(token, publicKey, { algorithms: ['RS256'] });
  console.log("✅ Token valid:", verified);
  // ✅ Token từ server (vì chỉ server có private key)
  // ✅ Payload không bị thay đổi (vì signature valid)
} catch (error) {
  console.log("❌ Token invalid:", error.message);
  // ❌ Token bị tamper hoặc signature giả
}
```

**💡 Tại Sao JWT Dùng RS256 (Không Dùng HS256)?**

```typescript
// HS256 (HMAC with SHA-256):
- Symmetric: 1 secret key (server giữ)
- Sign: HMAC(payload, secret)
- Verify: HMAC(payload, secret)
⚠️ VẤN ĐỀ: Client KHÔNG verify được (không có secret key)
⚠️ Nếu client có secret → client có thể forge tokens!

// RS256 (RSA with SHA-256):
- Asymmetric: Private key (server) + Public key (share)
- Sign: RSA(hash(payload), privateKey)
- Verify: RSA(signature, publicKey)
✅ Client verify được (có public key)
✅ Client KHÔNG thể forge tokens (không có private key)
✅ Microservices verify được (share public key)
```

---

#### **📚 Tóm Tắt Cơ Chế:**

| Loại                | Keys               | Operation                      | Use Case                          |
| ------------------- | ------------------ | ------------------------------ | --------------------------------- |
| **Hashing**         | ❌ No key          | Input → Hash (one-way)         | Passwords, checksums              |
| **Symmetric Encrypt** | 1 key (shared)    | Encrypt/Decrypt (same key)     | Database encryption, HTTPS data   |
| **Asymmetric Encrypt** | 2 keys (pub+priv) | Encrypt (pub), Decrypt (priv)  | HTTPS handshake, PGP email        |
| **Digital Signature** | 2 keys (pub+priv) | Sign (priv), Verify (pub)      | JWT, code signing, blockchain     |

---

#### **1️⃣ HASHING - One-Way Function (Hàm Một Chiều)**

**🔑 Đặc Điểm:**
- **One-way**: Input → Hash, KHÔNG thể Hash → Input
- **Deterministic**: Cùng input → cùng hash
- **Fixed length**: SHA-256 luôn 64 hex chars (256 bits)
- **Avalanche effect**: Thay đổi 1 bit input → hoàn toàn khác hash

**📌 Use Cases:**
1. **Password Storage**: Never store plaintext passwords
2. **Data Integrity**: Verify files không bị thay đổi (checksums)
3. **Unique Identifiers**: Generate tokens, session IDs
4. **Blockchain**: Bitcoin sử dụng SHA-256

---

**🔐 1.1. Password Hashing với bcrypt**

```typescript
import bcrypt from 'bcrypt';

// =====================================
// PASSWORD HASHING WITH BCRYPT
// =====================================

// 🔹 REGISTER - Hash password khi user đăng ký
async function registerUser(email: string, password: string) {
  // Salt rounds = độ phức tạp (10 = 2^10 = 1024 iterations)
  // Càng cao càng secure nhưng càng chậm
  const saltRounds = 10;
  
  // bcrypt tự động generate salt và combine với hash
  const hashedPassword = await bcrypt.hash(password, saltRounds);
  
  // Lưu vào database
  await db.users.create({
    email,
    password: hashedPassword, // VD: $2b$10$Xu... (60 chars)
  });
  
  console.log('Original:', password);          // "MySecurePass123"
  console.log('Hashed:', hashedPassword);      // "$2b$10$Xu4K..."
  // ⚠️ Không thể reverse từ hash về password!
}

// 🔹 LOGIN - Verify password khi user đăng nhập
async function loginUser(email: string, password: string) {
  // Lấy user từ database
  const user = await db.users.findByEmail(email);
  
  if (!user) {
    throw new Error('User not found');
  }
  
  // So sánh password với hash (bcrypt.compare tự extract salt)
  const isValid = await bcrypt.compare(password, user.password);
  
  if (!isValid) {
    throw new Error('Invalid password');
  }
  
  // Generate JWT token nếu password đúng
  const token = generateJWT(user.id);
  return { user, token };
}

// 🔹 CHANGE PASSWORD - Hash lại khi user đổi mật khẩu
async function changePassword(userId: string, oldPassword: string, newPassword: string) {
  const user = await db.users.findById(userId);
  
  // Verify old password
  const isValid = await bcrypt.compare(oldPassword, user.password);
  if (!isValid) {
    throw new Error('Old password is incorrect');
  }
  
  // Hash new password
  const newHashedPassword = await bcrypt.hash(newPassword, 10);
  
  // Update database
  await db.users.update(userId, {
    password: newHashedPassword,
    passwordChangedAt: new Date(),
  });
}
```

**💡 Giải Thích:**
- **bcrypt format**: `$2b$10$salt(22 chars)hash(31 chars)` (total 60 chars)
  - `$2b$` = bcrypt algorithm version
  - `10` = salt rounds (cost factor)
  - `salt` = random salt (22 chars)
  - `hash` = actual hash (31 chars)
- **Salt**: Random value thêm vào password trước khi hash
  - Mục đích: Ngăn rainbow table attacks
  - Mỗi user có salt khác nhau → cùng password cũng khác hash
- **bcrypt.compare()**: Tự động extract salt từ hash và compare

---

**🔐 1.2. Data Integrity với SHA-256**

```typescript
import crypto from 'crypto';

// =====================================
// SHA-256 FOR DATA INTEGRITY
// =====================================

// 🔹 FILE CHECKSUM - Verify file không bị thay đổi
function generateFileChecksum(fileContent: Buffer): string {
  return crypto
    .createHash('sha256')
    .update(fileContent)
    .digest('hex'); // 64 hex chars (256 bits)
}

// Example: Download file verification
async function downloadAndVerify(url: string, expectedChecksum: string) {
  const fileContent = await downloadFile(url);
  const actualChecksum = generateFileChecksum(fileContent);
  
  if (actualChecksum !== expectedChecksum) {
    throw new Error('File corrupted! Checksum mismatch');
  }
  
  console.log('✅ File verified successfully');
  return fileContent;
}

// 🔹 GENERATE UNIQUE TOKEN - Session ID, API keys
function generateSessionToken(userId: string): string {
  const timestamp = Date.now().toString();
  const random = crypto.randomBytes(16).toString('hex');
  
  // Hash combination để tạo unique token
  return crypto
    .createHash('sha256')
    .update(`${userId}:${timestamp}:${random}`)
    .digest('hex');
}

// 🔹 HMAC - Hash with secret key (for API signatures)
function generateHMAC(data: string, secretKey: string): string {
  return crypto
    .createHmac('sha256', secretKey)
    .update(data)
    .digest('hex');
}

// Example: Verify webhook payload từ third-party service
function verifyWebhook(payload: string, signature: string, secret: string): boolean {
  const expectedSignature = generateHMAC(payload, secret);
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

**💡 Giải Thích:**
- **SHA-256**: Cryptographic hash function (256-bit output)
  - Không dùng cho password (quá nhanh → vulnerable to brute-force)
  - Dùng cho checksums, data integrity
- **HMAC** (Hash-based Message Authentication Code):
  - SHA-256 + secret key
  - Verify cả integrity VÀ authenticity
  - Dùng trong webhook signatures, API authentication

---

#### **2️⃣ ENCRYPTION - Two-Way Function (Mã Hóa Hai Chiều)**

> **� Xem lại phần [🔐 B. ENCRYPTION](#-b-encryption---mã-hóa-hai-chiều) ở trên để hiểu rõ cơ chế hoạt động của Symmetric (1 key) vs Asymmetric (2 keys), Public/Private Key, và Key Distribution Problem!**

**�🔑 Đặc Điểm:**
- **Two-way**: Plaintext ⇄ Ciphertext (encrypt ↔ decrypt)
- **Requires key**: Symmetric (1 key) hoặc Asymmetric (2 keys)
- **Protects confidentiality**: Giấu dữ liệu khỏi unauthorized access

**📌 Use Cases:**
1. **HTTPS/TLS**: Encrypt network traffic
2. **Database Encryption**: Protect sensitive PII (emails, phone numbers)
3. **File Encryption**: Encrypt files trước khi upload cloud
4. **API Keys**: Encrypt secrets trong config

**🔍 Nhắc Lại Cơ Chế:**

```typescript
// SYMMETRIC (AES): 1 key cho cả encrypt & decrypt
const key = "shared-secret-key";
const encrypted = AES.encrypt("data", key);      // Encrypt với key
const decrypted = AES.decrypt(encrypted, key);   // Decrypt với CÙNG key
// ⚠️ Vấn đề: Làm sao gửi key an toàn?

// ASYMMETRIC (RSA): 2 keys (public + private)
const { publicKey, privateKey } = generateKeys();
const encrypted = RSA.encrypt("data", publicKey);      // Encrypt với PUBLIC key
const decrypted = RSA.decrypt(encrypted, privateKey);  // Decrypt với PRIVATE key
// ✅ Giải pháp: Public key share thoải mái, chỉ private key giữ bí mật!
```

---

**🔐 2.1. Symmetric Encryption - AES (Advanced Encryption Standard)**

```typescript
import crypto from 'crypto';

// =====================================
// SYMMETRIC ENCRYPTION WITH AES-256-GCM
// =====================================

interface EncryptedData {
  iv: string;           // Initialization Vector (12 bytes for GCM)
  encryptedText: string; // Ciphertext
  authTag: string;      // Authentication Tag (16 bytes)
}

// 🔹 ENCRYPT - Mã hóa dữ liệu với AES-256-GCM
function encryptAES(plaintext: string, secretKey: string): EncryptedData {
  // Generate random IV (Initialization Vector)
  // ⚠️ PHẢI random mỗi lần encrypt, KHÔNG reuse!
  const iv = crypto.randomBytes(12);
  
  // Create cipher với AES-256-GCM mode
  // GCM = Galois/Counter Mode (authenticated encryption)
  const cipher = crypto.createCipheriv(
    'aes-256-gcm',
    Buffer.from(secretKey, 'hex'), // 32 bytes (256 bits)
    iv
  );
  
  // Encrypt plaintext
  let encryptedText = cipher.update(plaintext, 'utf8', 'hex');
  encryptedText += cipher.final('hex');
  
  // Get authentication tag (verify integrity khi decrypt)
  const authTag = cipher.getAuthTag();
  
  return {
    iv: iv.toString('hex'),
    encryptedText,
    authTag: authTag.toString('hex'),
  };
}

// 🔹 DECRYPT - Giải mã dữ liệu
function decryptAES(encrypted: EncryptedData, secretKey: string): string {
  // Create decipher
  const decipher = crypto.createDecipheriv(
    'aes-256-gcm',
    Buffer.from(secretKey, 'hex'),
    Buffer.from(encrypted.iv, 'hex')
  );
  
  // Set authentication tag (verify không bị tamper)
  decipher.setAuthTag(Buffer.from(encrypted.authTag, 'hex'));
  
  // Decrypt ciphertext
  let plaintext = decipher.update(encrypted.encryptedText, 'hex', 'utf8');
  plaintext += decipher.final('utf8');
  
  return plaintext;
}

// 🔹 EXAMPLE - Encrypt PII trong database
interface User {
  id: string;
  email: string;         // Plaintext (for login)
  phone: string;         // Encrypted (sensitive PII)
  ssn: string;           // Encrypted (very sensitive)
}

async function saveUser(user: User, encryptionKey: string) {
  const encryptedPhone = encryptAES(user.phone, encryptionKey);
  const encryptedSSN = encryptAES(user.ssn, encryptionKey);
  
  await db.users.create({
    id: user.id,
    email: user.email, // Không encrypt (cần query by email)
    phone: JSON.stringify(encryptedPhone),
    ssn: JSON.stringify(encryptedSSN),
  });
}

async function getUser(userId: string, encryptionKey: string): Promise<User> {
  const dbUser = await db.users.findById(userId);
  
  const encryptedPhone = JSON.parse(dbUser.phone);
  const encryptedSSN = JSON.parse(dbUser.ssn);
  
  return {
    id: dbUser.id,
    email: dbUser.email,
    phone: decryptAES(encryptedPhone, encryptionKey),
    ssn: decryptAES(encryptedSSN, encryptionKey),
  };
}
```

**💡 Giải Thích:**
- **AES-256-GCM**:
  - AES = Advanced Encryption Standard (industry standard)
  - 256 = key length (256 bits = 32 bytes)
  - GCM = Galois/Counter Mode (authenticated encryption)
    - Vừa encrypt VỪA authenticate (detect tampering)
- **IV (Initialization Vector)**:
  - Random 12 bytes cho GCM mode
  - PHẢI unique mỗi lần encrypt
  - Không cần secret (lưu cùng ciphertext)
- **Auth Tag**:
  - 16 bytes tag verify integrity
  - Nếu data bị modify → decrypt throw error

---

**🔐 2.2. Asymmetric Encryption - RSA (Public/Private Key)**

```typescript
import crypto from 'crypto';

// =====================================
// ASYMMETRIC ENCRYPTION WITH RSA
// =====================================

// 🔹 GENERATE KEY PAIR - Tạo public/private keys
function generateRSAKeyPair(): { publicKey: string; privateKey: string } {
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048, // 2048 bits (secure for most use cases)
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem',
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem',
    },
  });
  
  return { publicKey, privateKey };
}

// 🔹 ENCRYPT với PUBLIC KEY - Anyone có public key có thể encrypt
function encryptRSA(plaintext: string, publicKey: string): string {
  const buffer = Buffer.from(plaintext, 'utf8');
  
  const encrypted = crypto.publicEncrypt(
    {
      key: publicKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    buffer
  );
  
  return encrypted.toString('base64');
}

// 🔹 DECRYPT với PRIVATE KEY - Chỉ owner của private key mới decrypt được
function decryptRSA(ciphertext: string, privateKey: string): string {
  const buffer = Buffer.from(ciphertext, 'base64');
  
  const decrypted = crypto.privateDecrypt(
    {
      key: privateKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    buffer
  );
  
  return decrypted.toString('utf8');
}

// 🔹 EXAMPLE - Secure message exchange
const alice = generateRSAKeyPair();
const bob = generateRSAKeyPair();

// Alice gửi message cho Bob
const message = 'Secret meeting at 3pm';
const encryptedMessage = encryptRSA(message, bob.publicKey); // Dùng Bob's public key
console.log('Encrypted:', encryptedMessage);

// Bob decrypt message
const decryptedMessage = decryptRSA(encryptedMessage, bob.privateKey); // Dùng Bob's private key
console.log('Decrypted:', decryptedMessage); // "Secret meeting at 3pm"

// ⚠️ Alice KHÔNG thể decrypt (không có Bob's private key)
```

**💡 Giải Thích:**
- **RSA Asymmetric**:
  - Public key: Share freely, dùng để ENCRYPT
  - Private key: Keep secret, dùng để DECRYPT
  - Math: Easy encrypt, hard decrypt without private key (based on factorization)
- **Use Cases**:
  - HTTPS/TLS handshake (exchange symmetric keys)
  - PGP email encryption
  - SSH authentication
- **Limitations**:
  - Slow (10-100x slower than AES)
  - Size limit (RSA-2048 max ~245 bytes plaintext)
  - → Thường dùng để encrypt symmetric key, rồi dùng AES cho data

---

#### **3️⃣ DIGITAL SIGNATURES - Sign & Verify (Chữ Ký Số)**

> **💡 Xem lại phần [🔐 C. DIGITAL SIGNATURE](#-c-digital-signature---chữ-ký-số) ở trên để hiểu rõ cơ chế: Sign với Private Key (chỉ signer có), Verify với Public Key (ai cũng verify được), và tại sao dùng cho JWT RS256!**

**🔑 Đặc Điểm:**
- **Sign với private key**: Chỉ owner có thể sign
- **Verify với public key**: Anyone có thể verify
- **Proves authenticity**: Message từ đúng người (chỉ họ có private key)
- **Proves integrity**: Message không bị thay đổi (hash khớp)

**📌 Use Cases:**
1. **JWT Tokens**: Sign payload với RS256
2. **API Authentication**: Verify requests từ trusted clients
3. **Code Signing**: Verify software không bị tamper
4. **Blockchain**: Sign transactions

**🔍 Nhắc Lại Cơ Chế:**

```typescript
// DIGITAL SIGNATURE: Đảo ngược Encryption!

// ENCRYPTION (Bảo mật):
Encrypt với: RECEIVER's PUBLIC KEY    → Decrypt với: RECEIVER's PRIVATE KEY
Mục đích: Giấu message, chỉ receiver đọc được

// SIGNATURE (Xác thực):
Sign với: SIGNER's PRIVATE KEY        → Verify với: SIGNER's PUBLIC KEY
Mục đích: Chứng minh message từ signer, ai cũng verify được

// VÍ DỤ:
const { publicKey, privateKey } = generateKeys();

// Sign document
const hash = SHA256(document);
const signature = RSA.encrypt(hash, privateKey);  // Sign = Encrypt hash với PRIVATE key

// Verify signature
const hash1 = SHA256(document);
const hash2 = RSA.decrypt(signature, publicKey);  // Verify = Decrypt với PUBLIC key
if (hash1 === hash2) console.log("✅ Valid signature!");
```

---

**🔐 3.1. JWT Digital Signature với RS256**

```typescript
import jwt from 'jsonwebtoken';
import crypto from 'crypto';

// =====================================
// JWT DIGITAL SIGNATURE WITH RS256
// =====================================

// 🔹 GENERATE RSA KEYS for JWT
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

// 🔹 SIGN JWT - Server tạo token khi user login
function signJWT(payload: object): string {
  // Sign với PRIVATE KEY
  const token = jwt.sign(
    payload,
    privateKey,
    {
      algorithm: 'RS256',    // RSA with SHA-256
      expiresIn: '1h',       // Token expires trong 1 giờ
      issuer: 'my-app',      // App name
    }
  );
  
  return token;
}

// 🔹 VERIFY JWT - Server verify token từ client
function verifyJWT(token: string): object {
  try {
    // Verify với PUBLIC KEY
    const payload = jwt.verify(token, publicKey, {
      algorithms: ['RS256'],
      issuer: 'my-app',
    });
    
    return payload as object;
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      throw new Error('Token expired');
    }
    if (error instanceof jwt.JsonWebTokenError) {
      throw new Error('Invalid token');
    }
    throw error;
  }
}

// 🔹 EXAMPLE - Authentication flow
interface JWTPayload {
  userId: string;
  email: string;
  role: string;
}

// Login → Generate JWT
async function login(email: string, password: string): Promise<string> {
  const user = await authenticateUser(email, password);
  
  const payload: JWTPayload = {
    userId: user.id,
    email: user.email,
    role: user.role,
  };
  
  const token = signJWT(payload);
  console.log('Generated JWT:', token);
  // eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOi...
  
  return token;
}

// Protected route → Verify JWT
async function getProfile(token: string): Promise<JWTPayload> {
  const payload = verifyJWT(token) as JWTPayload;
  
  console.log('Verified user:', payload.userId);
  return payload;
}

// 🔹 JWT STRUCTURE
// JWT có 3 phần (separated by dot):
// HEADER.PAYLOAD.SIGNATURE

// 1. HEADER (algorithm + type)
const header = {
  alg: 'RS256',
  typ: 'JWT',
};

// 2. PAYLOAD (claims)
const payload = {
  userId: '123',
  email: 'user@example.com',
  role: 'admin',
  iat: 1234567890,  // Issued at
  exp: 1234571490,  // Expires at
};

// 3. SIGNATURE (sign header + payload với private key)
// signature = RSA-SHA256(
//   base64(header) + '.' + base64(payload),
//   privateKey
// )

// ✅ Verify process:
// 1. Decode header + payload từ JWT
// 2. Compute signature với public key
// 3. Compare với signature trong JWT
// 4. Nếu match → valid, không match → tampered
```

**💡 Giải Thích:**
- **RS256** (RSA + SHA-256):
  - Sign với private key → chỉ server mới sign được
  - Verify với public key → client/services verify được
  - SHA-256: Hash algorithm để sign
- **JWT Flow**:
  1. Server sign payload với private key
  2. Client lưu token (localStorage/cookie)
  3. Client gửi token trong Authorization header
  4. Server verify token với public key
  5. Nếu valid → allow access
- **Security**:
  - Private key PHẢI keep secret (trên server)
  - Public key có thể share (cho clients verify)
  - Nếu private key leak → attacker có thể forge tokens!

---

**🔐 3.2. Manual RSA Signature (Low-Level)**

```typescript
import crypto from 'crypto';

// =====================================
// MANUAL RSA DIGITAL SIGNATURE
// =====================================

// 🔹 SIGN DATA - Tạo chữ ký số
function signData(data: string, privateKey: string): string {
  const sign = crypto.createSign('SHA256');
  sign.update(data);
  sign.end();
  
  const signature = sign.sign(privateKey, 'base64');
  return signature;
}

// 🔹 VERIFY SIGNATURE - Xác thực chữ ký
function verifySignature(data: string, signature: string, publicKey: string): boolean {
  const verify = crypto.createVerify('SHA256');
  verify.update(data);
  verify.end();
  
  return verify.verify(publicKey, signature, 'base64');
}

// 🔹 EXAMPLE - API Request Signature
interface APIRequest {
  method: string;
  path: string;
  body: object;
  timestamp: number;
}

// Client signs request
function signAPIRequest(request: APIRequest, privateKey: string): string {
  // Serialize request to string
  const requestString = JSON.stringify({
    method: request.method,
    path: request.path,
    body: request.body,
    timestamp: request.timestamp,
  });
  
  // Sign request
  return signData(requestString, privateKey);
}

// Server verifies request
function verifyAPIRequest(request: APIRequest, signature: string, publicKey: string): boolean {
  const requestString = JSON.stringify({
    method: request.method,
    path: request.path,
    body: request.body,
    timestamp: request.timestamp,
  });
  
  // Verify signature
  const isValid = verifySignature(requestString, signature, publicKey);
  
  if (!isValid) {
    console.log('❌ Invalid signature - request tampered or wrong key');
    return false;
  }
  
  // Check timestamp (prevent replay attacks)
  const now = Date.now();
  const age = now - request.timestamp;
  
  if (age > 5 * 60 * 1000) { // 5 minutes
    console.log('❌ Request too old - possible replay attack');
    return false;
  }
  
  console.log('✅ Signature valid');
  return true;
}

// Example usage
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

const request: APIRequest = {
  method: 'POST',
  path: '/api/users',
  body: { name: 'John' },
  timestamp: Date.now(),
};

// Client signs
const signature = signAPIRequest(request, privateKey);
console.log('Signature:', signature);

// Server verifies
const isValid = verifyAPIRequest(request, signature, publicKey);
console.log('Valid?', isValid); // true
```

**💡 Giải Thích:**
- **Digital Signature Process**:
  1. Hash data với SHA-256
  2. Encrypt hash với private key → signature
  3. Gửi data + signature
  4. Receiver hash data
  5. Decrypt signature với public key
  6. Compare hashes → nếu match = valid
- **Security Benefits**:
  - **Authenticity**: Chỉ owner của private key mới sign được
  - **Integrity**: Nếu data thay đổi → hash khác → verify fail
  - **Non-repudiation**: Signer không thể deny đã sign

---

#### **📚 Khi Nào Dùng Gì?**

| Scenario                           | Solution                          | Reason                                      |
| ---------------------------------- | --------------------------------- | ------------------------------------------- |
| **Store passwords**                | bcrypt Hashing                    | One-way, slow (prevent brute-force)        |
| **Verify file integrity**          | SHA-256 Checksum                  | Fast, detect corruption/tampering           |
| **Encrypt database PII**           | AES-256-GCM                       | Symmetric, fast, authenticated              |
| **HTTPS/TLS**                      | RSA (key exchange) + AES (data)   | RSA slow → dùng cho key, AES cho data       |
| **JWT authentication**             | RS256 Digital Signature           | Public verify, private sign                 |
| **API request authentication**     | HMAC or RSA Signature             | Verify request từ trusted client            |
| **Webhook verification**           | HMAC-SHA256                       | Shared secret, fast                         |
| **Email encryption (PGP)**         | RSA + AES                         | RSA cho key exchange, AES cho message       |

---

#### **🔥 Best Practices**

**✅ DO:**
1. **Passwords**: Dùng bcrypt/argon2, KHÔNG dùng SHA-256
2. **Sensitive data**: Encrypt với AES-256-GCM trong database
3. **HTTPS**: Always enable trong production
4. **JWT**: Dùng RS256 (không dùng HS256 với shared secret)
5. **Key rotation**: Rotate encryption keys định kỳ
6. **IV/Salt**: Always random, unique mỗi lần
7. **Secrets**: Store trong environment variables/secret managers

**❌ DON'T:**
1. **KHÔNG dùng MD5/SHA-1**: Deprecated, vulnerable
2. **KHÔNG hardcode keys**: Trong source code
3. **KHÔNG reuse IV**: Trong AES encryption
4. **KHÔNG dùng ECB mode**: Trong AES (dùng GCM/CBC)
5. **KHÔNG share private keys**: Keep secret!
6. **KHÔNG dùng custom crypto**: Dùng libraries proven secure

---

#### **🎯 Common Mistakes & Corrections**

**❌ Mistake 1: Dùng SHA-256 cho passwords**
```typescript
// ❌ BAD - SHA-256 too fast, vulnerable to brute-force
const hashedPassword = crypto.createHash('sha256').update(password).digest('hex');
```

**✅ Correction:**
```typescript
// ✅ GOOD - bcrypt slow, secure
const hashedPassword = await bcrypt.hash(password, 10);
```

---

**❌ Mistake 2: Reuse IV trong AES**
```typescript
// ❌ BAD - Same IV for multiple encryptions
const iv = Buffer.from('1234567890123456');
const cipher1 = crypto.createCipheriv('aes-256-gcm', key, iv);
const cipher2 = crypto.createCipheriv('aes-256-gcm', key, iv); // ❌ Same IV!
```

**✅ Correction:**
```typescript
// ✅ GOOD - Random IV mỗi lần
const iv1 = crypto.randomBytes(12);
const iv2 = crypto.randomBytes(12); // Different IV
```

---

**❌ Mistake 3: Hardcode encryption keys**
```typescript
// ❌ BAD - Key in source code
const key = 'my-secret-key-12345678901234567890';
```

**✅ Correction:**
```typescript
// ✅ GOOD - Key from environment
const key = process.env.ENCRYPTION_KEY;
if (!key || key.length !== 32) {
  throw new Error('Invalid ENCRYPTION_KEY');
}
```

---

**❌ Mistake 4: Không verify JWT signature**
```typescript
// ❌ BAD - Decode without verify
const payload = JSON.parse(
  Buffer.from(token.split('.')[1], 'base64').toString()
);
```

**✅ Correction:**
```typescript
// ✅ GOOD - Always verify signature
const payload = jwt.verify(token, publicKey);
```

---

**🎯 Kết Luận:**

**Hashing:**
- ✅ One-way, dùng cho passwords (bcrypt), checksums (SHA-256)
- ✅ Không thể decrypt

**Encryption:**
- ✅ Two-way, dùng cho sensitive data (AES), key exchange (RSA)
- ✅ Symmetric (AES) nhanh, Asymmetric (RSA) chậm nhưng không cần share key

**Digital Signatures:**
- ✅ Verify authenticity & integrity
- ✅ JWT (RS256), API authentication, webhooks

**💡 Key Takeaway:**
- Hash cho verification, Encryption cho confidentiality, Signature cho authenticity
- Dùng proven libraries (bcrypt, crypto, jsonwebtoken)
- Never roll your own crypto!

</details>