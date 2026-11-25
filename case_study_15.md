# Case 15: Smart Parking Fee Management

## Problem statement
Calculate parking charges from entry/exit times, vehicle category, overnight parking, daily limits and time validation.

## Objectives
Parse/validate HH:MM, handle midnight, bill started hours and apply category rate/cap.

## Assumptions
24-hour time; earlier exit means next day; any started hour billed. Car Rs 30/hour cap Rs 240; motorcycle Rs 15/hour cap Rs 120. Duration over 24h is excluded from sample assumptions.

## Algorithm
Parse times to minutes; validate fields; add a day if exit earlier; round duration up to whole hours; find vehicle rate/cap; print fee.

## Flowchart

```text
Start -> Parse and validate time -> Convert to minutes -> Handle overnight -> Round up
    charged hours -> Apply vehicle cap -> Print -> Stop
```

## Pseudocode

```text
START; FOR vehicle: parse and validate; if invalid print; else convert to minutes; handle
  midnight; hours=ceiling(duration/60); fee=min(hours*rate,cap); print; END; STOP.
```

## Python source code
See [`../programs/case_15_smart_parking_fee.py`](../programs/case_15_smart_parking_fee.py). The file uses documented sample data and runs directly.

## Test cases
Car 08:20-11:05: 2h45, 3 hours, Rs 90. Motorcycle 22:15-01:10: 2h55, 3 hours, Rs 45. Same start/end is zero hours under the chosen assumption.

## Output screenshot
![Captured console output](../output-screenshots/case_15_output.png)

Accessible transcript: [`../output-screenshots/case_15_output.txt`](../output-screenshots/case_15_output.txt).

## Conclusion
Time validation and midnight adjustment support typical overnight parking, while vehicle caps limit the charge.

## Limitations
A same-time exit is interpreted as zero duration. Confirm this convention and partial-day cap policy with faculty.
