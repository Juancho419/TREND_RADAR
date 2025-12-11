"""
Service layer for the Trend Radar MVP.

This module exposes a simple function `run_analysis` that:
- loads configuration
- runs the analysis
- writes the CSV report
- returns the path to the CSV file

Both the console entry point (app.py) and any UI (e.g. Tkinter)
should call this function instead of re-implementing the flow.
"""

from pathlib import Path
from typing import Optional

from config_loader import load_config
from analyzer import analyze_topics
from reporter import write_csv_report


def run_analysis(time_range_override: Optional[str] = None) -> Path:
    """
    Run the full analysis pipeline.

    Parameters:
    - time_range_override: if provided, this value will override the
      time_range from the YAML config.

    Returns:
    - Path to the generated CSV report.
    """
    # Load config from YAML
    config = load_config()
    region = config["region"]
    time_range = config["time_range"]
    topics = config["topics"]

    # Optionally override time_range (for UI input in the future)
    if time_range_override:
        time_range = time_range_override

    # Run analysis
    results = analyze_topics(topics, region=region, time_range=time_range)

    # Define output CSV path
    output_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "processed"
        / "trend_report.csv"
    )

    # Write CSV report
    write_csv_report(results, output_path)

    return output_path
