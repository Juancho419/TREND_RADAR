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
