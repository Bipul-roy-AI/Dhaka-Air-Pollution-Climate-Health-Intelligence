"""
ERA5 Daily Data Extraction Template

Requires:
- CDS API account
- ~/.cdsapirc configuration
- cdsapi Python package

Variables:
- 2m temperature
- Relative humidity
- 10m wind components
- Total precipitation
- Boundary layer height
- Surface pressure

Download period:
2000-2025
Study area:
Dhaka, Bangladesh
"""

import cdsapi

client = cdsapi.Client()

client.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '2m_temperature',
            '2m_relative_humidity',
            '10m_u_component_of_wind',
            '10m_v_component_of_wind',
            'total_precipitation',
            'boundary_layer_height',
            'surface_pressure'
        ],
        'year': [str(y) for y in range(2000, 2026)],
        'month': [f'{m:02d}' for m in range(1,13)],
        'day': [f'{d:02d}' for d in range(1,32)],
        'time': ['00:00','06:00','12:00','18:00'],
        'area': [24.0, 90.2, 23.6, 90.6],
        'format': 'netcdf'
    },
    'era5_dhaka_daily.nc'
)
