"""
Data models for the Trend Radar MVP.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class TrendTopic:
    """
    Represent one topic to track from te config file.
    """
    name: str
    category: str

@dataclass
class TrendResult:
    """
    Represent the analysis result for one topic.
    Later we will fill tese fields with real data from Google Trends.
    """
    
    topic: TrendTopic
    trend_status: str # e.g., "Rising", "Falling", "Stable"
    current_interest: int # e.g., 0-100 scale
    growth_pct: float # e.g., percentage growth over a time
    top_regions: List[str] # e.g. ["Bogotá", "Medellín"]
    related_queries: List[str] # e.g. top 3-5 related seach
