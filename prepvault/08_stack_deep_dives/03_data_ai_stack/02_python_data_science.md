---
title: Python for Data Science
tags: ['stack/data']
created: 2026-06-10
---

# Python for Data Science

## Overview
Data Science interviews test your statistical reasoning and your ability to build predictive models using Python's scientific stack. You need to demonstrate understanding of feature engineering, model selection, and evaluation — not just calling `fit()`.

## Scikit-Learn — The ML Toolbox

### Pipeline Architecture
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'salary', 'experience']),
    ('cat', OneHotEncoder(drop='first'), ['department', 'role']),
])

# Full model pipeline
pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, max_depth=10)),
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Feature Engineering
```python
# Feature interactions
df['age_salary_ratio'] = df['age'] / (df['salary'] + 1)

# Binning
pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['child', 'young', 'adult', 'senior'])

# Date features
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Text features
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=500, stop_words='english')
text_features = tfidf.fit_transform(df['description'])
```

### Evaluation & Validation
```python
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix

# Cross-validation
scores = cross_val_score(pipeline, X, y, cv=5, scoring='f1_macro')
print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")

# Hyperparameter tuning
param_grid = {
    'model__n_estimators': [50, 100, 200],
    'model__max_depth': [5, 10, 15, None],
    'model__min_samples_leaf': [1, 4, 8],
}
grid = GridSearchCV(pipeline, param_grid, cv=3, scoring='roc_auc', n_jobs=-1)
grid.fit(X_train, y_train)
```

## Statistical Methods

### Hypothesis Testing
```python
from scipy import stats

# A/B Test — are the two groups significantly different?
control = df[df.group == 'control']['conversion_rate']
treatment = df[df.group == 'treatment']['conversion_rate']

t_stat, p_value = stats.ttest_ind(treatment, control)
# p < 0.05 → reject null hypothesis
```

### Regression Diagnostics
```python
import statsmodels.api as sm

# OLS with summary statistics
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())  # R², p-values, VIF, Durbin-Watson, etc.
```

## Common Interview Questions

1. **"How do you handle class imbalance?"** — SMOTE (oversampling minority class), class weights, undersampling majority, or use metrics like PR-AUC instead of accuracy.

2. **"Explain the bias-variance tradeoff."** — High bias = underfitting (model too simple). High variance = overfitting (model too complex). Regularization (L1/L2) controls this.

3. **"How do you detect and handle outliers?"** — Z-score (>3 std from mean), IQR method (< Q1-1.5*IQR or > Q3+1.5*IQR), or domain-specific rules.

4. **"Explain cross-validation and why we use it."** — Splits data into k folds, trains on k-1 folds, evaluates on the held-out fold. Provides a more reliable estimate of model performance than a single train/test split.

## Related Topics
- [[08_stack_deep_dives/03_data_ai_stack/01_python_data_analytics|Python for Data Analytics]]
- [[08_stack_deep_dives/03_data_ai_stack/03_machine_learning|Machine Learning Mastery]]
- [[08_stack_deep_dives/03_data_ai_stack/index|Data & AI Stack Index]]
- [[02_role_tracks/04_ml_engineer|ML Engineer Track]]

## Resources
- [Scikit-Learn Docs](https://scikit-learn.org/stable/)
- [StatQuest on YouTube](https://www.youtube.com/@statquest)
- [Kaggle Learn](https://www.kaggle.com/learn)