# Phase 3.3 — Machine Learning Framework

## Objective

Develop a reproducible machine learning framework for PM2.5 analysis using environmental and climate predictors.

---

# Temporal Validation Strategy

A chronological split is used to avoid temporal leakage.

| Dataset | Period |
|---|---|
| Training | 2000–2020 |
| Validation | 2021–2023 |
| Testing | 2024–2025 |

---

# Forecasting Framework

Purpose:

Predict PM2.5 behaviour using historical and environmental variables.

Files:

```
data/

forecasting_train.csv

forecasting_validation.csv

forecasting_test.csv
```

---

# Attribution Framework

Purpose:

Investigate environmental relationships with PM2.5 variability.

Files:

```
data/

attribution_train.csv

attribution_validation.csv

attribution_test.csv
```

---

# Current Outputs

Available:

```
results/

model_evaluation_metrics.csv

prediction_results.csv

split_verification_report.csv
```

---

# Future Extensions

Planned:

- Random Forest modelling
- XGBoost modelling
- Feature importance analysis
- SHAP interpretation
- Model visualization
