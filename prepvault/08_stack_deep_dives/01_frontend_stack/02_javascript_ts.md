---
title: JavaScript & TypeScript Deep Dive
tags: ['stack/frontend']
created: 2026-06-10
---

# JavaScript & TypeScript Deep Dive

## Overview
JS/TS is the lingua franca of frontend interviews. You need to master the language fundamentals, asynchronous patterns, and TypeScript's type system cold — no Googling allowed.

## JavaScript Core — Must-Know Topics

### Execution Context & The Event Loop
```javascript
console.log('1');               // Synchronous - Call Stack
setTimeout(() => console.log('2'), 0); // Macrotask - Callback Queue
Promise.resolve().then(() => console.log('3')); // Microtask - Microtask Queue
console.log('4');               // Synchronous
// Output: 1, 4, 3, 2
```
**Order of execution**: Call Stack → Microtask Queue (Promise `.then`, `queueMicrotask`) → Macrotask Queue (`setTimeout`, `setInterval`, I/O)

### Closures & Scope
A **closure** is a function that remembers its lexical scope even when executed outside of it.

```javascript
function createCounter() {
  let count = 0;
  return function() {
    count++;
    return count;
  };
}
const counter = createCounter();
counter(); // 1
counter(); // 2
```
**Interview Pattern**: Module pattern, currying, memoization all rely on closures.

### `this` Keyword
| Context | `this` value |
|---------|-------------|
| Global (non-strict) | `window` / `globalThis` |
| Object method | The object |
| Arrow function | Lexical scope (outer function's `this`) |
| Constructor (`new`) | New instance |
| Event handler | The element (unless arrow function) |
| Explicit bind | Whatever `.call()`, `.apply()`, `.bind()` specifies |

### Prototypal Inheritance vs. Classes
```javascript
// ES6 Class (syntactic sugar over prototypes)
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
}
class Dog extends Animal {
  speak() { return `${this.name} barks`; }
}
// What happens under the hood: Dog.prototype → Animal.prototype → Object.prototype
```

### Async Patterns
| Pattern | When to use |
|---------|-------------|
| **Callbacks** | Legacy APIs, `setTimeout`, event listeners |
| **Promises** | Modern async operations, chainable |
| **Async/Await** | Clean sequential async code, error handling |
| **`Promise.all()`** | Parallel independent requests |
| **`Promise.allSettled()`** | All results (success + failure) needed |
| **`Promise.race()`** | Timeout first, fastest response wins |

### Common JS Interview Questions
1. **Implement `debounce`**: Returns a function that delays invocation until after X ms of inactivity
2. **Implement `throttle`**: Ensures a function is called at most once every X ms
3. **Deep clone**: Handle nested objects, arrays, circular references (use `WeakMap`)
4. **Flatten nested array**: Recursive reduce with `Array.isArray()` check
5. **Polyfill `Promise.all`**: Manually implement the race/all behavior

## TypeScript — The Type System

### Basic to Intermediate Types
```typescript
// Unions & Intersections
type Status = 'idle' | 'loading' | 'success' | 'error';
type HasId = { id: string };
type Timestamped = { createdAt: Date };
type PersistedEntity = HasId & Timestamped;

// Generics
function identity<T>(arg: T): T { return arg; }

// Mapped Types
type Readonly<T> = { readonly [K in keyof T]: T[K]; };

// Utility Types
Partial<T>, Required<T>, Pick<T, K>, Omit<T, K>,
Record<K, V>, Exclude<T, U>, ReturnType<T>
```

### Type Guards & Narrowing
```typescript
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

// Discriminated Unions
type Shape = 
  | { kind: 'circle'; radius: number }
  | { kind: 'square'; side: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case 'circle': return Math.PI * shape.radius ** 2;
    case 'square': return shape.side ** 2;
  }
}
```

### Advanced Patterns
- **Template Literal Types**: ``type EventName = `on${Capitalize<string>}` ``
- **Conditional Types**: `type IsString<T> = T extends string ? true : false;`
- **`satisfies`** (TS 4.9+): Type-check without widening
- **`as const`**: Literal type inference instead of widening

### Interview Question: "Implement a strongly typed event emitter"
```typescript
type Events = {
  userLoggedIn: { userId: string };
  pageViewed: { path: string };
};
class TypedEmitter<T extends Record<string, object>> {
  private handlers = new Map<keyof T, Set<Function>>();
  on<K extends keyof T>(event: K, handler: (data: T[K]) => void) { ... }
  emit<K extends keyof T>(event: K, data: T[K]) { ... }
}
```

## Performance & Memory
- **Memory Leaks**: Global variables, forgotten timers, detached DOM nodes, closures holding large data
- **WeakMap / WeakSet**: Garbage-collectable keys — ideal for caches and metadata
- **Web Workers**: Offload CPU-intensive tasks to a separate thread

## Related Topics
- [[08_stack_deep_dives/01_frontend_stack/01_html_css|HTML & CSS]]
- [[08_stack_deep_dives/01_frontend_stack/03_react|React Mastery]]
- [[08_stack_deep_dives/01_frontend_stack/index|Frontend Stack Index]]
- [[02_role_tracks/02_frontend_engineer|Frontend Engineer Track]]

## Resources
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [You Don't Know JS (Kyle Simpson)](https://github.com/getify/You-Dont-Know-JS)