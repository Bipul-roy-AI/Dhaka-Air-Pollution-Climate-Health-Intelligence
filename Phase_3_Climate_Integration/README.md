# Phase 3 — Climate Integration

## Objective

Integrate meteorological drivers with Dhaka air pollution observations (2000-2025).

## Workflow

1. Acquire ERA5 reanalysis data
2. Quality control climate variables
3. Merge climate and pollution datasets
4. Analyze climate-pollution relationships
5. Develop predictive models

## ERA5 Variables

Daily variables:

- 2m temperature
- 2m relative humidity
- 10m wind components
- Total precipitation
- Boundary layer height
- Surface pressure

## Study Location

Dhaka, Bangladesh

Approximate coordinates:

Latitude: 23.81
Longitude: 90.41

## Planned Outputs

```
Phase_3_Climate_Integration/

├── climate_data/
│   └── era5_dhaka_daily_2000_2025.csv
│
├── preprocessing/
│   └── climate_quality_check.ipynb
│
├── analysis/
│   ├── climate_pollution_correlation.ipynb
│   └── climate_feature_engineering.ipynb
│
└── results/
    ├── climate_summary.csv
    └── correlation_matrix.csv
```
