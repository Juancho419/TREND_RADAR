"""
Simple analyzer for the Trend Radar MVP.

Right now it:
- calls the trends client to get a dummy data structure
- uses fake numbers to build TrendResult objects

Later, the fake numbers will be replaced with real metrics
computed from the trend data.
"""

from typing import List

from models import TrendTopic, TrendResult
from trends_client import fetch_trend_data

def classify_trend(growth_pct: float) -> str:
    """
    Classify the trend_status based on growth_pct.

    Rules (first version):
    - cold:    growth_pct < 5
    - warm:    5 <= growth_pct < 15
    - hot:     15 <= growth_pct < 30
    - boiling: growth_pct >= 30
    """
    if growth_pct < 5.0:
        return "cold"
    if growth_pct < 15.0:
        return "warm"
    if growth_pct < 30.0:
        return "hot"
    return "boiling"


def analyze_topics(topics: List[TrendTopic], region: str, time_range: str) -> List[TrendResult]:
    """
    Temporary analyzer.

    It receives:
    - topics: list of TrendTopic
    - region: country code, e.g. "CO"
    - time_range: string like "12_months"

    For each topic it:
    - calls fetch_trend_data (dummy for now)
    - prints a small debug line
    - creates a TrendResult with fake numeric values
    """
    results: List[TrendResult] = []

    for index, topic in enumerate(topics, start=1):
        # 1) Call the trends client (dummy implementation for now)
        trend_data = fetch_trend_data(topic, region=region, time_range=time_range)

        print(
            f"[DEBUG] Fetched trend data for '{topic.name}' "
            f"(region={trend_data['region']}, time_range={trend_data['time_range']})"
        )

        # 2) Use interest_over_time to compute current_interest and growth_pct
        series = trend_data.get("interest_over_time", [])

        if len(series) >= 2:
            start_value = float(series[0])
            end_value = float(series[-1])
            current_interest = int(end_value)

            if start_value > 0:
                growth_pct = ((end_value - start_value) / start_value) * 100.0
            else:
                # Avoid division by zero: if start is 0, treat growth as 0 for now
                growth_pct = 0.0
        elif len(series) == 1:
            # Only one point: current_interest is that value, no growth information
            current_interest = int(series[0])
            growth_pct = 0.0
        else:
            # Empty series: no data
            current_interest = 0
            growth_pct = 0.0

        trend_status = classify_trend(growth_pct)

        result = TrendResult(
            topic=topic,
            trend_status=trend_status,
            current_interest=current_interest,
            growth_pct=growth_pct,
            top_regions=[],
            related_queries=[],
        )
        results.append(result)

    return results
