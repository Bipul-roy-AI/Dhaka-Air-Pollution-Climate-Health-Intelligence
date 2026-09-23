# Phase 3 — Climate Integration

## Objective

Integrate air pollution observations with satellite remote sensing and climate reanalysis datasets.

---

# Data Sources

## Remote Sensing

- MODIS Aerosol Optical Depth (AOD)
- MODIS Land Surface Temperature (LST)
- Sentinel-5P NO2

## Climate Data

ERA5-Land variables:

- Temperature
- Dewpoint temperature
- Rainfall
- Surface pressure
- Wind speed

---

# Processing Workflow

```
Remote Sensing Data
        ↓
Climate Data Extraction
        ↓
Monthly Aggregation
        ↓
Feature Engineering
        ↓
Statistical Analysis
```

---

# Statistical Analysis

Implemented:

- Summary statistics
- Pearson correlation
- Spearman correlation
- Seasonal analysis
- Trend analysis
- Lag correlation
- Partial correlation
- Variance Inflation Factor (VIF)

---

# Results

Stored in:

```
results/

phase3_2_3_results/

phase3_2_4_results/
```

Outputs include:

- Correlation matrices
- Climate-pollution relationships
- Feature statistics
- Multicollinearity assessment

---

# Figures

Stored in:

```
figures/
```

Including:

- PM2.5 trend analysis
- Seasonal patterns
- Extreme pollution analysis
