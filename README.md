# NEXORA 2026 — Gateway Visit Prioritization

## Problem Statement

LPDG operates a radio network with many gateways that carry meter readings. When a gateway starts failing, the connected meters may stop being read correctly.

The operations team can send only 15 site visits per week. The purpose of this project is to prioritize which gateways should be considered for field visits using the available telemetry data.

## Part 1 — Weekly Gateway Ranking

The Part 1 solution follows this pipeline:

```text
Challenge Telemetry Data
          ↓
     Load Data
          ↓
 Weekly Gateway Metrics
          ↓
   Priority Score
          ↓
      Ranking
          ↓
   Top 15 Gateways
          ↓
    Add Reason
          ↓
  predictions.csv