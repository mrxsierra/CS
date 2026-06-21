---
type: concept
tags: [foundations, rust, language-internals, memory-safety]
created: 2026-06-10
---

# Rust Internals: Ownership, Borrowing, and Lifetimes

Rust’s core value proposition is memory safety without a garbage collector.

---

## 1. The Ownership System
Every value in Rust has a unique owner.
- **Rules**:
    1. Each value has a variable called its owner.
    2. There can only be one owner at a time.
    3. When the owner goes out of scope, the value is dropped.
- **Move Semantics**: Assigning a variable to another "moves" the value, making the original variable invalid.

## 2. Borrowing & References
Accessing data without taking ownership.
- **Immutable Borrow (`&T`)**: You can have any number of immutable references at once.
- **Mutable Borrow (`&mut T`)**: You can have exactly one mutable reference at a time, and no immutable references.
- **Data Race Prevention**: These rules are enforced at compile time to prevent data races.

## 3. Lifetimes
Lifetimes are a way for the compiler to ensure that all borrows are valid.
- **Syntax**: `'a` (e.g., `fn longest<'a>(x: &'a str, y: &'a str) -> &'a str`).
- **Purpose**: Prevents "Dangling Pointers" (references to memory that has been freed).

## 4. Traits & Generics
- **Traits**: Define shared behavior (similar to interfaces).
- **Send & Sync**: 
    - `Send`: Can be transferred across thread boundaries.
    - `Sync`: Can be shared across thread boundaries.
- **Static vs. Dynamic Dispatch**: 
    - `impl Trait` (Static): Monomorphization (no runtime cost).
    - `dyn Trait` (Dynamic): Vtable (runtime overhead).

---

## Common Interview Questions
- **"What is 'Smart Pointer' (Box, Rc, Arc)?"**: 
    - `Box<T>`: Heap allocation.
    - `Rc<T>`: Reference counting (not thread-safe).
    - `Arc<T>`: Atomic reference counting (thread-safe).
- **"Explain 'Unsafe' Rust."**: A way to bypass the borrow checker for low-level systems programming (e.g., FFI, raw pointers), but the developer assumes responsibility for safety.

## Related Topics
- [[08_Stack_Deep_Dives/02_Backend_Stack/04_Rust_Systems|Rust Backend Stack]]
- [[01_Foundations/04_Operating_Systems|OS (Memory Management)]]
