---
type: concept
tags: [foundations, language-internals, go, goroutines]
created: 2026-06-10
---

# Go Internals

## 1. Goroutines & The Scheduler
- **M:N Scheduler**: Mapping M goroutines to N OS threads.
- **The G-M-P Model**: Goroutine, Machine (Thread), Processor (Context).
- **Work Stealing**: How the scheduler balances load across threads.

## 2. Memory & Stack
- **Stack vs. Heap Escape Analysis**: How the compiler decides where to allocate memory.
- **Segmented Stacks vs. Stack Copying**: How Go grows goroutine stacks.

## 3. Channels
- **Hchan Structure**: The lock and buffer mechanism behind channels.
- **Send/Receive Flow**: How goroutines park and unpark during channel operations.
