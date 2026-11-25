# Case 9: Multi-Currency Travel Budget Analysis

## Problem statement
Convert travel expenses using supplied currency rates, add conversion fees, compare with a budget, and identify the largest expense category.

## Objectives
Look up rates in tuples, convert amounts, include fees, total expenses and compare the budget.

## Assumptions
Illustrative rates: EUR Rs 90, GBP Rs 106, JPY Rs 0.56 per unit. Conversion fee=2% of converted base value. Budget Rs 80,000. Rates are INR/foreign unit.

## Algorithm
Loop over expense categories; find rate in tuple list; convert; add 2% fee; accumulate total and largest category; report budget balance.

## Flowchart

```text
Start -> Load expenses and rate tuples -> Find rate -> Convert and add fee -> Update
    total/largest -> Compare budget -> Stop
```

## Pseudocode

```text
START; total=0; FOR expense: find matching rate; base=amount*rate; fee=base*2%;
  converted=base+fee; add total; update largest; END; compare budget; STOP.
```

## Python source code
See [`../programs/case_09_multi_currency_travel_budget.py`](../programs/case_09_multi_currency_travel_budget.py). The file uses documented sample data and runs directly.

## Test cases
Accommodation 420 EUR => Rs 38,556; meals 185 GBP => Rs 20,002.20; transport 96 JPY => Rs 54.84; activities 140 EUR => Rs 12,852; total Rs 71,465.04; within budget; accommodation largest.

## Output screenshot
![Captured console output](../output-screenshots/case_09_output.png)

Accessible transcript: [`../output-screenshots/case_09_output.txt`](../output-screenshots/case_09_output.txt).

## Conclusion
The budget check includes conversion fees. Replace sample rates with values prescribed by the instructor if required.

## Limitations
Rates are illustrative, not live rates. Amounts are positive sample expenses.
