---
title: Machine Learning Mastery
tags: ['stack/data']
created: 2026-06-10
---

# Machine Learning Mastery

## Overview
ML interviews test your theoretical understanding of algorithms — why they work, when to use them, and how to tune them. Be ready to derive loss functions, explain gradient descent, and compare model families.

## Supervised Learning Algorithms

### Linear & Logistic Regression
```python
# Linear: y = wx + b (continuous output)
# Logistic: P(y=1) = 1 / (1 + e^-(wx + b)) (binary classification)

# Loss functions
# Linear regression: MSE = 1/n * sum(y - y_pred)²
# Logistic regression: BCE = -1/n * sum(y * log(p) + (1-y) * log(1-p))

# Regularization
# L1 (Lasso): Adds |w| to loss → sparse weights (feature selection)
# L2 (Ridge): Adds w² to loss → small but non-zero weights
# ElasticNet: Combines L1 + L2
```

### Decision Trees & Ensemble Methods
| Algorithm | Type | Key Idea | Strengths |
|-----------|------|----------|-----------|
| **Decision Tree** | Single | Recursive splits minimizing impurity | Interpretable |
| **Random Forest** | Bagging | Train many trees on bootstrapped data | Reduces variance |
| **XGBoost / LightGBM** | Boosting | Sequentially train trees on residuals | Highly accurate |
| **CatBoost** | Boosting | Native categorical handling | Good for mixed data |

```python
# Gradient Boosting — conceptual pseudocode
model = 0
for i in range(n_estimators):
    residuals = y - model.predict(X)          # Compute errors
    weak_tree = train_tree(X, residuals)      # Fit tree to errors
    model += learning_rate * weak_tree        # Add to ensemble
```

### Support Vector Machines (SVMs)
- Finds the **maximum margin hyperplane** between classes
- **Kernel trick**: Maps data to higher dimensions without explicit computation
  - RBF kernel: `K(x, y) = exp(-gamma * ||x - y||²)` — most common, works well for non-linear data
  - Polynomial kernel: `K(x, y) = (x·y + c)^d`
- **C parameter**: Tradeoff between wide margin and misclassification (high C = harder margin)
- **Gamma parameter**: Influence radius of a single training example (high gamma = complex, overfit risk)

### K-Nearest Neighbors (KNN)
```python
# KNN does NOT train a model — it memorizes the training data
# At prediction: find k closest points, vote on label
# Time complexity: O(ND) per prediction (slow for large datasets!)
# Use KD-Tree or Ball-Tree for acceleration
```

## Unsupervised Learning

### K-Means Clustering
```python
# Steps:
# 1. Initialize k centroids randomly
# 2. Assign each point to nearest centroid
# 3. Recompute centroids as mean of assigned points
# 4. Repeat until convergence

# Choosing k: Elbow method (inertia), Silhouette score, Gap statistic
```

### PCA (Principal Component Analysis)
- **Purpose**: Dimensionality reduction, noise reduction, visualization
- **How it works**: Finds axes (principal components) that maximize variance
- **Key concept**: Eigenvalues = amount of variance captured by each component
- **Scree plot**: Shows variance explained per component — look for the "elbow"

## Model Evaluation — Deep Dive

### Classification Metrics
| Metric | Formula | When to Use |
|--------|---------|-------------|
| **Accuracy** | (TP+TN)/(P+N) | Balanced classes |
| **Precision** | TP/(TP+FP) | Minimize false positives (spam detection) |
| **Recall** | TP/(TP+FN) | Minimize false negatives (cancer screening) |
| **F1 Score** | 2·P·R/(P+R) | Imbalanced classes, both FP and FN matter |
| **ROC-AUC** | Area under TPR vs. FPR curve | Ranking quality, threshold-independent |
| **PR-AUC** | Area under Precision vs. Recall | Highly imbalanced classes |

### Regression Metrics
- **MSE** / **RMSE**: Sensitive to outliers (squared error)
- **MAE**: Robust to outliers (absolute error)
- **R²**: Proportion of variance explained (1.0 = perfect, 0.0 = mean baseline)
- **MAPE**: Percentage error — scale-independent but undefined for zero values

## Common Interview Questions

1. **"Explain the difference between Bagging and Boosting."** — Bagging (Random Forest): parallel training on bootstrap samples, reduces variance. Boosting (XGBoost): sequential training on residuals, reduces bias → can overfit if not regularized.

2. **"What is the bias-variance tradeoff?"** — Simple models have high bias (underfit). Complex models have high variance (overfit). Goal: find the sweet spot that minimizes total error.

3. **"How do you detect overfitting?"** — Training accuracy >> Validation accuracy. Solution: more data, regularization (L1/L2), simpler model, cross-validation, early stopping.

4. **"What is the difference between L1 and L2 regularization?"** — L1 adds absolute value penalty → sparse solutions, feature selection. L2 adds squared penalty → small weights, better when all features are relevant.

## Related Topics
- [[08_stack_deep_dives/03_data_ai_stack/04_deep_learning|Deep Learning Foundations]]
- [[08_stack_deep_dives/03_data_ai_stack/02_python_data_science|Python for Data Science]]
- [[08_stack_deep_dives/03_data_ai_stack/index|Data & AI Stack Index]]
- [[02_role_tracks/04_ml_engineer|ML Engineer Track]]

## Resources
- [Scikit-Learn ML Map](https://scikit-learn.org/stable/machine_learning_map.html)
- [Elements of Statistical Learning (Hastie)](https://hastie.su.domains/ElemStatLearn/)
- [XGBoost Docs](https://xgboost.readthedocs.io/)