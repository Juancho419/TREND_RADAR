"""
Trends client for the Trend Radar MVP.

This module will be responsible for talking to Google Trends
(or any other data source) and returning clean data for analysis.
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

    For now, this function returns a dummy dictionary, just to define the shape
    of the data we expect.
    """
    # Temporary dummy data structure with realistic shape
    interest_over_time: List[int] = [10, 20, 30, 40, 50]
    interest_by_region = [
        {"name": "Bogotá", "value": 80},
        {"name": "Medellín", "value": 70},
    ]
    related_queries = [
        f"how to use {topic.name}",
        f"{topic.name} examples",
    ]

    return {
        "topic_name": topic.name,
        "region": region,
        "time_range": time_range,
        "interest_over_time": interest_over_time,
        "interest_by_region": interest_by_region,
        "related_queries": related_queries,
    }
