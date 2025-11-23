# 🎪 Q11: DOM Events - Event Flow, Delegation & Event Properties (Bubbling, Capturing, target vs currentTarget)




**⚡ Quick Summary:**
> Event Bubbling = child → parent. Capturing = parent → child. Delegation = listen ở parent

**💡 Ghi Nhớ:**
- 🎯 **Bubbling**: Event từ child lên parent (default)
- ⬇️ **Capturing**: Event từ parent xuống child (useCapture: true)
- 🎭 **target vs currentTarget**: target = phần tử gốc, currentTarget = phần tử có listener

**❓ Câu Hỏi:**

Giải thích chi tiết cơ chế hoạt động của DOM Events trong JavaScript, bao gồm:

1. Event Flow (Event Bubbling vs Event Capturing)
2. Event Delegation Pattern
3. Sự khác biệt giữa `target` và `currentTarget`
4. Các best practices và common mistakes



**📚 Phần 1: Event Flow - 3 Phases của DOM Events**

**🔥 Cơ Chế Hoạt Động:**

Khi một event xảy ra trên DOM element, nó đi qua 3 phases (giai đoạn):

```
Phase 1: CAPTURING PHASE (Giai đoạn bắt - từ trên xuống)
   ↓
   document
   ↓
   html
   ↓
   body
   ↓
   parent div
   ↓
Phase 2: TARGET PHASE (Giai đoạn mục tiêu)
   ↓
   target element (element được click)
   ↓
Phase 3: BUBBLING PHASE (Giai đoạn nổi - từ dưới lên)
   ↑
   parent div
   ↑
   body
   ↑
   html
   ↑
   document
```

**💡 Giải Thích Tiếng Việt:**

- **Capturing Phase (Bắt sự kiện)**: Event "rơi xuống" từ window → document → html → body → ... → target element
- **Target Phase (Mục tiêu)**: Event chạm đến element được click (target)
- **Bubbling Phase (Nổi lên)**: Event "nổi lên" từ target element → ... → body → html → document → window

**🎯 Code Example với Chú Thích Tiếng Việt:**

```typescript
// 📌 HTML Structure (Cấu trúc HTML)
// <div id="grandparent" style="padding: 50px; background: red;">
//   Grandparent (Ông)
//   <div id="parent" style="padding: 30px; background: blue;">
//     Parent (Cha)
//     <div id="child" style="padding: 20px; background: green;">
//       <button id="button">Click Me!</button>
//     </div>
//   </div>
// </div>

// ============================================
// 🔵 EXAMPLE 1: EVENT BUBBLING (Mặc định)
// Event nổi lên từ dưới lên: Button → Child → Parent → Grandparent
// ============================================

// Chú thích: addEventListener() mặc định lắng nghe ở BUBBLING phase
// Tham số thứ 3 = false (hoặc không truyền) nghĩa là bubbling  
document.getElementById('button')?.addEventListener('click', (e: Event) => {
  console.log('1️⃣ Button clicked (bubbling)');
  // Chạy đầu tiên vì button là target element (phần tử được click)
});

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('2️⃣ Child div clicked (bubbling)');
  // Chạy thứ 2 - event nổi lên từ button
});

document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('3️⃣ Parent div clicked (bubbling)');
  // Chạy thứ 3 - event tiếp tục nổi lên
});

document.getElementById('grandparent')?.addEventListener('click', (e: Event) => {
  console.log('4️⃣ Grandparent div clicked (bubbling)');
  // Chạy cuối cùng - event nổi đến tận ông nội
});

// 📝 KẾT QUẢ khi click button:
// 1️⃣ Button clicked (bubbling)
// 2️⃣ Child div clicked (bubbling)
// 3️⃣ Parent div clicked (bubbling)
// 4️⃣ Grandparent div clicked (bubbling)

// ============================================
// 🟢 EXAMPLE 2: EVENT CAPTURING (Bắt sự kiện)
// Event rơi xuống từ trên xuống: Grandparent → Parent → Child → Button
// ============================================

// Chú thích: Tham số thứ 3 = true nghĩa là CAPTURING phase
document.getElementById('grandparent')?.addEventListener(
  'click',
  (e: Event) => {
    console.log('1️⃣ Grandparent clicked (capturing)');
    // Chạy đầu tiên - ông nội bắt event trước
  },
  true // ⚠️ true = capturing phase (bắt từ trên xuống)
);

document.getElementById('parent')?.addEventListener(
  'click',
  (e: Event) => {
    console.log('2️⃣ Parent clicked (capturing)');
    // Chạy thứ 2 - cha bắt event
  },
  true
);

document.getElementById('child')?.addEventListener(
  'click',
  (e: Event) => {
    console.log('3️⃣ Child clicked (capturing)');
    // Chạy thứ 3 - con bắt event
  },
  true
);

document.getElementById('button')?.addEventListener(
  'click',
  (e: Event) => {
    console.log('4️⃣ Button clicked (capturing)');
    // Chạy cuối cùng - đến target element
  },
  true
);

// 📝 KẾT QUẢ khi click button:
// 1️⃣ Grandparent clicked (capturing)
// 2️⃣ Parent clicked (capturing)
// 3️⃣ Child clicked (capturing)
// 4️⃣ Button clicked (capturing)

// ============================================
// 🛑 EXAMPLE 3: STOP PROPAGATION
// Dừng event lan truyền (không nổi lên hoặc rơi xuống nữa)
// ============================================

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('Child clicked');
  e.stopPropagation(); // ⛔ Dừng event tại đây - không lan truyền nữa
  // Event KHÔNG nổi lên parent và grandparent
});

document.getElementById('parent')?.addEventListener('click', () => {
  console.log('Parent clicked'); // ❌ KHÔNG chạy vì bị stopPropagation()
});

// ============================================
// 🚫 EXAMPLE 4: PREVENT DEFAULT
// Ngăn hành vi mặc định của trình duyệt
// ============================================

// Ví dụ 1: Ngăn link navigate
document.getElementById('myLink')?.addEventListener('click', (e: Event) => {
  e.preventDefault(); // ⛔ Ngăn trình duyệt chuyển trang
  console.log('Link clicked but navigation prevented');
  // Chú thích: Thay vì chuyển trang, ta có thể xử lý logic khác
});

// Ví dụ 2: Ngăn form submit
document.getElementById('myForm')?.addEventListener('submit', (e: Event) => {
  e.preventDefault(); // ⛔ Ngăn form gửi đi (reload trang)
  console.log('Form submit prevented - validating data...');
  // Chú thích: Validate dữ liệu trước khi submit bằng AJAX
});
```

---

**📚 Phần 2: Event Delegation (Kỹ Thuật Ủy Quyền Event)**

**🔥 Khái Niệm:**

Event Delegation là kỹ thuật thay vì gắn event listener cho từng element con, ta chỉ gắn 1 listener duy nhất cho element cha, sau đó kiểm tra xem element nào được click thông qua `event.target`.

**💡 Lợi Ích:**

1. **Performance tốt hơn**: Chỉ có 1 event listener thay vì hàng trăm/ngàn listeners
2. **Memory hiệu quả**: Ít listeners = ít bộ nhớ  
3. **Dynamic content**: Tự động handle các elements được thêm sau
4. **Maintainability**: Code dễ bảo trì hơn

**🎯 Code Example với Chú Thích Chi Tiết:**

```typescript
// ============================================
// ❌ CÁCH KHÔNG HIỆU QUẢ: Attach event cho từng item
// ============================================

// HTML: <ul id="todoList">
//         <li class="todo-item" data-id="1">Task 1 <button class="delete">X</button></li>
//         <li class="todo-item" data-id="2">Task 2 <button class="delete">X</button></li>
//         <li class="todo-item" data-id="3">Task 3 <button class="delete">X</button></li>
//       </ul>

// ❌ VẤN ĐỀ: Nếu có 1000 items thì tạo 1000 event listeners!
const todoItems = document.querySelectorAll('.todo-item');
todoItems.forEach((item) => {
  item.addEventListener('click', (e: Event) => {
    console.log('Todo clicked:', item.dataset.id);
    // Chú thích: Mỗi item có 1 listener riêng → tốn memory
  });
});

// ============================================
// ✅ CÁCH HIỆU QUẢ: EVENT DELEGATION
// ============================================

// ✅ Chỉ cần 1 listener trên parent (ul)
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;

  // Chú thích: Kiểm tra xem element được click có phải là todo-item không
  if (target.classList.contains('todo-item')) {
    console.log('✅ Todo clicked:', target.dataset.id);
    // Chú thích: Xử lý click vào todo item
  }

  // Chú thích: Kiểm tra xem có phải click vào nút delete không
  if (target.classList.contains('delete')) {
    // closest() tìm parent element gần nhất có class 'todo-item'
    const todoItem = target.closest('.todo-item') as HTMLElement;
    console.log('🗑️ Delete clicked for todo:', todoItem?.dataset.id);
    todoItem?.remove(); // Xóa todo item
  }
});

// ✅ Thêm item mới - KHÔNG CẦN attach listener
function addTodoItem(text: string, id: string): void {
  const todoList = document.getElementById('todoList');
  const newItem = document.createElement('li');
  newItem.className = 'todo-item';
  newItem.dataset.id = id;
  newItem.innerHTML = `${text} <button class="delete">X</button>`;
  todoList?.appendChild(newItem);
  
  // 🎉 Event delegation tự động handle item mới!
  // Không cần addEventListener() ở đây
}
```

---

**📚 Phần 3: target vs currentTarget - Hiểu Rõ Sự Khác Biệt**

**🔥 Định Nghĩa:**

- **`event.target`**: Element THỰC SỰ được click (có thể là element con sâu bên trong)
- **`event.currentTarget`**: Element có EVENT LISTENER được attach (luôn là element ta gọi addEventListener)

**🎯 Code Example:**

```typescript
// HTML: <div id="parent">
//         <button id="child">Click Me!</button>
//       </div>

document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('target:', e.target); // <button id="child">
  console.log('currentTarget:', e.currentTarget); // <div id="parent">
  
  // Chú thích:
  // - target = button (thứ được click thực sự)
  // - currentTarget = div parent (nơi có addEventListener)
});
```

**📌 So Sánh:**

| Property | target | currentTarget |
|----------|--------|---------------|
| **Định nghĩa** | Element THỰC SỰ được click | Element CÓ addEventListener() |
| **Trong event delegation** | Con hoặc cháu của currentTarget | Luôn là parent element |
| **Sử dụng** | Xác định element cụ thể được tương tác | Truy cập data/properties của parent |

---

**✅ Best Practices:**

1. Sử dụng Event Delegation cho dynamic content
2. Sử dụng `closest()` để tìm parent element
3. Check target type trước khi xử lý
4. Sử dụng `stopPropagation()` khi cần thiết
5. Sử dụng `preventDefault()` cho forms và links

**❌ Common Mistakes:**

1. Nhầm lẫn target vs currentTarget
2. Không check element type
3. Quên stopPropagation() khi có nested events
4. Event delegation nhưng không check target
5. Mix capturing và bubbling không rõ ràng
