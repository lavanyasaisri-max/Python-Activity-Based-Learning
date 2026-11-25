# Case 23: Student Timetable Conflict Detection

## Problem statement
Compare course schedules stored as tuples, detect time overlaps, unavailable rooms and validate the proposed timetable.

## Objectives
Unpack tuple records, compare intervals on matching days, check room conflicts and blocked room periods.

## Assumptions
Tuple: (course, day, start, end, room); end is exclusive; periods are positive; unavailable tuple (day, period, room). Sample intentionally contains conflicts.

## Algorithm
Validate periods; compare each class with later same-day classes using interval overlap rule; report time/room clashes; check unavailable room periods; count issues.

## Flowchart

```text
Start -> Load tuples -> Validate periods -> Compare same-day intervals -> Check shared
    rooms/blocked periods -> Print issues -> Stop
```

## Pseudocode

```text
START; FOR each tuple A validate; FOR later tuple B: if same day and startA<endB and
  startB<endA report; if same room report room clash; END; check unavailable periods; END;
  report valid or issue count; STOP.
```

## Python source code
See [`../programs/case_23_timetable_conflict_detection.py`](../programs/case_23_timetable_conflict_detection.py). The file uses documented sample data and runs directly.

## Test cases
Python Mon 1-3 and Math Mon 3-5 do not overlap. Python Mon 1-3 and Physics Mon 2-4 overlap. English/Lab Tue overlap in R101. Blocked R101 periods on Mon 4 and Tue 2 are detected. Total issue count is 5; the room clash is reported as detail under its time conflict.

## Output screenshot
![Captured console output](../output-screenshots/case_23_output.png)

Accessible transcript: [`../output-screenshots/case_23_output.txt`](../output-screenshots/case_23_output.txt).

## Conclusion
Tuple unpacking and interval comparison identify both course conflicts and room availability issues.

## Limitations
Intervals are half-open [start,end), so a class may begin when a prior class ends. The sample data intentionally has errors.
