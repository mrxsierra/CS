---
type: concept
tags: [foundations, language-internals, java, jvm]
created: 2026-06-10
---

# Java (JVM) Internals

## 1. JVM Architecture
- **ClassLoader Subsystem**: Loading, Linking, and Initializing classes.
- **Runtime Data Areas**: Method Area, Heap Area, Stack Area, PC Registers, Native Method Stack.

## 2. Garbage Collection (GC)
- **Generational GC**: Eden Space, Survivor Space, Old Gen.
- **Modern Collectors**: G1 GC, ZGC (Low latency), Shenandoah.

## 3. Concurrency
- **The Java Memory Model (JMM)**: Visibility, atomicity, and reordering.
- **Project Loom**: Virtual Threads and how they differ from OS threads.
- **Synchronized vs. Locks**: Monitor locks and the `java.util.concurrent` package.
