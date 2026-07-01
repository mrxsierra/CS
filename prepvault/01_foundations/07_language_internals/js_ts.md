---
type: concept
tags: [foundations, javascript, typescript, language-internals]
created: 2026-06-10
---

# JavaScript & TypeScript Internals

Mastering the language you code in is the difference between a Junior and a Senior engineer.

---

## 1. JavaScript: The V8 Engine & Execution
- **The Event Loop**: (See [[08_stack_deep_dives/02_backend_stack/01_node_js|Node.js Deep Dive]] for details).
- **Prototypal Inheritance**: JavaScript uses prototypes, not classes (ES6 classes are sugar). Every object has an internal link to another object called its prototype.
- **Closures**: A function bundled together with its lexical environment. Allows a function to access variables from an outer scope even after that scope has closed.
- **Hoisting**: JavaScript's default behavior of moving declarations to the top. `var` is hoisted and initialized as `undefined`; `let`/`const` are hoisted but not initialized (Temporal Dead Zone).

## 2. Memory Management
- **Stack**: Primitive values and execution context.
- **Heap**: Objects, arrays, and functions.
- **Garbage Collection**: Uses the "Mark-and-Sweep" algorithm. Memory leaks often occur from global variables, detached DOM nodes, or uncleared intervals.

## 3. TypeScript: Type System & Compiler
- **Structural Typing**: TypeScript uses "Duck Typing." If two objects have the same shape, they are considered to be of the same type.
- **Interfaces vs. Types**: 
    - **Interfaces**: Better for defining object shapes; can be merged (declaration merging).
    - **Types**: Better for unions, intersections, and primitives.
- **Generics**: Components that can work over a variety of types rather than a single one.
- **The Compiler (tsc)**: Transforms TS into JS and performs type checking.

---

## Common Interview Questions
- **"What is the difference between `==` and `===`?"**: `==` performs type coercion; `===` checks both value and type.
- **"Explain 'this' in JavaScript."**: The value of `this` is determined by how a function is called (Global, Object method, Constructor, or explicitly bound via `call/apply/bind`).
- **"What are Decorators in TypeScript?"**: A special kind of declaration that can be attached to a class, method, or property to modify its behavior.

## Related Topics
- [[08_stack_deep_dives/01_frontend_stack/index|Frontend Stack]]
- [[08_stack_deep_dives/02_backend_stack/01_node_js|Node.js]]
