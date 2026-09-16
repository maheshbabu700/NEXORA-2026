# What It Cannot Do

## 1. It does not prove that a gateway has failed

The system uses telemetry indicators to prioritize gateways for field visits.

A high score means that the gateway has higher priority based on the selected indicators. It does not prove that the gateway is actually broken.

---

## 2. It does not guarantee that every selected gateway needs a visit

The ranking is based on the available telemetry data and the scoring rules.

Some high-priority gateways may not require a physical visit.

---

## 3. The scoring weights are rule-based

The priority score uses selected telemetry indicators with fixed weights.

Different weights could produce a different ranking.

A future version could evaluate the weights using additional operational outcomes and field-visit results.

---

## 4. It does not predict future failures

The current Part 1 implementation ranks gateways using the available weekly telemetry.

It does not train a predictive machine learning model to forecast future gateway failures.

---

## 5. More data could improve the decision

Additional weeks of telemetry and more confirmed field outcomes could help evaluate whether the ranking identifies gateways that actually require visits.

The challenge also indicates that additional time/data could be used to understand where the approach falls over and how it could be improved.