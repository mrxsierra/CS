---
type: concept
tags: [foundations, system-design, blueprint, junior, data]
created: 2026-06-10
---

# System Design Blueprint: Expense Tracker (e.g., Mint/YNAB)

Focuses on CRUD operations, data aggregation, and integration with 3rd-party APIs.

---

## 1. Requirements
- **Functional**:
    - Add/Edit/Delete transactions.
    - Categorize expenses (Food, Rent, etc.).
    - View reports/summaries (Monthly spending).
    - Link bank accounts (Optional/Advanced).
- **Non-Functional**:
    - High reliability (Financial data must not be lost).
    - Accuracy (Calculations must be correct).
    - Privacy/Security (Sensitive financial info).

## 2. Data Model
- **SQL (PostgreSQL)** is preferred here due to the need for ACID compliance and complex queries/aggregations.
- **Tables**:
    - `users`: id, email, password_hash
    - `categories`: id, name, user_id
    - `transactions`: id, amount, category_id, date, description, user_id

## 3. Architecture
- **Monolith / Microservices**: A small team might start with a Monolith.
- **REST API**: For mobile and web clients.
- **Background Jobs**: For processing bank imports or generating large monthly PDF reports.

## 4. Aggregation Logic
- **Pre-aggregation**: Instead of calculating "Monthly Spend" every time the user opens the app, maintain a `monthly_summaries` table that updates whenever a transaction is added/modified.
- **Materialized Views**: Use SQL Materialized Views for complex reporting.

## 5. Security
- **Encryption at rest**: Encrypt sensitive fields (bank info).
- **Authentication**: JWT or Session-based.
- **Input Validation**: Critical to prevent double-spending or injection.

---

## Role-Specific Applications
- **Frontend**: Data visualization (Charts/Graphs), form validation for currency, offline sync (storing transactions locally).
- **Backend**: Ensuring transaction atomicity, designing robust aggregation queries, securing financial endpoints.
- **Data Engineering**: Building ETL pipelines to import data from financial providers (Plaid API).
