from pathlib import Path
import pandas as pd


def load_data(data_dir="data"):
    data_dir = Path(data_dir)

    gateway_master = pd.read_csv(
        data_dir / "gateway_master.csv",
        encoding="cp1252"
    )

    field_visits = pd.read_csv(
        data_dir / "field_visits.csv"
    )

    meter_success = pd.read_csv(
        data_dir / "meter_read_success.csv"
    )

    engineer_review = pd.read_excel(
        data_dir / "engineer_review_2026-02.xlsx"
    )

    telemetry_files = sorted(
        (data_dir / "telemetry").glob("month=*/part-0.parquet")
    )

    telemetry = pd.concat(
        [pd.read_parquet(file) for file in telemetry_files],
        ignore_index=True
    )

    return {
        "gateway_master": gateway_master,
        "field_visits": field_visits,
        "meter_success": meter_success,
        "engineer_review": engineer_review,
        "telemetry": telemetry,
    }