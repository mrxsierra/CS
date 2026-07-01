---
title: MLOps & Model Deployment
tags: ['stack/data']
created: 2026-06-10
---

# MLOps & Model Deployment

## Overview
MLOps is what separates "notebook ML" from "production ML." Interviews test your understanding of model serving, monitoring, experiment tracking, and the full ML lifecycle.

## MLflow — Experiment Tracking & Model Registry

### Tracking Experiments
```python
import mlflow

mlflow.set_experiment("customer_churn_v2")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("model_type", "XGBoost")
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("max_depth", 10)
    
    # Log metrics
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_metric("f1_score", 0.89)
    mlflow.log_metric("roc_auc", 0.95)
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Log artifacts
    mlflow.log_artifact("feature_importance.png")
```

### Model Registry — Staging to Production
```python
# Register model
mlflow.register_model("runs:/<run_id>/model", "customer_churn_model")

# Transition stages: None → Staging → Production → Archived
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="customer_churn_model",
    version=3,
    stage="Production"
)
```

## Model Serving Patterns

### Real-time Serving (REST API)
```python
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow

app = FastAPI()
model = mlflow.sklearn.load_model("models:/customer_churn_model/Production")

class Input(BaseModel):
    age: float
    salary: float
    tenure: float

@app.post("/predict")
async def predict(input: Input):
    features = [[input.age,_input.salary,_input.tenure]]
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return {"prediction": int(prediction), "probability": float(probability)}
```

### Batch Inference (Scheduled)
```python
# Spark batch prediction
df = spark.read.parquet("s3://data/unlabeled/")
model = mlflow.spark.load_model("models:/churn_model/Production")
predictions = model.transform(df)
predictions.write.mode("overwrite").parquet("s3://data/predictions/")
```

### Streaming Inference (Real-time, Event-Driven)
```
Events → Kafka → Flink/Spark Streaming → Model → Output Topic → Database
```

## Model Monitoring

### Drift Detection
| Drift Type | Description | Detection Method |
|-----------|-------------|-----------------|
| **Data Drift** | Input distribution changes | KS-test, PSI (Population Stability Index) |
| **Concept Drift** | Relationship X→Y changes | Monitor accuracy over time windows |
| **Label Drift** | Target distribution changes | Compare predicted vs. actual distributions |

```python
from scipy.stats import ks_2samp

def detect_drift(reference_data, production_data, threshold=0.05):
    stat, p_value = ks_2samp(reference_data['age'], production_data['age'])
    return {
        'drifted': p_value < threshold,
        'p_value': p_value,
        'statistic': stat
    }
```

### Performance Monitoring
| Metric | Warning | Critical |
|--------|---------|----------|
| **Latency (p99)** | > 200ms | > 500ms |
| **Throughput** | < 100 req/s | < 50 req/s |
| **Error Rate** | > 1% | > 5% |
| **Prediction Confidence** | Avg < 0.7 | Avg < 0.5 |

## The ML Lifecycle

```
Data Collection → Data Validation → Feature Engineering → Training → Evaluation → Deployment → Monitoring
      ↑                                                                                             |
      └───────────────────────────── Retrain (if drift detected) ──────────────────────────────────┘
```

### Key MLOps Practices
- **Version everything**: Data, code, model, and hyperparameters
- **Reproducibility**: Pin dependencies, use Docker, seed random generators
- **A/B testing**: Serve multiple models, compare business metrics
- **Rollback**: Keep previous model versions ready for fast rollback
- **Feature Store**: Centralized feature computation + serving (Feast, Tecton)

## Common Interview Questions

1. **"What is the difference between batch and real-time inference?"** — Batch: process large volumes periodically (e.g., nightly recommendations), lower cost. Real-time: predict on individual requests (e.g., fraud detection), needs low latency, higher infrastructure cost.

2. **"How do you detect concept drift?"** — Track model accuracy over sliding time windows. If accuracy drops significantly compared to a reference window, concept drift likely occurred. Set up automated retraining triggered by drift alerts.

3. **"Explain A/B testing for ML models."** — Route a percentage of traffic to the new model (treatment) and compare against the current model (control) on business metrics (revenue, engagement). Use statistical significance to decide if the new model is better.

4. **"What metrics would you monitor for a deployed model?"** — Prediction latency, throughput, error rate, data drift (PSI on input features), concept drift (accuracy over time), and business KPIs impacted by the model.

## Related Topics
- [[08_stack_deep_dives/03_data_ai_stack/05_llms_langchain|LLMs & AI Orchestration]]
- [[08_stack_deep_dives/03_data_ai_stack/03_machine_learning|Machine Learning Mastery]]
- [[08_stack_deep_dives/03_data_ai_stack/index|Data & AI Stack Index]]
- [[02_role_tracks/04_ml_engineer|ML Engineer Track]]

## Resources
- [MLflow Docs](https://mlflow.org/docs/latest/index.html)
- [Google MLOps Guide](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [Feast Feature Store](https://feast.dev/)