---
type: role
tags: [role/data-scientist, track]
created: 2024-06-13
---

# Data Scientist Interview Track

## 1. Role Overview
A Data Scientist (DS) is a multi-disciplinary professional who extracts actionable insights from large, complex datasets to drive business value. The role sits at the intersection of **Statistics**, **Computer Science (specifically Machine Learning and Data Engineering)**, and **Business Strategy**. 

Data Scientists are not just builders of models; they are storytellers and decision-makers. They identify the "right" questions to ask, design experiments to test hypotheses, and translate mathematical results into strategic recommendations.

### The "Flavor" of the Role
Depending on the company, Data Science roles usually lean in one of three directions:
- **Product/Analytics Focus:** Emphasis on metrics, A/B testing, and product intuition (common at Meta, Uber, Airbnb).
- **Inference/Statistical Focus:** Emphasis on causal inference, experimental design, and rigorous statistical modeling (common in biotech, policy, and research units).
- **Machine Learning Focus:** Emphasis on building predictive models, feature engineering, and deploying models into production (common at Amazon, Netflix, and AI-heavy startups).

---

## 2. Typical Interview Process
The Data Science interview loop is notoriously diverse, often spanning 5-7 stages:

1. **Recruiter Screen (15-30 min):** Basic background, salary expectations, and checking for "culture fit."
2. **Technical Screen / Take-Home (60-90 min or 2-3 days):**
   - **Take-Home:** Analyze a dataset, build a model, and provide a report or presentation.
   - **Live Screen:** SQL problems or a basic "Data Coding" challenge in Python.
3. **The Onsite Loop (4-5 hours):**
   - **Coding Round:** SQL (complex joins/window functions) and Python (Pandas/NumPy logic or basic DSA).
   - **Statistics & Probability:** High-level theory and brainteasers.
   - **Machine Learning Theory:** Understanding the "why" behind the algorithms (bias-variance, loss functions).
   - **Case Study / Business Sense:** A vague problem (e.g., "Retention is dropping on Instagram. How would you investigate?")
   - **Applied Machine Learning:** Designing an end-to-end ML system for a specific use case.
   - **Behavioral:** STAR-method questions about past projects and team collaboration.

---

## 3. Foundational Prerequisites
Data Science relies heavily on foundations from computer science and mathematics:

- **[[01_foundations/01_dsa|DSA]]:** While DS coding is rarely as intense as SWE coding, you need to understand Arrays, HashMaps, and basic sorting to manipulate data efficiently.
- **[[01_foundations/10_sql_database_deep_dive|SQL & Databases]]:** You must be a "SQL Ninja." You'll spend 60% of your time extracting data.
- **[[01_foundations/08_ai_for_engineers|AI & Machine Learning Foundations]]:** Linear algebra (matrix multiplication), Calculus (gradients), and basic ML frameworks.
- **[[01_foundations/02_sdlc|SDLC]]:** Version control (Git) and the lifecycle of data products.

---

## 4. Core Competencies

### A. Statistics & Probability
- **Distributions:** Normal (Gaussian), Bernoulli, Poisson (rare events), Exponential (time between events), and Binomial.
- **Hypothesis Testing:** P-values, Z-tests, T-tests, ANOVA (comparing 3+ groups), and Chi-square tests (categorical data).
- **Experimental Design:** Sample size calculation (Power Analysis), Type I ($\alpha$) and Type II ($\beta$) errors.
- **Probability:** Bayes' Theorem, Law of Large Numbers, Central Limit Theorem.
- **Causal Inference:** Selection bias, confounding variables, and matching methods.

### B. Machine Learning (Theory & Practice)
- **Supervised Learning:** 
  - *Regression:* Linear, Logistic, Lasso (L1), Ridge (L2), Elastic Net.
  - *Tree-based:* Decision Trees, Random Forests, XGBoost, LightGBM, CatBoost.
  - *Classification:* SVMs, K-Nearest Neighbors, Naive Bayes.
- **Unsupervised Learning:** K-Means, PCA (Principal Component Analysis), DBSCAN, Hierarchical Clustering.
- **Deep Learning:** Neural Networks, CNNs (Computer Vision), RNNs/LSTMs (Time series), Transformers (NLP).
- **Model Evaluation:** Precision, Recall, F1-Score, ROC-AUC, RMSE, MAE, Log Loss.

### C. The Python Data Stack
- **NumPy:** Vectorized operations, broadcasting, and linear algebra.
- **Pandas:** Data manipulation, merging, grouping, time-series analysis, and handling missing data.
- **Scikit-Learn:** Standard ML library for modeling, pipeline building, and cross-validation.
- **Visualization:** Matplotlib, Seaborn, and Plotly (for interactive charts).

---

## 5. Role-Specific Deep Dives

### Deep Dive 1: A/B Testing & Experimentation
A/B testing is the "Bread and Butter" of product-focused Data Science.
1. **The Setup:** Define the **Null Hypothesis ($H_0$)** and **Alternative Hypothesis ($H_1$)**.
2. **Metrics:** Pick a **Primary Metric** (e.g., Conversion Rate) and **Guardrail Metrics** (e.g., Latency, Uninstalls).
3. **Sample Size:** Use Power Analysis to determine how long the test needs to run. Factors include:
   - **Baseline Conversion Rate.**
   - **Minimum Detectable Effect (MDE).**
   - **Statistical Power (usually 80%).**
   - **Significance Level ($\alpha$, usually 5%).**
4. **Analysis:** After the test, check the P-value. If $p < 0.05$, you reject the null hypothesis.
5. **Advanced Topics:**
   - **Multi-Armed Bandits:** Efficiently exploring while exploiting.
   - **Network Effects:** Dealing with interference (e.g., Uber drivers).
   - **Metric Cannibalization:** When a new feature increases metric A but hurts metric B.

### Deep Dive 2: Machine Learning System Design - Search Ranking
Interviewers often ask you to "Design a Search Ranking System."
- **Objective:** Surface the most relevant content for a user's query.
- **Data Collection:** Queries, user clicks (CTR), item metadata.
- **Candidate Generation:** Retrieve 1000 items using BM25 or a simple embedding-based search.
- **Ranking Model:** A Learning-to-Rank (LTR) model using LambdaMART or a Deep Neural Network.
- **Features:**
  - **Query Features:** Length, language, intent.
  - **Item Features:** Popularity, age, quality score.
  - **User Features:** Past search history, location, device.
- **Evaluation:** NDCG (Normalized Discounted Cumulative Gain) is the industry standard for ranking.

### Deep Dive 3: Causal Inference in Industry
When you can't run an A/B test (e.g., "What is the effect of a specific marketing campaign?"), you use Causal Inference.
- **Selection Bias:** When the groups you are comparing are fundamentally different.
- **Confounders:** Variables that affect both the treatment and the outcome.
- **Techniques:**
  - **Propensity Score Matching:** Matching "similar" individuals in the treated and control groups.
  - **Regression Discontinuity Design (RDD):** Comparing individuals just above and just below a cutoff.
  - **Difference-in-Differences (DiD):** Comparing the trend of the treated group vs the trend of the control group.

---

## 6. Common Interview Questions & Detailed Walkthroughs

### A. Statistics & Logic Brainteasers
1. **"You flip a coin 10 times and get 10 heads. What is the probability the next flip is heads?"**
   - *Logic:* If the coin is fair, it's 0.5. If you suspect the coin is biased (Bayesian approach), you'd calculate the probability based on the prior belief that the coin is fair vs. the evidence.
2. **"Explain P-value to a non-technical manager."**
   - *Answer:* It's the probability of seeing the results we observed (or more extreme) if the "null hypothesis" (that there is no effect) were actually true. A small p-value means the results are unlikely to have happened by chance alone.
3. **"What is the difference between Bias and Variance?"**
   - *Answer:* Bias is the error from erroneous assumptions in the learning algorithm (underfitting). Variance is the error from sensitivity to small fluctuations in the training set (overfitting).
4. **"What is Simpson's Paradox?"**
   - *Answer:* A phenomenon in which a trend appears in several different groups of data but disappears or reverses when these groups are combined.

### B. SQL Coding Challenge
**Problem:** "Calculate the 7-day rolling average of revenue per day."
```sql
SELECT 
  date,
  revenue,
  AVG(revenue) OVER(
    ORDER BY date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) as rolling_avg
FROM daily_revenue;
```

### C. Python for Data Manipulation
**Problem:** "Given a Pandas DataFrame of sales, find the month with the highest growth rate."
```python
import pandas as pd
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month')['revenue'].sum().reset_index()
monthly_sales['growth'] = monthly_sales['revenue'].pct_change()
top_month = monthly_sales.loc[monthly_sales['growth'].idxmax()]
print(f"Top growth month: {top_month['month']} with {top_month['growth']*100:.2f}% growth")
```

---

## 7. Data Science at FAANG vs. Startups

### FAANG (Meta, Google, Amazon)
- **Specialization:** You will likely focus on one narrow area (e.g., "Ads Bidding Strategy").
- **Infrastructure:** You'll use sophisticated internal tools. You rarely build your own pipelines.
- **Rigor:** High emphasis on statistical significance and documented methodology.
- **The Interview:** Very standardized. Heavy focus on SQL and Product Sense.

### Startups (Seed to Series C)
- **Generalization:** You are the "Data Person." You'll build pipelines, write SQL, build models, and create dashboards.
- **Speed:** "Perfect is the enemy of good." Decisions are made on smaller samples and intuition.
- **Impact:** You have a direct line to the CEO/CTO and your models go to production in days.
- **The Interview:** More focused on your portfolio and your ability to "get things done."

---

## 8. Top 10 Essential Data Science Concepts
1. **Linear Algebra Foundations:** Matrix multiplication, Eigenvalues, and SVD.
2. **Probability Theory:** Bayes' Theorem and common distributions.
3. **Information Theory:** Entropy, Information Gain, and Cross-Entropy.
4. **The Normal Distribution:** Why the 68-95-99.7 rule matters.
5. **The Bias-Variance Tradeoff:** The heart of model optimization.
6. **Gradient Descent:** How machines "learn."
7. **Dimensionality Reduction:** PCA and t-SNE.
8. **Ensemble Methods:** Bagging (Random Forest) and Boosting (XGBoost).
9. **SQL Window Functions:** Essential for data extraction.
10. **Product Metrics:** CAC, LTV, Retention, and Churn.

---

## 9. Recommended Reading List
- *Practical Statistics for Data Scientists* by Peter Bruce & Andrew Bruce.
- *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* by Aurélien Géron.
- *Designing Data-Intensive Applications* by Martin Kleppmann.
- *Decode and Conquer* by Lewis Lin (for product/case questions).
- *The Elements of Statistical Learning* by Hastie, Tibshirani, and Friedman.

---

## 10. Recommended Roadmap
1. **Phase 1: Statistics (Weeks 1-2):** Review probability, p-values, and hypothesis testing.
2. **Phase 2: SQL (Weeks 3-4):** Solve 100+ problems on LeetCode/StrataScratch. Focus on joins and window functions.
3. **Phase 3: ML Theory (Weeks 5-7):** Understand the math behind Gradient Descent and Backpropagation.
4. **Phase 4: Case Studies (Weeks 8-9):** Practice structured thinking for product and strategy questions.
5. **Phase 5: Programming (Week 10):** Master Pandas and NumPy. Practice building end-to-end pipelines.

---

## 11. Data Science Glossary
- **Overfitting:** When a model performs perfectly on training data but poorly on unseen data.
- **Regularization:** Penalizing model complexity (L1/L2).
- **Hyperparameters:** Parameters not learned from data (e.g., learning rate).
- **Data Leakage:** When information from outside the training dataset is used to create the model.
- **Precision:** True Positives / (True Positives + False Positives).
- **Recall:** True Positives / (True Positives + False Negatives).
- **F1 Score:** Harmonic mean of Precision and Recall.

---

## 12. Mathematical Foundations for Data Science
You don't need to be a mathematician, but you must understand the "Engine" under the hood.

### Linear Algebra
- **Matrix Multiplication:** Essential for understanding how neural networks process data.
- **Eigenvalues & Eigenvectors:** The basis for **Principal Component Analysis (PCA)**. PCA finds the directions (eigenvectors) along which the data has the most variance.
- **Singular Value Decomposition (SVD):** Used in recommendation systems (Matrix Factorization) and image compression.

### Calculus
- **Gradients & Partial Derivatives:** How we calculate the "slope" of the loss function.
- **The Chain Rule:** The core of **Backpropagation**. It allows us to compute the gradient of the loss with respect to every weight in a deep network.

---

## 13. Deep Dive into Advanced Algorithms
### How XGBoost Works
XGBoost (Extreme Gradient Boosting) is the "King of Kaggle." 
1. **Decision Trees:** It builds trees sequentially.
2. **Residuals:** Each new tree tries to predict the *errors* (residuals) of the previous trees.
3. **Regularization:** Unlike standard GBM, XGBoost has built-in L1 and L2 regularization to prevent overfitting.
4. **Hardware Optimization:** It uses parallel processing and handling of sparse patterns to be extremely fast.

### The Transformer Architecture (High Level)
Even for general DS roles, knowing the Transformer is becoming mandatory.
- **Self-Attention:** Allows the model to look at other words in the input sequence to better understand a specific word (e.g., "The animal didn't cross the street because **it** was too tired" -> "it" refers to animal).
- **Encoder vs. Decoder:** BERT is an Encoder-only model (good for understanding text). GPT is a Decoder-only model (good for generating text).

---

## 14. Data Visualization Masterclass
"A picture is worth a thousand rows."
- **Anscombe's Quartet:** Four datasets that have identical simple descriptive statistics (mean, variance, correlation) but yet appear very different when graphed. This proves why visualization is critical.
- **The Lie Factor:** Edward Tufte's concept of how much a graphic deviates from the actual data.
- **Color Theory:** Using color to represent data (e.g., sequential for scale, diverging for positive/negative, qualitative for categories).

---

## 15. Handling "Big Data"
When data doesn't fit on one machine:
- **Apache Spark (PySpark):** A distributed computing framework. Key concept: **Lazy Evaluation** (Spark doesn't execute transformations until an action like `collect()` or `count()` is called).
- **Data Shuffling:** The process of moving data between partitions across the network. This is the most expensive operation in Spark.

---

## 16. More Detailed Interview Questions
**Q: What is the difference between an L1 and L2 penalty?**
- **L1 (Lasso):** Adds the absolute value of the weights to the loss function. It leads to **sparsity** (some weights become exactly zero), which performs feature selection.
- **L2 (Ridge):** Adds the square of the weights. it penalizes large weights but doesn't make them zero. It's better when you have many small effects.

**Q: Explain the ROC-AUC curve.**
- **ROC Curve:** Plots True Positive Rate (Sensitivity) vs. False Positive Rate (1 - Specificity) at various threshold settings.
- **AUC (Area Under the Curve):** A single number representing the probability that the model ranks a random positive example higher than a random negative example. AUC = 0.5 is random guessing; AUC = 1.0 is perfect.

---

## Related Topics

- [[01_foundations/01_dsa|Data Structures & Algorithms]]
- [[01_foundations/10_sql_database_deep_dive|SQL Masterclass]]
- [[02_role_tracks/06_data_engineer|Data Engineering (The Plumbing)]]
- [[04_company_guides/meta|Meta Data Science Guide]]
