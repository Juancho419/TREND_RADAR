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

        # 2) Very simple fake logic just to have different numbers
        current_interest = 20 * index
        growth_pct = 5.0 * index
        trend_status = "warm"

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
