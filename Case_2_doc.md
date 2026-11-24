Case 2: 
Progressive Electricity Billing
Problem statement
Calculate household bills over several months using progressive usage slabs, fixed charges, a surcharge and a rebate; compare bills and flag unusual increases.
Objectives
Calculate slab charges, apply conditional charges and rebates, compare consecutive bills.
Assumptions
Readings: 92, 168, 241 kWh. First 100 units Rs 2, next 100 Rs 3.50, above 200 Rs 5. Fixed charge Rs 45. Rebate Rs 20 through 100 units. Above 200 units add surcharge equal to 5% of energy charge. Bill increase above 50% is unusual.
Algorithm
For each month calculate energy by progressive slabs; apply surcharge/rebate; add fixed fee; print bill; compare with prior month's bill and flag an increase above 50%.
Flowchart
Start -> Initialize monthly readings -> For each month apply slabs -> Apply
    rebate/surcharge -> Calculate bill -> Compare prior bill -> More months? -> Stop
Pseudocode
START; previous=0; FOR each month: slab energy; conditional surcharge/rebate;
  bill=energy+fixed+surcharge-rebate; print; compare increase with previous; previous=bill;
  END; STOP.
Python source code
See ../programs/case_02_progressive_electricity_billing.py. The file uses documented sample data and runs directly.
Test cases
92 units => Rs 209.00; 168 => Rs 483.00; 241 => Rs 837.75 including surcharge. Increases month to month exceed 50% and trigger alerts.
Output screenshot
Captured console output

Accessible transcript: ../output-screenshots/case_02_output.txt.
Conclusion
Progressive slabs charge different rates by usage band. The itemized output and comparison identify a large monthly increase.
Limitations
Energy charge is computed per band. No tax or other fee is included. All sample readings and rates are illustrative.
