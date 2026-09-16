import pandas as pd


def add_reasons(ranking):
    """
    Add a simple explanation for why each gateway was prioritized.
    """

    df = ranking.copy()

    def make_reason(row):
        indicators = {
            "poor signal strength": row["avg_rssi_bad"],
            "poor RSRP": row["avg_rscp_bad"],
            "poor signal quality": row["avg_ecio_bad"],
            "frequent reboots": row["avg_reboots"],
            "long offline duration": row["avg_offline_duration"],
            "high load": row["avg_load"],
        }

        strongest = max(indicators, key=indicators.get)

        return f"High priority mainly due to {strongest}"

    df["reason"] = df.apply(make_reason, axis=1)

    return df


def create_predictions(ranking, output_file="predictions.csv"):
    """
    Create the final predictions.csv file.
    """

    df = add_reasons(ranking)

    predictions = df[
        ["week_start", "rank", "gateway_id", "score", "reason"]
    ].copy()

    predictions["week_start"] = pd.to_datetime(
        predictions["week_start"]
    ).dt.strftime("%Y-%m-%d")

    predictions.to_csv(
        output_file,
        index=False
    )

    return predictions
    