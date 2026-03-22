Bạn hãy phân tích toàn diện source code dự án sau để tôi hiểu rõ flow, kiến trúc, thư viện, business logic và các quyết định kỹ thuật.

Thông tin cung cấp:
- Tên dự án: [Tên]
- Mô tả ngắn: [Nếu có]
- Cấu trúc thư mục (tree): [Dán vào]
- File cấu hình phụ thuộc (package.json, requirements.txt…): [Dán nếu có]
- Module quan trọng (nếu biết): [Liệt kê]

Yêu cầu phân tích:

=====================
1. Tổng quan & Business domain
=====================
- Hệ thống giải quyết bài toán gì?
- Đối tượng người dùng chính
- Các thực thể (entities) & quy tắc nghiệp vụ quan trọng
- Use cases chính

=====================
2. Flow xử lý chính
=====================
- Flow khi user thực hiện hành động quan trọng
- Luồng dữ liệu: UI → API → Service → DB → Response
- Các điểm async (queue, event, cron job…)

Vẽ flow dạng ASCII:
Ví dụ:
User → Controller → Service → Repository → Database → Response

=====================
3. Kiến trúc hệ thống
=====================
- Loại kiến trúc (Monolith, Microservices, Clean Architecture…)
- Các layer và trách nhiệm
- Sự phụ thuộc giữa các module
- Điểm coupling cao

=====================
4. Công nghệ & thư viện
=====================
Phân tích từ file dependencies:

- Framework chính
- State management
- Networking / API
- UI / Styling
- Logging / Monitoring
- Testing

Với mỗi thư viện quan trọng:
- Vai trò trong dự án
- Ảnh hưởng tới kiến trúc
- Trade-offs (ưu/nhược điểm)
- Lựa chọn thay thế khả thi

=====================
5. Thiết kế chi tiết & patterns
=====================
- Cấu trúc thư mục phản ánh điều gì?
- Pattern sử dụng (MVC, Repository, DDD…)
- Cách xử lý:
  - State
  - Error handling
  - Caching
  - Validation

=====================
6. Hiệu năng & khả năng mở rộng
=====================
- Bottlenecks tiềm ẩn
- Chiến lược scaling (horizontal/vertical)
- Caching & tối ưu performance
- Bundle size / query optimization

=====================
7. Bảo mật
=====================
- Authentication & Authorization
- Các rủi ro bảo mật tiềm ẩn
- Best practices chưa được áp dụng

=====================
8. CI/CD & vận hành
=====================
- Quy trình build & deploy
- Logging & monitoring
- Rollback & disaster recovery

=====================
9. Đánh giá & cải tiến
=====================
- Điểm mạnh kiến trúc & codebase
- Điểm yếu & technical debt
- Đề xuất cải tiến thực tế

=====================
10. Trade-offs & quyết định kỹ thuật
=====================
- Vì sao các lựa chọn hiện tại hợp lý hoặc chưa hợp lý?
- Nếu xây lại từ đầu:
  - Giữ gì?
  - Thay đổi gì?
  - Lý do