---
type: concept
tags: [stack, backend, python, fastapi, async, pydantic]
created: 2026-06-10
---

# Backend Stack: Python & FastAPI Deep Dive

FastAPI is the modern standard for high-performance Python APIs, leveraging type hints and asynchronous programming.

---

## 1. Why FastAPI?
- **Speed**: Performance on par with Node.js and Go (thanks to Starlette and Pydantic).
- **Type Safety**: Uses Python 3.10+ type hints for data validation and serialization.
- **Auto-Docs**: Automatically generates Interactive API docs (Swagger UI / ReDoc).
- **Async First**: Built-in support for `async` and `await`.

## 2. Core Concepts: Pydantic & Dependency Injection
- **Pydantic**: Handles data validation. If a client sends a string instead of an int, Pydantic returns a clear error before the logic even runs.
- **Dependency Injection**: A powerful system for sharing logic (e.g., database sessions, authentication) across multiple routes.
```python
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    ...
```

## 3. Asynchronous Programming in Python
Python's `asyncio` is at the heart of FastAPI.
- **Coroutines**: Functions defined with `async def`.
- **Event Loop**: Orchestrates the execution of coroutines.
- **When to use `async def`?**: Use for I/O bound tasks (Database queries, API calls). Use normal `def` for CPU-bound tasks or when using blocking libraries.

## 4. Middleware & Starlette
FastAPI is a layer on top of **Starlette** (a lightweight ASGI toolkit).
- **Middleware**: Functions that run before every request and after every response (e.g., CORS, GZip compression).
- **ASGI (Asynchronous Server Gateway Interface)**: The successor to WSGI, allowing for asynchronous communication.

## 5. Deployment Stack
- **Uvicorn**: A lightning-fast ASGI server implementation.
- **Gunicorn with Uvicorn workers**: Recommended for production to manage multiple processes.

## Common Interview Questions
- **"What is the difference between FastAPI and Flask?"**: Flask is WSGI (synchronous), FastAPI is ASGI (asynchronous). FastAPI has built-in validation (Pydantic) and auto-docs.
- **"Explain how FastAPI handles dependency injection."**: Explain the `Depends()` syntax and how it manages lifecycle (e.g., closing DB connections).
- **"How does FastAPI achieve its high performance?"**: Mention Starlette, Pydantic, and the use of `asyncio` for non-blocking I/O.

## Related Topics
- [[01_foundations/05_networking|Networking (HTTP/REST)]]
- [[08_stack_deep_dives/02_backend_stack/03_flask_django|Flask vs Django]]
