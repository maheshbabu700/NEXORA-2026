from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

print("Checking NEXORA challenge data...\n")

gateway_master = pd.read_csv(
    DATA_DIR / "gateway_master.csv",
    encoding="cp1252"
)

field_visits = pd.read_csv(
    DATA_DIR / "field_visits.csv"
)

meter_success = pd.read_csv(
    DATA_DIR / "meter_read_success.csv"
)

engineer_review = pd.read_excel(
    DATA_DIR / "engineer_review_2026-02.xlsx"
)

telemetry = pd.read_parquet(
    DATA_DIR / "telemetry/month=2026-02/part-0.parquet"
)

print("gateway_master:", gateway_master.shape)
print("field_visits:", field_visits.shape)
print("meter_read_success:", meter_success.shape)
print("engineer_review:", engineer_review.shape)
print("telemetry:", telemetry.shape)

print("\nGateway master columns:")
print(gateway_master.columns.tolist())

print("\nMeter success columns:")
print(meter_success.columns.tolist())

print("\nTelemetry columns:")
print(telemetry.columns.tolist())

print("\nData check completed successfully.")