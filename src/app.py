from service import run_analysis


def main() -> None:
    """
    Console entry point for the Trend Radar MVP.

    For now, it just:
    - runs the analysis with the default config
    - prints where the CSV report was written
    """
    print("Trend Radar - MVP (console)")

    output_path = run_analysis()

    print(f"\nAnalysis completed.")
    print(f"CSV report written to: {output_path}")


if __name__ == "__main__":
    main()
