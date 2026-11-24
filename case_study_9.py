"""Case 9: Travel budget conversion using supplied illustrative exchange rates."""
categories = ["Accommodation", "Meals", "Transport", "Activities"]
amounts = [420.0, 185.0, 96.0, 140.0]
currencies = ["EUR", "GBP", "JPY", "EUR"]
# Sample rates are illustrative: rupees per one foreign currency unit.
rates = [("EUR", 90.0), ("GBP", 106.0), ("JPY", 0.56)]
conversion_fee_rate = 0.02
budget_rupees = 80000.0
total_rupees = 0.0
largest_category = ""
largest_cost = -1.0
print("MULTI-CURRENCY TRAVEL BUDGET")
print("Rates (illustrative): 1 EUR=Rs90, 1 GBP=Rs106, 1 JPY=Rs0.56; conversion fee 2%")
print("Category        Amount   Currency   Base INR   Fee INR   Total INR")
for i in range(len(categories)):
    rate = 0.0
    for currency, value in rates:
        if currency == currencies[i]:
            rate = value
    base_cost = amounts[i] * rate
    fee = base_cost * conversion_fee_rate
    converted_cost = base_cost + fee
    total_rupees += converted_cost
    if converted_cost > largest_cost:
        largest_cost = converted_cost
        largest_category = categories[i]
    print(f"{categories[i]:15} {amounts[i]:7.2f} {currencies[i]:9} {base_cost:10.2f} {fee:9.2f} {converted_cost:11.2f}")
print(f"Total planned spend: Rs {total_rupees:.2f}")
print(f"Budget: Rs {budget_rupees:.2f}; remaining: Rs {budget_rupees-total_rupees:.2f}")
print("Budget status:", "WITHIN BUDGET" if total_rupees <= budget_rupees else "OVER BUDGET")
print(f"Largest category: {largest_category} (Rs {largest_cost:.2f})")
