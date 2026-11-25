# Case 19: Multi-Product Shopping Budget Constraint

## Problem statement
Evaluate product quantities, apply discount conditions and reduce purchases according to priority until the payable amount fits a budget.

## Objectives
Compute discount and total; reduce low-priority purchases deterministically; report final basket.

## Assumptions
Rice, Oil, Headphones, Notebook; unit prices 65,150,1200,55; quantities 10,3,1,8; priorities 1,2,4,1 where larger is more important. Remove one unit from lowest priority; ties use list order. 5% discount if subtotal >= Rs 2000; budget Rs 2500.

## Algorithm
Calculate subtotal and discount; while over budget choose lowest-priority available item, reduce one unit, recalculate; print final basket.

## Flowchart

```text
Start -> Calculate subtotal/discount -> Over budget? -> Select lowest-priority available
    item -> Reduce one unit -> Recalculate -> Repeat or print -> Stop
```

## Pseudocode

```text
START; calculate subtotal/discount; WHILE total>budget: find lowest priority with quantity;
  reduce 1; recalculate; END; print; STOP.
```

## Python source code
See [`../programs/case_19_shopping_budget_constraint.py`](../programs/case_19_shopping_budget_constraint.py). The file uses documented sample data and runs directly.

## Test cases
Initial subtotal Rs 3540, discount Rs 177, payable Rs 3363. Final quantities: Rice 8, Oil 3, Headphones 1, Notebook 8; subtotal Rs 2610, discount Rs 130.50, payable Rs 2479.50 (within budget).

## Output screenshot
![Captured console output](../output-screenshots/case_19_output.png)

Accessible transcript: [`../output-screenshots/case_19_output.txt`](../output-screenshots/case_19_output.txt).

## Conclusion
A simple priority rule produces a repeatable basket reduction and recalculates the threshold discount after each change.

## Limitations
This greedy policy is not an optimization proof; equal priorities use the earlier item first. Quantities stay nonnegative.
