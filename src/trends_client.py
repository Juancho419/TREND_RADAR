"""
Dummy trends client for the Trend Radar MVP.

This is TEMPORARY test data and WILL be replaced by real Google Trends logic.
It does NOT define which topics the Radar will support, it only simulates shape.
"""

from typing import List

from models import TrendTopic


def fetch_trend_data(topic: TrendTopic, region: str, time_range: str) -> dict:
    """
    Placeholder function to fetch trend data for a single topic.

    Parameters:
    - topic: TrendTopic object (name and category)
    - region: country code, e.g. "CO"
    - time_range: string like "12_months"

    Returns:
    - A dictionary with the expected structure.
    """
    # Simple dummy time series (0–100)
    interest_over_time: List[int] = [10, 20, 35, 50, 70]

    interest_by_region = [
        {"name": "Bogotá", "value": 80},
        {"name": "Medellín", "value": 65},
    ]

    related_queries = [
        f"{topic.name} use cases",
        f"{topic.name} in {region}",
    ]

    return {
        "topic_name": topic.name,
        "region": region,
        "time_range": time_range,
        "interest_over_time": interest_over_time,
        "interest_by_region": interest_by_region,
        "related_queries": related_queries,
    }
