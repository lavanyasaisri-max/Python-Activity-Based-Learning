"""Case 19: Prioritized basket reduction to fit a fixed shopping budget."""
products = ["Rice", "Oil", "Headphones", "Notebook"]
unit_prices = [65.0, 150.0, 1200.0, 55.0]
quantities = [10, 3, 1, 8]
priority = [1, 2, 4, 1]  # Larger number means higher purchase priority.
budget = 2500.0
discount_threshold = 2000.0
discount_rate = 0.05
subtotal = 0.0
for i in range(len(products)):
    subtotal += unit_prices[i] * quantities[i]
discount = subtotal * discount_rate if subtotal >= discount_threshold else 0.0
total = subtotal - discount
print("MULTI-PRODUCT SHOPPING BUDGET")
print(f"Initial subtotal Rs {subtotal:.2f}; discount Rs {discount:.2f}; payable Rs {total:.2f}; budget Rs {budget:.2f}")
print("If over budget, units are removed from lowest priority first; each unit removal is recalculated.")
while total > budget:
    lowest_priority_index = -1
    for i in range(len(products)):
        if quantities[i] > 0 and (lowest_priority_index == -1 or priority[i] < priority[lowest_priority_index]):
            lowest_priority_index = i
    if lowest_priority_index == -1:
        break
    quantities[lowest_priority_index] -= 1
    subtotal = 0.0
    for i in range(len(products)):
        subtotal += unit_prices[i] * quantities[i]
    discount = subtotal * discount_rate if subtotal >= discount_threshold else 0.0
    total = subtotal - discount
print("Final basket")
print("Product          Unit Price  Quantity   Line Total")
for i in range(len(products)):
    print(f"{products[i]:16} {unit_prices[i]:10.2f} {quantities[i]:9} {unit_prices[i]*quantities[i]:12.2f}")
print(f"Subtotal Rs {subtotal:.2f}; discount Rs {discount:.2f}; payable Rs {total:.2f}")
print("Budget status:", "WITHIN BUDGET" if total <= budget else "BUDGET CANNOT BE MET")
