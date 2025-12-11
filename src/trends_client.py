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

    Later, it will:
    - call Google Trends
    - retrieve interest over time, interest by region, and related queries
    """
    # Temporary dummy data structure
    return {
        "topic_name": topic.name,
        "region": region,
        "time_range": time_range,
        "interest_over_time": [],
        "interest_by_region": [],
        "related_queries": [],
    }
