# 📡 Q29: EventEmitter & Observer Pattern

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">📡 Q29: EventEmitter & Observer Pattern</span></summary>


**⚡ Quick Summary:**
> EventEmitter = publish/subscribe pattern. on() subscribe, emit() publish, off() unsubscribe

**💡 Ghi Nhớ:**
- 📡 **Pattern**: Publisher/Subscriber, decoupled communication
- 🎯 **Methods**: on/once/off/emit
- ⚠️ **Memory**: Remember off() để tránh memory leak!

**Trả lời:**

- **EventEmitter**: Pattern để emit và listen events
- **Observer Pattern**: Design pattern cho one-to-many dependency
- **Pub/Sub**: Publisher-Subscriber pattern cho loose coupling
- **Ưu điểm**: Decoupled components, flexible communication
- **Nhược điểm**: Có thể gây memory leaks, hard to debug

**Code Example:**

```typescript
// Custom EventEmitter
class EventEmitter {
  private events: Map<string, Function[]> = new Map();

  on(event: string, listener: Function): void {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(listener);
  }

  off(event: string, listener: Function): void {
    const listeners = this.events.get(event);
    if (listeners) {
      const index = listeners.indexOf(listener);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    }
  }

  emit(event: string, ...args: any[]): void {
    const listeners = this.events.get(event);
    if (listeners) {
      listeners.forEach((listener) => listener(...args));
    }
  }

  once(event: string, listener: Function): void {
    const onceWrapper = (...args: any[]) => {
      listener(...args);
      this.off(event, onceWrapper);
    };
    this.on(event, onceWrapper);
  }
}

// Usage
const emitter = new EventEmitter();

// Subscribe to events
emitter.on('user:login', (user: any) => {
  console.log('User logged in:', user.name);
});

emitter.on('user:logout', (user: any) => {
  console.log('User logged out:', user.name);
});

// Emit events
emitter.emit('user:login', { name: 'John', id: 1 });
emitter.emit('user:logout', { name: 'John', id: 1 });

// Observer Pattern
interface Observer {
  update(data: any): void;
}

class Subject {
  private observers: Observer[] = [];
  private state: any;

  addObserver(observer: Observer): void {
    this.observers.push(observer);
  }

  removeObserver(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1);
    }
  }

  notifyObservers(): void {
    this.observers.forEach((observer) => observer.update(this.state));
  }

  setState(newState: any): void {
    this.state = newState;
    this.notifyObservers();
  }
}

// Concrete Observer
class UserNotificationObserver implements Observer {
  update(data: any): void {
    console.log('Notification: User state changed to', data);
  }
}

// Usage
const subject = new Subject();
const notificationObserver = new UserNotificationObserver();

subject.addObserver(notificationObserver);
subject.setState('logged_in');

// Pub/Sub Pattern
class PubSub {
  private subscribers: Map<string, Function[]> = new Map();

  subscribe(topic: string, callback: Function): () => void {
    if (!this.subscribers.has(topic)) {
      this.subscribers.set(topic, []);
    }
    this.subscribers.get(topic)!.push(callback);

    // Return unsubscribe function
    return () => {
      const callbacks = this.subscribers.get(topic);
      if (callbacks) {
        const index = callbacks.indexOf(callback);
        if (index > -1) {
          callbacks.splice(index, 1);
        }
      }
    };
  }

  publish(topic: string, data: any): void {
    const callbacks = this.subscribers.get(topic);
    if (callbacks) {
      callbacks.forEach((callback) => callback(data));
    }
  }
}

// Usage
const pubsub = new PubSub();

const unsubscribe = pubsub.subscribe('user:update', (user: any) => {
  console.log('User updated:', user);
});

pubsub.publish('user:update', { name: 'John', age: 30 });

// Cleanup
unsubscribe();
```

**Best Practices:**

- Sử dụng EventEmitter cho component communication
- Sử dụng Observer pattern cho state management
- Sử dụng Pub/Sub cho loose coupling
- Cleanup listeners để tránh memory leaks

**Mistakes:**

```typescript
// ❌ Sai: Không cleanup listeners
emitter.on('event', handler);
// Memory leak nếu không remove listener

// ✅ Đúng: Cleanup listeners
const cleanup = () => emitter.off('event', handler);
// Call cleanup when component unmounts
```

</details>