# Case 12: Attendance Recovery Computation

## Problem statement
Calculate current attendance and the minimum future classes needed to reach an eligibility threshold under several attendance patterns.

## Objectives
Compute the current percentage and simulate future attendance scenarios until the threshold is attained or shown impossible.

## Assumptions
Current 28 attended of 40; threshold 75%. Scenarios: attend all classes; attend 4 of each 5; attend 3 of each 5. Repeating scenario pattern starts with the first value in its block.

## Algorithm
For each scenario, simulate future classes in the repeated pattern one at a time; update attended/held counts; stop at the first count reaching threshold; if future pattern rate is below threshold and current attendance is below threshold, report impossible.

## Flowchart

```text
Start -> Read current attendance -> For each future pattern add one class -> Recompute
    percentage -> Threshold reached? -> Print minimum/impossible -> Stop
```

## Pseudocode

```text
START; FOR each pattern: extra=0; WHILE projected percentage < threshold and extra<limit:
  choose pattern[extra mod pattern length]; update counts; extra++; END; print earliest
  qualifying count or impossible; END; STOP.
```

## Python source code
See [`../programs/case_12_attendance_recovery.py`](../programs/case_12_attendance_recovery.py). The file uses documented sample data and runs directly.

## Test cases
Current 70%. Attend every class: 8 classes => 36/48=75%. Attend 4 of each 5: 24 future classes, 20 attended =>48/64=75%. Attend 3 of each 5: impossible because its long-run rate is below threshold.

## Output screenshot
![Captured console output](../output-screenshots/case_12_output.png)

Accessible transcript: [`../output-screenshots/case_12_output.txt`](../output-screenshots/case_12_output.txt).

## Conclusion
The one-class-at-a-time simulation avoids skipping a minimum when attendance patterns repeat in blocks.

## Limitations
Attendance pattern is assumed to repeat from its first entry. A future attendance rate below current threshold cannot recover to the threshold.
