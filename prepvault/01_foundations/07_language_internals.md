---
type: concept
tags: [foundations, language-internals, compilers, runtime]
created: 2026-06-10
---

# Language Internals: High-Level Overview

To pass 2026-27 interviews, you must know at least one language deeply enough to explain its behavior under the hood. This includes memory allocation, garbage collection, and concurrency models.

## Core Language Guides
- [[01_foundations/07_language_internals/js_ts|JavaScript / TypeScript]]
- [[01_foundations/07_language_internals/java|Java (JVM)]]
- [[01_foundations/07_language_internals/python|Python]]
- [[01_foundations/07_language_internals/go|Go]]
- [[01_foundations/07_language_internals/rust|Rust]]

## Common Concepts Across Languages
- **Stack vs. Heap**: Where data is stored and how its lifetime is managed.
- **Garbage Collection (GC)**: Reference counting vs. Tracing (Mark & Sweep) - and why Rust doesn't need one.
- **Compilation vs. Interpretation**: JIT (Just-In-Time) compilation vs. Bytecode execution.
- **Concurrency Models**: Multi-threading, Event Loops, and Coroutines.
