---
type: role
tags: [role/general-swe, track]
created: 2024-06-10
---

# General Software Engineer Interview Track

## 1. Role Overview
The General Software Engineer (SWE) role is the most common entry point for developers at tech companies, ranging from early-stage startups to FAANG giants. Unlike specialized roles (Frontend, Backend, ML), the General SWE is expected to be a "versatile problem solver" who can adapt to any part of the stack.

### The Interview Philosophy
Companies interview for General SWEs using a "Signal over Knowledge" approach. They aren't looking to see if you know a specific framework's API; they want to see if you can:
-   Deconstruct a vague problem into technical requirements.
-   Identify the optimal data structure for a specific use case.
-   Reason about time and space complexity.
-   Write code that is not just "correct" but also "clean" and "testable."

### Typical Interview Stages
1.  **Recruiter Screen (15-30 min):** Basic fit, salary expectations, and high-level technical background.
2.  **Online Assessment (OA) (60-90 min):** Automated coding challenges on platforms like HackerRank, LeetCode, or CodeSignal. Usually 2-3 problems ranging from Easy to Medium-Hard.
3.  **Technical Phone Screen (45-60 min):** Collaborative coding with an engineer. Focus is on "thinking out loud" and basic DSA proficiency.
4.  **The "Onsite" Loop (4-6 hours):**
    -   **Coding Round 1 & 2:** Focus on core DSA (Trees, Graphs, DP, etc.).
    -   **System Design Round:** Focus on high-level architecture (Scaling, DBs, APIs).
    -   **Object-Oriented Design (OOD) / Practical Coding:** Focus on code structure and maintainability.
    -   **Behavioral Round:** Cultural fit and leadership principles.

---

## 2. Foundational Prerequisites
Before diving into role-specific prep, ensure you have mastered the foundations. These are the building blocks of every SWE interview:

-   **[[01_Foundations/01_DSA|Data Structures & Algorithms]]:** The non-negotiable core. You must be comfortable with Arrays, HashMaps, Linked Lists, Trees, Graphs, Heaps, and Tries. Understand the "big-O" of every operation.
-   **[[01_Foundations/03_System_Design|System Design Fundamentals]]:** Understanding how to build for millions of users. Topics include Load Balancing, Caching, Sharding, and CAP Theorem.
-   **[[01_Foundations/04_Operating_Systems|Operating Systems]]:** Knowing how the underlying machine works. Processes vs. Threads, Context Switching, Deadlocks, and Memory Management (Stack vs. Heap).
-   **[[01_Foundations/05_Networking|Networking]]:** The glue of the internet. TCP/IP, HTTP/S, DNS, and the OSI model. Understanding how a request travels from a client to a server.
-   **[[01_Foundations/02_SDLC|Software Development Lifecycle]]:** Version control (Git), Testing (Unit, Integration, E2E), and CI/CD pipelines. Familiarity with Agile/Scrum methodologies.

---

## 3. 2026-27 Ecosystem Focus
Companies now hire based on ecosystem fit. Choose one of the following to master:
- **Ecosystem A (Modern Startup)**: TypeScript, Next.js, Node.js (NestJS/Fastify) or Go, PostgreSQL, Redis, Docker.
- **Ecosystem B (Enterprise & GCC)**: Java (Spring Boot) or C# (.NET Core), React/Angular, Kafka, Docker.
- **Ecosystem C (AI-Native)**: Python (FastAPI/Django), React, Vector Databases (Pinecone/PGVector), Redis.

## 4. 12-Week Learning Pathway
- **Week 1-3: Frontend Framework Mechanics**: Master Virtual DOM, state management, and SSR.
- **Week 4-7: Backend API Architecture**: Design REST/GraphQL APIs, Auth, and DB connections.
- **Week 8-12: System Integration**: Transaction boundaries, caching, and Docker orchestration.

## 5. Core Competencies & Skills

### A. Algorithmic Problem Solving
This is where 80% of candidates fail. To succeed, you need to move beyond "memorizing LeetCode" to "understanding patterns."
-   **Pattern Recognition:** When you see "shortest path," think BFS. When you see "top k," think Min-Heap. When you see "combinations," think Backtracking.
-   **Complexity Analysis:** You must be able to explain *why* a solution is O(N log N) vs O(N²). Always consider the worst-case, average-case, and best-case.
-   **Edge Case Handling:** Professional SWEs check for nulls, empty inputs, extremely large values, and duplicates before they are asked.

### B. Coding Fluency
Choose one language (Python, Java, C++, or Go) and know it inside out.
-   **Standard Libraries:** Do you know how to use `PriorityQueue` in Java or `heapq` in Python without Googling?
-   **Idiomatic Code:** Are you writing Pythonic code or just translating Java into Python syntax?
-   **Cleanliness:** Variable naming matters. `i` and `j` are fine for loops, but `idx_map` is better than `m`.

### C. Software Engineering Best Practices
A General SWE is expected to write code that lives in a shared codebase.
-   **SOLID Principles:** Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
-   **DRY (Don't Repeat Yourself):** Abstracting common logic into reusable functions/classes.
-   **KISS (Keep It Simple, Stupid):** Avoiding over-engineering. Pick the simplest solution that meets the requirements.
-   **YAGNI (You Ain't Gonna Need It):** Don't build features for "future use cases" unless specifically asked.

---

## 4. Role-Specific Deep Dives

### Deep Dive 1: The Problem-Solving Framework (The "Interview Protocol")
Use this 6-step process in every coding round. This is the difference between an "Intermediate" and a "Senior" signal.
1.  **Clarify (5-7 min):** 
    -   Don't just ask about edge cases. Ask about the *source* and *usage* of data. 
    -   "Is the data stream-based or batch?" 
    -   "What is the read/write ratio?" 
    -   "Can I assume the data fits in memory?" 
2.  **Brainstorm & Strategy (5-10 min):** 
    -   Talk through 2-3 approaches. Mention the tradeoffs explicitly. 
    -   "I could use a brute force O(N²) approach, but a HashMap would bring it down to O(N) at the cost of O(N) space."
3.  **Confirm Approach:** Get the interviewer's "buy-in." If they seem hesitant, ask: "Does this approach seem optimal to you, or should I explore the space-time tradeoff further?"
4.  **Code (15-20 min):** 
    -   Write clean, structured code. 
    -   **Modularize:** If you need to validate a string, write `if (!isValid(s)) return;` and implement `isValid` later. This shows you prioritize high-level logic.
5.  **Dry Run (5 min):** 
    -   Trace your code with a small, concrete example. 
    -   Don't just say "it works." Show the state of variables at each step of the loop. 
    -   Find the bugs yourself. Interviewers *love* when you find your own off-by-one error.
6.  **Optimize & Wrap Up:** Discuss what you would do with more time. Mention unit tests, better error handling, or performance profiling.

### Deep Dive 2: Low-Level Design (LLD) and OOP
Many Generalist interviews (especially at Google and Amazon) include an LLD round. You might be asked to "Design a Parking Lot" or "Design an Elevator System."
-   **Key Steps for LLD:**
    1.  **Requirement Clarification:** Functional (Park vehicle, unpark, pay) and Non-functional (Scalability, Thread safety).
    2.  **Class Diagram:** Identify entities (Vehicle, ParkingSpot, Level, Gate, Ticket).
    3.  **Relationships:** Inheritance (Car/Truck extends Vehicle) and Composition (Level contains ParkingSpots).
    4.  **API Design:** Define the public methods of each class.
    5.  **Design Patterns:** Apply patterns like Factory (to create different vehicle types) or Singleton (for the ParkingManager).

### Deep Dive 3: The Seniority Spectrum
What interviewers look for based on level:
-   **Junior (L3):** Can they write correct code? Do they understand basic DSA? Do they need constant hand-holding?
-   **Mid-Level (L4):** Can they solve complex problems independently? Is their code clean and well-structured? Do they understand system design basics?
-   **Senior (L5):** Can they navigate ambiguity? Do they consider scale, reliability, and maintenance? Do they mentor the interviewer during the session?
-   **Staff+ (L6+):** Can they solve "system-wide" problems? Do they think about business impact, cross-team dependencies, and long-term technical debt?

### Deep Dive 4: Soft Skills & "Thinking Aloud"
The "Generalist" round is often a test of communication.
-   **The "Silent Coder" Trap:** If you code in silence for 10 minutes, the interviewer has no idea if you're stuck or if you're a genius. If you're wrong, they can't help you.
-   **Narrate your thoughts:** "I'm thinking of using a heap here because I need the top K elements, and a heap will keep my time complexity to N log K."
-   **Handle Hints Gracefully:** If an interviewer gives you a hint, take it! Don't be defensive. Say, "That's a great point, let me rethink the tree traversal with that in mind."

---

## 5. Common Interview Questions & Solutions

### A. Algorithmic Patterns (The "Must-Knows")
1.  **Sliding Window:** "Find the longest substring without repeating characters."
2.  **Two Pointers:** "Three Sum" problem (finding three numbers that sum to zero).
3.  **Fast & Slow Pointers:** "Linked List Cycle" detection.
4.  **Merge Intervals:** "Meeting Rooms II" (minimum number of conference rooms).
5.  **BFS on Graphs:** "Number of Islands" or "Word Ladder."
6.  **DFS / Backtracking:** "Generate Parentheses" or "Sudoku Solver."
7.  **Dynamic Programming:** "Climbing Stairs" (Easy) to "Longest Common Subsequence" (Hard).

### B. System Design Scenarios
1.  **Design a URL Shortener (TinyURL):** Focus on Hash generation, redirection, and read/write scaling.
2.  **Design a Rate Limiter:** Focus on algorithms like Token Bucket vs. Leaky Bucket.
3.  **Design a News Feed:** Focus on "Pull vs. Push" models for updates.
4.  **Design a Web Crawler:** Focus on BFS, politeness protocols, and deduplication.

### C. Low-Level Design (LLD) Scenarios
1.  **Design a Parking Lot:** Managing different vehicle types and payment logic.
2.  **Design an Elevator System:** Optimizing for wait time vs. throughput.
3.  **Design a Library Management System:** Handling book checkouts, renewals, and fines.
4.  **Design a Movie Ticket Booking System (BookMyShow):** Handling concurrent bookings for the same seat.

### D. Behavioral Questions (The "STAR" Method)
-   "Tell me about a time you had a conflict with a teammate."
-   "Tell me about a technical challenge you overcame."
-   "Describe a time you failed and what you learned."
*Tip: Use the **S**ituation, **T**ask, **A**ction, **R**esult framework to keep your answers structured.*

---

## 6. Company-Specific Patterns

### Google
-   **Style:** Very heavy on algorithmic complexity and "out-of-the-box" thinking.
-   **Focus:** Strong emphasis on Graphs, Recursion, and Dynamic Programming.
-   **Tip:** Be prepared for "follow-up" questions that drastically change the problem constraints. Google cares about "Googleyness" — intellectual humble and collaborative.

### Meta (Facebook)
-   **Style:** Focus on speed and accuracy. Many problems are straight from LeetCode.
-   **Focus:** Arrays, Strings, and common Tree traversals.
-   **Tip:** You are expected to solve two Medium problems in 40 minutes perfectly. Meta values "Moving Fast" and "Impact."

### Amazon
-   **Style:** Deeply integrated with their 16 **Leadership Principles**.
-   **Focus:** OOD (Parking Lot style) and practical problem solving.
-   **Tip:** Spend 50% of your prep on behavioral stories. Amazon will hire a slightly weaker coder who is a perfect cultural fit (Leadership Principles) over a coding genius who fails them.

### Microsoft
-   **Style:** Balanced. Mix of standard DSA and practical engineering questions.
-   **Focus:** Linked Lists, Trees, and Strings are very common.
-   **Tip:** Microsoft values "Growth Mindset." Be open about what you don't know and show how you'd learn it.

---

## 7. The Final Roadmap: How to Prepare
1.  **Phase 1: Foundation (Weeks 1-2):** Review DSA basics. Implement every major data structure from scratch. Review Networking and OS fundamentals.
2.  **Phase 3: Pattern Mastery (Weeks 3-6):** Solve 10-15 problems for each major pattern (Sliding Window, BFS, etc.). Focus on Medium difficulty. Use LeetCode, NeetCode, or similar platforms.
3.  **Phase 4: System Design & LLD (Weeks 7-8):** Read "Grokking the System Design Interview" and practice 10-12 common scenarios. Understand SOLID and Design Patterns.
4.  **Phase 5: Behavioral & Mocks (Weeks 9-10):** Prepare 10-12 core stories using the STAR method. Map them to various Leadership Principles. Conduct 5+ mock interviews on Pramp or with friends.
5.  **Phase 6: Refinement (Last week):** Re-do problems you struggled with. Review company-specific guides on Glassdoor/Blind. Rest and build confidence.

---
## 8. Top 10 Essential Generalist Concepts
1. **Big-O Complexity:** The language used to evaluate algorithm efficiency.
2. **Recursion & Memoization:** Solving complex problems by breaking them into overlapping sub-problems.
3. **Pointers & Memory:** Understanding how data is stored in the Stack vs. the Heap.
4. **Concurrency & Threading:** Managing multiple tasks simultaneously and avoiding race conditions.
5. **Data Structures:** Choosing the right "tool" (HashMap, Tree, Queue) for the job.
6. **API Design (REST/GraphQL):** How to structure communication between services.
7. **Database Indexing:** How to speed up data retrieval.
8. **Scalability Principles:** Caching, Load Balancing, and Sharding.
9. **Testing Strategies:** Unit vs. Integration vs. End-to-End.
10. **The SDLC:** How code goes from an idea to production.

---

## 9. Recommended Reading List
- *Cracking the Coding Interview* by Gayle Laakmann McDowell.
- *Introduction to Algorithms (CLRS)* (for deep theory).
- *Designing Data-Intensive Applications* by Martin Kleppmann.
- *Clean Code* by Robert C. Martin.
- *The Pragmatic Programmer* by Andrew Hunt & David Thomas.

---

## 10. Glossary of Terms

-   **Big-O:** A notation used to describe the efficiency of an algorithm.
-   **Concurrency:** The ability of different parts or units of a program to be executed out-of-order or in partial order, without affecting the final outcome.
-   **Idempotency:** A property of certain operations in mathematics and computer science whereby they can be applied multiple times without changing the result beyond the initial application.
-   **Technical Debt:** The implied cost of additional rework caused by choosing an easy (limited) solution now instead of using a better approach that would take longer.

## Related Topics
-   [[01_Foundations/01_DSA|Mastering DSA]]
-   [[03_Interview_Formats/01_Coding_Rounds|Survival Guide for Coding Rounds]]
-   [[03_Interview_Formats/03_Behavioral_Rounds|Cracking the Behavioral Interview]]
-   [[05_Templates/interview_question_template|Problem Solving Template]]
