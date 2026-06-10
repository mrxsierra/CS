---
type: concept
tags: [foundations, language-internals, python, gil]
created: 2026-06-10
---

# Python Internals

## 1. The Global Interpreter Lock (GIL)
- **What is it?**: A mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once.
- **Bypassing the GIL**: Using `multiprocessing`, `asyncio`, or C extensions.

## 2. Memory Management
- **Reference Counting**: The primary mechanism for object deallocation.
- **Generational GC**: How Python detects and breaks reference cycles.

## 3. Data Structures Under the Hood
- **Dictionaries**: Hash table implementation and collision resolution.
- **Generators**: How `yield` preserves function state without blocking.
