"""Case 2: Progressive electricity billing using sample household readings."""
months = ["August", "September", "October"]
units_used = [92, 168, 241]
fixed_charge = 45.0
rebate_limit = 100
rebate = 20.0
previous_bill = 0.0
print("PROGRESSIVE ELECTRICITY BILLING")
print("Slabs: first 100 units Rs 2.00/unit; next 100 Rs 3.50/unit; above 200 Rs 5.00/unit")
print("Month       Units   Energy   Fixed  Rebate  Surcharge   Total")
for index in range(len(months)):
    units = units_used[index]
    if units <= 100:
        energy = units * 2.0
    elif units <= 200:
        energy = 100 * 2.0 + (units - 100) * 3.5
    else:
        energy = 100 * 2.0 + 100 * 3.5 + (units - 200) * 5.0
    surcharge = energy * 0.05 if units > 200 else 0.0
    discount = rebate if units <= rebate_limit else 0.0
    bill = energy + fixed_charge + surcharge - discount
    print(f"{months[index]:10} {units:5}  {energy:7.2f}  {fixed_charge:6.2f}  {discount:6.2f}  {surcharge:9.2f}  {bill:7.2f}")
    if index > 0:
        increase = bill - previous_bill
        if previous_bill > 0 and increase / previous_bill > 0.50:
            print(f"  ALERT: bill increased by Rs {increase:.2f} ({increase / previous_bill * 100:.1f}%)")
    previous_bill = bill
