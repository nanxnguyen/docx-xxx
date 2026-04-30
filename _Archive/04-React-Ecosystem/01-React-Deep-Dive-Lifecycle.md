# ⚛️ Q25: React Hooks & Advanced Patterns - Lifecycle, Performance, Architecture

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"React Hooks thay thế Class Components với API sạch hơn và tái sử dụng tốt hơn.**

**🪝 Hooks Cốt Lõi (Bắt Buộc Biết):**
1. **useState**: Quản lý state. Cập nhật theo hàm `setState(prev => prev + 1)` tránh closure cũ.
2. **useEffect**: Hiệu ứng phụ, vòng đời. Hàm cleanup ngăn rò rỉ bộ nhớ. Mảng phụ thuộc kiểm soát chạy lại.
3. **useRef**: Giá trị thay đổi được nhưng không gây render lại. Truy cập DOM, lưu giá trị trước, timers.
4. **useMemo**: Cache tính toán nặng. Chỉ tính lại khi dependencies thay đổi.
5. **useCallback**: Cache tham chiếu hàm. Ngăn component con render lại khi truyền callbacks.
6. **useContext**: Truy cập giá trị Context. Tránh prop drilling.
7. **useReducer**: Logic state phức tạp. Thay thế useState khi có nhiều giá trị phụ.

**🔄 Ánh Xạ Vòng Đời (Class → Hooks):**
- **componentDidMount**: `useEffect(() => {}, [])`
- **componentDidUpdate**: `useEffect(() => {}, [deps])`
- **componentWillUnmount**: `useEffect(() => { return cleanup }, [])`
- **getDerivedStateFromProps**: `useMemo(() => compute(props), [props])`
- **shouldComponentUpdate**: `React.memo()` + `useMemo/useCallback`

**⚙️ Virtual DOM và Reconciliation:**
- **Virtual DOM**: Biểu diễn cây trong bộ nhớ → thuật toán so sánh nhanh.
- **Reconciliation**: So sánh VDOM cũ vs mới → cập nhật DOM tối thiểu.
- **Prop key**: Giúp React nhận diện item nào thay đổi → cập nhật danh sách hiệu quả. KHÔNG bao giờ dùng index làm key khi danh sách động.
- **Kiến trúc Fiber**: Rendering tăng dần → tạm dừng/tiếp tục công việc → hiệu năng cảm nhận tốt hơn.

**🚀 Tối Ưu Hiệu Năng:**
1. **React.memo()**: So sánh nông props → bỏ qua render lại nếu props không đổi.
2. **useMemo()**: Cache tính toán nặng → tránh tính lại mỗi lần render.
3. **useCallback()**: Cache tham chiếu hàm → ngăn component con render lại.
4. **Chia Code**: `React.lazy()` + Suspense → tải components theo yêu cầu.
5. **Ảo hóa**: `react-window` cho danh sách dài → chỉ render items hiển thị.
6. **Tránh hàm/object inline**: Tạo tham chiếu mới mỗi lần render → con render lại.

**🎨 Mẫu Thiết Kế Nâng Cao:**
- **HOC (Component Bậc Cao)**: Bọc component để inject props. Ví dụ: `withAuth(Component)`.
- **Render Props**: Truyền hàm làm children. Ví dụ: `<DataProvider>{data => <List data={data} />}</DataProvider>`.
- **Compound Components**: Các component giao tiếp qua Context. Ví dứ: `<Tabs><Tab /></Tabs>`.
- **Custom Hooks**: Trích xuất logic tái sử dụng. Bắt đầu bằng `use`. Trả về state/functions.

**⚡ Tính Năng React 18+:**
1. **Concurrent Rendering**: Render có thể ngắt → UI phản hồi trong khi cập nhật nặng.
2. **useTransition()**: Đánh dấu cập nhật không khẩn cấp → giữ UI phản hồi.
3. **useDeferredValue()**: Trì hoãn render nặng → debouncing tích hợp sẵn.
4. **Suspense cho Data Fetching**: Trạng thái loading khai báo.
5. **Server Components**: Render trên server → không có JS bundle cho component đó.
6. **Batching Tự Động**: Gộp nhiều setState → 1 lần render (kể cả trong async).

**⚠️ Lỗi Thường Gặp:**
- **Thiếu dependencies trong useEffect**: ESLint cảnh báo → sửa hoặc vô hiệu nếu cố ý.
- **Vòng lặp vô hạn**: useEffect không có deps array + setState bên trong → render vô hạn.
- **Lạm dụng useMemo/useCallback**: Tối ưu sớm → chỉ dùng khi đo được vấn đề hiệu năng.
- **Thay đổi state trực tiếp**: `state.value = 1` → React không phát hiện → dùng `setState`.

**💡 Kiến Thức Senior:**
- **useEffect vs useLayoutEffect**: useLayoutEffect chạy đồng bộ sau render, TRƯỚC trình duyệt vẽ → dùng khi cần đo DOM.
- **StrictMode**: Gọi effects 2 lần trong dev → bắt lỗi side effects sớm.
- **Profiler**: Component `<Profiler>` + DevTools → đo hiệu năng render.
- **Batching**: React 18 tự động gộp mọi cập nhật (kể cả setTimeout, promises) → ít render hơn.
- **Keys trong Reconciliation**: Key thay đổi → unmount component cũ + mount mới → reset state.

---

**Trả lời:**

Câu hỏi này bao gồm tất cả kiến thức quan trọng về React từ cơ bản đến nâng cao, bao gồm:
- Tất cả React Hooks (useState, useEffect, useRef, useReducer, useContext, useMemo, useCallback, useLayoutEffect, useImperativeHandle, useSyncExternalStore)
- Lifecycle của Class Component vs Functional Component
- Virtual DOM, Reconciliation, key trong lists
- Performance optimization (React.memo, PureComponent)
- Advanced patterns (HOC, Render Props, Compound Components)
- React 18+ features (Suspense, Server Components, Concurrent Rendering, useTransition, useDeferredValue)
- React Router, Portal, Batching, Code Splitting

#### **📚 PHẦN 1: REACT HOOKS - TẤT CẢ CÁC HOOK CƠ BẢN & NÂNG CAO**

---

##### **1.1. useState - State Management Hook**

**🎯 Mục đích:**
Quản lý state trong functional component (trước đây chỉ có class component mới có state).

**📖 Cách hoạt động:**
```typescript
const [state, setState] = useState(initialValue);

// Cách hoạt động bên trong React:
// 1. Lần render đầu tiên: React tạo một "fiber node" cho component
// 2. useState tạo một "hook object" với giá trị initial
// 3. Hook object được lưu trong linked list trên fiber node
// 4. setState trigger re-render bằng cách đánh dấu fiber "dirty"
// 5. Reconciliation: React so sánh old state vs new state
// 6. Nếu khác (Object.is comparison) → re-render component
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC USAGE
// ══════════════════════════════════════════════════════════

function Counter() {
  const [count, setCount] = useState(0); // Primitive state
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// FUNCTIONAL UPDATES (Quan trọng cho async updates)
// ══════════════════════════════════════════════════════════

function Counter() {
  const [count, setCount] = useState(0);
  
  // ❌ Sai: Có thể bị stale closure khi gọi nhiều lần
  const handleClick = () => {
    setCount(count + 1);
    setCount(count + 1); // Chỉ tăng 1 lần vì count cũ!
  };
  
  // ✅ Đúng: Luôn dùng giá trị mới nhất
  const handleClickCorrect = () => {
    setCount(prev => prev + 1);
    setCount(prev => prev + 1); // Tăng 2 lần đúng!
  };
  
  return <button onClick={handleClickCorrect}>Increment Twice</button>;
}

// ══════════════════════════════════════════════════════════
// LAZY INITIALIZATION (Tối ưu performance)
// ══════════════════════════════════════════════════════════

function ExpensiveComponent() {
  // ❌ Sai: Chạy expensive function mỗi lần re-render
  const [data, setData] = useState(expensiveComputation());
  
  // ✅ Đúng: Chỉ chạy 1 lần khi mount
  const [data, setData] = useState(() => expensiveComputation());
  
  return <div>{data}</div>;
}

function expensiveComputation() {
  console.log('Computing...'); // Chỉ log 1 lần với lazy init
  let result = 0;
  for (let i = 0; i < 1000000; i++) {
    result += i;
  }
  return result;
}

// ══════════════════════════════════════════════════════════
// OBJECT/ARRAY STATE (Immutability pattern)
// ══════════════════════════════════════════════════════════

function UserForm() {
  const [user, setUser] = useState({
    name: '',
    email: '',
    address: { city: '', street: '' }
  });
  
  // ❌ Sai: Mutate trực tiếp (React không detect change)
  const handleChangeBad = (e) => {
    user.name = e.target.value; // Mutation!
    setUser(user); // React không re-render vì cùng reference
  };
  
  // ✅ Đúng: Tạo object mới (immutable update)
  const handleChange = (e) => {
    setUser(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };
  
  // ✅ Nested object update
  const handleAddressChange = (field, value) => {
    setUser(prev => ({
      ...prev,
      address: {
        ...prev.address,
        [field]: value
      }
    }));
  };
  
  return (
    <form>
      <input name="name" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <input 
        name="city" 
        onChange={(e) => handleAddressChange('city', e.target.value)} 
      />
    </form>
  );
}

// ══════════════════════════════════════════════════════════
// ARRAY STATE OPERATIONS
// ══════════════════════════════════════════════════════════

function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', done: false }
  ]);
  
  // Thêm item
  const addTodo = (text) => {
    setTodos(prev => [...prev, { id: Date.now(), text, done: false }]);
  };
  
  // Xóa item
  const removeTodo = (id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  };
  
  // Update item
  const toggleTodo = (id) => {
    setTodos(prev => prev.map(todo => 
      todo.id === id ? { ...todo, done: !todo.done } : todo
    ));
  };
  
  // Insert at position
  const insertAt = (index, text) => {
    setTodos(prev => [
      ...prev.slice(0, index),
      { id: Date.now(), text, done: false },
      ...prev.slice(index)
    ]);
  };
  
  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>
          <input 
            type="checkbox" 
            checked={todo.done}
            onChange={() => toggleTodo(todo.id)}
          />
          {todo.text}
          <button onClick={() => removeTodo(todo.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}
```

**⚠️ Common Mistakes:**

```typescript
// ❌ 1. Không dùng functional update khi cần previous state
const [count, setCount] = useState(0);
setCount(count + 1); // Stale closure issue

// ✅ Fix
setCount(prev => prev + 1);

// ❌ 2. Mutate state trực tiếp
const [arr, setArr] = useState([1, 2, 3]);
arr.push(4); // Mutation!
setArr(arr); // Không re-render

// ✅ Fix
setArr(prev => [...prev, 4]);

// ❌ 3. Set state trong render (infinite loop)
function Component() {
  const [count, setCount] = useState(0);
  setCount(1); // ❌ Infinite loop!
  return <div>{count}</div>;
}

// ✅ Fix: Set state trong event handler hoặc useEffect
useEffect(() => {
  setCount(1);
}, []);
```

---

##### **1.2. useEffect - Side Effects Hook**

**🎯 Mục đích:**
Xử lý side effects (API calls, subscriptions, DOM manipulation, timers) trong functional components.

**📖 Cách hoạt động:**
```typescript
useEffect(() => {
  // Effect function (chạy sau render)
  return () => {
    // Cleanup function (chạy trước khi component unmount hoặc effect re-run)
  };
}, [dependencies]); // Dependency array

// Timeline:
// 1. Component render (JSX → Virtual DOM)
// 2. React commit changes to real DOM
// 3. Browser paint screen
// 4. useEffect callback chạy (AFTER paint - không block UI)
// 5. Khi dependencies thay đổi:
//    - Cleanup function chạy trước
//    - Effect function chạy lại
// 6. Khi component unmount: Cleanup chạy cuối cùng
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// useEffect COVERS CÁC LIFECYCLE NÀO?
// ══════════════════════════════════════════════════════════

// Class component lifecycle:
class ClassComponent extends React.Component {
  componentDidMount() {
    // Chạy 1 lần sau mount
  }
  
  componentDidUpdate(prevProps, prevState) {
    // Chạy mỗi khi props/state thay đổi
  }
  
  componentWillUnmount() {
    // Cleanup trước khi unmount
  }
}

// Functional component equivalent:
function FunctionalComponent() {
  // ✅ componentDidMount + componentWillUnmount
  useEffect(() => {
    console.log('Mounted');
    return () => console.log('Unmounted'); // cleanup
  }, []); // Empty deps = chỉ chạy 1 lần
  
  // ✅ componentDidUpdate (khi count thay đổi)
  useEffect(() => {
    console.log('Count changed:', count);
  }, [count]); // Chạy khi count thay đổi
  
  // ✅ componentDidMount + componentDidUpdate (mỗi lần render)
  useEffect(() => {
    console.log('Every render');
  }); // No deps = chạy mỗi lần render
}

// ══════════════════════════════════════════════════════════
// DEPENDENCY ARRAY RULES
// ══════════════════════════════════════════════════════════

function Example({ userId }) {
  const [user, setUser] = useState(null);
  
  // ❌ Sai: Missing dependency
  useEffect(() => {
    fetchUser(userId).then(setUser); // userId không có trong deps!
  }, []); // ESLint sẽ warning
  
  // ✅ Đúng: Include all dependencies
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Re-fetch khi userId thay đổi
  
  // ✅ Ignore ESLint (nếu chắc chắn không cần)
  useEffect(() => {
    fetchUser(userId).then(setUser);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []); // Chỉ fetch 1 lần (nhưng có thể stale)
}

// ══════════════════════════════════════════════════════════
// CLEANUP FUNCTION - KHI NÀO CHẠY?
// ══════════════════════════════════════════════════════════

function Timer() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    console.log('Effect running');
    const timer = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);
    
    // Cleanup chạy khi:
    // 1. Component unmount
    // 2. Trước khi effect chạy lại (nếu deps thay đổi)
    return () => {
      console.log('Cleanup running');
      clearInterval(timer); // ⚠️ Quan trọng: tránh memory leak!
    };
  }, []); // Empty deps = cleanup chỉ chạy khi unmount
  
  return <div>{count}</div>;
}

// ══════════════════════════════════════════════════════════
// REAL-WORLD EXAMPLES
// ══════════════════════════════════════════════════════════

// 1. Data Fetching
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let cancelled = false; // Prevent setting state on unmounted component
    
    const fetchUser = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        
        if (!cancelled) {
          setUser(data);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    
    fetchUser();
    
    return () => {
      cancelled = true; // Cleanup: mark as cancelled
    };
  }, [userId]);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div>{user?.name}</div>;
}

// 2. Event Listeners
function WindowSize() {
  const [size, setSize] = useState({ width: 0, height: 0 });
  
  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };
    
    // Add listener
    window.addEventListener('resize', handleResize);
    handleResize(); // Set initial size
    
    // Cleanup: Remove listener
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // No deps = setup once
  
  return <div>{size.width} x {size.height}</div>;
}

// 3. Subscriptions (WebSocket, EventEmitter)
function ChatRoom({ roomId }) {
  const [messages, setMessages] = useState([]);
  
  useEffect(() => {
    const socket = new WebSocket(`ws://chat.com/${roomId}`);
    
    socket.onmessage = (event) => {
      setMessages(prev => [...prev, JSON.parse(event.data)]);
    };
    
    // Cleanup: Close connection
    return () => {
      socket.close();
    };
  }, [roomId]); // Re-connect khi đổi room
  
  return (
    <ul>
      {messages.map((msg, i) => <li key={i}>{msg.text}</li>)}
    </ul>
  );
}

// 4. Document Title
function PageTitle({ title }) {
  useEffect(() => {
    const prevTitle = document.title;
    document.title = title;
    
    return () => {
      document.title = prevTitle; // Restore
    };
  }, [title]);
}

// 5. Local Storage Sync
function useSyncWithLocalStorage(key, value) {
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);
}

function Settings() {
  const [theme, setTheme] = useState('light');
  useSyncWithLocalStorage('theme', theme);
  
  return <button onClick={() => setTheme('dark')}>Dark Mode</button>;
}
```

**⚠️ Common Mistakes:**

```typescript
// ❌ 1. Không cleanup subscriptions/timers
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  // ❌ Missing cleanup → memory leak
}, []);

// ✅ Fix
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);
}, []);

// ❌ 2. Infinite loop (missing deps hoặc deps sai)
useEffect(() => {
  setCount(count + 1); // ❌ count thay đổi → effect chạy lại → count thay đổi...
}, [count]);

// ✅ Fix: Không set state của chính dependency
useEffect(() => {
  // Fetch data based on count, không set count
}, [count]);

// ❌ 3. Async function trực tiếp trong useEffect
useEffect(async () => { // ❌ Error: useEffect không nhận async function
  const data = await fetchData();
}, []);

// ✅ Fix: Tạo async function bên trong
useEffect(() => {
  const fetchData = async () => {
    const data = await fetch('/api');
  };
  fetchData();
}, []);

// ❌ 4. Race condition (fetch data)
useEffect(() => {
  fetchUser(userId).then(setUser); // ❌ Nếu userId đổi nhanh, response cũ có thể về sau
}, [userId]);

// ✅ Fix: Use cleanup để ignore stale responses
useEffect(() => {
  let cancelled = false;
  fetchUser(userId).then(data => {
    if (!cancelled) setUser(data);
  });
  return () => { cancelled = true; };
}, [userId]);
```

---

##### **1.3. useRef - Mutable Reference Hook**

**🎯 Mục đích:**
1. Access DOM elements trực tiếp
2. Lưu giá trị mutable không trigger re-render
3. Lưu previous value của state/props

**📖 useRef vs useState:**

```typescript
// useState: Trigger re-render khi thay đổi
const [count, setCount] = useState(0);
setCount(1); // → Component re-render

// useRef: KHÔNG trigger re-render
const countRef = useRef(0);
countRef.current = 1; // → Component KHÔNG re-render

// Timeline:
// useState: Change state → Schedule re-render → Re-render → Paint
// useRef: Change ref.current → (Nothing happens, no re-render)
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// 1. DOM ACCESS (Primary use case)
// ══════════════════════════════════════════════════════════

function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);
  
  useEffect(() => {
    // Access DOM node directly
    inputRef.current?.focus();
  }, []);
  
  return <input ref={inputRef} />;
}

// Complex DOM manipulation
function VideoPlayer() {
  const videoRef = useRef<HTMLVideoElement>(null);
  
  const play = () => videoRef.current?.play();
  const pause = () => videoRef.current?.pause();
  const seek = (time: number) => {
    if (videoRef.current) {
      videoRef.current.currentTime = time;
    }
  };
  
  return (
    <>
      <video ref={videoRef} src="/video.mp4" />
      <button onClick={play}>Play</button>
      <button onClick={pause}>Pause</button>
      <button onClick={() => seek(10)}>Seek to 10s</button>
    </>
  );
}

// ══════════════════════════════════════════════════════════
// 2. PERSIST VALUES ACROSS RENDERS (không trigger re-render)
// ══════════════════════════════════════════════════════════

function Timer() {
  const [count, setCount] = useState(0);
  const intervalRef = useRef<number>(null);
  
  const start = () => {
    // Lưu interval ID để clear sau này
    intervalRef.current = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);
  };
  
  const stop = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  };
  
  useEffect(() => {
    return () => stop(); // Cleanup
  }, []);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// 3. TRACK PREVIOUS VALUE
// ══════════════════════════════════════════════════════════

function usePrevious<T>(value: T): T | undefined {
  const ref = useRef<T>();
  
  useEffect(() => {
    ref.current = value; // Update ref AFTER render
  });
  
  return ref.current; // Return PREVIOUS value (before update)
}

function Counter() {
  const [count, setCount] = useState(0);
  const prevCount = usePrevious(count);
  
  return (
    <div>
      <p>Current: {count}</p>
      <p>Previous: {prevCount}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// 4. AVOID RE-RENDERS (Performance optimization)
// ══════════════════════════════════════════════════════════

function ClickTracker() {
  const [renderCount, setRenderCount] = useState(0);
  const clickCountRef = useRef(0); // Không trigger re-render
  
  const handleClick = () => {
    clickCountRef.current++; // Update ref (no re-render)
    console.log('Clicks:', clickCountRef.current);
    
    // Force re-render để show UI
    setRenderCount(prev => prev + 1);
  };
  
  return (
    <div>
      <p>Renders: {renderCount}</p>
      <p>Clicks: {clickCountRef.current}</p>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// 5. CALLBACK REF (Advanced)
// ══════════════════════════════════════════════════════════

function MeasureElement() {
  const [height, setHeight] = useState(0);
  
  // Callback ref: được gọi khi element mount/unmount
  const measureRef = useCallback((node: HTMLDivElement | null) => {
    if (node !== null) {
      setHeight(node.getBoundingClientRect().height);
    }
  }, []);
  
  return (
    <>
      <div ref={measureRef}>
        <p>Measure me!</p>
      </div>
      <p>Height: {height}px</p>
    </>
  );
}
```

**⚠️ Common Mistakes:**

```typescript
// ❌ 1. Expect re-render khi thay đổi ref
const countRef = useRef(0);
countRef.current++;
// ❌ Component không re-render → UI không update

// ✅ Fix: Dùng useState nếu cần re-render
const [count, setCount] = useState(0);

// ❌ 2. Mutate ref.current trong render
function Component() {
  const ref = useRef(0);
  ref.current++; // ❌ Side effect trong render!
  return <div>{ref.current}</div>;
}

// ✅ Fix: Update trong useEffect hoặc event handler
useEffect(() => {
  ref.current++;
}, []);

// ❌ 3. Không check null khi access DOM
const inputRef = useRef<HTMLInputElement>(null);
inputRef.current.focus(); // ❌ Có thể null!

// ✅ Fix: Check null hoặc dùng optional chaining
inputRef.current?.focus();
```

---

##### **1.4. useLayoutEffect - Synchronous Effect Hook**

**🎯 Mục đích:**
Chạy effect TRƯỚC KHI browser paint (synchronous), dùng cho DOM measurements hoặc mutations cần xảy ra trước khi user thấy UI.

**📖 useEffect vs useLayoutEffect Timeline:**

```typescript
// useEffect:
// 1. React renders component (Virtual DOM)
// 2. React commits to real DOM
// 3. Browser PAINTS screen (user thấy UI)
// 4. useEffect runs (AFTER paint - không block UI)

// useLayoutEffect:
// 1. React renders component
// 2. React commits to real DOM
// 3. useLayoutEffect runs (BEFORE paint - BLOCKS UI)
// 4. Browser paints (user thấy UI đã updated)
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// KHI NÀO DÙNG useLayoutEffect?
// ══════════════════════════════════════════════════════════

// ✅ Use case 1: DOM measurements (avoid flicker)
function Tooltip() {
  const [tooltip, setTooltip] = useState({ x: 0, y: 0 });
  const buttonRef = useRef<HTMLButtonElement>(null);
  
  // ❌ useEffect: User thấy tooltip nhảy vì chạy SAU paint
  useEffect(() => {
    const rect = buttonRef.current?.getBoundingClientRect();
    setTooltip({ x: rect.left, y: rect.bottom });
  }, []);
  
  // ✅ useLayoutEffect: Tooltip đúng vị trí ngay từ đầu
  useLayoutEffect(() => {
    const rect = buttonRef.current?.getBoundingClientRect();
    setTooltip({ x: rect.left, y: rect.bottom });
  }, []);
  
  return (
    <>
      <button ref={buttonRef}>Hover me</button>
      <div style={{ position: 'absolute', left: tooltip.x, top: tooltip.y }}>
        Tooltip
      </div>
    </>
  );
}

// ✅ Use case 2: Scroll position (avoid jump)
function RestoreScroll() {
  const contentRef = useRef<HTMLDivElement>(null);
  
  useLayoutEffect(() => {
    // Restore scroll TRƯỚC khi paint → no visual jump
    const savedScroll = localStorage.getItem('scrollPos');
    if (savedScroll && contentRef.current) {
      contentRef.current.scrollTop = parseInt(savedScroll);
    }
  }, []);
  
  useEffect(() => {
    const handleScroll = () => {
      if (contentRef.current) {
        localStorage.setItem('scrollPos', contentRef.current.scrollTop.toString());
      }
    };
    
    contentRef.current?.addEventListener('scroll', handleScroll);
    return () => contentRef.current?.removeEventListener('scroll', handleScroll);
  }, []);
  
  return <div ref={contentRef} style={{ height: 400, overflow: 'auto' }}>
    {/* Long content */}
  </div>;
}

// ✅ Use case 3: Animate before paint
function AnimatedBox() {
  const boxRef = useRef<HTMLDivElement>(null);
  
  useLayoutEffect(() => {
    // Set initial position BEFORE paint
    if (boxRef.current) {
      boxRef.current.style.transform = 'translateX(-100px)';
      boxRef.current.style.opacity = '0';
    }
    
    // Then animate (browser batches with paint)
    requestAnimationFrame(() => {
      if (boxRef.current) {
        boxRef.current.style.transition = 'all 0.3s';
        boxRef.current.style.transform = 'translateX(0)';
        boxRef.current.style.opacity = '1';
      }
    });
  }, []);
  
  return <div ref={boxRef}>Animated Box</div>;
}
```

**⚠️ Khi nào KHÔNG nên dùng useLayoutEffect:**

```typescript
// ❌ Data fetching (không cần sync)
useLayoutEffect(() => {
  fetch('/api').then(setData); // Block UI unnecessarily!
}, []);

// ✅ Dùng useEffect thay vì
useEffect(() => {
  fetch('/api').then(setData);
}, []);

// ❌ Subscriptions (không cần sync)
useLayoutEffect(() => {
  const sub = eventEmitter.on('event', handler);
  return () => sub.off();
}, []);

// ✅ Dùng useEffect
useEffect(() => {
  const sub = eventEmitter.on('event', handler);
  return () => sub.off();
}, []);

// Rule of thumb:
// - useEffect: 99% cases (default choice)
// - useLayoutEffect: Chỉ khi có visual bugs (flicker, jump, wrong position)
```

---

##### **1.5. useReducer - Complex State Management Hook**

**🎯 Mục đích:**
Quản lý state phức tạp với logic xử lý tập trung (giống Redux pattern).

**📖 Khi nào dùng useReducer thay vì useState:**
- State có nhiều sub-values liên quan
- State update logic phức tạp (nhiều actions)
- Next state phụ thuộc vào previous state
- Muốn centralize state logic (dễ test)

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC PATTERN
// ══════════════════════════════════════════════════════════

type State = { count: number };
type Action = 
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'reset' }
  | { type: 'set'; payload: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    case 'set':
      return { count: action.payload };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// REAL-WORLD: TODO APP
// ══════════════════════════════════════════════════════════

type Todo = { id: number; text: string; done: boolean };
type TodoState = { todos: Todo[]; filter: 'all' | 'active' | 'completed' };
type TodoAction =
  | { type: 'ADD_TODO'; text: string }
  | { type: 'TOGGLE_TODO'; id: number }
  | { type: 'DELETE_TODO'; id: number }
  | { type: 'SET_FILTER'; filter: 'all' | 'active' | 'completed' }
  | { type: 'CLEAR_COMPLETED' };

function todoReducer(state: TodoState, action: TodoAction): TodoState {
  switch (action.type) {
    case 'ADD_TODO':
      return {
        ...state,
        todos: [...state.todos, { 
          id: Date.now(), 
          text: action.text, 
          done: false 
        }]
      };
      
    case 'TOGGLE_TODO':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.id ? { ...todo, done: !todo.done } : todo
        )
      };
      
    case 'DELETE_TODO':
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.id)
      };
      
    case 'SET_FILTER':
      return { ...state, filter: action.filter };
      
    case 'CLEAR_COMPLETED':
      return {
        ...state,
        todos: state.todos.filter(todo => !todo.done)
      };
      
    default:
      return state;
  }
}

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, {
    todos: [],
    filter: 'all'
  });
  
  const visibleTodos = state.todos.filter(todo => {
    if (state.filter === 'active') return !todo.done;
    if (state.filter === 'completed') return todo.done;
    return true;
  });
  
  return (
    <div>
      <input 
        type="text"
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            dispatch({ type: 'ADD_TODO', text: e.currentTarget.value });
            e.currentTarget.value = '';
          }
        }}
      />
      
      <ul>
        {visibleTodos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => dispatch({ type: 'TOGGLE_TODO', id: todo.id })}
            />
            {todo.text}
            <button onClick={() => dispatch({ type: 'DELETE_TODO', id: todo.id })}>
              Delete
            </button>
          </li>
        ))}
      </ul>
      
      <div>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'all' })}>
          All
        </button>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'active' })}>
          Active
        </button>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'completed' })}>
          Completed
        </button>
        <button onClick={() => dispatch({ type: 'CLEAR_COMPLETED' })}>
          Clear Completed
        </button>
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// LAZY INITIALIZATION
// ══════════════════════════════════════════════════════════

function init(initialCount: number): State {
  // Expensive computation
  return { count: initialCount * 2 };
}

function Counter() {
  // Init function chỉ chạy 1 lần
  const [state, dispatch] = useReducer(reducer, 10, init);
  // state.count = 20 (10 * 2)
}
```

**⚠️ useReducer vs useState:**

```typescript
// useState: Simple state
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const [email, setEmail] = useState('');

// useReducer: Complex related state
type FormState = { name: string; email: string; errors: string[] };
const [state, dispatch] = useReducer(formReducer, initialState);

// Rule:
// - 1-3 related values → useState
// - 4+ related values OR complex logic → useReducer
```

---

##### **1.6. useContext - Consume Context Values**

**🎯 Mục đích:** Share data across component tree mà không cần pass props (theme, auth, language).

**📖 Cách hoạt động:**

```typescript
// Context flow:
// 1. createContext() → Tạo Context object
// 2. <Provider value={...}> → Cung cấp value
// 3. useContext(Context) → Subscribe và nhận value
// 4. Khi value thay đổi → All consumers re-render

// Performance note:
// - Context re-render TẤT CẢ consumers khi value thay đổi
// - Không có selector mechanism (khác Redux)
// - Cần optimize bằng React.memo hoặc useMemo
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC USAGE
// ══════════════════════════════════════════════════════════

type Theme = 'light' | 'dark';
const ThemeContext = createContext<Theme>('light');

function App() {
  const [theme, setTheme] = useState<Theme>('light');
  
  return (
    <ThemeContext.Provider value={theme}>
      <Toolbar />
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  return <ThemedButton />;
}

function ThemedButton() {
  const theme = useContext(ThemeContext); // ✅ Clean syntax
  
  return (
    <button className={theme}>
      I am styled with {theme} theme
    </button>
  );
}

// Old way (before hooks):
function ThemedButtonOld() {
  return (
    <ThemeContext.Consumer>
      {theme => ( // ❌ Wrapper hell
        <button className={theme}>
          I am styled with {theme} theme
        </button>
      )}
    </ThemeContext.Consumer>
  );
}

// ══════════════════════════════════════════════════════════
// MULTIPLE CONTEXTS
// ══════════════════════════════════════════════════════════

const ThemeContext = createContext('light');
const UserContext = createContext(null);
const LanguageContext = createContext('en');

function App() {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);
  const [lang, setLang] = useState('en');
  
  return (
    <ThemeContext.Provider value={theme}>
      <UserContext.Provider value={user}>
        <LanguageContext.Provider value={lang}>
          <Dashboard />
        </LanguageContext.Provider>
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}

function Dashboard() {
  const theme = useContext(ThemeContext);
  const user = useContext(UserContext);
  const lang = useContext(LanguageContext);
  
  return (
    <div className={theme}>
      Welcome {user?.name} ({lang})
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// CUSTOM HOOK PATTERN (Best practice)
// ══════════════════════════════════════════════════════════

type AuthContextType = {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  loading: boolean;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Custom hook với error checking
function useAuth() {
  const context = useContext(AuthContext);
  
  if (context === undefined) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  
  return context;
}

// Provider component
function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(false);
  
  const login = async (email: string, password: string) => {
    setLoading(true);
    try {
      const user = await authService.login(email, password);
      setUser(user);
    } finally {
      setLoading(false);
    }
  };
  
  const logout = () => {
    authService.logout();
    setUser(null);
  };
  
  const value = useMemo(
    () => ({ user, login, logout, loading }),
    [user, loading]
  );
  
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// Usage
function App() {
  return (
    <AuthProvider>
      <Dashboard />
    </AuthProvider>
  );
}

function Dashboard() {
  const { user, logout } = useAuth(); // ✅ Type-safe, error checking
  
  return (
    <div>
      <p>Welcome {user?.name}</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// PERFORMANCE OPTIMIZATION
// ══════════════════════════════════════════════════════════

// ❌ Problem: All consumers re-render khi BẤT KỲ value nào thay đổi
function AppBad() {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');
  
  // ❌ New object mỗi render → all consumers re-render
  const value = { user, theme, setUser, setTheme };
  
  return (
    <AppContext.Provider value={value}>
      <Component1 /> {/* Re-render khi theme đổi dù chỉ dùng user */}
      <Component2 /> {/* Re-render khi user đổi dù chỉ dùng theme */}
    </AppContext.Provider>
  );
}

// ✅ Solution 1: Split contexts
function AppGood() {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');
  
  const userValue = useMemo(() => ({ user, setUser }), [user]);
  const themeValue = useMemo(() => ({ theme, setTheme }), [theme]);
  
  return (
    <UserContext.Provider value={userValue}>
      <ThemeContext.Provider value={themeValue}>
        <Component1 /> {/* Chỉ re-render khi user đổi */}
        <Component2 /> {/* Chỉ re-render khi theme đổi */}
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

// ✅ Solution 2: React.memo cho consumers
const Component1 = React.memo(function Component1() {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
});
```

---

##### **1.7. useMemo - Memoized Value Hook**

**🎯 Mục đích:**
Cache kết quả của expensive calculations, chỉ re-compute khi dependencies thay đổi.

**📖 Khi nào dùng useMemo:**
1. Expensive calculations (sorting, filtering large arrays)
2. Preventing re-creation of objects/arrays (pass to child components)
3. Optimizing child component re-renders

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC PATTERN
// ══════════════════════════════════════════════════════════

function ProductList({ products, filter }) {
  // ❌ Without useMemo: Sort lại MỖI lần component re-render
  const sortedProducts = products.sort((a, b) => a.price - b.price);
  
  // ✅ With useMemo: Chỉ sort khi products hoặc filter thay đổi
  const sortedProducts = useMemo(() => {
    console.log('Sorting...'); // Chỉ log khi re-compute
    return products
      .filter(p => p.category === filter)
      .sort((a, b) => a.price - b.price);
  }, [products, filter]); // Dependencies
  
  return (
    <ul>
      {sortedProducts.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}

// ══════════════════════════════════════════════════════════
// EXPENSIVE COMPUTATION
// ══════════════════════════════════════════════════════════

function Fibonacci({ n }) {
  const result = useMemo(() => {
    function fib(num) {
      if (num <= 1) return num;
      return fib(num - 1) + fib(num - 2);
    }
    return fib(n);
  }, [n]);
  
  return <div>Fibonacci({n}) = {result}</div>;
}

// ══════════════════════════════════════════════════════════
// PREVENT CHILD RE-RENDERS
// ══════════════════════════════════════════════════════════

function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  // ❌ New object mỗi render → Child re-render dù props "giống"
  const config = { theme: 'dark', lang: 'en' };
  
  // ✅ Stable reference → Child chỉ re-render khi config thực sự đổi
  const config = useMemo(() => ({
    theme: 'dark',
    lang: 'en'
  }), []); // No deps = never re-create
  
  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child config={config} /> {/* Không re-render khi name thay đổi */}
    </>
  );
}

const Child = React.memo(({ config }) => {
  console.log('Child rendered');
  return <div>{config.theme}</div>;
});

// ══════════════════════════════════════════════════════════
// DERIVED STATE
// ══════════════════════════════════════════════════════════

function TodoList({ todos }) {
  // Stats chỉ re-compute khi todos thay đổi
  const stats = useMemo(() => ({
    total: todos.length,
    completed: todos.filter(t => t.done).length,
    active: todos.filter(t => !t.done).length,
    completionRate: todos.length > 0 
      ? (todos.filter(t => t.done).length / todos.length * 100).toFixed(1)
      : '0'
  }), [todos]);
  
  return (
    <div>
      <p>Total: {stats.total}</p>
      <p>Completed: {stats.completed}</p>
      <p>Active: {stats.active}</p>
      <p>Completion: {stats.completionRate}%</p>
    </div>
  );
}
```

**⚠️ Khi KHÔNG nên dùng useMemo:**

```typescript
// ❌ 1. Cheap calculations
const doubled = useMemo(() => count * 2, [count]);
// ✅ Just compute directly
const doubled = count * 2;

// ❌ 2. Primitives (không cần memoize)
const greeting = useMemo(() => 'Hello', []);
// ✅ Just use constant
const greeting = 'Hello';

// ❌ 3. Over-optimization (premature optimization)
const data = useMemo(() => transform(props.data), [props.data]);
// ✅ Profile first! Nếu không có performance issue, đừng dùng

// Rule: Chỉ dùng useMemo khi:
// - Có performance issue đo được (React DevTools Profiler)
// - Computation thực sự expensive (>10ms)
// - Prevent child re-renders (với React.memo)
```

---

##### **1.8. useCallback - Memoized Function Hook**

**🎯 Mục đích:**
Cache function reference, tránh re-create function mỗi render (optimization cho child components).

**📖 useCallback vs useMemo:**

```typescript
// useCallback: Memoize FUNCTION
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);

// Equivalent to:
const memoizedCallback = useMemo(() => {
  return () => doSomething(a, b);
}, [a, b]);

// useMemo: Memoize RETURN VALUE
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC USAGE
// ══════════════════════════════════════════════════════════

function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  // ❌ New function mỗi render → Child re-render
  const handleClick = () => {
    console.log('Clicked');
  };
  
  // ✅ Stable reference → Child không re-render
  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []); // No deps = never re-create
  
  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child onClick={handleClick} /> {/* Không re-render khi name đổi */}
    </>
  );
}

const Child = React.memo(({ onClick }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>Click</button>;
});

// ══════════════════════════════════════════════════════════
// WITH DEPENDENCIES
// ══════════════════════════════════════════════════════════

function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  // Function re-create khi query thay đổi
  const handleSearch = useCallback(async () => {
    const data = await fetch(`/api/search?q=${query}`);
    setResults(await data.json());
  }, [query]); // Dependency: query
  
  // Debounced version
  const debouncedSearch = useCallback(
    debounce(handleSearch, 300),
    [handleSearch]
  );
  
  return (
    <div>
      <input 
        value={query} 
        onChange={e => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// EVENT HANDLERS WITH STATE
// ══════════════════════════════════════════════════════════

function TodoItem({ todo, onToggle, onDelete }) {
  // ❌ Tạo function mới mỗi render (nếu không memo)
  const handleToggle = () => onToggle(todo.id);
  const handleDelete = () => onDelete(todo.id);
  
  // ✅ Stable references (nếu parent truyền memoized callbacks)
  const handleToggle = useCallback(() => {
    onToggle(todo.id);
  }, [todo.id, onToggle]);
  
  const handleDelete = useCallback(() => {
    onDelete(todo.id);
  }, [todo.id, onDelete]);
  
  return (
    <li>
      <input type="checkbox" onChange={handleToggle} />
      {todo.text}
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
}

// ══════════════════════════════════════════════════════════
// CUSTOM HOOKS
// ══════════════════════════════════════════════════════════

function useDebounce(callback, delay, deps) {
  const timeoutRef = useRef(null);
  
  return useCallback((...args) => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    
    timeoutRef.current = setTimeout(() => {
      callback(...args);
    }, delay);
  }, [callback, delay, ...deps]);
}

// Usage
function Search() {
  const [query, setQuery] = useState('');
  
  const search = useCallback((q) => {
    console.log('Searching for:', q);
  }, []);
  
  const debouncedSearch = useDebounce(search, 500, []);
  
  return (
    <input 
      value={query}
      onChange={e => {
        setQuery(e.target.value);
        debouncedSearch(e.target.value);
      }}
    />
  );
}
```

**⚠️ Common Mistakes:**

```typescript
// ❌ 1. useCallback without React.memo (vô ích)
function Parent() {
  const handleClick = useCallback(() => {}, []); // Vô ích vì Child không memo!
  return <Child onClick={handleClick} />;
}

function Child({ onClick }) { // ❌ Không memo → vẫn re-render
  return <button onClick={onClick}>Click</button>;
}

// ✅ Fix: Dùng React.memo
const Child = React.memo(({ onClick }) => {
  return <button onClick={onClick}>Click</button>;
});

// ❌ 2. Missing dependencies
const handleClick = useCallback(() => {
  console.log(count); // ❌ count không có trong deps → stale
}, []);

// ✅ Fix: Include count
const handleClick = useCallback(() => {
  console.log(count);
}, [count]);

// ❌ 3. Over-optimization
const handleClick = useCallback(() => {
  setCount(c => c + 1);
}, []); // ❌ Không cần thiết nếu không pass cho child

// ✅ Just use regular function
const handleClick = () => {
  setCount(c => c + 1);
};
```

---

##### **1.9. useImperativeHandle - Customize Ref Exposure**

**🎯 Mục đích:**
Customize giá trị exposed qua ref từ child component (advanced pattern, ít dùng).

**📖 Khi nào dùng:**
- Expose specific methods từ child (thay vì toàn bộ DOM node)
- Tạo reusable components với imperative API
- Integration với third-party libraries

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC PATTERN
// ══════════════════════════════════════════════════════════

type InputHandle = {
  focus: () => void;
  clear: () => void;
};

const CustomInput = forwardRef<InputHandle, { placeholder?: string }>(
  (props, ref) => {
    const inputRef = useRef<HTMLInputElement>(null);
    
    // Expose custom methods thay vì DOM node
    useImperativeHandle(ref, () => ({
      focus: () => {
        inputRef.current?.focus();
      },
      clear: () => {
        if (inputRef.current) {
          inputRef.current.value = '';
        }
      }
    }), []); // Deps: re-create methods khi deps thay đổi
    
    return <input ref={inputRef} placeholder={props.placeholder} />;
  }
);

// Usage
function Parent() {
  const inputRef = useRef<InputHandle>(null);
  
  return (
    <>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current?.focus()}>Focus</button>
      <button onClick={() => inputRef.current?.clear()}>Clear</button>
    </>
  );
}

// ══════════════════════════════════════════════════════════
// FORM VALIDATION
// ══════════════════════════════════════════════════════════

type FormHandle = {
  submit: () => void;
  reset: () => void;
  validate: () => boolean;
  getValues: () => Record<string, any>;
};

const Form = forwardRef<FormHandle, { onSubmit: (data: any) => void }>(
  ({ onSubmit }, ref) => {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});
    
    const validate = useCallback(() => {
      // Validation logic
      const newErrors = {};
      if (!values.email) newErrors.email = 'Required';
      setErrors(newErrors);
      return Object.keys(newErrors).length === 0;
    }, [values]);
    
    useImperativeHandle(ref, () => ({
      submit: () => {
        if (validate()) {
          onSubmit(values);
        }
      },
      reset: () => {
        setValues({});
        setErrors({});
      },
      validate,
      getValues: () => values
    }), [values, validate, onSubmit]);
    
    return (
      <form>
        {/* Form fields */}
      </form>
    );
  }
);

// Usage
function Parent() {
  const formRef = useRef<FormHandle>(null);
  
  return (
    <>
      <Form ref={formRef} onSubmit={console.log} />
      <button onClick={() => formRef.current?.submit()}>Submit</button>
      <button onClick={() => formRef.current?.reset()}>Reset</button>
    </>
  );
}
```

**⚠️ Best Practices:**

```typescript
// ❌ Don't expose entire DOM node
useImperativeHandle(ref, () => inputRef.current);

// ✅ Expose specific methods
useImperativeHandle(ref, () => ({
  focus: () => inputRef.current?.focus()
}));

// ❌ Don't overuse (prefer props/callbacks)
// Imperative API should be last resort

// ✅ Use declarative approach when possible
<Input autoFocus onClear={handleClear} /> // Declarative
vs
inputRef.current.focus(); // Imperative
```

---

##### **1.10. useSyncExternalStore - Sync with External Store**

**🎯 Mục đích:**
Subscribe to external stores (Redux, Zustand, browser APIs) một cách an toàn với React 18+ concurrent rendering.

**📖 Tại sao cần hook này:**
- React 18+ có concurrent rendering → có thể render nhiều lần trước commit
- External stores (không phải React state) có thể thay đổi giữa các lần render
- useSyncExternalStore đảm bảo consistency

**💡 Chi tiết kỹ thuật:**

```typescript
// ══════════════════════════════════════════════════════════
// BASIC PATTERN
// ══════════════════════════════════════════════════════════

const store = {
  listeners: new Set(),
  state: { count: 0 },
  
  subscribe(listener) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  },
  
  getSnapshot() {
    return this.state;
  },
  
  increment() {
    this.state = { count: this.state.count + 1 };
    this.listeners.forEach(listener => listener());
  }
};

function Counter() {
  const state = useSyncExternalStore(
    store.subscribe.bind(store),  // subscribe function
    store.getSnapshot.bind(store) // getSnapshot function
  );
  
  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => store.increment()}>Increment</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// BROWSER APIs (window.online)
// ══════════════════════════════════════════════════════════

function useOnlineStatus() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('online', callback);
      window.addEventListener('offline', callback);
      return () => {
        window.removeEventListener('online', callback);
        window.removeEventListener('offline', callback);
      };
    },
    () => navigator.onLine, // getSnapshot
    () => true // getServerSnapshot (SSR)
  );
}

function StatusBar() {
  const isOnline = useOnlineStatus();
  return <div>{isOnline ? '🟢 Online' : '🔴 Offline'}</div>;
}

// ══════════════════════════════════════════════════════════
// WINDOW SIZE
// ══════════════════════════════════════════════════════════

function useWindowSize() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('resize', callback);
      return () => window.removeEventListener('resize', callback);
    },
    () => ({ width: window.innerWidth, height: window.innerHeight }),
    () => ({ width: 0, height: 0 }) // SSR fallback
  );
}

// ══════════════════════════════════════════════════════════
// ZUSTAND STORE (Example)
// ══════════════════════════════════════════════════════════

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));

// Zustand internally uses useSyncExternalStore (React 18+)
function Counter() {
  const count = useStore(state => state.count);
  const increment = useStore(state => state.increment);
  
  return <button onClick={increment}>{count}</button>;
}
```

**💡 Note:**
- Hầu hết developers KHÔNG cần dùng trực tiếp
- Libraries (Redux, Zustand, Jotai) đã integrate internally
- Chỉ cần khi build custom state management library

---

#### **📚 PHẦN 2: LIFECYCLE - CLASS VS FUNCTIONAL COMPONENTS**

---

##### **2.1. Class Component Lifecycle**

```typescript
class MyComponent extends React.Component {
  // ══════════════════════════════════════════════════════════
  // MOUNTING PHASE (Component được tạo và thêm vào DOM)
  // ══════════════════════════════════════════════════════════
  
  constructor(props) {
    super(props);
    // 1. Khởi tạo state
    this.state = { count: 0 };
    // 2. Bind methods
    this.handleClick = this.handleClick.bind(this);
    // ⚠️ KHÔNG gọi setState() ở đây!
    // ⚠️ KHÔNG có side effects (API calls, subscriptions)
  }
  
  static getDerivedStateFromProps(props, state) {
    // 2. Sync state với props (HIẾM khi dùng)
    // Chạy TRƯỚC mỗi render (mount + update)
    // Must return object to update state, or null
    if (props.value !== state.value) {
      return { value: props.value };
    }
    return null;
  }
  
  componentDidMount() {
    // 3. Component đã mount vào DOM
    // ✅ PERFECT cho:
    // - API calls / Data fetching
    // - Subscriptions (WebSocket, EventEmitter)
    // - DOM manipulation
    // - Setup timers/intervals
    
    // Example:
    fetch('/api/data')
      .then(res => res.json())
      .then(data => this.setState({ data }));
    
    this.timer = setInterval(() => {
      this.setState({ time: new Date() });
    }, 1000);
    
    document.addEventListener('click', this.handleClick);
  }
  
  // ══════════════════════════════════════════════════════════
  // UPDATING PHASE (Props hoặc State thay đổi)
  // ══════════════════════════════════════════════════════════
  
  shouldComponentUpdate(nextProps, nextState) {
    // 4. Quyết định có render lại không (performance optimization)
    // Return false → skip render
    // ⚠️ PureComponent tự động implement shallow comparison
    
    return nextProps.id !== this.props.id || 
           nextState.count !== this.state.count;
  }
  
  getSnapshotBeforeUpdate(prevProps, prevState) {
    // 5. Capture DOM info TRƯỚC khi update (HIẾM dùng)
    // Return value → pass vào componentDidUpdate
    
    // Example: Preserve scroll position
    if (prevProps.list.length < this.props.list.length) {
      return this.listRef.scrollHeight;
    }
    return null;
  }
  
  componentDidUpdate(prevProps, prevState, snapshot) {
    // 6. Component đã re-render
    // ✅ PERFECT cho:
    // - Fetch data khi props thay đổi
    // - DOM manipulation based on changes
    // - Update third-party libraries
    
    // ⚠️ MUST so sánh props/state trước khi setState (tránh infinite loop!)
    if (this.props.userId !== prevProps.userId) {
      this.fetchUser(this.props.userId);
    }
    
    // Use snapshot from getSnapshotBeforeUpdate
    if (snapshot !== null) {
      this.listRef.scrollTop = 
        this.listRef.scrollHeight - snapshot;
    }
  }
  
  // ══════════════════════════════════════════════════════════
  // UNMOUNTING PHASE (Component bị remove khỏi DOM)
  // ══════════════════════════════════════════════════════════
  
  componentWillUnmount() {
    // 7. Cleanup trước khi unmount
    // ✅ REQUIRED để tránh memory leaks:
    // - Clear timers/intervals
    // - Cancel network requests
    // - Unsubscribe
    // - Remove event listeners
    
    clearInterval(this.timer);
    document.removeEventListener('click', this.handleClick);
    this.subscription.unsubscribe();
  }
  
  // ══════════════════════════════════════════════════════════
  // ERROR HANDLING
  // ══════════════════════════════════════════════════════════
  
  static getDerivedStateFromError(error) {
    // 8. Update state khi có error
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    // 9. Log error info
    logErrorToService(error, errorInfo);
  }
  
  render() {
    // 10. Return JSX (MUST be pure function)
    // ⚠️ KHÔNG setState, side effects ở đây!
    return <div>{this.state.count}</div>;
  }
}
```

**📊 Lifecycle Diagram:**

```
MOUNTING:
constructor → getDerivedStateFromProps → render → componentDidMount

UPDATING (props/state change):
getDerivedStateFromProps → shouldComponentUpdate → render → 
getSnapshotBeforeUpdate → componentDidUpdate

UNMOUNTING:
componentWillUnmount

ERROR:
getDerivedStateFromError → componentDidCatch
```

---

##### **2.2. Functional Component Lifecycle (với Hooks)**

```typescript
function MyComponent(props) {
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: constructor
  // ══════════════════════════════════════════════════════════
  const [count, setCount] = useState(0);
  const [data, setData] = useState(null);
  
  // Lazy initialization (như constructor logic)
  const [expensiveState, setExpensiveState] = useState(() => {
    return computeExpensiveValue();
  });
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: getDerivedStateFromProps
  // ══════════════════════════════════════════════════════════
  // ❌ Không cần! Chỉ compute trong render
  const derivedValue = props.value * 2;
  
  // Hoặc nếu cần sync với state:
  const [value, setValue] = useState(props.initialValue);
  useEffect(() => {
    setValue(props.initialValue);
  }, [props.initialValue]);
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: componentDidMount
  // ══════════════════════════════════════════════════════════
  useEffect(() => {
    // Chạy SAU first render
    console.log('Mounted');
    
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
    
    const timer = setInterval(() => {}, 1000);
    
    document.addEventListener('click', handleClick);
    
    // EQUIVALENT TO: componentWillUnmount
    return () => {
      console.log('Unmounted');
      clearInterval(timer);
      document.removeEventListener('click', handleClick);
    };
  }, []); // Empty deps = chỉ chạy khi mount/unmount
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: componentDidUpdate (specific value)
  // ══════════════════════════════════════════════════════════
  useEffect(() => {
    // Chạy khi userId thay đổi
    console.log('userId changed:', props.userId);
    fetchUser(props.userId);
  }, [props.userId]); // Dependency: userId
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: componentDidUpdate (every render)
  // ══════════════════════════════════════════════════════════
  useEffect(() => {
    // Chạy SAU mỗi render
    console.log('Component updated');
  }); // No deps = chạy mỗi render
  
  // Track previous value (like prevProps/prevState)
  const prevCount = usePrevious(count);
  useEffect(() => {
    if (prevCount !== count) {
      console.log(`Count changed from ${prevCount} to ${count}`);
    }
  }, [count, prevCount]);
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: shouldComponentUpdate
  // ══════════════════════════════════════════════════════════
  // Dùng React.memo thay vì hook
  // (xem phần React.memo bên dưới)
  
  // ══════════════════════════════════════════════════════════
  // EQUIVALENT TO: getSnapshotBeforeUpdate
  // ══════════════════════════════════════════════════════════
  // Dùng useLayoutEffect (chạy TRƯỚC browser paint)
  useLayoutEffect(() => {
    const snapshot = listRef.current.scrollHeight;
    // Update DOM synchronously
  }, [list]);
  
  // ══════════════════════════════════════════════════════════
  // RENDER
  // ══════════════════════════════════════════════════════════
  return <div>{count}</div>;
}

// Wrap với React.memo cho shouldComponentUpdate behavior
export default React.memo(MyComponent, (prevProps, nextProps) => {
  // Return true = skip re-render
  return prevProps.id === nextProps.id;
});
```

**📊 So sánh Class vs Functional:**

| Class Component | Functional Component |
|----------------|---------------------|
| `constructor` | `useState(() => initialValue)` |
| `componentDidMount` | `useEffect(() => {}, [])` |
| `componentDidUpdate` | `useEffect(() => {}, [deps])` |
| `componentWillUnmount` | `useEffect(() => { return cleanup }, [])` |
| `shouldComponentUpdate` | `React.memo(Component, areEqual)` |
| `getDerivedStateFromProps` | Compute trong render hoặc `useEffect` |
| `getSnapshotBeforeUpdate` | `useLayoutEffect` |
| `componentDidCatch` | Chưa có hook (dùng Error Boundary class) |

---

#### **📚 PHẦN 3: VIRTUAL DOM & PERFORMANCE**

---

##### **3.1. Virtual DOM & Reconciliation**

**🎯 Virtual DOM là gì:**
- JavaScript object đại diện cho Real DOM
- React tạo Virtual DOM tree mỗi khi state/props thay đổi
- So sánh (diffing) old Virtual DOM vs new Virtual DOM
- Chỉ update những thay đổi thực sự lên Real DOM

**📖 Reconciliation Process:**

```typescript
// 1. Initial render
const vdom = { type: 'div', props: { className: 'box' }, children: ['Hello'] };
// → React tạo real DOM: <div class="box">Hello</div>

// 2. State changes
setState({ text: 'World' });

// 3. New Virtual DOM
const newVdom = { type: 'div', props: { className: 'box' }, children: ['World'] };

// 4. Diffing algorithm
// - Same type (div) → keep element, update children
// - Different type → destroy & re-create
// - Update: only text node changes

// 5. Commit phase: Update real DOM
element.textContent = 'World'; // Chỉ update text, không re-create div
```

**💡 Key trong Lists - TẠI SAO QUAN TRỌNG:**

```typescript
// ❌ KHÔNG DÙNG INDEX làm key
{items.map((item, index) => <Item key={index} data={item} />)}
// Problem: Khi thêm/xóa item → index thay đổi → React re-render sai items

// Example: [A, B, C] → Xóa A → [B, C]
// React nghĩ: B có key=0 → giữ nguyên (SAI! B giờ có key=1)
//            C có key=1 → giữ nguyên (SAI! C giờ có key=0)
// → Input values, scroll position, animations BỊ LOẠN

// ✅ DÙNG STABLE UNIQUE ID
{items.map(item => <Item key={item.id} data={item} />)}
// React biết chính xác item nào added/removed/moved
```

**⚠️ Khi nào được dùng index:**
- List KHÔNG bao giờ thay đổi order (static)
- Không có filter/sort
- Items không có unique ID

---

##### **3.2. PureComponent vs React.memo**

**🎯 PureComponent (Class):**

```typescript
// Shallow comparison của props & state
class MyComponent extends React.PureComponent {
  render() {
    return <div>{this.props.name}</div>;
  }
}

// Equivalent to:
class MyComponent extends React.Component {
  shouldComponentUpdate(nextProps, nextState) {
    return !shallowEqual(this.props, nextProps) || 
           !shallowEqual(this.state, nextState);
  }
}

// ⚠️ Chỉ shallow comparison:
// { a: 1 } !== { a: 1 } → re-render (mặc dù giống nhau)
// [1,2,3] !== [1,2,3] → re-render
```

**🎯 React.memo (Functional):**

```typescript
// Default: Shallow comparison của props
const MyComponent = React.memo(({ name, age }) => {
  return <div>{name} - {age}</div>;
});

// Custom comparison
const MyComponent = React.memo(
  ({ user }) => <div>{user.name}</div>,
  (prevProps, nextProps) => {
    return prevProps.user.id === nextProps.user.id; // true = skip render
  }
);

// Combine với useMemo/useCallback
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  // ✅ Stable reference
  const config = useMemo(() => ({ theme: 'dark' }), []);
  const handleClick = useCallback(() => {}, []);
  
  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child config={config} onClick={handleClick} /> {/* Không re-render */}
    </>
  );
}

const Child = React.memo(({ config, onClick }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>{config.theme}</button>;
});
```

---

##### **3.3. state vs props & Parent/Child Re-rendering**

**📖 state vs props:**

```typescript
// STATE: Owned by component, mutable (via setState)
const [count, setCount] = useState(0); // Component controls this

// PROPS: Passed from parent, READ-ONLY
function Child({ count }) { // Cannot modify count
  // count = 10; // ❌ Error!
  return <div>{count}</div>;
}

// Data flow: Parent state → Child props (one-way)
function Parent() {
  const [count, setCount] = useState(0);
  return <Child count={count} />; // Pass state as props
}
```

**📖 Parent re-render → Child re-render?**

```typescript
// ✅ YES: Default behavior
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <Child /> {/* Re-render ngay cả khi không có props! */}
    </>
  );
}

// 🔧 Optimization 1: React.memo
const Child = React.memo(() => {
  console.log('Child rendered');
  return <div>Child</div>;
}); // Không re-render nếu props không đổi

// 🔧 Optimization 2: children prop
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <Layout>
      <Child /> {/* Không re-render! */}
    </Layout>
  );
}

function Layout({ children }) {
  const [theme, setTheme] = useState('light');
  return <div className={theme}>{children}</div>;
  // children là stable reference → không re-create
}

// 🔧 Optimization 3: Component composition
function Parent() {
  const child = useMemo(() => <Child />, []); // Cache element
  return <div>{child}</div>;
}
```

---

#### **📚 PHẦN 4: ADVANCED PATTERNS**

---

##### **4.1. Higher-Order Components (HOC)**

```typescript
// HOC = Function nhận component, return enhanced component
function withLoading(Component) {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) return <div>Loading...</div>;
    return <Component {...props} />;
  };
}

// Usage
const UserListWithLoading = withLoading(UserList);
<UserListWithLoading isLoading={true} users={[]} />

// HOC for authentication
function withAuth(Component) {
  return function AuthComponent(props) {
    const { user } = useAuth();
    if (!user) return <Navigate to="/login" />;
    return <Component {...props} user={user} />;
  };
}
```

---

##### **4.2. Render Props**

```typescript
// Component với function as child
function DataFetcher({ url, render }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch(url).then(res => res.json()).then(data => {
      setData(data);
      setLoading(false);
    });
  }, [url]);
  
  return render({ data, loading });
}

// Usage
<DataFetcher 
  url="/api/users"
  render={({ data, loading }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
/>

// Modern alternative: Custom hooks
function useDataFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { /* fetch logic */ }, [url]);
  return { data, loading };
}

function UserList() {
  const { data, loading } = useDataFetch('/api/users');
  if (loading) return <Spinner />;
  return <ul>{data.map(user => <li key={user.id}>{user.name}</li>)}</ul>;
}
```

---

##### **4.3. Compound Components**

```typescript
// Components hoạt động cùng nhau qua Context
const TabsContext = createContext();

function Tabs({ children, defaultTab }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
}

function TabList({ children }) {
  return <div className="tab-list">{children}</div>;
}

function Tab({ id, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  return (
    <button 
      className={activeTab === id ? 'active' : ''}
      onClick={() => setActiveTab(id)}
    >
      {children}
    </button>
  );
}

function TabPanel({ id, children }) {
  const { activeTab } = useContext(TabsContext);
  return activeTab === id ? <div>{children}</div> : null;
}

// Usage (flexible API)
<Tabs defaultTab="home">
  <TabList>
    <Tab id="home">Home</Tab>
    <Tab id="profile">Profile</Tab>
  </TabList>
  <TabPanel id="home">Home content</TabPanel>
  <TabPanel id="profile">Profile content</TabPanel>
</Tabs>
```

---

#### **📚 PHẦN 5: REACT FEATURES**

---

##### **5.1. React Batching (Automatic in React 18+)**

```typescript
// React 17: Chỉ batch trong event handlers
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  // → 1 re-render (batched)
}

setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // → 2 re-renders (KHÔNG batch)
}, 1000);

// React 18: Automatic batching mọi nơi
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // → 1 re-render (batched tự động)
}, 1000);

// Opt-out batching
import { flushSync } from 'react-dom';

flushSync(() => {
  setCount(c => c + 1);
}); // Render immediately
setFlag(f => !f); // Render again
```

---

##### **5.2. Code Splitting & Lazy Loading**

```typescript
// Route-based splitting
const Home = lazy(() => import('./Home'));
const About = lazy(() => import('./About'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Suspense>
  );
}

// Component-based splitting
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);
  return (
    <>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<div>Loading chart...</div>}>
          <HeavyChart />
        </Suspense>
      )}
    </>
  );
}

// Named exports
const { TabPanel } = lazy(() => 
  import('./Tabs').then(module => ({ default: module.TabPanel }))
);
```

---

##### **5.3. React Portal**

```typescript
// Render children vào DOM node khác (ngoài parent hierarchy)
function Modal({ children, isOpen }) {
  if (!isOpen) return null;
  
  return createPortal(
    <div className="modal-overlay">
      <div className="modal">{children}</div>
    </div>,
    document.getElementById('modal-root') // Target container
  );
}

// index.html
<body>
  <div id="root"></div>
  <div id="modal-root"></div> <!-- Portal target -->
</body>

// Use cases:
// - Modals, Dialogs
// - Tooltips, Popovers
// - Notifications (toast)
```

---

##### **5.4. Error Boundaries**

```typescript
// Chỉ có thể dùng Class Component (chưa có hook)
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, errorInfo) {
    logErrorToService(error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <App />
</ErrorBoundary>

// ⚠️ Error boundaries KHÔNG catch:
// - Event handlers (dùng try/catch)
// - Async code (setTimeout, promises)
// - Server-side rendering
// - Errors trong Error Boundary itself
```

---

#### **📚 PHẦN 6: REACT 18+ FEATURES**

---

##### **6.1. Suspense for Data Fetching**

```typescript
// Suspense-enabled data fetching
const resource = fetchData('/api/users'); // Returns special object

function UserList() {
  const users = resource.read(); // Suspends if not ready
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <UserList /> {/* Suspends while loading */}
    </Suspense>
  );
}

// Libraries hỗ trợ: React Query, SWR, Relay
```

---

##### **6.2. Server Components (React 18+)**

```typescript
// Server Component (.server.jsx)
async function UserProfile({ userId }) {
  const user = await db.users.findById(userId); // Direct DB access!
  return <div>{user.name}</div>;
}

// Client Component (.client.jsx)
'use client';
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Benefits:
// - Zero bundle size (server components không ship JS)
// - Direct backend access (DB, filesystem)
// - Automatic code splitting
```

---

##### **6.3. Concurrent Rendering - useTransition & useDeferredValue**

```typescript
// useTransition: Mark updates as non-urgent
function SearchBox() {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();
  
  const handleChange = (e) => {
    setQuery(e.target.value); // Urgent: update input
    
    startTransition(() => {
      setSearchResults(e.target.value); // Non-urgent: can interrupt
    });
  };
  
  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending && <Spinner />}
      <Results />
    </>
  );
}

// useDeferredValue: Defer value updates
function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text); // Lags behind
  
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredText} /> {/* Uses old value while busy */}
    </>
  );
}
```

---

##### **6.4. Hydration (SSR/Next.js)**

```typescript
// Server-side: Generate HTML
const html = renderToString(<App />);
// Send HTML to client → User sees content immediately

// Client-side: Hydrate (attach event listeners)
hydrateRoot(document.getElementById('root'), <App />);

// React 18: Selective Hydration
<Suspense fallback={<Spinner />}>
  <Comments /> {/* Hydrate sau khi ready */}
</Suspense>
// User có thể interact với page khác ngay lập tức
```

---

#### **📚 PHẦN 7: ROUTING & MISC**

---

##### **7.1. React Router**

```typescript
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/users/123">User 123</Link>
      </nav>
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/users/:id" element={<User />} />
        <Route path="*" element={<NotFound />} /> {/* 404 */}
      </Routes>
    </BrowserRouter>
  );
}

function User() {
  const { id } = useParams(); // Get URL params
  const navigate = useNavigate(); // Programmatic navigation
  
  return (
    <>
      <h1>User {id}</h1>
      <button onClick={() => navigate('/about')}>Go to About</button>
    </>
  );
}
```

---

##### **7.2. Fragments**

```typescript
// Avoid extra DOM nodes
function List() {
  return (
    <>
      <li>Item 1</li>
      <li>Item 2</li>
    </> // No wrapper div in DOM
  );
}

// With key (trong loops)
{items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.description}</dd>
  </React.Fragment>
))}
```

---

##### **7.3. startTransition (React 18)**

```typescript
import { startTransition } from 'react';

// Mark state updates as non-urgent
function TabContainer() {
  const [tab, setTab] = useState('home');
  
  function selectTab(nextTab) {
    startTransition(() => {
      setTab(nextTab); // Low priority
    });
  }
  
  // Input stays responsive even if TabPanel render is slow
}
```

---

##### **7.4. React.lazy & Suspense Integration**

```typescript
const OtherComponent = lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <OtherComponent />
    </Suspense>
  );
}

// Multiple lazy components
<Suspense fallback={<Spinner />}>
  <ComponentA />
  <ComponentB />
</Suspense>
// Waits for BOTH before showing (avoid cascading spinners)
```

---

## **🚀 PHẦN 8: REACT PERFORMANCE & RENDERING DEEP DIVE**

### **8.1. React Rendering Phases - Render vs Commit**

```typescript
// ===================================================
// 🎯 REACT RENDERING PROCESS
// ===================================================

/**
 * React rendering có 2 PHASE:
 * 
 * 1️⃣ RENDER PHASE (Pure, có thể pause/abort)
 *    - Gọi component functions/render methods
 *    - So sánh Virtual DOM cũ vs mới (Reconciliation)
 *    - Tính toán những gì cần thay đổi
 *    - ⚠️ Có thể bị interrupt/restart (Concurrent Mode)
 * 
 * 2️⃣ COMMIT PHASE (Synchronous, không thể interrupt)
 *    - Apply changes vào DOM
 *    - Run useLayoutEffect
 *    - Run useEffect (sau khi paint)
 *    - Browser paint screen
 */

// 📊 Timeline:
/*
┌─────────────────────────────────────────────────────────────────┐
│  REACT RENDERING TIMELINE                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  setState() called                                              │
│       ↓                                                         │
│  ┌─────────────────────────────┐                              │
│  │  RENDER PHASE (Interruptible)│                              │
│  ├─────────────────────────────┤                              │
│  │  1. Call Component()         │                              │
│  │  2. Create new VirtualDOM    │                              │
│  │  3. Diff with old VirtualDOM │                              │
│  │  4. Mark changes             │                              │
│  └─────────────────────────────┘                              │
│       ↓                                                         │
│  ┌─────────────────────────────┐                              │
│  │  COMMIT PHASE (Synchronous)  │                              │
│  ├─────────────────────────────┤                              │
│  │  1. Apply DOM changes        │                              │
│  │  2. useLayoutEffect cleanup  │                              │
│  │  3. useLayoutEffect effect   │                              │
│  │  4. Browser Paint            │ ← User sees changes          │
│  │  5. useEffect cleanup        │                              │
│  │  6. useEffect effect         │                              │
│  └─────────────────────────────┘                              │
└─────────────────────────────────────────────────────────────────┘
*/

// ✅ Example: Measure DOM before paint
function MeasureBeforePaint() {
  const ref = useRef<HTMLDivElement>(null);
  
  useLayoutEffect(() => {
    // ✅ Runs BEFORE browser paint
    // DOM updated but not visible yet
    const height = ref.current?.offsetHeight;
    console.log('Height before paint:', height);
  }, []);
  
  useEffect(() => {
    // ✅ Runs AFTER browser paint
    // User already sees the update
    console.log('After paint');
  }, []);
  
  return <div ref={ref}>Content</div>;
}
```

---

### **8.2. React Fiber Architecture (Advanced)**

```typescript
// ===================================================
// 🧬 REACT FIBER - Reconciliation Engine
// ===================================================

/**
 * 🎯 Fiber là gì?
 * 
 * Fiber = JavaScript object đại diện cho một React element
 * 
 * Mỗi component instance có một Fiber node, chứa:
 * - type: Component type (function/class/div)
 * - props: Props hiện tại
 * - state: State hiện tại
 * - hooks: Linked list of hooks (useState, useEffect...)
 * - child, sibling, return: Pointers tạo thành Fiber tree
 * - alternate: Pointer tới Fiber version trước (double buffering)
 * - effectTag: Thay đổi cần apply (Placement, Update, Deletion)
 */

// 📊 Fiber Tree Structure:
/*
        App (Fiber)
        /    \
    Header  Content (Fiber)
              /    \
          Sidebar  Main (Fiber)
          
Mỗi node là một Fiber object:
{
  type: 'div',
  props: { className: 'container' },
  state: null,
  hooks: null, // Linked list nếu là function component
  child: <pointer to first child>,
  sibling: <pointer to next sibling>,
  return: <pointer to parent>,
  alternate: <pointer to previous version>,
  effectTag: 'Update',
  memoizedState: { ... } // Cached state
}
*/

// ===================================================
// ⚡ CONCURRENT RENDERING (React 18+)
// ===================================================

/**
 * Concurrent Rendering cho phép React:
 * - Pause rendering để handle urgent updates
 * - Resume rendering sau
 * - Abandon rendering nếu không cần nữa
 * 
 * Priority levels:
 * 1. Immediate (clicks, input)
 * 2. User-blocking (hover)
 * 3. Normal (data fetching)
 * 4. Low (analytics)
 * 5. Idle (offscreen prep)
 */

function SearchWithPriority() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const deferredQuery = useDeferredValue(query);
  
  // User input: HIGH PRIORITY (immediate)
  const handleChange = (e) => {
    setQuery(e.target.value); // Instant UI update
  };
  
  // Search results: LOW PRIORITY (can be deferred)
  useEffect(() => {
    // This update can be interrupted
    const filtered = expensiveSearch(deferredQuery);
    setResults(filtered);
  }, [deferredQuery]);
  
  return (
    <div>
      {/* Input always responsive */}
      <input value={query} onChange={handleChange} />
      
      {/* Results can lag behind */}
      <ResultsList results={results} />
    </div>
  );
}
```

---

### **8.3. React.memo Deep Dive - Memoization Pattern**

```typescript
// ===================================================
// 🎯 REACT.MEMO - Component Memoization
// ===================================================

// ❌ Without memo: Re-renders on every parent render
const ExpensiveComponent = ({ data }) => {
  console.log('Rendering ExpensiveComponent');
  return <div>{heavyComputation(data)}</div>;
};

function Parent() {
  const [count, setCount] = useState(0);
  const data = { value: 100 }; // New object every render!
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      {/* ❌ Re-renders even though data.value is same */}
      <ExpensiveComponent data={data} />
    </div>
  );
}

// ✅ With memo: Skip re-render if props unchanged
const MemoizedComponent = memo(({ data }) => {
  console.log('Rendering MemoizedComponent');
  return <div>{heavyComputation(data)}</div>;
});

function ParentOptimized() {
  const [count, setCount] = useState(0);
  
  // ✅ Stable reference with useMemo
  const data = useMemo(() => ({ value: 100 }), []);
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      {/* ✅ No re-render! data reference is stable */}
      <MemoizedComponent data={data} />
    </div>
  );
}

// ===================================================
// 🔍 CUSTOM COMPARISON FUNCTION
// ===================================================

interface Props {
  user: { id: string; name: string; age: number };
}

// Only re-render if user.id changes (ignore name/age)
const UserCard = memo(
  ({ user }: Props) => {
    console.log('Rendering UserCard');
    return <div>{user.name}</div>;
  },
  (prevProps, nextProps) => {
    // Return TRUE to SKIP re-render
    // Return FALSE to RE-RENDER
    return prevProps.user.id === nextProps.user.id;
  }
);

// ===================================================
// ⚠️ COMMON MISTAKES với React.memo
// ===================================================

// ❌ MISTAKE 1: Inline object props
function Bad() {
  return <MemoizedComponent data={{ value: 100 }} />; // New object every time!
}

// ✅ FIX: Extract to stable reference
const DATA = { value: 100 }; // Outside component or useMemo
function Good() {
  return <MemoizedComponent data={DATA} />;
}

// ❌ MISTAKE 2: Inline function props
function Bad2() {
  return <MemoizedComponent onClick={() => console.log('click')} />; // New function!
}

// ✅ FIX: useCallback
function Good2() {
  const handleClick = useCallback(() => console.log('click'), []);
  return <MemoizedComponent onClick={handleClick} />;
}

// ❌ MISTAKE 3: Children prop
function Bad3() {
  return (
    <MemoizedComponent>
      <div>Child</div> {/* New element every render */}
    </MemoizedComponent>
  );
}

// ✅ FIX: Extract children or use composition
const CHILD = <div>Child</div>;
function Good3() {
  return <MemoizedComponent>{CHILD}</MemoizedComponent>;
}
```

---

### **8.4. useMemo vs useCallback - When & Why**

```typescript
// ===================================================
// 🎯 USEMEMO - Memoize VALUES
// ===================================================

function ProductList({ products }) {
  // ❌ Without useMemo: Recalculate every render
  const expensiveTotal = products.reduce((sum, p) => sum + p.price, 0);
  
  // ✅ With useMemo: Only recalculate when products change
  const total = useMemo(
    () => products.reduce((sum, p) => sum + p.price, 0),
    [products]
  );
  
  return <div>Total: {total}</div>;
}

// ===================================================
// 🎯 USECALLBACK - Memoize FUNCTIONS
// ===================================================

function Parent() {
  const [count, setCount] = useState(0);
  
  // ❌ New function every render → Child re-renders
  const handleClick = () => {
    console.log('Clicked');
  };
  
  // ✅ Stable function reference → Child doesn't re-render
  const handleClickMemo = useCallback(() => {
    console.log('Clicked');
  }, []); // Empty deps = never recreate
  
  return <MemoizedChild onClick={handleClickMemo} />;
}

// ===================================================
// 📊 PERFORMANCE COMPARISON
// ===================================================

// Benchmark: When to use useMemo/useCallback?
function BenchmarkExample() {
  const [filter, setFilter] = useState('');
  const items = Array.from({ length: 10000 }, (_, i) => ({
    id: i,
    name: `Item ${i}`,
  }));
  
  // ⚠️ useMemo NOT needed: Simple calculation
  const count = items.length; // Fast, no need to memoize
  
  // ✅ useMemo needed: Expensive calculation
  const filtered = useMemo(
    () => items.filter((item) => item.name.includes(filter)),
    [items, filter]
  );
  
  // ✅ useCallback needed: Passed to memoized child
  const handleSelect = useCallback((id: number) => {
    console.log('Selected:', id);
  }, []);
  
  return (
    <div>
      <input value={filter} onChange={(e) => setFilter(e.target.value)} />
      <ItemList items={filtered} onSelect={handleSelect} />
    </div>
  );
}

// ===================================================
// ⚠️ OVER-OPTIMIZATION TRAP
// ===================================================

// ❌ DON'T do this: useMemo for everything
function OverOptimized() {
  const a = useMemo(() => 1 + 2, []); // Silly!
  const b = useMemo(() => 'Hello', []); // Waste of memory
  return <div>{a} {b}</div>;
}

// ✅ DO this: Only memoize when needed
function WellOptimized() {
  const a = 1 + 2; // Fast, no memo needed
  const b = 'Hello'; // Primitive, no memo needed
  
  // Only memo expensive computations or for stable refs
  const expensive = useMemo(() => heavyComputation(), []);
  
  return <div>{a} {b} {expensive}</div>;
}

/**
 * 🎯 RULES OF THUMB:
 * 
 * Use useMemo when:
 * ✅ Expensive computation (>5ms)
 * ✅ Creating objects/arrays passed to memoized children
 * ✅ Derived data from large arrays/objects
 * 
 * Use useCallback when:
 * ✅ Passing callbacks to memoized children
 * ✅ Function is a dependency of useEffect/useMemo
 * ✅ Function used in event handlers of optimized components
 * 
 * DON'T use when:
 * ❌ Simple calculations (<1ms)
 * ❌ Component already re-renders anyway
 * ❌ Just to "feel" optimized
 */
```

---

### **8.5. Profiler API & Performance Debugging**

```typescript
// ===================================================
// 📊 PROFILER API - Measure Render Performance
// ===================================================

import { Profiler, ProfilerOnRenderCallback } from 'react';

const onRenderCallback: ProfilerOnRenderCallback = (
  id, // Profiler id
  phase, // "mount" or "update"
  actualDuration, // Time spent rendering
  baseDuration, // Estimated time without memoization
  startTime, // When React began rendering
  commitTime, // When React committed update
  interactions // Set of interactions (deprecated)
) => {
  console.log(`${id} (${phase})`);
  console.log(`Actual: ${actualDuration.toFixed(2)}ms`);
  console.log(`Base: ${baseDuration.toFixed(2)}ms`);
  
  // Send to analytics
  if (actualDuration > 16) { // Slower than 60fps
    analytics.track('slow_render', {
      component: id,
      duration: actualDuration,
    });
  }
};

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <Header />
      <Profiler id="Content" onRender={onRenderCallback}>
        <Content />
      </Profiler>
    </Profiler>
  );
}

// ===================================================
// 🔍 WHY-DID-YOU-RENDER (Debug Re-renders)
// ===================================================

// Install: npm install @welldone-software/why-did-you-render
import whyDidYouRender from '@welldone-software/why-did-you-render';

if (process.env.NODE_ENV === 'development') {
  whyDidYouRender(React, {
    trackAllPureComponents: true,
    logOnDifferentValues: true,
  });
}

// Mark components to track
const MyComponent = ({ data }) => {
  return <div>{data.value}</div>;
};
MyComponent.whyDidYouRender = true;

// Console output khi re-render không cần thiết:
// MyComponent re-rendered because:
// - data.value changed from 100 to 100 (same value!)
// - data is different object reference

// ===================================================
// ⚡ CHROME DEVTOOLS - React Profiler
// ===================================================

/**
 * Chrome DevTools → Profiler tab
 * 
 * 1. Record rendering
 * 2. Interact with app
 * 3. Stop recording
 * 4. Analyze:
 *    - Flame graph: Which components rendered
 *    - Ranked: Slowest components
 *    - Component tree: Why component rendered
 *    
 * Look for:
 * - ⚠️ Yellow bars: Slow renders (>12ms)
 * - 🔴 Red bars: Very slow (>16ms, drops frames)
 * - Gray: Didn't render (optimized!)
 */
```

---

### **8.6. Bundle Splitting & Code Splitting Strategies**

```typescript
// ===================================================
// 📦 CODE SPLITTING - Lazy Load Components
// ===================================================

import { lazy, Suspense } from 'react';

// ✅ Route-based splitting
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Profile = lazy(() => import('./pages/Profile'));
const Settings = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<PageLoader />}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

// ===================================================
// 📦 COMPONENT-BASED SPLITTING
// ===================================================

// Heavy chart library loaded only when needed
const Chart = lazy(() => import('./components/Chart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <Chart data={data} />
        </Suspense>
      )}
    </div>
  );
}

// ===================================================
// 📦 VENDOR SPLITTING (Webpack)
// ===================================================

// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      cacheGroups: {
        // Vendor bundle: node_modules
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        // Common bundle: shared code
        common: {
          minChunks: 2,
          name: 'common',
          chunks: 'async',
        },
      },
    },
  },
};

// Results in:
// - main.js (your code)
// - vendors.js (React, lodash, etc)
// - common.js (shared components)
// - [route].js (lazy-loaded pages)
```

---

#### **🎯 TÓM TẮT Q25 - REACT COMPREHENSIVE**

**✅ Đã cover:**
1. **All Hooks**: useState, useEffect, useRef, useLayoutEffect, useReducer, useContext, useMemo, useCallback, useImperativeHandle, useSyncExternalStore
2. **Lifecycle**: Class component lifecycle đầy đủ + mapping sang Functional
3. **Virtual DOM**: Reconciliation, key trong lists, tại sao không dùng index
4. **Performance**: PureComponent, React.memo, state vs props, parent/child re-render optimization
5. **Advanced Patterns**: HOC, Render Props, Compound Components
6. **React Features**: Batching, Code Splitting, Portal, Error Boundaries, Fragments
7. **React 18+**: Suspense, Server Components, Concurrent Rendering, useTransition, useDeferredValue, Hydration
8. **Routing**: React Router basics
9. **🆕 Rendering Deep Dive**: Render vs Commit phases, Fiber architecture, Concurrent rendering
10. **🆕 Performance Optimization**: React.memo deep dive, useMemo/useCallback best practices, Profiler API, why-did-you-render
11. **🆕 Bundle Splitting**: Code splitting strategies, lazy loading, vendor splitting

**💡 Key Takeaways cho Interview:**
- Hiểu sâu useEffect cleanup function và dependency array
- Biết khi nào dùng useMemo/useCallback (không over-optimize)
- Virtual DOM diffing algorithm và tầm quan trọng của key
- React.memo + stable references (useMemo/useCallback) để tối ưu re-renders
- React 18 concurrent features (useTransition, useDeferredValue)
- Error Boundaries chỉ catch rendering errors, không catch event handlers/async
- **🆕 Render phase có thể interrupt, Commit phase synchronous**
- **🆕 Fiber = JavaScript object representing React element**
- **🆕 Only memoize expensive computations (>5ms) or for stable refs**
- **🆕 Use Profiler API & Chrome DevTools to find bottlenecks**

---

#### **📚 PHẦN 9: REACT DESIGN PATTERNS - ADVANCED COMPONENT ARCHITECTURE**

---

## **📊 REACT PATTERNS OVERVIEW**

```
┌──────────────────────────────────────────────────────────────┐
│          REACT DESIGN PATTERNS (Component Architecture)      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  🧩 COMPONENT COMPOSITION PATTERNS                           │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Compound Components                                 │ │
│  │    Shared state giữa parent-children (như HTML <select>)│ │
│  │    VD: <Tabs>, <Accordion>, <Dropdown>               │ │
│  │                                                       │ │
│  │  • Render Props                                       │ │
│  │    Pass function as prop để render UI động            │ │
│  │    VD: <DataProvider render={(data) => ...} />        │ │
│  │                                                       │ │
│  │  • Children as Function (Render Props variant)        │ │
│  │    {(data) => <div>{data}</div>}                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  🎨 LOGIC REUSE PATTERNS                                     │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Higher-Order Components (HOC)                      │ │
│  │    Wrap component để add behavior                     │ │
│  │    VD: withAuth(Component), withRouter(Component)     │ │
│  │                                                       │ │
│  │  • Custom Hooks (Modern Replacement for HOC)          │ │
│  │    useAuth(), useRouter() - Recommended approach      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  🏗️ ARCHITECTURAL PATTERNS                                   │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Container/Presentational (Smart/Dumb)              │ │
│  │    Container = logic, Presentational = UI             │ │
│  │                                                       │ │
│  │  • Controlled vs Uncontrolled Components              │ │
│  │    Controlled = React state, Uncontrolled = DOM state │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

##### **9.1. COMPOUND COMPONENTS PATTERN**

**🎯 Mục đích:**
Tạo components phức tạp với shared state giữa parent-children, API linh hoạt cho user.

**📖 Use Cases:**
- Complex UI components: Tabs, Accordion, Dropdown, Menu
- Flexible structure (user controls layout)
- Implicit communication (như HTML `<select>` + `<option>`)

**💡 Chi tiết kỹ thuật:**

```typescript
// ===================================================
// 🧩 COMPOUND COMPONENTS - Shared State via Context
// ===================================================

import { createContext, useContext, useState, ReactNode } from 'react';

// Context for shared state
type TabsContextType = {
  activeTab: string;
  setActiveTab: (tab: string) => void;
};

const TabsContext = createContext<TabsContextType | undefined>(undefined);

function useTabs() {
  const context = useContext(TabsContext);
  if (!context) {
    throw new Error('Tabs compound components must be used within <Tabs>');
  }
  return context;
}

// ===================================================
// Parent Component (Provides Context)
// ===================================================

type TabsProps = {
  defaultTab?: string;
  children: ReactNode;
};

function Tabs({ defaultTab, children }: TabsProps) {
  const [activeTab, setActiveTab] = useState(defaultTab || '');

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
}

// ===================================================
// Child Components (Consume Context)
// ===================================================

type TabListProps = {
  children: ReactNode;
};

function TabList({ children }: TabListProps) {
  return <div className="tab-list" role="tablist">{children}</div>;
}

type TabProps = {
  value: string;
  children: ReactNode;
};

function Tab({ value, children }: TabProps) {
  const { activeTab, setActiveTab } = useTabs();
  const isActive = activeTab === value;

  return (
    <button
      role="tab"
      aria-selected={isActive}
      className={`tab ${isActive ? 'active' : ''}`}
      onClick={() => setActiveTab(value)}
    >
      {children}
    </button>
  );
}

type TabPanelsProps = {
  children: ReactNode;
};

function TabPanels({ children }: TabPanelsProps) {
  return <div className="tab-panels">{children}</div>;
}

type TabPanelProps = {
  value: string;
  children: ReactNode;
};

function TabPanel({ value, children }: TabPanelProps) {
  const { activeTab } = useTabs();

  if (activeTab !== value) return null;

  return (
    <div role="tabpanel" className="tab-panel">
      {children}
    </div>
  );
}

// ===================================================
// Attach Sub-components to Parent (Compound Pattern)
// ===================================================

Tabs.List = TabList;
Tabs.Tab = Tab;
Tabs.Panels = TabPanels;
Tabs.Panel = TabPanel;

// ===================================================
// USAGE: Flexible, Declarative API
// ===================================================

function App() {
  return (
    <Tabs defaultTab="profile">
      <Tabs.List>
        <Tabs.Tab value="profile">Profile</Tabs.Tab>
        <Tabs.Tab value="settings">Settings</Tabs.Tab>
        <Tabs.Tab value="notifications">Notifications</Tabs.Tab>
      </Tabs.List>

      <Tabs.Panels>
        <Tabs.Panel value="profile">
          <h2>Profile Content</h2>
          <p>User profile information...</p>
        </Tabs.Panel>

        <Tabs.Panel value="settings">
          <h2>Settings Content</h2>
          <p>Application settings...</p>
        </Tabs.Panel>

        <Tabs.Panel value="notifications">
          <h2>Notifications Content</h2>
          <p>Notification preferences...</p>
        </Tabs.Panel>
      </Tabs.Panels>
    </Tabs>
  );
}

/**
 * ✅ Advantages:
 * - Flexible structure (user controls layout)
 * - Implicit state sharing (no prop drilling)
 * - Semantic API (reads like HTML)
 * - Extensible (easy to add new sub-components)
 * 
 * ❌ Disadvantages:
 * - Only works with direct children (or Context)
 * - More boilerplate (multiple components)
 * - Harder to enforce structure
 */
```

---

##### **9.2. RENDER PROPS PATTERN**

**🎯 Mục đích:**
Share logic giữa components mà vẫn giữ UI flexibility (function as prop).

**📖 Use Cases:**
- Data fetching components
- Mouse tracking, scroll position
- Animation controllers

**💡 Chi tiết kỹ thuật:**

```typescript
// ===================================================
// 🎨 RENDER PROPS - Function as Child
// ===================================================

// ===================================================
// EXAMPLE 1: Mouse Tracker
// ===================================================

type MousePosition = { x: number; y: number };

type MouseTrackerProps = {
  render: (position: MousePosition) => ReactNode;
};

function MouseTracker({ render }: MouseTrackerProps) {
  const [position, setPosition] = useState<MousePosition>({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (event: MouseEvent) => {
      setPosition({ x: event.clientX, y: event.clientY });
    };

    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return <>{render(position)}</>;
}

// Usage: Different UI based on same logic
function App() {
  return (
    <div>
      {/* Render as coordinates */}
      <MouseTracker
        render={({ x, y }) => (
          <p>Mouse position: ({x}, {y})</p>
        )}
      />

      {/* Render as dot following cursor */}
      <MouseTracker
        render={({ x, y }) => (
          <div
            style={{
              position: 'fixed',
              left: x,
              top: y,
              width: 20,
              height: 20,
              borderRadius: '50%',
              background: 'red',
              pointerEvents: 'none'
            }}
          />
        )}
      />
    </div>
  );
}

// ===================================================
// EXAMPLE 2: Data Fetcher (Children as Function)
// ===================================================

type DataFetcherProps<T> = {
  url: string;
  children: (data: {
    data: T | null;
    loading: boolean;
    error: Error | null;
  }) => ReactNode;
};

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    setLoading(true);

    fetch(url)
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, [url]);

  return <>{children({ data, loading, error })}</>;
}

// Usage
function UserProfile() {
  return (
    <DataFetcher<User> url="/api/users/123">
      {({ data, loading, error }) => {
        if (loading) return <div>Loading...</div>;
        if (error) return <div>Error: {error.message}</div>;
        if (!data) return <div>No data</div>;

        return (
          <div>
            <h1>{data.name}</h1>
            <p>{data.email}</p>
          </div>
        );
      }}
    </DataFetcher>
  );
}

/**
 * ✅ Advantages:
 * - Maximum flexibility (UI completely controlled by consumer)
 * - Logic reuse without UI assumptions
 * - Type-safe with TypeScript generics
 * 
 * ❌ Disadvantages:
 * - Callback hell (nested render props)
 * - Verbose syntax
 * - Harder to read
 * 
 * 💡 Modern Alternative: Custom Hooks (recommended)
 */

// ===================================================
// MODERN: Custom Hook (Replaces Render Props)
// ===================================================

function useMousePosition() {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (event: MouseEvent) => {
      setPosition({ x: event.clientX, y: event.clientY });
    };

    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return position;
}

// Usage (much cleaner!)
function App() {
  const { x, y } = useMousePosition();

  return <p>Mouse: ({x}, {y})</p>;
}
```

---

##### **9.3. HIGHER-ORDER COMPONENTS (HOC)**

**🎯 Mục đích:**
Wrap component để add behavior (authentication, logging, analytics).

**📖 Pattern:**
```typescript
// HOC = Function that takes a component and returns a new component
type HOC = <P>(Component: ComponentType<P>) => ComponentType<P>;

// ⚠️ Mostly replaced by Custom Hooks (React 16.8+)
```

**💡 Chi tiết kỹ thuật:**

```typescript
// ===================================================
// 🎁 HIGHER-ORDER COMPONENT - Wrap Component
// ===================================================

import { ComponentType } from 'react';

// ===================================================
// EXAMPLE 1: withAuth (Authentication HOC)
// ===================================================

type WithAuthProps = {
  user: { name: string; role: string } | null;
};

function withAuth<P extends object>(
  Component: ComponentType<P & WithAuthProps>
): ComponentType<P> {
  return function AuthenticatedComponent(props: P) {
    const [user, setUser] = useState<{ name: string; role: string } | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      // Check authentication
      fetch('/api/auth/me')
        .then((res) => res.json())
        .then((data) => {
          setUser(data);
          setLoading(false);
        })
        .catch(() => {
          setUser(null);
          setLoading(false);
        });
    }, []);

    if (loading) {
      return <div>Loading...</div>;
    }

    if (!user) {
      return <div>Please log in</div>;
    }

    // Pass user prop to wrapped component
    return <Component {...props} user={user} />;
  };
}

// Usage
type DashboardProps = WithAuthProps & {
  title: string;
};

function Dashboard({ user, title }: DashboardProps) {
  return (
    <div>
      <h1>{title}</h1>
      <p>Welcome, {user.name}!</p>
    </div>
  );
}

// Wrap component with HOC
const AuthenticatedDashboard = withAuth(Dashboard);

// Use wrapped component
<AuthenticatedDashboard title="My Dashboard" />;

// ===================================================
// EXAMPLE 2: withLoading (Loading State HOC)
// ===================================================

type WithLoadingProps = {
  loading: boolean;
};

function withLoading<P extends WithLoadingProps>(
  Component: ComponentType<P>
): ComponentType<P> {
  return function LoadingComponent(props: P) {
    if (props.loading) {
      return <div className="spinner">Loading...</div>;
    }

    return <Component {...props} />;
  };
}

// Usage
type UserListProps = WithLoadingProps & {
  users: User[];
};

function UserList({ users }: UserListProps) {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

const UserListWithLoading = withLoading(UserList);

// Use with loading prop
<UserListWithLoading loading={isLoading} users={users} />;

/**
 * ✅ Advantages:
 * - Reuse component logic (authentication, logging, etc.)
 * - Separation of concerns (logic vs presentation)
 * - Composable (wrap multiple HOCs)
 * 
 * ❌ Disadvantages:
 * - Wrapper hell (nested HOCs)
 * - Props collision (HOC props vs component props)
 * - Ref forwarding issues (need forwardRef)
 * - Hard to debug (many wrapper components)
 * 
 * 💡 Modern Alternative: Custom Hooks (cleaner, no wrappers)
 */

// ===================================================
// MODERN: Custom Hook (Replaces HOC)
// ===================================================

function useAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/auth/me')
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch(() => {
        setUser(null);
        setLoading(false);
      });
  }, []);

  return { user, loading };
}

// Usage (no wrapper needed!)
function Dashboard() {
  const { user, loading } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>Please log in</div>;

  return <div>Welcome, {user.name}!</div>;
}
```

---

##### **9.4. CONTAINER/PRESENTATIONAL PATTERN**

**🎯 Mục đích:**
Separate logic (Container/Smart) from UI (Presentational/Dumb).

**📖 Separation of Concerns:**
- **Container (Smart)**: Logic, state, data fetching, event handlers
- **Presentational (Dumb)**: UI only, props in → JSX out

**💡 Chi tiết kỹ thuật:**

```typescript
// ===================================================
// 🏗️ CONTAINER/PRESENTATIONAL (Smart/Dumb Components)
// ===================================================

// ===================================================
// PRESENTATIONAL COMPONENT (Dumb - UI Only)
// ===================================================

type UserCardProps = {
  name: string;
  email: string;
  avatar: string;
  onEdit: () => void;
  onDelete: () => void;
};

function UserCard({ name, email, avatar, onEdit, onDelete }: UserCardProps) {
  // ✅ No logic, no state, no side effects
  // Just props → UI
  return (
    <div className="user-card">
      <img src={avatar} alt={name} />
      <h3>{name}</h3>
      <p>{email}</p>
      <button onClick={onEdit}>Edit</button>
      <button onClick={onDelete}>Delete</button>
    </div>
  );
}

// ===================================================
// CONTAINER COMPONENT (Smart - Logic + State)
// ===================================================

function UserCardContainer({ userId }: { userId: string }) {
  // ✅ All logic here: state, data fetching, handlers
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      });
  }, [userId]);

  const handleEdit = () => {
    console.log('Edit user:', userId);
    // Navigate to edit page or open modal
  };

  const handleDelete = async () => {
    if (confirm('Delete user?')) {
      await fetch(`/api/users/${userId}`, { method: 'DELETE' });
      setUser(null);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>User not found</div>;

  // ✅ Pass data + handlers to presentational component
  return (
    <UserCard
      name={user.name}
      email={user.email}
      avatar={user.avatar}
      onEdit={handleEdit}
      onDelete={handleDelete}
    />
  );
}

/**
 * ✅ Advantages:
 * - Testability:
 *   - Container: Test logic (mocks, integration tests)
 *   - Presentational: Test UI (Storybook, snapshot tests)
 * - Reusability:
 *   - Presentational component can be used with different containers
 * - Clarity:
 *   - Clear separation (logic vs presentation)
 * 
 * ❌ Disadvantages:
 * - More files (2 files instead of 1)
 * - Boilerplate (passing props down)
 * - Over-engineering for simple components
 * 
 * 💡 Modern Approach: Custom Hooks + Component
 */

// ===================================================
// MODERN: Custom Hook + Component (Simpler)
// ===================================================

// Hook (replaces Container logic)
function useUser(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      });
  }, [userId]);

  const handleEdit = () => {
    console.log('Edit user:', userId);
  };

  const handleDelete = async () => {
    if (confirm('Delete user?')) {
      await fetch(`/api/users/${userId}`, { method: 'DELETE' });
      setUser(null);
    }
  };

  return { user, loading, handleEdit, handleDelete };
}

// Component (presentational + hook)
function UserCard({ userId }: { userId: string }) {
  const { user, loading, handleEdit, handleDelete } = useUser(userId);

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div className="user-card">
      <img src={user.avatar} alt={user.name} />
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button onClick={handleEdit}>Edit</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}

// ✅ Benefits: Same separation, fewer files, easier to follow
```

---

##### **9.5. CONTROLLED VS UNCONTROLLED COMPONENTS**

**🎯 Mục đích:**
Hiểu sự khác biệt giữa React-controlled state vs DOM-controlled state.

**📖 So sánh:**

| Aspect | **Controlled** | **Uncontrolled** |
|--------|---------------|------------------|
| **State location** | React state | DOM |
| **Value prop** | `value={state}` | No value prop |
| **Access value** | `state` variable | `ref.current.value` |
| **Re-renders** | Every keystroke | No re-renders |
| **Validation** | Real-time | On submit |
| **Use case** | Forms with validation | Simple forms, file inputs |

**💡 Chi tiết kỹ thuật:**

```typescript
// ===================================================
// 🎛️ CONTROLLED vs UNCONTROLLED COMPONENTS
// ===================================================

// ===================================================
// UNCONTROLLED INPUT (DOM State)
// ===================================================

function UncontrolledForm() {
  const nameRef = useRef<HTMLInputElement>(null);
  const emailRef = useRef<HTMLInputElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // ✅ Read value from DOM (not React state)
    const name = nameRef.current?.value;
    const email = emailRef.current?.value;

    console.log({ name, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* ❌ No value prop, no onChange - DOM controls state */}
      <input ref={nameRef} type="text" placeholder="Name" />
      <input ref={emailRef} type="email" placeholder="Email" />
      <button type="submit">Submit</button>
    </form>
  );
}

/**
 * ✅ Good for:
 * - Simple forms (no validation needed)
 * - File inputs (<input type="file"> - always uncontrolled)
 * - Performance (no re-renders on every keystroke)
 * 
 * ❌ Bad for:
 * - Real-time validation
 * - Conditional rendering based on input
 * - Formatting (e.g., phone numbers)
 */

// ===================================================
// CONTROLLED INPUT (React State)
// ===================================================

function ControlledForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [errors, setErrors] = useState<{ name?: string; email?: string }>({});

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setName(value);

    // ✅ Real-time validation
    if (value.length < 3) {
      setErrors((prev) => ({ ...prev, name: 'Name must be at least 3 characters' }));
    } else {
      setErrors((prev) => ({ ...prev, name: undefined }));
    }
  };

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setEmail(value);

    // ✅ Real-time validation
    if (!validateEmail(value)) {
      setErrors((prev) => ({ ...prev, email: 'Invalid email' }));
    } else {
      setErrors((prev) => ({ ...prev, email: undefined }));
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (Object.keys(errors).length === 0) {
      console.log({ name, email });
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* ✅ value + onChange - React controls state */}
      <div>
        <input
          type="text"
          value={name}
          onChange={handleNameChange}
          placeholder="Name"
        />
        {errors.name && <span className="error">{errors.name}</span>}
      </div>

      <div>
        <input
          type="email"
          value={email}
          onChange={handleEmailChange}
          placeholder="Email"
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>

      <button type="submit" disabled={Object.keys(errors).length > 0}>
        Submit
      </button>
    </form>
  );
}

/**
 * ✅ Good for:
 * - Real-time validation
 * - Formatting (phone numbers, credit cards)
 * - Conditional UI (show/hide based on input)
 * - Multi-step forms (preserve state between steps)
 * 
 * ❌ Bad for:
 * - Large forms (many re-renders)
 * - File inputs (use uncontrolled)
 */

// ===================================================
// HYBRID APPROACH (Best of Both Worlds)
// ===================================================

import { useForm } from 'react-hook-form';

function HybridForm() {
  // ✅ react-hook-form: Uncontrolled internally, controlled API
  const { register, handleSubmit, formState: { errors } } = useForm();

  const onSubmit = (data: any) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register('name', {
          required: 'Name is required',
          minLength: { value: 3, message: 'Min 3 characters' }
        })}
        placeholder="Name"
      />
      {errors.name && <span>{errors.name.message}</span>}

      <input
        {...register('email', {
          required: 'Email is required',
          pattern: { value: /^\S+@\S+$/i, message: 'Invalid email' }
        })}
        placeholder="Email"
      />
      {errors.email && <span>{errors.email.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}

/**
 * ✅ react-hook-form advantages:
 * - Uncontrolled internally (better performance)
 * - Controlled-like API (validation, error messages)
 * - Less re-renders (only re-render on submit or validation)
 */
```

---

##### **9.6. WHEN TO USE WHAT? - DECISION MATRIX**

**📊 Pattern Selection Guide:**

| Pattern | **Use Case** | **Modern Alternative** | **Status** |
|---------|--------------|----------------------|-----------|
| **Compound Components** | Complex UI (Tabs, Accordion, Dropdown) | Still relevant | ✅ Active |
| **Render Props** | Logic reuse with UI flexibility | Custom Hooks | ⚠️ Legacy |
| **HOC** | Wrap component with behavior (auth, logging) | Custom Hooks | ⚠️ Deprecated |
| **Container/Presentational** | Separate logic from UI | Custom Hooks + Component | ✅ Active |
| **Controlled** | Real-time validation, formatting | react-hook-form | ✅ Active |
| **Uncontrolled** | Simple forms, file inputs, performance | Still relevant | ✅ Active |

**💡 Best Practices:**

```typescript
// ══════════════════════════════════════════════════════════
// PATTERN DECISION TREE
// ══════════════════════════════════════════════════════════

/**
 * Question 1: Do you need shared state between parent-children?
 * → YES: Use Compound Components (Tabs, Accordion)
 * → NO: Continue to Q2
 * 
 * Question 2: Do you need to reuse logic across components?
 * → YES: Use Custom Hooks (modern approach)
 * → NO: Continue to Q3
 * 
 * Question 3: Do you need to separate logic from UI?
 * → YES: Use Custom Hook + Component pattern
 * → NO: Continue to Q4
 * 
 * Question 4: Are you building a form?
 * → YES: Need validation? → Controlled + react-hook-form
 *        Simple form? → Uncontrolled + useRef
 * → NO: Use simple component
 */

// ══════════════════════════════════════════════════════════
// MIGRATION GUIDE (Old → New)
// ══════════════════════════════════════════════════════════

// ❌ OLD: Render Props
<DataProvider render={(data) => <Component data={data} />} />

// ✅ NEW: Custom Hook
function Component() {
  const data = useData();
  return <div>{data}</div>;
}

// ❌ OLD: HOC
const AuthenticatedComponent = withAuth(Component);

// ✅ NEW: Custom Hook
function Component() {
  const { user } = useAuth();
  if (!user) return <Login />;
  return <div>Welcome {user.name}</div>;
}

// ❌ OLD: Container/Presentational (2 files)
// UserCardContainer.tsx + UserCard.tsx

// ✅ NEW: Custom Hook + Component (1 file)
function UserCard({ userId }) {
  const { user, loading, handleEdit, handleDelete } = useUser(userId);
  
  if (loading) return <div>Loading...</div>;
  
  return (
    <div className="user-card">
      <h3>{user.name}</h3>
      <button onClick={handleEdit}>Edit</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
}
```

**🎯 Key Takeaways:**

1. **Custom Hooks** replaced most HOC/Render Props patterns
2. **Compound Components** still best for complex UI (Tabs, Dropdowns)
3. **Controlled** for validation, **Uncontrolled** for performance
4. **react-hook-form** best for form management (hybrid approach)
5. Always choose **simplest pattern** that solves the problem
6. Don't over-engineer: Use patterns when you have clear need

---
