# Phase 2 Results Summary

Computed from Dhaka daily air quality dataset (2000-2025, 9459 daily observations).

## Long-term Trend Analysis

Methods:
- Annual aggregation
- Mann-Kendall trend test
- Linear slope estimation

Significant increasing trends were detected for:
- PM2.5
- PM10
- NO2
- SO2
- Ozone
- AQI

## Correlation Analysis

Strong relationships:

- PM2.5 and PM10: Pearson r = 0.992
- PM2.5 and AQI: Pearson r = 0.962
- PM2.5 and SO2: Pearson r = 0.878

## PCA

Variance explained:

- PC1: 60.47%
- PC2: 22.90%
- PC3: 10.41%

The first three components explain 93.78% of variance.

## Change Point Analysis

Pettitt test detected:

- PM2.5 change point: 2009 (p=0.0206)
- NO2 change point: 2010 (p=0.0071)
- AQI change point: 2009 (p=0.0432)

## Next Steps

Phase 2 artifact tables and notebooks will be added with reproducible scripts.
