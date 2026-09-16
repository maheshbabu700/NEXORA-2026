import pandas as pd


def create_weekly_ranking(telemetry):
    """
    Create a weekly priority ranking for gateways.

    Higher score = higher priority for a field visit.
    """

    df = telemetry.copy()

    # Convert timestamp column to datetime
    df["DateDt"] = pd.to_datetime(df["DateDt"])

    # Create Monday-based week start
    df["week_start"] = (
        df["DateDt"] - pd.to_timedelta(df["DateDt"].dt.weekday, unit="D")
    ).dt.normalize()

    # Calculate weekly gateway indicators
    summary = df.groupby(
        ["week_start", "gateway_id"]
    ).agg(
        avg_rssi_bad=("rssi_bad", "mean"),
        avg_rscp_bad=("rscp_rsrp_bad", "mean"),
        avg_ecio_bad=("ecio_rsrq_bad", "mean"),
        avg_reboots=("reboot_cnt", "mean"),
        avg_offline_duration=("avg_offline_duration", "mean"),
        avg_load=("avg_load1", "mean"),
    ).reset_index()

    # Calculate priority score
    summary["score"] = (
        summary["avg_rssi_bad"] * 3
        + summary["avg_rscp_bad"] * 3
        + summary["avg_ecio_bad"] * 2
        + summary["avg_reboots"] * 2
        + summary["avg_offline_duration"] * 2
        + summary["avg_load"]
    )

    # Sort highest priority first
    summary = summary.sort_values(
        ["week_start", "score"],
        ascending=[True, False]
    ).reset_index(drop=True)

    # Assign rank within each week
    summary["rank"] = (
        summary.groupby("week_start").cumcount() + 1
    )

    return summary


def get_top_15_each_week(telemetry):
    """
    Return the top 15 gateways for the 8 challenge weeks.
    """

    ranking = create_weekly_ranking(telemetry)

    challenge_weeks = pd.to_datetime([
        "2026-02-02",
        "2026-02-09",
        "2026-02-16",
        "2026-02-23",
        "2026-03-02",
        "2026-03-09",
        "2026-03-16",
        "2026-03-23",
    ])

    ranking = ranking[
        ranking["week_start"].isin(challenge_weeks)
    ].copy()

    top_15 = ranking[ranking["rank"] <= 15].copy()

    return top_15