---
type: concept
tags: [foundations, system-design, blueprint, junior]
created: 2026-06-10
---

# System Design Blueprint: Student Portal / LMS (e.g., Canvas/Coursera)

Focuses on complex relationships, file storage, and role-based access control (RBAC).

---

## 1. Requirements
- **Functional**:
    - Manage Courses, Enrollments, and Grades.
    - Upload and download course materials (PDFs, Videos).
    - Discussion forums for students and instructors.
- **Non-Functional**:
    - High availability (especially during finals/registration).
    - Scalability (handling peaks in traffic).
    - Read-heavy (mostly viewing materials).

## 2. Data Model (Relational)
- **Tables**:
    - `users`: id, name, role (Student, Instructor, Admin)
    - `courses`: id, title, description, instructor_id
    - `enrollments`: user_id, course_id, status
    - `assignments`: id, course_id, title, max_score
    - `submissions`: id, assignment_id, student_id, file_url, score

## 3. Storage Strategy
- **Relational DB**: For metadata, grades, and relational data.
- **Object Storage (S3)**: For course materials (videos, lecture slides) and student submissions.
- **CDN (CloudFront)**: To deliver large lecture videos with low latency globally.

## 4. Key Design Patterns
- **Role-Based Access Control (RBAC)**: Ensuring students can only see their own grades and instructors can only modify their own courses.
- **Caching**: Cache course catalog and announcements using Redis to reduce DB load.

## 5. Scalability during Registration
- Use **Message Queues** to handle enrollment requests if the DB starts to bottleneck.
- Horizontal scaling of the web servers behind a Load Balancer.

---

## Role-Specific Applications
- **Frontend**: Handling large file uploads with progress bars, building responsive dashboards for different user roles.
- **Backend**: Designing a robust RBAC middleware, optimizing JOIN-heavy queries for student records.
- **DevOps**: Auto-scaling clusters during enrollment periods, managing storage buckets and CDN distribution.
