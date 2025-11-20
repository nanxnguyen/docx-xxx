# 🌐 Q18: DOM API & Query Methods




**⚡ Quick Summary:**
> querySelector = CSS selector. getElementById = nhanh nhất. querySelectorAll = NodeList

**💡 Ghi Nhớ:**
- ⚡ **getElementById**: Nhanh nhất, live
- 🎯 **querySelector**: CSS selector, static
- 📋 **querySelectorAll**: Return NodeList (not array)

**Trả lời:**

- **DOM API**: Các methods để manipulate DOM elements
- **Query Methods**: Các methods để select elements từ DOM
- **Hoạt động**: getElementById, querySelector, getElementsByClassName, etc.
- **Ưu điểm**: Flexible element selection, powerful manipulation
- **Nhược điểm**: Có thể chậm với large DOM, cần hiểu rõ performance

**Code Example:**

```typescript
// Query Methods
// getElementById - trả về single element
const element = document.getElementById('myId');
if (element) {
  element.textContent = 'Hello World';
}

// querySelector - trả về first matching element
const firstDiv = document.querySelector('div');
const firstClass = document.querySelector('.my-class');
const firstId = document.querySelector('#my-id');

// querySelectorAll - trả về NodeList
const allDivs = document.querySelectorAll('div');
const allClasses = document.querySelectorAll('.my-class');

// getElementsByClassName - trả về HTMLCollection
const elementsByClass = document.getElementsByClassName('my-class');

// getElementsByTagName - trả về HTMLCollection
const elementsByTag = document.getElementsByTagName('div');

// DOM Manipulation
const div = document.createElement('div');
div.textContent = 'New element';
div.className = 'my-class';
div.id = 'new-id';

// Append to DOM
document.body.appendChild(div);

// Insert before
const existingElement = document.getElementById('existing');
existingElement?.parentNode?.insertBefore(div, existingElement);

// Remove element
div.remove();

// Update attributes
div.setAttribute('data-id', '123');
div.getAttribute('data-id'); // '123'
div.removeAttribute('data-id');

// Update classes
div.classList.add('new-class');
div.classList.remove('old-class');
div.classList.toggle('active');
div.classList.contains('active'); // true/false

// Update styles
div.style.color = 'red';
div.style.backgroundColor = 'blue';
div.style.display = 'none';

// Update content
div.textContent = 'Text content';
div.innerHTML = '<span>HTML content</span>';
div.innerText = 'Text only (no HTML)';

// Event handling
div.addEventListener('click', (e: Event) => {
  console.log('Div clicked');
});

// Remove event listener
const clickHandler = (e: Event) => console.log('Clicked');
div.addEventListener('click', clickHandler);
div.removeEventListener('click', clickHandler);
```

**Best Practices:**

- Sử dụng querySelector cho modern development
- Sử dụng getElementById cho single elements
- Sử dụng addEventListener thay vì onclick
- Sử dụng proper error handling

**Mistakes:**

```typescript
// ❌ Sai: Không check null
const element = document.getElementById('myId');
element.textContent = 'Hello'; // Error nếu element null

// ✅ Đúng: Check null
const element = document.getElementById('myId');
if (element) {
  element.textContent = 'Hello';
}

// ❌ Sai: Sử dụng innerHTML với user input
const userInput = '<script>alert("XSS")</script>';
div.innerHTML = userInput; // XSS vulnerability

// ✅ Đúng: Sử dụng textContent
div.textContent = userInput; // Safe
```

