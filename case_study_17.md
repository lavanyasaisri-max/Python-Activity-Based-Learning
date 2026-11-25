# Case 17: Student Performance Trend Analysis

## Problem statement
Compare student assessment scores by subject, identify improvements/declines and weak subjects, and classify overall performance.

## Objectives
Use nested lists to compare three scores per subject and apply clear subject and student criteria.

## Assumptions
Three sample students, three subjects, three assessments. Weak subject average <50. Any weak subject means Needs Support; otherwise net change >=15 means Strong Improvement, negative means Declining, else Steady.

## Algorithm
For each student and subject compute last-minus-first change, classify monotonic trend, count weak averages, and sum changes; apply ordered classification rules.

## Flowchart

```text
Start -> Load nested score matrix -> Compare assessments per subject -> Count weak
    subjects and net change -> Classify student -> Print -> Stop
```

## Pseudocode

```text
START; FOR student: weak=0, change=0; FOR subject: compute average and trend; update totals;
  END; classify using weak count, net change; print; END; STOP.
```

## Python source code
See [`../programs/case_17_student_performance_trends.py`](../programs/case_17_student_performance_trends.py). The file uses documented sample data and runs directly.

## Test cases
Asha changes +12,+7,+14 and is Strong Improvement. Ravi changes -8,+3,+13 and is Steady (+8). Mina has weak Physics average and Needs Support.

## Output screenshot
![Captured console output](../output-screenshots/case_17_output.png)

Accessible transcript: [`../output-screenshots/case_17_output.txt`](../output-screenshots/case_17_output.txt).

## Conclusion
The nested score matrix supports student-level and subject-level trends. The explicit rule order makes classifications reproducible.

## Limitations
Sample records are fictional. Weak threshold and classifications are assumptions for demonstration.
