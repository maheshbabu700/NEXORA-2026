# Part 1 — Decisions

## Decision 1 — Use a rule-based scoring approach

### What I chose
I used a rule-based priority score based on gateway telemetry indicators.

### What else I could have done
I could have trained a machine learning model to predict gateway failures.

### Why I did not choose it
Part 1 does not require a machine learning model. A rule-based approach is simpler, easier to explain, and suitable for producing the required weekly ranking.

---

## Decision 2 — Create weekly gateway-level indicators

### What I chose
I aggregated telemetry measurements by week and gateway before calculating the priority score.

### What else I could have done
I could have used individual hourly telemetry records directly.

### Why I did not choose it
The required output is a weekly ranking. Weekly aggregation makes the ranking easier to interpret and avoids allowing a single hourly measurement to dominate the result.

---

## Decision 3 — Rank gateways by priority score

### What I chose
I sorted gateways by their calculated score in descending order and assigned a rank within each week.

### What else I could have done
I could have created separate rankings for each individual telemetry indicator.

### Why I did not choose it
A single combined score provides one clear priority order for the field team.

---

## Decision 4 — Select the top 15 gateways

### What I chose
I selected the top 15 gateways for each challenge week.

### What else I could have done
I could have produced a longer list and allowed the operations team to choose the final gateways manually.

### Why I did not choose it
The challenge specifies that the operations team can send 15 site visits per week, so the output directly provides the required 15 prioritized gateways.

---

## Decision 5 — Part 2 area

### What I chose
For this submission, I focused on completing Part 1 rather than implementing a Part 2 specialization.

### What else I could have done
I could have selected one of the Part 2 areas such as Data Engineering, Software Development, DevOps, Data Science, Machine Learning, or MLOps.

### Why I did not choose it
My priority was to complete and validate the mandatory Part 1 pipeline correctly. The Part 1 output was generated and successfully checked using the provided validator.