---
type: role
tags: [role/data-analyst, track]
created: 2024-06-13
---

# Data Analyst Interview Track

## 1. Role Overview
A Data Analyst (DA) is the bridge between raw data and business decisions. Their primary goal is to collect, process, and perform statistical analyses of data to help companies make better decisions. While Data Scientists often focus on *predicting* the future using machine learning, Data Analysts focus on *describing* the past and present to identify trends, opportunities, and risks.

### The Analyst's "Toolkit"
The role is defined by three pillars:
- **Data Retrieval:** Being able to query complex, often messy, databases using SQL.
- **Data Interpretation:** Using statistics and business logic to find the "why" behind the numbers.
- **Data Communication:** Presenting findings via dashboards (BI tools) and compelling reports to non-technical stakeholders (Product Managers, Executives).

---

## 2. Typical Interview Process
Data Analyst interviews are highly practical and focus on how you handle real-world business data.

1. **Recruiter Screen (15-20 min):** Basic background and checking your comfort level with SQL and BI tools.
2. **Technical Screen (45-60 min):**
   - **SQL Test:** Live coding or a platform-based test (e.g., HackerRank) focused on joins, aggregations, and subqueries.
   - **Excel Test (Sometimes):** Checking your ability with Pivot Tables, VLOOKUP/XLOOKUP, and basic formulas.
3. **The Onsite Loop (3-4 hours):**
   - **Data Visualization Round:** Explaining how you would design a dashboard for a specific KPI (e.g., "Design a dashboard for a Sales Manager").
   - **Case Study / Analytical Thinking:** Solving a business problem (e.g., "Sales in the North region are down 12%. Walk me through your analysis").
   - **Python/R Round (Optional):** Basic data manipulation using Pandas or Dplyr.
   - **Behavioral:** Focus on how you handle messy data, tight deadlines, and difficult stakeholders.

---

## 3. Foundational Prerequisites
Analysts need a solid base in data management and logic:

- **[[01_foundations/10_sql_database_deep_dive|SQL & Databases]]:** The single most important skill. You must understand relational schemas, indexing, and query optimization.
- **Statistics Basics:** Mean, Median, Mode, Standard Deviation, and basic probability.
- **[[01_foundations/02_sdlc|SDLC]]:** Understanding how data flows from an application (Frontend/Backend) into the database.
- **Business Domain Knowledge:** Understanding the specific metrics for the industry (e.g., FinTech vs. E-commerce).

---

## 4. Core Competencies

### A. SQL Mastery (The Foundation)
- **Joins:** Inner, Left, Right, Full, and Cross Joins. Know when to use each to avoid data loss or duplicates.
- **Aggregations:** `GROUP BY`, `HAVING`, `COUNT(DISTINCT)`.
- **Window Functions:** `RANK()`, `LEAD()`, `LAG()`, `ROW_NUMBER()`, `NTILE()`, `SUM() OVER()`.
- **Data Cleaning in SQL:** `CASE WHEN`, `COALESCE`, `CAST/CONVERT`, and String manipulation (`SUBSTR`, `TRIM`, `REPLACE`).
- **Optimization:** Avoiding `SELECT *`, using indexes effectively, and CTEs (Common Table Expressions) for readability and modularity.

### B. Business Intelligence (BI) & Visualization
- **Tools:** Tableau, Power BI, Looker, Mode, Sigma, or Google Data Studio.
- **Design Principles:** 
  - **Data-to-Ink Ratio:** Maximize information while minimizing noise.
  - **Chart Choice:** Line for trends over time, Bar for comparing categories, Scatter for relationships/correlations, Heatmaps for densities.
  - **Gestalt Principles:** Using proximity, similarity, and color to group related data points.
- **Dashboarding:** Building self-service tools that allow stakeholders to "slice and dice" data without asking you for a new query.

### C. Spreadsheet Excellence (Excel/Google Sheets)
- **Pivot Tables:** Summarizing large datasets quickly.
- **Advanced Formulas:** `XLOOKUP`, `INDEX/MATCH`, `SUMIFS`, `GETPIVOTDATA`, `ARRAYFORMULA`.
- **Data Cleaning:** Text-to-columns, removing duplicates, conditional formatting, and data validation rules.

### D. Metric Definition & KPIs
- **Customer Metrics:** 
  - **CAC (Acquisition Cost):** Total marketing spend / New customers acquired.
  - **LTV (Lifetime Value):** Predicted revenue from a customer over their entire relationship.
  - **Churn Rate:** % of users leaving per month.
- **Product Metrics:** 
  - **DAU/MAU:** Daily/Monthly Active Users (Stickiness).
  - **Conversion Rate:** % of users who complete a desired action (e.g., buying).
- **Business Metrics:** MRR (Monthly Recurring Revenue), ARPU (Average Revenue Per User), Gross Margin.

---

## 5. Role-Specific Deep Dives

### Deep Dive 1: The "Metric Drop" Framework
The most common case study question for Analysts.
1. **Clarify the Metric:** "How exactly is 'Retention' defined in this context? Is it 7-day or 30-day? Is it based on login or purchase?"
2. **Verify Data Integrity:** "Is the tracking broken? Did we have a data ingestion failure last night? Did the definition change?"
3. **Internal vs. External Factors:**
   - **Internal:** Did we launch a new app version? A new marketing campaign? A price hike? A buggy feature?
   - **External:** Competitor move? Seasonal trend (e.g., post-holiday slump)? Global event (e.g., internet outage)?
4. **Segmentation (The 'Slice and Dice'):**
   - **User Type:** New vs. Power users.
   - **Geography:** Is it only in the US? Only in Berlin?
   - **Platform:** iOS vs. Android vs. Web.
   - **Channel:** Organic vs. Paid search vs. Email.
5. **Synthesis:** Provide a summary and a proposed "Next Step" (e.g., "The drop is isolated to Android users in Germany; let's check with the QA team for bugs in version 2.4").

### Deep Dive 2: Cohort Analysis
- **Definition:** Grouping users based on a shared characteristic (usually the week/month they signed up) and tracking their behavior over time.
- **Why it matters:** It tells you if the product is getting better over time. If the "January Cohort" has 20% retention at Month 3, but the "March Cohort" has 30%, your onboarding/product improvements are working.

### Deep Dive 3: Marketing Attribution Models
How do we know which ad caused a user to buy?
- **First-Click:** Credits the very first ad the user saw.
- **Last-Click:** Credits the last ad before the purchase (most common but biased).
- **Linear:** Credits all touchpoints equally.
- **Time-Decay:** Gives more credit to touchpoints closer to the purchase.

---

## 6. Data Analysis at FAANG vs. Startups

### FAANG (Meta, Google, Amazon)
- **The "Business Intelligence" Machine:** You are part of a massive team. You might only look at one narrow product vertical.
- **Data Governance:** The data is clean, well-documented, and massive. You will use internal tools (e.g., Presto).
- **Rigor:** You need to prove that a 1% change is statistically significant.
- **The Interview:** Heavy emphasis on SQL efficiency and "Product Thinking".

### Startups (Seed to Series C)
- **The "Data Generalist":** You are the first hire. You set up the BI tool, write the tracking plan, and build everything.
- **Scrappiness:** You don't have time for perfect significance. You use "directional" data.
- **Direct Impact:** You sit next to the CEO and your work has immediate impact.
- **The Interview:** More about your past projects and your ability to work autonomously.

---

## 7. Common Interview Questions & Detailed Walkthroughs

### A. SQL Case Study
**Problem:** "Given a table `orders (order_id, user_id, order_date, amount)`, find the top 5 users by total spend who placed an order in the last 30 days."
```sql
SELECT 
  user_id, 
  SUM(amount) as total_spend
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
```

### B. Visualization/BI Scenario
**Question:** "A VP of Marketing wants to see 'Ad Spend Efficiency'. What dashboard do you build?"
- *Approach:*
  1. **Primary KPI:** ROAS (Return on Ad Spend) = Revenue / Ad Spend.
  2. **Breakdowns:** By Channel (Facebook vs. Google), By Campaign, and By Region.
  3. **Trend Line:** Daily ROAS vs. Target ROAS.
  4. **Funnel chart:** Impression -> Click -> Sign-up -> Purchase.

### C. Analytical Logic
**Question:** "If our conversion rate doubled overnight, is that a good thing?"
- *Analytical Answer:* "On the surface, yes. But I would first investigate if the *denominator* (traffic) crashed, leaving only the most loyal users. Or if there's a bug in the tracking that's double-counting conversions."

---

## 8. The Rise of the "Analytics Engineer"
A new hybrid role between Data Analyst and Data Engineer.
- **Goal:** To bring software engineering best practices to data modeling.
- **The Stack:** dbt (data build tool), Snowflake, and version control (Git).
- **The Workflow:** Instead of writing messy SQL scripts, you write modular, tested, and documented data models that the entire company can use.

---

## 9. Top 10 Essential Data Analyst Tools
1. **SQL:** The language of databases (Postgres, Snowflake).
2. **Excel/Google Sheets:** For quick analysis.
3. **Tableau/Power BI:** For professional viz.
4. **Python (Pandas):** For automation.
5. **dbt:** For data transformation.
6. **Jupyter Notebooks:** For exploratory analysis.
7. **Amplitude:** For product analytics.
8. **GitHub:** For version control.
9. **Google Analytics:** For web traffic.
10. **Slack:** For communicating insights.

---

## 10. Recommended Reading List
- *Lean Analytics* by Alistair Croll & Benjamin Yoskovitz.
- *Storytelling with Data* by Cole Nussbaumer Knaflic.
- *The Visual Display of Quantitative Information* by Edward Tufte.
- *SQL for Data Analysis* by Cathy Tanimura.

---

## 11. Recommended Roadmap
1. **Phase 1: SQL (Weeks 1-2):** Master Joins and Window Functions.
2. **Phase 2: Metrics (Weeks 3-4):** Learn industry-specific KPIs.
3. **Phase 3: Visualization (Week 5):** Build dashboards.
4. **Phase 4: Case Practice (Weeks 6-7):** Practice the "Metric Drop" framework.
5. **Phase 5: Python Basics (Week 8):** Master Pandas.

---

## 12. Data Analyst Glossary
- **ETL:** Extract, Transform, Load.
- **Granularity:** Level of detail.
- **Outlier:** Anomalous data point.
- **Normalization:** Reducing database redundancy.
- **CLV:** Customer Lifetime Value.
- **ROAS:** Return on Ad Spend.

---

## 13. Advanced SQL for Analysts
Mastering these techniques will set you apart from junior analysts.

### Self-Joins
- **Use Case:** Comparing a row to other rows in the same table (e.g., finding users who did Action A and then Action B within 24 hours).
- **SQL Example:**
```sql
SELECT a.user_id, a.event_time as time_a, b.event_time as time_b
FROM events a
JOIN events b ON a.user_id = b.user_id
WHERE a.event_name = 'view' AND b.event_name = 'click'
AND b.event_time > a.event_time 
AND b.event_time <= a.event_time + INTERVAL '24 hours';
```

### Advanced Window Functions
- **`LEAD` and `LAG`:** To access data from previous or subsequent rows without a join.
- **`NTILE(4)`:** To divide users into quartiles based on spend.

---

## 14. Data Warehousing & Modeling
Analysts often work closely with the warehouse.
- **Star Schema:** A central "Fact" table (e.g., `sales`) surrounded by "Dimension" tables (e.g., `products`, `customers`, `dates`). Optimized for read performance.
- **Snowflake Schema:** A more normalized version of the Star schema where dimensions are broken down into further tables.
- **SCD (Slowly Changing Dimensions):** How to handle changes in dimension data over time (e.g., a customer moves to a new city). **Type 2** (adding a new row with a start/end date) is the most common.

---

## 15. Stakeholder Management & Soft Skills
A Data Analyst's output is only useful if it's understood and trusted.
- **The "Executive Summary":** Always start your reports with a 3-sentence summary: 1. What was the question? 2. What is the answer? 3. What is the recommended action?
- **Data Storytelling:** Don't just show a chart; explain the narrative. "We see a spike in churn in June. This aligns with our removal of the 'Free Trial' period, suggesting the trial was a key acquisition driver."
- **Handling Ambiguity:** When a stakeholder asks for "The Retention Rate," clarify if they mean 7-day, 30-day, or Cohort-based retention.

---

## 16. More Detailed Interview Scenarios
**Scenario A: The "Messy Data" Question**
**Q: "You find that the 'Country' field in our database is 40% NULL. How do you proceed with a regional sales report?"**
- **A:** First, I'd investigate if the NULLs are random or systematic (e.g., only new users). Second, I'd try to "backfill" using other data (e.g., IP address or Credit Card billing zip code). If I can't backfill, I'd report the regional sales with a "Unknown" category and explicitly mention the limitation in the summary.

**Scenario B: The "Tradeoff" Question**
**Q: "We can only build one dashboard this month: 'Marketing Spend' or 'Product Engagement'. How do you decide?"**
- **A:** I would evaluate based on **Business Impact** and **Urgency**. I'd ask the leadership: "Which team is currently making the most expensive decisions without data?" If Marketing is about to commit to a $1M campaign, their dashboard is higher priority.

---

## Related Topics

- [[01_foundations/10_sql_database_deep_dive|SQL Database Deep Dive]]
- [[02_role_tracks/09_data_scientist|Data Scientist Track (The Next Step)]]
- [[03_interview_formats/03_behavioral_rounds|Stakeholder Management Tips]]
