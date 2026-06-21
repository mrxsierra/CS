---
title: Python for Data Analytics
tags: ['stack/data']
created: 2026-06-10
---

# Python for Data Analytics

## Overview
Python is the default language for data work. For analytics interviews, you need to demonstrate proficiency with Pandas, NumPy, and visualization libraries at production scale — not just Jupyter notebook tinkering.

## Pandas — The Data Workhorse

### DataFrame Operations
```python
import pandas as pd

# Reading data
df = pd.read_csv('sales.csv', parse_dates=['date'])

# Filtering & selection
df[df.revenue > 1000]                       # Boolean indexing
df.loc[df.region == 'NA', ['date', 'revenue']]  # Label-based
df.iloc[10:20, 0:3]                         # Position-based

# Grouped operations
monthly = df.groupby(df.date.dt.to_period('M')).agg({
    'revenue': 'sum',
    'orders': 'count',
    'customer_id': 'nunique'
}).rename(columns={'customer_id': 'unique_customers'})

# Pivot tables
pivot = df.pivot_table(
    index='region', columns='product_category', 
    values='revenue', aggfunc='sum'
)
```

### Chaining vs. Mutation
```python
# Best practice: method chaining (returns new objects)
result = (df
    .query('revenue > 0')
    .assign(revenue_eur=lambda df: df.revenue * 0.85)
    .groupby('region')
    .agg({'revenue_eur': 'sum', 'order_id': 'count'})
    .sort_values('revenue_eur', ascending=False)
)
```

### Common Interview Patterns
```python
# Rolling window calculations
df['revenue_ma_7d'] = df.revenue.rolling(7).mean()

# Cumulative sums
df['cumulative_revenue'] = df.revenue.cumsum()

# Handling missing data
df.fillna({'revenue': df.revenue.median()}, inplace=False)

# Merges — understanding join types
pd.merge(users, orders, on='user_id', how='left')  # All users, even without orders
pd.merge(users, orders, on='user_id', how='inner')  # Only users with orders
```

### Interview Question: "Calculate daily active users (DAU) from event logs"
```python
events = pd.read_csv('events.csv')
events['date'] = pd.to_datetime(events['timestamp']).dt.date
dau = events.groupby('date')['user_id'].nunique()
```

## NumPy — Performance Foundation

```python
import numpy as np

# Vectorized operations (no Python loops!)
arr = np.array([1, 2, 3, 4, 5], dtype=np.float64)
arr * 2 + 1          # Fast C-level operations
arr.mean(), arr.std(), arr.sum()

# Broadcasting
matrix = np.random.randn(1000, 100)
normalized = (matrix - matrix.mean(axis=0)) / matrix.std(axis=0)

# Boolean masking
arr[arr > 0]         # Filter positive values
```

## Visualization
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Quick EDA — pairplot
sns.pairplot(df, hue='segment')

# Time series — trend + seasonality
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(df.date, df.revenue, label='Daily')
ax.plot(df.date, df.revenue.rolling(7).mean(), label='7d MA', linewidth=2)
```

## Performance Tips
- Avoid `iterrows()` — use vectorized operations
- Use `pd.read_csv(..., dtype={'col': 'int32'})` for memory efficiency
- Use `category` dtype for low-cardinality string columns
- Profile with `df.info(memory_usage='deep')`

## Related Topics
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/02_Python_Data_Science|Python for Data Science]]
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/Index|Data & AI Stack Index]]
- [[02_Role_Tracks/06_Data_Engineer|Data Engineering Track]]

## Resources
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)