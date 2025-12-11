"""
Configuration loader for the Trend Radar MVP.

This module will:
- Read config/topics.yaml
- Parse region, time range and topics
- Return the data in a Python-friendly structure
"""

from pathlib import Path
from typing import Any, Dict, List

import yaml

from models import TrendTopic


def load_config() -> Dict[str, Any]:
    """
    Load configuration from config/topics.yaml.

    Returns a dictionary with:
    - region: str
    - time_range: str
    - topics: list of TrendTopic objects
    """
    # 1. Build the path to the YAML file
    config_path = Path(__file__).resolve().parent.parent / "config" / "topics.yaml"
    print(f"Loading configuration from: {config_path}")

    # 2. Open and read the YAML file
    with config_path.open("r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)

    # 3. Extract basic fields
    region: str = raw_data.get("region", "")
    time_range: str = raw_data.get("time_range", "")
    raw_topics: List[Dict[str, str]] = raw_data.get("topics", [])

    # 4. Convert raw topics (dicts) into TrendTopic objects
    topics: List[TrendTopic] = []
    for item in raw_topics:
        name = item.get("name", "")
        category = item.get("category", "")
        topics.append(TrendTopic(name=name, category=category))

    print("Configuration loaded:")
    print(f"  region     : {region}")
    print(f"  time_range : {time_range}")
    print(f"  topics     : {len(topics)} topics found")

    return {
        "region": region,
        "time_range": time_range,
        "topics": topics,
    }
