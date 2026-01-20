# Weather Data Analyzer

A Python tool designed to analyze historical weather patterns, identify temperature extremes, simulate climate changes, and export visual reports.

## Key Features
* **Statistical Analysis**: Automatically calculates mean, max, and min for temperature and humidity.
* **Hot Day Categorization**: Flags "Hot Days" where temperatures exceed 30°C.
* **Climate Simulation**: Includes a simulator to project how an increase in global temperatures affects your specific dataset.
* **Advanced Visualization**: 
    * Time-series plots for temperature and humidity.
    * Correlation heatmaps to study the relationship between weather variables.
    * Comparison plots for original vs. simulated data.
* **PDF Export**: Automatically saves all generated plots into a single, multi-page PDF report (`weather_plots.pdf`).

## Tech Stack
* **Language**: Python 3.x
* **Libraries**: `pandas`, `matplotlib`, `seaborn`

## Data Structure
The script expects a CSV file with the following columns:
* `Date`: Date of observation.
* `Temperature`: Numerical values (Celsius).
* `Humidity`: Numerical values (Percentage).
