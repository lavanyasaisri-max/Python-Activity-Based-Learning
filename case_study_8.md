# Case 8: Manufacturing Cost and Profitability Analysis

## Problem statement
Calculate material, labour, wastage, and machine costs for products; compare revenue and profit with a target margin.

## Objectives
Aggregate costs, account for wastage, compute revenue/profit/margin, test a target.

## Assumptions
Products Desk, Chair, Shelf; wastage is 8% of material+labour+machine production cost. Margin=profit/total cost. Target=20%. Input figures are illustrative.

## Algorithm
For each product sum unit costs times quantity; add 8% wastage; compute revenue, profit and margin; compare margin with 20%; print breakdown.

## Flowchart

```text
Start -> Load products -> Calculate base costs -> Add wastage -> Compute
    revenue/profit/margin -> Compare target -> Print -> Stop
```

## Pseudocode

```text
START; FOR each product: base cost; wastage=base*8%; total cost=base+wastage;
  revenue=price*quantity; profit=revenue-cost; margin=profit/cost*100; compare target; END;
  STOP.
```

## Python source code
See [`../programs/case_08_manufacturing_cost_profitability.py`](../programs/case_08_manufacturing_cost_profitability.py). The file uses documented sample data and runs directly.

## Test cases
Desk: cost Rs 37,152, revenue Rs 42,000, target not met. Chair: cost Rs 34,290, revenue Rs 38,000, target not met. Shelf: cost Rs 21,951, revenue Rs 26,250, target not met.

## Output screenshot
![Captured console output](../output-screenshots/case_08_output.png)

Accessible transcript: [`../output-screenshots/case_08_output.txt`](../output-screenshots/case_08_output.txt).

## Conclusion
Wastage is included before profitability is assessed, making the margin comparison reflect a production cost estimate.

## Limitations
All input prices, quantities and target rates are sample assumptions, not supplied faculty data.
