"""
Google Trends integration (experimental).

This module will use the `pytrends` library or similar to fetch real
Google Trends data. For now, it only defines the function signature
and returns a dummy structure, so it is safe to import.
"""

from typing import List


def fetch_trend_data_google(
    topic_name: str,
    region: str,
    time_range: str,
) -> dict:
    """
    Fetch real trend data for a single topic using Google Trends.

    Parameters:
    - topic_name: search term or topic to query in Google Trends.
    - region: country code, e.g. "CO".
    - time_range: string describing the time window, e.g. "today 12-m".

    Returns:
    - A dictionary with the same structure as the dummy client:
      {
        "topic_name": str,
        "region": str,
        "time_range": str,
        "interest_over_time": List[int],
        "interest_by_region": List[dict],
        "related_queries": List[str],
      }

    NOTE:
    This implementation is still a placeholder. It does NOT perform
    any network requests yet. It only returns an empty shape, so that
    the rest of the codebase can be wired safely.
    """
        # Temporary dummy implementation:
    # We simulate a strong but realistic growth curve (0–100).
    interest_over_time: List[int] = [5, 15, 30, 55, 90]

    # Fake regional interest
    interest_by_region = [
        {"name": "Bogotá", "value": 90},
        {"name": "Medellín", "value": 80},
        {"name": "Cali", "value": 70},
    ]

    # Fake related queries
    related_queries: List[str] = [
        f"{topic_name} latest news",
        f"{topic_name} opportunities in {region}",
        f"how to start with {topic_name}",
    ]

    return {
        "topic_name": topic_name,
        "region": region,
        "time_range": time_range,
        "interest_over_time": interest_over_time,
        "interest_by_region": interest_by_region,
        "related_queries": related_queries,
    }

    return {
        "topic_name": topic_name,
        "region": region,
        "time_range": time_range,
        "interest_over_time": interest_over_time,
        "interest_by_region": interest_by_region,
        "related_queries": related_queries,
    }

