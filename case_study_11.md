# Case 11: Examination Result and Grace-Mark Validation

## Problem statement
Process subject marks and pass thresholds, apply a limited grace policy, respect maximum marks and generate a classification.

## Objectives
Apply subject pass criteria, enforce a grace cap and maximum marks, compute average and classification.

## Assumptions
Marks [78,34,39,65], pass thresholds [35,35,40,35], maximum 100, total grace allowance 2. Add only exact near-miss shortfalls when remaining grace is enough. Classification: >=75 distinction, >=60 first, >=50 second, otherwise pass class; any failed subject means FAIL.

## Algorithm
For each subject apply available grace to eligible shortfall; cap at maximum; accumulate total and pass status; calculate average; classify.

## Flowchart

```text
Start -> Load subject marks and rules -> Check shortfall -> Apply permitted grace -> Cap
    at maximum -> Accumulate -> Classify -> Stop
```

## Pseudocode

```text
START; grace=0; FOR each subject: if near pass and allowance remains, add shortfall; cap at
  max; accumulate and check pass; END; if any fail classify FAIL else use average bands; STOP.
```

## Python source code
See [`../programs/case_11_exam_result_grace_marks.py`](../programs/case_11_exam_result_grace_marks.py). The file uses documented sample data and runs directly.

## Test cases
Physics 34 gets 1; Programming 39 gets 1; grace used 2; final total 218/400; average 54.50%; classification Second Class.

## Output screenshot
![Captured console output](../output-screenshots/case_11_output.png)

Accessible transcript: [`../output-screenshots/case_11_output.txt`](../output-screenshots/case_11_output.txt).

## Conclusion
The limited allowance is applied subject by subject without exceeding subject maximum marks. A failing subject overrides the average band.

## Limitations
Grace is allocated in listed subject order, so changing subject order could change allocation when several subjects need grace.
