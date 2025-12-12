## First CSV report structure

The main CSV/Excel report should contain one row per topic with at least these columns:

- topic_name
- category
- trend_status      (cold / warm / hot / boiling)
- current_interest  (last value from Google Trends)
- growth_pct        (percentage change over the selected time range)
- top_regions       (comma-separated list of top 3 regions or cities)
- top_related_queries   (comma-separated list of 3–5 related queries)

## Trend status rules (conceptual)

For each topic we assign a trend_status based on Google Trends data:

- cold: low interest and flat or decreasing over time
- warm: medium interest and slight positive growth
- hot: clear positive growth over the last months
- boiling: very strong and recent spike in interest

The exact numeric thresholds will be decided later, after we inspect real data.

## Numeric rules for trend_status (first version)

For now we will classify topics only using growth_pct:

- cold:   growth_pct < 5%
- warm:   5% <= growth_pct < 15%
- hot:    15% <= growth_pct < 30%
- boiling: growth_pct >= 30%

These thresholds are experimental and will probably be adjusted
once we start using real data from Google Trends.

## Shape of trend_data (first version)

The function `fetch_trend_data(topic, region, time_range)` will return
a dictionary with this structure:

- topic_name: string
- region: string
- time_range: string

- interest_over_time: list of integers (0–100)
  Example: [10, 20, 30, 40, 50]

- interest_by_region: list of dicts with:
  - name: region or city name
  - value: integer (0–100)
  Example:
    [
      {"name": "Bogotá", "value": 80},
      {"name": "Medellín", "value": 70}
    ]

- related_queries: list of strings with related search queries
  Example:
    ["how to use AI at work", "AI tools for small business"]

## Google Trends integration plan (experimental branch)

Goal:
Use real Google Trends data for each topic without changing the
analyzer or the reporter.

Design:

- A new module `trends_google.py` will contain the real integration.

- It will expose a single function:

  ```python
  fetch_trend_data_google(topic_name: str, region: str, time_range: str) -> dict
  ```



