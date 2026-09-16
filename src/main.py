import argparse
from pathlib import Path

from data_loader import load_data
from ranking import get_top_15_each_week
from output import create_predictions


def main():
    parser = argparse.ArgumentParser(
        description="Generate weekly gateway visit priorities."
    )

    parser.add_argument(
        "--data",
        default="data",
        help="Path to the challenge data directory"
    )

    parser.add_argument(
        "--output",
        default="predictions.csv",
        help="Path for the predictions CSV file"
    )

    args = parser.parse_args()

    print("Loading challenge data...")
    data = load_data(args.data)

    print("Creating weekly gateway ranking...")
    ranking = get_top_15_each_week(data["telemetry"])

    if len(ranking) != 120:
        raise ValueError(
            f"Expected 120 predictions, but got {len(ranking)}"
        )

    print("Creating predictions.csv...")
    predictions = create_predictions(
        ranking,
        args.output
    )

    print(f"Created: {Path(args.output).resolve()}")
    print(f"Rows: {len(predictions)}")


if __name__ == "__main__":
    main()