from pathlib import Path
from config_loader import load_config
from analyzer import analyze_topics
from reporter import write_csv_report


def main() -> None:
    """
    Entry point for the Trend Radar MVP.
    For now, it:
    - prints a start message
    - loads configuration
    - prints a small summary of the config
    """
    print("Trend Radar - MVP skeleton is running.")

    config = load_config()

    region = config["region"]
    time_range = config["time_range"]
    topics = config["topics"]

    print("\nConfig summary:")
    print(f"  Region      : {region}")
    print(f"  Time range  : {time_range}")
    print(f"  Topics count: {len(topics)}")

    print("\nTopics detail:")
    for topic in topics:
        print(f"  - {topic.name} [{topic.category}]")

    # Fake analysis step
    print("\nRunning fake analysis...")
    results = analyze_topics(topics, region=region, time_range=time_range)


    print("\nFake analysis results:")
    for r in results:
        print(
            f"  - {r.topic.name}: status={r.trend_status}, "
            f"interest={r.current_interest}, growth={r.growth_pct}%"
        )
    
    # Write CSV report to data/processed/trend_report.csv
    output_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "processed"
        / "trend_report.csv"
    )
    write_csv_report(results, output_path)


if __name__ == "__main__":
    main()