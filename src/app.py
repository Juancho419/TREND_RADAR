from config_loader import load_config


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

if __name__ == "__main__":
    main()
