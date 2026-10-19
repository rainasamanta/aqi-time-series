# AQI Time Series Analysis & Forecasting
### An end-to-end time series analysis of daily Air Quality Index (AQI) data across 4 Indian cities, featuring exploratory analysis, a Diwali impact study, SARIMA forecasting benchmarked against simple baselines, and an interactive Streamlit dashboard.

## Cities
Bengaluru | Delhi | Kolkata | Mumbai

## Study Period
January 2019 - March 2025 (9,116 daily city AQI records)

## Objectives
- Explore AQI patterns across cities
- Measure how AQI changes around Diwali
- Investigate seasonality and trends
- Build SARIMA forecasting models
- Test whether SARIMA beats simple seasonal baselines

## Dashboard
[Live Streamlit App](https://aqi-time-series.streamlit.app/)

## Analysis Pipeline
1. **Data cleaning and EDA:** date parsing, duplicate and missing-date checks, CPCB AQI categories, distribution and seasonal plots
2. **Diwali impact study:** festival-period AQI (5 days) compared with the average of the week before and the week after, so the normal seasonal rise cancels out; Wilcoxon signed-rank test on the six yearly impacts
3. **Model selection:** STL decomposition, ADF and KPSS tests, OCSB and Canova-Hansen seasonal tests, AIC grid search on 2019-2022, model constraint setting chosen on a 2023 validation year
4. **Forecasting:** final models refitted on 2019-2023, 15-month forecast (Jan 2024 - Mar 2025) compared with two baselines (same month last year, and each month's 2019-2023 average), plus convergence and Ljung-Box residual checks

## Data Split
| Part | Period | Used for |
|---|---|---|
| Train | Jan 2019 - Dec 2022 (48 months) | AIC grid search |
| Validation | Jan - Dec 2023 (12 months) | Choosing constrained vs unconstrained models |
| Test | Jan 2024 - Mar 2025 (15 months) | Final evaluation, used once |

## SARIMA Models
| City | Model | Constrained |
|---|---|---|
| Bengaluru | SARIMA(1,0,1)(1,0,0,12) | Yes |
| Delhi | SARIMA(0,1,1)(0,1,1,12) | Yes* |
| Kolkata | SARIMA(1,1,0)(1,0,0,12) | No |
| Mumbai | SARIMA(1,1,0)(1,0,0,12) | No |

\*Delhi was chosen as unconstrained on the validation year, but its final refit did not converge, so it was refitted with constraints (a safety rule based on the training fit only).

## Forecast Performance
SARIMA compared with two simple baselines on the same test period (lower MAE is better; best per city in bold).

| City | SARIMA MAE | SARIMA R² | Last Year MAE | Last Year R² | Monthly Avg MAE | Monthly Avg R² |
|---|---|---|---|---|---|---|
| Bengaluru | 9.90 | 0.453 | 8.65 | 0.625 | **4.36** | **0.898** |
| Delhi | 26.44 | 0.877 | 22.38 | 0.880 | **21.87** | **0.904** |
| Kolkata | 39.46 | 0.301 | **12.05** | **0.887** | 29.85 | 0.444 |
| Mumbai | **23.23** | **0.417** | 38.22 | -0.610 | 24.10 | 0.299 |

- **Last Year:** each month forecast as the same month in 2023
- **Monthly Avg:** each month forecast as its 2019–2023 average

## Key Findings
- Delhi had unhealthy air (AQI above 200) on 46.6% of days, compared with 0% in Bengaluru
- No city showed a consistent Diwali effect: festival AQI rose in only 3-4 of 6 years per city, and a Wilcoxon test found no significant effect (p ≥ 0.438 per city, p = 0.726 pooled)
- Simple seasonal baselines beat SARIMA in 3 of 4 cities; SARIMA was most accurate only in Mumbai, by 3.6% (MAE 23.23 vs 24.10)
- AQI is so seasonal that each month's historical average forecasts very well (R² 0.898 in Bengaluru, 0.904 in Delhi)
- Kolkata's SARIMA forecast was too low in all 15 test months; the same-month-last-year baseline performed best (R² = 0.887)
- Mumbai's January-March AQI fell 38.1% from 2023 to 2024 (181.3 to 112.2), a level shift that made both baselines over-forecast
- With only six years of monthly data, SARIMA results were sensitive to the model selection window, and several seasonal models failed to converge
