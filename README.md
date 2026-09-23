# Dhaka Air Pollution Climate Health Intelligence

## Overview

The Dhaka Air Pollution Climate Health Intelligence Project is a long-term environmental data science framework investigating air pollution dynamics in Dhaka, Bangladesh.

The project integrates:

- Ground-based PM2.5 observations
- Satellite remote sensing products
- Climate reanalysis datasets
- Statistical time-series analysis
- Machine learning preparation workflows

Study period: **2000–2025**

---

# Research Objectives

This project investigates:

1. Long-term PM2.5 pollution behaviour
2. Seasonal pollution variability
3. Relationships between pollution and climate variables
4. Satellite-based pollution indicators
5. Machine learning frameworks for PM2.5 analysis

---

# Research Workflow

```
Air Quality Data
        ↓
Data Quality Control
        ↓
Pollution Dynamics Analysis
        ↓
Remote Sensing + Climate Integration
        ↓
Feature Engineering
        ↓
Machine Learning Framework
        ↓
Model Evaluation
```

---

# Repository Structure

## Phase 2 — Pollution Dynamics

Contains:

- Long-term pollution analysis
- Trend analysis
- PCA analysis
- Correlation analysis

## Phase 3 — Climate Integration

Contains:

- MODIS AOD integration
- MODIS LST integration
- Sentinel-5P NO2 integration
- ERA5-Land climate variables
- Feature engineering
- Climate-pollution relationship analysis

## Phase 3.3 — Machine Learning Framework

Contains:

- Temporal train/validation/test splits
- Forecasting datasets
- Attribution datasets
- Model evaluation outputs

---

# Key Analyses Completed

## Pollution Dynamics

Methods:

- Descriptive statistics
- Trend analysis
- PCA
- Correlation analysis
- Seasonal analysis

## Climate Integration

Variables:

- PM2.5
- AOD
- LST
- NO2
- Temperature
- Rainfall
- Pressure
- Wind speed

Methods:

- Pearson correlation
- Spearman correlation
- Lag correlation
- Partial correlation
- VIF analysis

---

# Machine Learning Framework

A strict temporal split is used:

| Dataset | Period |
|---|---|
| Training | 2000–2020 |
| Validation | 2021–2023 |
| Testing | 2024–2025 |

Two modelling perspectives:

## Forecasting Framework

Predict future PM2.5 behaviour using historical and environmental variables.

## Attribution Framework

Investigate relationships between environmental drivers and PM2.5 variability.

---

# Figures

Repository figures include:

- Long-term PM2.5 trends
- Seasonal pollution cycle
- Observation coverage
- Extreme pollution frequency analysis

---

# Reproducibility

All datasets, methods, scripts, figures, and results are organized by research phase.
