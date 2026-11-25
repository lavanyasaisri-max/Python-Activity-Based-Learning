# Case 16: Multi-Day Water Tank Simulation

## Problem statement
Simulate tank level over several intervals, detect overflow/shortage, and find the first interval the target is reached.

## Objectives
Update inventory over time, clamp physical level, report overflow/shortage and detect threshold crossing.

## Assumptions
Initial level 3200 L, capacity 5000 L, target 4000 L; supplied six-day inflow/outflow arrays. Overflow/shortage measured before level is clamped.

## Algorithm
For each day calculate raw level; measure excess over capacity or deficit below zero; clamp to tank limits; record first threshold day; print daily status.

## Flowchart

```text
Start -> Initialize tank -> For each day update raw level -> Measure overflow/shortage ->
    Clamp -> Check target -> Print -> Stop
```

## Pseudocode

```text
START; FOR each day: raw=level+inflow-outflow; overflow=max(0,raw-capacity);
  shortage=max(0,-raw); clamp level; if target first reached record day; print; END; report
  crossing; STOP.
```

## Python source code
See [`../programs/case_16_water_tank_simulation.py`](../programs/case_16_water_tank_simulation.py). The file uses documented sample data and runs directly.

## Test cases
Day 1 ending level 3800 L; day 2 3900; day 3 3500; day 5 4000 and first target crossing. No sample overflow/shortage.

## Output screenshot
![Captured console output](../output-screenshots/case_16_output.png)

Accessible transcript: [`../output-screenshots/case_16_output.txt`](../output-screenshots/case_16_output.txt).

## Conclusion
The simulation tracks daily changes and separates overflow/shortage from the valid stored water level.

## Limitations
The sample uses liters and assumes all inflow/outflow occurs within each daily interval.
