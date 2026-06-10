---
type: role
tags: [role/ml, track]
created: 2024-06-10
---

# Machine Learning (ML) Engineer Interview Track

## 1. Role Overview
Machine Learning Engineering is the intersection of Data Science and Software Engineering. While a Data Scientist might focus on research and model building in a notebook, the ML Engineer is responsible for taking those models and making them work in a production environment—handling massive datasets, ensuring low latency, and managing the entire model lifecycle.

### The Interview Philosophy
ML Engineering interviews are "The Triple Threat." You will be tested on:
-   **Coding & DSA:** Standard software engineering rigor, usually in Python.
-   **ML Theory:** Understanding the "why" behind the algorithms (not just using Scikit-Learn).
-   **ML System Design:** How to build an end-to-end ML pipeline at scale.
-   **Math:** Linear algebra, calculus, and statistics are the language of ML.

### Typical Interview Stages
1.  **Technical Screen (60 min):** Algorithmic coding (often in Python) or a "take-home" ML project (e.g., "Build a classifier for this dataset").
2.  **Machine Learning Theory (45-60 min):** Deep dive into specific algorithms, math (calculus/linear algebra), and tradeoffs (bias/variance).
3.  **ML System Design (60 min):** Designing a system like "Uber's ETA prediction" or "Pinterest's image search."
4.  **Applied Coding:** Implementing an ML algorithm (like K-Means or a Neural Network layer) from scratch using only NumPy.
5.  **Behavioral / Project Deep Dive:** Discussing past ML projects, how you handled data quality issues, and how you measured business impact.

---

## 2. Foundational Prerequisites
You cannot be an ML Engineer without a strong mathematical and technical base:

-   **[[01_Foundations/01_DSA|DSA]]:** Focus on Vectors, Matrices, and Graph traversals. Understanding the complexity of matrix operations ($O(N^3)$ for naive multiplication).
-   **Mathematics for ML:** 
    -   **Linear Algebra:** Matrix multiplication, Eigenvalues, SVD (Singular Value Decomposition), Rank, Orthogonality, Vector spaces.
    -   **Calculus:** Gradients, Chain Rule, Partial Derivatives (essential for Backpropagation), Jacobians, Hessians.
    -   **Statistics & Probability:** Bayes Theorem, Distributions (Normal, Bernoulli, Poisson, Exponential), Hypothesis testing, p-values, Maximum Likelihood Estimation (MLE), Central Limit Theorem.
-   **[[01_Foundations/03_System_Design|System Design]]:** Specifically how it applies to data pipelines, high-throughput inference, and storage.
-   **[[01_Foundations/04_Operating_Systems|Operating Systems]]:** Understanding GPU memory management, multi-threading for data loading, and distributed computing resource allocation.
-   **[[01_Foundations/05_Networking|Networking]]:** Moving large datasets efficiently, optimizing inference latency over the network, understanding distributed training communication patterns.
-   **[[01_Foundations/02_SDLC|SDLC]]:** MLOps — versioning experiments, managing model deployment pipelines, CI/CD for ML systems.
-   **Python Proficiency:** Knowing the "Science Stack": NumPy, Pandas, Scikit-Learn, PyTorch/TensorFlow.

---

## 3. 2026-27 Ecosystem Focus: RAG & Agentic AI
The focus has shifted from raw training to **Model Operations (MLOps)** and Orchestration:
- **RAG Architectures**: Building semantic search with text embeddings and Vector Databases (Pinecone/Qdrant).
- **Agentic Workflows**: Custom LangChain/LlamaIndex flows with tool-calling capabilities.
- **MLOps**: Automated deployment, experiment tracking (MLflow), and production drift monitoring.

## 4. 12-Week Learning Pathway
- **Week 1-3: Core ML & Python Pipelining**: Master NumPy, Scikit-Learn, and evaluation metrics (Precision/Recall).
- **Week 4-7: LLMs & RAG Architectures**: Document chunking, Vector DBs, and LangChain agents.
- **Week 8-12: MLOps Deployments**: Containerizing models, FastAPI endpoints, and model monitoring.

## 5. Core Competencies

### A. Machine Learning Algorithms
-   **Supervised Learning:** 
    -   Linear/Logistic Regression (Regularization: L1, L2).
    -   Decision Trees, Random Forests (Bagging), Gradient Boosted Trees (XGBoost, LightGBM, CatBoost - Boosting).
    -   SVMs (Kernels: RBF, Polynomial; C and Gamma parameters).
    -   K-Nearest Neighbors ($O(ND)$ complexity).
-   **Unsupervised Learning:** K-Means Clustering, PCA (Principal Component Analysis), Anomaly Detection, Hierarchical Clustering, DBSCAN (Density-based).
-   **Deep Learning:** CNNs (Spatial data/Vision), RNNs/LSTMs (Sequential data), Transformers (Attention mechanism), GANs.

### B. Feature Engineering & Data Preprocessing
"Data is the fuel for ML."
-   **Data Cleaning:** Handling missing values (Mean/Median/Mode Imputation), outliers (Clipping, Z-score, IQR), and duplicates.
-   **Feature Scaling:** Normalization (0 to 1) vs. Standardization (mean=0, std=1). Why scale? (Gradient descent convergence).
-   **Encoding:** One-hot encoding, Label encoding, Target encoding (risk of leakage), Embeddings (learned representations).
-   **Handling Imbalanced Data:** SMOTE, Oversampling/Undersampling, focal loss, and precision-recall focus.

### C. Model Evaluation & Metrics
-   **Regression:** MSE (Mean Squared Error), MAE, RMSE, R-squared, MAPE.
-   **Classification:** Accuracy (misleading for imbalanced data), Precision, Recall, F1-Score, ROC-AUC, PR-AUC, Confusion Matrix.
-   **Ranking:** NDCG (Normalized Discounted Cumulative Gain), MRR (Mean Reciprocal Rank), Precision at K.

---

## 4. Role-Specific Deep Dives

### Deep Dive 1: Natural Language Processing (NLP)
The evolution of NLP is a common interview topic:
-   **Word Embeddings:** Word2Vec (Skip-gram vs CBOW), GloVe, FastText.
-   **Sequence Models:** RNNs, LSTMs, and GRUs. Understanding the vanishing gradient problem.
-   **Attention & Transformers:** The "Attention is All You Need" architecture. Self-attention, multi-head attention, and positional encoding.
-   **Pre-trained Models:** BERT (Encoder-only), GPT (Decoder-only), T5 (Encoder-Decoder).
-   **LLMs:** Tokenization (BPE), Fine-tuning (RLHF, SFT), and Prompt Engineering.

### Deep Dive 2: Recommendation Systems
Most tech giants (Amazon, Meta, Netflix) rely on these:
-   **Collaborative Filtering:** User-based vs Item-based.
-   **Matrix Factorization:** SVD, ALS (Alternating Least Squares).
-   **Content-Based Filtering:** Using item features for recommendations.
-   **Hybrid Models:** Deep learning approaches like Wide & Deep.
-   **Cold Start Problem:** How to recommend for new users/items (use popularity or demographics).

### Deep Dive 3: Computer Vision (CV)
-   **Convolutions:** How filters extract features (edges, shapes).
-   **Architectures:** ResNet (Residual connections), VGG, Inception, Vision Transformers (ViT).
-   **Tasks:** Image Classification, Object Detection (YOLO, Faster R-CNN), Semantic Segmentation (U-Net).

### Deep Dive 4: MLOps, Infrastructure, and Scalability
-   **Distributed Training:** Data Parallelism vs Model Parallelism.
-   **Model Serving:** Serving via REST/gRPC. Latency vs Throughput tradeoffs.
-   **Monitoring:** Detecting **Data Drift** (input changes) and **Concept Drift** (target relationship changes).
-   **Optimization:** Quantization (Float32 -> INT8), Pruning (removing weights), and Distillation.

---

## 5. Common Interview Questions & Detailed Walkthroughs

### Applied Coding 1: Implement Logistic Regression (NumPy)
**Problem:** Write a class that trains a logistic regression model.
**Key steps:**
1.  Initialize weights $w$ and bias $b$ to 0.
2.  Define `sigmoid(z) = 1 / (1 + exp(-z))`.
3.  **Forward:** `y_pred = sigmoid(X.dot(w) + b)`.
4.  **Loss (Cross-Entropy):** `J = -mean(y*log(y_pred) + (1-y)*log(1-y_pred))`.
5.  **Backward:** `dw = X.T.dot(y_pred - y) / m`, `db = sum(y_pred - y) / m`.
6.  **Update:** `w -= alpha * dw`, `b -= alpha * db`.

### ML System Design: "Design a News Feed Ranking System"
1.  **Objective:** Rank posts to maximize user engagement (likes, shares, time spent).
2.  **Architecture:**
    -   **Retrieval:** Use simple models or heuristics to get 1000 candidate posts.
    -   **Ranking:** Use a deep neural network to score each post.
    -   **Re-ranking:** Apply diversity filters (no two posts from same user) and business rules.
3.  **Features:** User history, post age, post type (video/image), social connection strength.
4.  **Metric:** Online A/B test for Daily Active Users (DAU) and CTR.

---

## 6. Machine Learning Glossary
-   **Overfitting:** High variance; model learns noise in training data.
-   **Underfitting:** High bias; model is too simple to learn the pattern.
-   **Regularization:** Techniques (L1, L2, Dropout) used to prevent overfitting.
-   **Backpropagation:** Algorithm for computing gradients of the loss function with respect to weights.
-   **Gradient Descent:** Optimization algorithm to minimize the loss.

---

## 7. Company-Specific Patterns

### Google
-   **Focus:** First principles. "Why do we use the log-sum-exp trick?"
-   **Tip:** Master TensorFlow and JAX. Be ready for deep math.

### Meta
-   **Focus:** Applied ML at scale. Recommendation systems for billions of users.
-   **Tip:** Understand sparse features and high-dimensional data handling.

---

## 8. Detailed Roadmap: How to Prepare
1.  **Weeks 1-2:** Math (Linear Algebra, Stats, Calculus).
2.  **Weeks 3-5:** Classic ML (Linear models, Trees, Clustering).
3.  **Weeks 6-8:** Deep Learning (CNNs, RNNs, Transformers). PyTorch/TensorFlow mastery.
4.  **Weeks 9-10:** ML System Design and MLOps.
5.  **Mocks:** Practice 10+ system design cases and 10+ theory sessions.

## Related Topics
-   [[01_Foundations/03_System_Design|System Design Foundations]]
-   [[02_Role_Tracks/06_Data_Engineer|Data Engineering for ML]]
-   [[05_Templates/algorithm_template|Algorithm Implementation Template]]
