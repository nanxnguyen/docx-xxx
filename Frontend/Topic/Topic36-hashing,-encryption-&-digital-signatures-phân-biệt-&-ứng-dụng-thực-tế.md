# 🔑 Topic 36: Hashing, Encryption & Digital Signatures - Phân Biệt & Ứng Dụng Thực Tế

## 1. ⭐ Senior/Staff Summary

Ba khái niệm này dễ bị nhầm vì đều liên quan đến cryptography, nhưng mục tiêu khác nhau:

- **Hashing**: biến dữ liệu thành fingerprint một chiều. Dùng để kiểm tra integrity, lưu password bằng password hashing algorithm, tạo checksum.
- **Encryption**: mã hóa để giấu nội dung. Có thể giải mã nếu có key. Dùng cho confidentiality: dữ liệu nhạy cảm, file, database field, network traffic.
- **Digital Signature**: ký bằng private key, verify bằng public key để chứng minh authenticity + integrity. Dùng cho JWT/JWS, code signing, API signing, document signing.

Điểm senior cần nhớ:

- ✅ Password không được encrypt để “sau này decrypt”; password phải hash bằng **Argon2id/bcrypt/scrypt/PBKDF2**, không dùng SHA-256 thường.
- ✅ Dữ liệu cần đọc lại như phone/SSN/card tokenized value thì dùng **encryption**, ưu tiên authenticated encryption như **AES-GCM**.
- ✅ Message cần chứng minh “ai gửi” và “không bị sửa” thì dùng **signature** hoặc **HMAC**, tùy shared secret hay public/private key.
- ✅ Key management quan trọng hơn thuật toán đẹp: key phải nằm trong KMS/Vault/HSM/secret manager, có rotation và access control.
- ✅ Frontend không giữ secret thật. Browser có thể dùng Web Crypto, nhưng secret nằm trong client không còn là secret.

> 💡 Mental model: **Hash = fingerprint**, **Encryption = khóa hộp**, **Signature = chữ ký + chống sửa nội dung**.

## 2. 🧠 Key Mental Model

### 2.1. So sánh nhanh

| Kỹ thuật | Có đảo ngược không? | Có key không? | Mục tiêu chính | Ví dụ |
|---|---|---|---|---|
| Hashing | Không | Không, trừ HMAC/KDF có secret/salt | Integrity, fingerprint | SHA-256 checksum |
| Password hashing | Không | Salt + cost factor | Chống brute-force password | Argon2id, bcrypt |
| Symmetric encryption | Có | 1 secret key | Confidentiality | AES-GCM |
| Asymmetric encryption | Có | Public/private key | Encrypt cho người giữ private key | RSA-OAEP |
| Digital signature | Không decrypt data | Private key sign, public key verify | Authenticity + integrity | RS256, ECDSA, EdDSA |
| HMAC | Không | Shared secret | Authenticity + integrity | Webhook signature |

### 2.2. Chọn đúng theo câu hỏi bảo mật

```text
Tôi cần kiểm tra dữ liệu có bị đổi không?
  → Hash hoặc HMAC.

Tôi cần lưu password?
  → Password hashing: Argon2id/bcrypt/scrypt/PBKDF2.

Tôi cần đọc lại dữ liệu gốc sau này?
  → Encryption.

Tôi cần chứng minh message/token do đúng server ký?
  → Digital signature hoặc HMAC.

Tôi cần nhiều service verify token nhưng không được sign token?
  → Asymmetric signature như RS256/ES256/EdDSA.
```

### 2.3. Confidentiality, integrity, authenticity

| Thuộc tính | Câu hỏi | Kỹ thuật |
|---|---|---|
| Confidentiality | Người lạ có đọc được nội dung không? | Encryption |
| Integrity | Nội dung có bị sửa không? | Hash, HMAC, signature, AEAD tag |
| Authenticity | Ai tạo/gửi nội dung này? | HMAC, digital signature |
| Non-repudiation | Người ký có thể chối không? | Digital signature với private key được bảo vệ |

## 3. 📚 Main Concepts

### 3.1. Hashing

Hash function nhận input bất kỳ độ dài và trả output cố định.

```text
"hello"       → SHA-256 → 2cf24dba...
"hello!"      → SHA-256 → ce06092f...
"large file"  → SHA-256 → fixed 256-bit digest
```

Đặc điểm:

- deterministic: cùng input → cùng hash
- one-way: không “decrypt hash”
- fixed length output
- avalanche effect: đổi nhỏ ở input → output khác lớn
- collision-resistant ở thuật toán tốt: khó tìm hai input khác nhau cùng hash

Hash dùng tốt cho:

- file checksum
- cache key/fingerprint
- content integrity
- hash index cho field đã encrypt
- blockchain/merkle tree

Hash không đủ cho:

- password storage nếu dùng SHA-256 thường
- authentication nếu không có secret
- confidentiality vì hash không giấu nội dung theo nghĩa đọc lại được

### 3.2. Password hashing

Password cần thuật toán **chậm có chủ đích** và có salt. Lý do: attacker có thể lấy database hash và brute-force offline.

Khuyến nghị hiện đại:

- **Argon2id**: lựa chọn mạnh cho hệ thống mới nếu stack hỗ trợ.
- **bcrypt**: phổ biến, ổn, có cost factor, nhưng không memory-hard như Argon2id.
- **scrypt**: memory-hard, tốt nếu Argon2id không có.
- **PBKDF2**: dùng khi cần FIPS/compliance hoặc legacy.
- **Không dùng MD5/SHA-1/SHA-256 thuần** cho password.

```ts
import bcrypt from 'bcrypt';

const password = 'correct horse battery staple';
const hash = await bcrypt.hash(password, 12);

const ok = await bcrypt.compare(password, hash);
```

**Salt** thường được algorithm tự generate và lưu chung trong hash format. Không cần tự nối `password + salt` nếu library đã làm đúng.

### 3.3. Salt vs pepper

| Khái niệm | Lưu ở đâu? | Mục đích |
|---|---|---|
| Salt | Lưu cùng password hash | Làm cùng password có hash khác nhau, chống rainbow table |
| Pepper | Secret riêng trong KMS/env/secret manager | Thêm lớp bảo vệ nếu database leak |

Pepper không thay thế password hashing. Nếu dùng pepper, phải có rotation plan vì đổi pepper có thể ảnh hưởng verify password.

### 3.4. HMAC

HMAC là hash có secret key. Nó chứng minh message đến từ bên biết secret và không bị sửa.

Use cases:

- webhook signature
- internal API request signing
- signed payload giữa hai service cùng giữ secret

```ts
import { createHmac, timingSafeEqual } from 'crypto';

function signPayload(payload: string, secret: string) {
  return createHmac('sha256', secret).update(payload).digest('hex');
}

function verifyPayload(payload: string, signature: string, secret: string) {
  const expected = signPayload(payload, secret);

  return timingSafeEqual(
    Buffer.from(expected, 'hex'),
    Buffer.from(signature, 'hex')
  );
}
```

> ⚠️ So sánh signature/hash nên dùng constant-time compare như `timingSafeEqual`, tránh timing attack.

### 3.5. Symmetric encryption

Symmetric encryption dùng cùng một secret key để encrypt/decrypt. Nó nhanh và phù hợp encrypt dữ liệu lớn.

Nên ưu tiên **authenticated encryption** như AES-GCM hoặc ChaCha20-Poly1305, vì vừa encrypt vừa phát hiện tampering.

```text
plaintext + key + IV/nonce → ciphertext + auth tag
ciphertext + key + IV/nonce + auth tag → plaintext hoặc fail
```

Điểm cần nhớ:

- IV/nonce phải unique cho mỗi lần encrypt với cùng key.
- Không dùng ECB mode.
- Không tự thiết kế format crypto.
- Auth tag phải được lưu và verify khi decrypt.
- Key không lưu cùng database ciphertext.

### 3.6. AES-GCM

AES-GCM là lựa chọn phổ biến cho field/file encryption.

```ts
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto';

type EncryptedValue = {
  iv: string;
  ciphertext: string;
  tag: string;
};

function encryptAesGcm(plaintext: string, key: Buffer): EncryptedValue {
  const iv = randomBytes(12);
  const cipher = createCipheriv('aes-256-gcm', key, iv);

  const ciphertext = Buffer.concat([
    cipher.update(plaintext, 'utf8'),
    cipher.final(),
  ]);

  return {
    iv: iv.toString('base64'),
    ciphertext: ciphertext.toString('base64'),
    tag: cipher.getAuthTag().toString('base64'),
  };
}

function decryptAesGcm(encrypted: EncryptedValue, key: Buffer): string {
  const decipher = createDecipheriv(
    'aes-256-gcm',
    key,
    Buffer.from(encrypted.iv, 'base64')
  );

  decipher.setAuthTag(Buffer.from(encrypted.tag, 'base64'));

  const plaintext = Buffer.concat([
    decipher.update(Buffer.from(encrypted.ciphertext, 'base64')),
    decipher.final(),
  ]);

  return plaintext.toString('utf8');
}
```

### 3.7. Asymmetric encryption

Asymmetric encryption dùng key pair:

- public key: share được
- private key: giữ bí mật

Flow encryption:

```text
Sender encrypt bằng receiver public key
Receiver decrypt bằng receiver private key
```

RSA-OAEP thường dùng để encrypt data nhỏ hoặc encrypt symmetric key, không dùng để encrypt file lớn trực tiếp.

```ts
import { constants, privateDecrypt, publicEncrypt } from 'crypto';

function encryptForReceiver(message: string, publicKey: string) {
  return publicEncrypt(
    {
      key: publicKey,
      padding: constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    Buffer.from(message)
  ).toString('base64');
}

function decryptFromSender(ciphertext: string, privateKey: string) {
  return privateDecrypt(
    {
      key: privateKey,
      padding: constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    Buffer.from(ciphertext, 'base64')
  ).toString('utf8');
}
```

### 3.8. Hybrid encryption

Thực tế thường dùng hybrid:

```text
1. Generate random Data Encryption Key (DEK)
2. Encrypt data bằng AES-GCM với DEK
3. Encrypt DEK bằng public key hoặc KMS master key
4. Lưu encrypted data + encrypted DEK
```

Vì sao?

- AES nhanh cho data lớn.
- Asymmetric/KMS tốt cho bảo vệ key nhỏ.
- Dễ rotate master key hơn.

### 3.9. Digital signature

Digital signature không phải “encrypt data bằng private key” theo nghĩa phổ thông. Cách nói dễ hiểu là: **hash data rồi chạy signature algorithm bằng private key**. Verify dùng public key để kiểm tra signature hợp lệ với data.

Signature cung cấp:

- authenticity: đúng người/service có private key ký
- integrity: data không bị sửa
- non-repudiation support: người ký khó chối nếu private key được bảo vệ

Không cung cấp:

- confidentiality: payload vẫn có thể đọc được nếu không encrypt
- replay protection: cần nonce/timestamp/expiry

```ts
import { createSign, createVerify } from 'crypto';

function signMessage(message: string, privateKey: string) {
  return createSign('RSA-SHA256')
    .update(message)
    .end()
    .sign(privateKey, 'base64');
}

function verifyMessage(message: string, signature: string, publicKey: string) {
  return createVerify('RSA-SHA256')
    .update(message)
    .end()
    .verify(publicKey, signature, 'base64');
}
```

### 3.10. JWT, JWS, HS256 vs RS256

JWT thường được ký theo JWS. JWT signed **không tự động encrypted**. Header và payload chỉ base64url encoded, ai có token đều đọc được.

| Algorithm | Loại | Sign | Verify | Khi dùng |
|---|---|---|---|---|
| HS256 | HMAC shared secret | secret | cùng secret | Monolith hoặc ít service, secret bảo vệ tốt |
| RS256 | RSA signature | private key | public key | Nhiều service verify, chỉ auth server sign |
| ES256/EdDSA | ECC/EdDSA signature | private key | public key | Token nhỏ hơn/hiện đại hơn nếu ecosystem hỗ trợ |

RS256 không “luôn an toàn hơn” HS256. Nó phù hợp hơn khi nhiều service cần verify mà không được quyền sign.

JWT pitfalls:

- không bao giờ trust JWT nếu chưa verify signature
- validate `alg`, `iss`, `aud`, `exp`, `nbf`
- không lưu secret/private key trong frontend
- không đưa PII nhạy cảm vào payload
- có key rotation bằng `kid` + JWKS

### 3.11. Database encryption

Với database:

- password: hash bằng Argon2id/bcrypt
- PII cần đọc lại: encrypt bằng AES-GCM hoặc field encryption service
- field cần search exact match: lưu hash index riêng
- key: KMS/Vault/Key Vault/Secret Manager

```ts
type UserRecord = {
  email: string;
  passwordHash: string;
  phoneEncrypted: EncryptedValue;
  phoneHash: string;
};

function hashForLookup(value: string, pepper: string) {
  return createHmac('sha256', pepper).update(value).digest('hex');
}
```

Hash index giúp search exact match, nhưng cũng có privacy risk nếu domain nhỏ. Ví dụ phone number có thể bị brute-force nếu không dùng pepper/HMAC.

### 3.12. Key management

Key management là phần hay sai nhất.

Nên:

- dùng KMS/Vault/HSM/secret manager
- tách quyền encrypt/decrypt theo service
- có key rotation
- log key usage, không log key material
- dùng envelope encryption cho data lớn
- backup/restore key theo quy trình

Không nên:

- hardcode key trong source
- lưu key cùng DB ciphertext
- commit `.env`
- share private key qua chat/email
- dùng cùng key cho mọi mục đích

### 3.13. Frontend implications

Frontend có thể dùng Web Crypto API cho hashing, verifying, encrypt local data, nhưng cần hiểu:

- Secret trong browser có thể bị user/devtools/extension đọc.
- Không dùng frontend để giữ signing secret.
- Không “mã hóa để bảo vệ khỏi chính user đang chạy browser”.
- HTTPS/TLS là bắt buộc để bảo vệ network.
- Client-side encryption chỉ hợp khi threat model chấp nhận, ví dụ end-to-end encryption nơi server không giữ key.

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Password hashing với bcrypt

```ts
import bcrypt from 'bcrypt';

const BCRYPT_COST = 12;

export async function hashPassword(password: string) {
  return bcrypt.hash(password, BCRYPT_COST);
}

export async function verifyPassword(password: string, passwordHash: string) {
  return bcrypt.compare(password, passwordHash);
}
```

### 4.2. SHA-256 checksum bằng Web Crypto

```ts
async function sha256Hex(input: string) {
  const data = new TextEncoder().encode(input);
  const digest = await crypto.subtle.digest('SHA-256', data);

  return [...new Uint8Array(digest)]
    .map((byte) => byte.toString(16).padStart(2, '0'))
    .join('');
}
```

Use case: integrity/checksum/cache key. Không dùng cho password.

### 4.3. Webhook HMAC verification

```ts
import { createHmac, timingSafeEqual } from 'crypto';

function verifyWebhook(rawBody: string, signatureHeader: string, secret: string) {
  const expected = createHmac('sha256', secret)
    .update(rawBody)
    .digest('hex');

  return timingSafeEqual(
    Buffer.from(signatureHeader, 'hex'),
    Buffer.from(expected, 'hex')
  );
}
```

> ⚠️ Webhook thường phải verify trên **raw body**, không phải object đã parse rồi stringify lại.

### 4.4. JWT sign/verify với RS256

```ts
import jwt from 'jsonwebtoken';

type AccessTokenPayload = {
  sub: string;
  roles: string[];
};

export function signAccessToken(payload: AccessTokenPayload, privateKey: string) {
  return jwt.sign(payload, privateKey, {
    algorithm: 'RS256',
    expiresIn: '15m',
    issuer: 'https://auth.example.com',
    audience: 'api.example.com',
    keyid: 'key-2026-01',
  });
}

export function verifyAccessToken(token: string, publicKey: string) {
  return jwt.verify(token, publicKey, {
    algorithms: ['RS256'],
    issuer: 'https://auth.example.com',
    audience: 'api.example.com',
  }) as AccessTokenPayload;
}
```

### 4.5. Field encryption service

```ts
import { randomBytes } from 'crypto';

class FieldEncryptionService {
  constructor(private readonly key: Buffer) {}

  encrypt(value: string) {
    return encryptAesGcm(value, this.key);
  }

  decrypt(value: EncryptedValue) {
    return decryptAesGcm(value, this.key);
  }

  generateDataKey() {
    return randomBytes(32);
  }
}
```

### 4.6. Before/after: password sai cách

```ts
// ❌ Sai: SHA-256 quá nhanh cho password.
const passwordHash = createHash('sha256').update(password).digest('hex');
```

```ts
// ✅ Đúng hơn: password hashing algorithm có cost.
const passwordHash = await bcrypt.hash(password, 12);
```

### 4.7. Before/after: key sai cách

```ts
// ❌ Sai: hardcode key.
const key = Buffer.from('12345678901234567890123456789012');
```

```ts
// ✅ Đúng hơn: load từ secret manager/KMS/env được bảo vệ.
const key = Buffer.from(process.env.FIELD_ENCRYPTION_KEY_HEX!, 'hex');
```

Trong production, env var vẫn chỉ là mức cơ bản. KMS/Vault/HSM tốt hơn cho key lifecycle, audit và rotation.

## 5. 🏗️ Production Notes / React Implications

### 5.1. Không tự viết crypto protocol

Tự ghép SHA/AES/RSA theo cảm tính rất dễ sai. Dùng thư viện chuẩn, mode chuẩn, format chuẩn.

Nên dùng:

- Node `crypto`
- Web Crypto API
- libsodium/tink/noble khi phù hợp
- framework/JWT library được maintain
- KMS/Vault/HSM provider

### 5.2. Frontend không giữ secret

Nếu secret nằm trong bundle, localStorage, IndexedDB hoặc JS memory, user/extension/XSS có thể lấy. Frontend chỉ nên:

- gọi API đã xác thực
- verify public signature nếu cần
- hash/checksum không secret
- encrypt local data bằng key user cung cấp trong mô hình E2EE

### 5.3. XSS làm hỏng mọi crypto ở client

Nếu attacker chạy JS trong origin của bạn, họ có thể đọc token, gọi API, hook function encrypt/decrypt. Vì vậy:

- chống XSS bằng CSP, escaping, sanitization
- tránh lưu token nhạy cảm trong localStorage nếu threat model không cho phép
- dùng HttpOnly cookie khi phù hợp
- rotate/revoke token khi compromise

### 5.4. Key rotation

Rotation cần thiết kế từ đầu:

- ciphertext lưu `keyId`
- JWT header có `kid`
- JWKS expose public keys đang dùng
- decrypt hỗ trợ old keys trong giai đoạn migration
- encrypt mới dùng key mới
- có job re-encrypt nếu cần

### 5.5. Searching encrypted data

Encrypted field không query như plaintext được. Các pattern:

- exact search: HMAC/hash index
- prefix/full-text search: cần search service/tokenization riêng
- range query: không làm bằng AES-GCM thông thường

Đừng đánh đổi privacy bằng cách lưu cả encrypted value và plaintext “cho dễ search”.

### 5.6. Compliance

Các domain như banking, healthcare, payment có thể yêu cầu:

- PCI-DSS
- HIPAA
- SOC2 controls
- FIPS-validated crypto modules
- audit trail cho key usage
- separation of duties

Crypto implementation phải đi cùng threat model và compliance, không chỉ code sample.

## 6. ⚠️ Common Pitfalls

### 6.1. Encrypt password thay vì hash password

Password không cần đọc lại. Hash bằng Argon2id/bcrypt/scrypt/PBKDF2.

### 6.2. Dùng SHA-256 thường cho password

SHA-256 nhanh, attacker brute-force nhanh. Dùng password hashing có cost/memory.

### 6.3. Reuse IV/nonce với AES-GCM

Với cùng key, IV/nonce phải unique. Reuse nonce trong GCM là lỗi nghiêm trọng.

### 6.4. Dùng AES-ECB

ECB lộ pattern dữ liệu. Dùng AES-GCM/ChaCha20-Poly1305.

### 6.5. Không verify JWT signature

Decode JWT không phải verify. Phải verify signature và claims (`iss`, `aud`, `exp`, `nbf`, `alg`).

### 6.6. Nhầm signing với encryption

Signed JWT vẫn đọc được payload. Nếu cần giấu payload, cần JWE/encryption hoặc không đưa dữ liệu nhạy cảm vào token.

### 6.7. Lưu key cùng database

Nếu DB leak và key cũng nằm đó, encryption gần như vô nghĩa.

### 6.8. Dùng cùng key cho nhiều mục đích

Tách key cho JWT signing, field encryption, webhook HMAC, session signing.

### 6.9. Không constant-time compare

So sánh signature bằng `===` có thể lộ timing trong một số ngữ cảnh. Dùng constant-time compare.

### 6.10. Không có crypto agility

Nếu không lưu algorithm/key version, sau này rotate/migrate rất đau.

## 7. ✅ Decision Guide / Checklist

### 7.1. Khi nào dùng gì?

| Use case | Chọn | Lý do |
|---|---|---|
| Lưu password | Argon2id/bcrypt/scrypt/PBKDF2 | Một chiều, chậm, có salt/cost |
| Check file integrity | SHA-256/SHA-512 | Fingerprint nhanh |
| Verify webhook | HMAC-SHA256 | Shared secret + integrity |
| Encrypt PII trong DB | AES-GCM + KMS | Confidentiality + tamper detection |
| Encrypt file lớn | Hybrid encryption | AES cho data, KMS/public key cho DEK |
| JWT trong microservices | RS256/ES256/EdDSA | Public verify, private sign |
| Monolith JWT đơn giản | HS256 có secret mạnh | Đơn giản nếu secret bảo vệ tốt |
| API request signing partner | HMAC hoặc asymmetric signature | Tùy shared secret hay public key model |
| Search exact encrypted field | HMAC/hash index | Query được mà không lưu plaintext |

### 7.2. Checklist crypto production

- [ ] Có threat model rõ.
- [ ] Dùng thuật toán và thư viện được kiểm chứng.
- [ ] Password dùng password hashing, không dùng fast hash.
- [ ] Encryption dùng AEAD như AES-GCM/ChaCha20-Poly1305.
- [ ] IV/nonce random hoặc unique đúng yêu cầu.
- [ ] Key nằm trong KMS/Vault/secret manager.
- [ ] Có key rotation và `keyId`.
- [ ] JWT verify signature + claims.
- [ ] Không đưa secret vào frontend.
- [ ] Không log key/token/plaintext nhạy cảm.
- [ ] Có test cho decrypt fail/tampered data.
- [ ] Có audit/monitoring cho key usage nếu domain yêu cầu.

### 7.3. Checklist JWT

- [ ] Allowlist algorithms, không tin `alg` từ token.
- [ ] Validate `iss`, `aud`, `exp`, `nbf`.
- [ ] Dùng `kid` cho key rotation.
- [ ] Access token short-lived.
- [ ] Không chứa PII nhạy cảm.
- [ ] Verify ở server/API, không chỉ decode ở frontend.

### 7.4. Checklist database encryption

- [ ] Phân loại field: hash, encrypt, tokenize, hoặc không lưu.
- [ ] Password là hash.
- [ ] PII cần đọc lại là encrypted.
- [ ] Field cần exact search có HMAC/hash index.
- [ ] Key không nằm trong DB.
- [ ] Có migration/rotation plan.

## 8. 🎤 Short Interview Answer

Theo em, hashing, encryption và digital signature giải quyết ba bài toán khác nhau. Hashing là một chiều, dùng để tạo fingerprint hoặc lưu password bằng thuật toán chuyên dụng như Argon2id/bcrypt. Encryption là hai chiều, dùng khi mình cần giấu dữ liệu nhưng vẫn đọc lại được, ví dụ AES-GCM cho PII trong database. Digital signature thì dùng private key để ký và public key để verify, giúp chứng minh message/token đến từ đúng bên và không bị sửa.

Điểm quan trọng là không dùng sai công cụ. Password không encrypt mà phải hash chậm có salt/cost. JWT signed không có nghĩa là payload được mã hóa. HS256 ổn nếu secret được bảo vệ tốt trong một hệ thống nhỏ, còn RS256/ES256 hợp hơn khi nhiều service cần verify nhưng không được quyền sign. Với dữ liệu nhạy cảm, thuật toán chỉ là một phần; key management, rotation, KMS/Vault và threat model mới là phần quyết định production có an toàn hay không.

Ở frontend, em không coi secret trong browser là secret. Client có thể dùng Web Crypto cho checksum hoặc verify public signature, nhưng signing secret, encryption key chính và password verification phải ở backend hoặc trong mô hình E2EE được thiết kế riêng.

## 9. 🧾 Ghi nhớ nhanh

- **Hash**: một chiều, fingerprint, không decrypt.
- **Password hash**: Argon2id/bcrypt/scrypt/PBKDF2, không dùng SHA-256 thường.
- **Salt**: chống rainbow table, thường lưu cùng hash.
- **HMAC**: hash + secret, dùng cho webhook/API signature.
- **Encryption**: hai chiều, bảo vệ confidentiality.
- **AES-GCM**: symmetric authenticated encryption phổ biến.
- **RSA-OAEP**: encrypt data nhỏ/key, không encrypt file lớn trực tiếp.
- **Digital signature**: private sign, public verify.
- **JWT signed không encrypted**: payload vẫn đọc được.
- **Key management > algorithm choice**: KMS/Vault/rotation/audit rất quan trọng.
- **Frontend không giữ secret thật**.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Hashing | Tạo digest một chiều từ dữ liệu |
| Digest | Output của hash function |
| Collision | Hai input khác nhau cho cùng hash |
| Salt | Random value dùng trong password hashing |
| Pepper | Secret bổ sung ngoài database cho password/hash index |
| Rainbow table | Bảng hash dựng sẵn để tra ngược password phổ biến |
| Password hashing | Hash chậm có salt/cost để chống brute-force |
| Argon2id | Password hashing memory-hard được khuyến nghị cho hệ mới |
| bcrypt | Password hashing phổ biến có cost factor |
| PBKDF2 | Key derivation/password hashing dùng nhiều trong compliance |
| HMAC | Message authentication code dựa trên hash và shared secret |
| Encryption | Mã hóa dữ liệu để chỉ người có key đọc được |
| Plaintext | Dữ liệu gốc chưa mã hóa |
| Ciphertext | Dữ liệu sau khi mã hóa |
| Symmetric key | Cùng key dùng encrypt và decrypt |
| Public key | Key công khai trong asymmetric crypto |
| Private key | Key bí mật để decrypt hoặc sign |
| AES-GCM | Authenticated encryption mode phổ biến |
| IV/nonce | Giá trị unique/random dùng khi encrypt |
| Auth tag | Tag dùng để phát hiện ciphertext bị sửa |
| RSA-OAEP | RSA encryption padding hiện đại hơn PKCS#1 v1.5 |
| Digital signature | Chữ ký số verify authenticity và integrity |
| JWS | JSON Web Signature, chuẩn ký payload JSON |
| JWT | JSON Web Token, token dạng header.payload.signature |
| JWKS | JSON Web Key Set, endpoint public keys để verify JWT |
| `kid` | Key ID trong JWT header để chọn public key verify |
| KMS | Key Management Service |
| Envelope encryption | Encrypt data bằng DEK, encrypt DEK bằng master key |
| Key rotation | Thay key theo chu kỳ/quy trình |
| AEAD | Authenticated Encryption with Associated Data |

## 11. 📚 Nguồn chính thức đã đối chiếu

- OWASP Password Storage Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html>
- OWASP Cryptographic Storage Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html>
- OWASP Key Management Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html>
- NIST Glossary - Digital Signature: <https://csrc.nist.gov/glossary/term/digital_signature>
- RFC 7515 - JSON Web Signature: <https://www.rfc-editor.org/rfc/rfc7515.html>
