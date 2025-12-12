"""
Trends client for the Trend Radar MVP.

This module acts as a thin wrapper:
- By default, it returns dummy data (USE_GOOGLE = False).
- In the future, it can call the real Google Trends integration
  in `trends_google.py` when USE_GOOGLE = True.
"""

from typing import List

from models import TrendTopic
from trends_google import fetch_trend_data_google

# Global flag to choose backend.
# - False -> dummy data (safe, no network calls).
# - True  -> use Google Trends (experimental).
USE_GOOGLE: bool = True


def _generate_dummy_data(topic: TrendTopic, region: str, time_range: str) -> dict:
    """
    Generate simple fake trend data for a topic.

    This is only for local testing. It does NOT represent real trends.
    """
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


def fetch_trend_data(topic: TrendTopic, region: str, time_range: str) -> dict:
    """
    Fetch trend data for a single topic.

    If USE_GOOGLE is False (default), returns dummy data.
    If USE_GOOGLE is True, calls the Google Trends integration.
    """
    if USE_GOOGLE:
        # Experimental path: real Google Trends (still a placeholder).
        data = fetch_trend_data_google(
            topic_name=topic.name,
            region=region,
            time_range=time_range,
        )
        # If for some reason Google returns an empty series, fall back.
        if not data.get("interest_over_time"):
            return _generate_dummy_data(topic, region, time_range)
        return data

    # Default: dummy mode (safe, offline).
    return _generate_dummy_data(topic, region, time_range)
