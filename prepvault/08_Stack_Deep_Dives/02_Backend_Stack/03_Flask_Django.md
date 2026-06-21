---
type: concept
tags: [stack, backend, python, flask, django, orm]
created: 2026-06-10
---

# Backend Stack: Flask vs. Django

Python's two most popular web frameworks represent two different philosophies: "Batteries Included" (Django) vs. "Minimalist" (Flask).

---

## 1. Django: The Batteries-Included Framework
Ideal for large-scale applications where you want to move fast by using proven patterns.

### Key Components:
- **Django ORM**: A powerful Object-Relational Mapper that handles migrations and database interactions.
- **Admin Interface**: A built-in, customizable dashboard for managing data.
- **Authentication**: Built-in user management, sessions, and security (protection against CSRF, SQLi, XSS).
- **Template Engine**: Django's own language for rendering HTML.

### Architecture: MVT (Model-View-Template)
- **Model**: Data structure (Database).
- **View**: Business logic (Handles the request and returns the response).
- **Template**: Presentation layer (HTML).

---

## 2. Flask: The Micro-framework
Ideal for small services, microservices, or when you want full control over every library you use.

### Key Characteristics:
- **Minimalist**: Only provides routing and template rendering (Jinja2).
- **Extensible**: You choose your ORM (e.g., SQLAlchemy), your auth (e.g., Flask-Login), and your validation.
- **Explicit**: Nothing happens "magically" in the background.

---

## 3. Comparison Table

| Feature | Django | Flask |
| :--- | :--- | :--- |
| **Philosophy** | Opinionated (The "Django Way") | Non-opinionated (Flexible) |
| **Learning Curve**| Steeper (Lots of concepts) | Shallow (Get started in minutes) |
| **ORM** | Built-in | None (Use SQLAlchemy) |
| **Auth** | Built-in | Extensions needed |
| **Scalability** | Great for monoliths | Great for microservices |

---

## 4. Key Interview Concepts
- **Django Middleware**: A framework of hooks into Django’s request/response processing. (e.g., checking if a user is authenticated before reaching the view).
- **SQLAlchemy (Flask)**: Understanding the Unit of Work pattern and how it differs from Django's Active Record pattern.
- **Migrations**: How to handle schema changes in production without losing data.

## Common Interview Questions
- **"When would you choose Flask over Django?"**: Choose Flask for simple APIs, microservices, or when you need a specific database/library not easily integrated with Django.
- **"Explain the Django Request/Response lifecycle."**: Middleware -> URL Conf -> View -> Model/Template -> Middleware -> Response.
- **"What is a 'fat model' vs 'thin view'?"**: A design philosophy where business logic resides in the Model (or a service layer) rather than the View.

## Related Topics
- [[01_Foundations/09_SQL_Database_Deep_Dive|SQL Deep Dive]]
- [[08_Stack_Deep_Dives/02_Backend_Stack/02_Python_FastAPI|FastAPI]]
