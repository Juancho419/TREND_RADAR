"""
Reporter module for the Trend Radar MVP.

For now, it writes a simple CSV file with fake analysis results.
Later, it will be reused when we have real Google Trends data.
"""

from pathlib import Path
from typing import List

from models import TrendResult


def write_csv_report(results: List[TrendResult], output_path: Path) -> None:
    """
    Write a basic CSV report with one row per topic.

    Columns:
    - topic_name
    - category
    - trend_status
    - current_interest
    - growth_pct
    """
    # Ensure parent folder exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Build CSV content
    lines = []
    header = "topic_name,category,trend_status,current_interest,growth_pct"
    lines.append(header)

    for r in results:
        line = (
            f"{r.topic.name},"
            f"{r.topic.category},"
            f"{r.trend_status},"
            f"{r.current_interest},"
            f"{r.growth_pct}"
        )
        lines.append(line)

    csv_content = "\n".join(lines)

    # Write to file
    with output_path.open("w", encoding="utf-8") as f:
        f.write(csv_content)

    print(f"\nCSV report written to: {output_path}")
