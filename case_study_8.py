"""Case 8: Manufacturing cost and profit analysis for three products."""
products = ["Desk", "Chair", "Shelf"]
quantities = [20, 50, 15]
material_per_unit = [1250.0, 420.0, 980.0]
labour_per_unit = [380.0, 160.0, 300.0]
machine_cost_per_unit = [90.0, 55.0, 75.0]
wastage_rate = 0.08
selling_price = [2100.0, 760.0, 1750.0]
target_profit_rate = 0.20
print("MANUFACTURING COST AND PROFITABILITY")
print("Item    Qty   Material   Labour   Machine   Wastage   Total Cost   Revenue    Profit   Margin   Target")
for i in range(len(products)):
    base_unit_cost = material_per_unit[i] + labour_per_unit[i] + machine_cost_per_unit[i]
    waste_total = base_unit_cost * quantities[i] * wastage_rate
    total_cost = base_unit_cost * quantities[i] + waste_total
    revenue = selling_price[i] * quantities[i]
    profit = revenue - total_cost
    margin = profit / total_cost * 100 if total_cost > 0 else 0
    target = "MET" if margin >= target_profit_rate * 100 else "NOT MET"
    print(f"{products[i]:7} {quantities[i]:3}  {material_per_unit[i]*quantities[i]:9.2f} {labour_per_unit[i]*quantities[i]:8.2f} {machine_cost_per_unit[i]*quantities[i]:9.2f} {waste_total:9.2f} {total_cost:11.2f} {revenue:9.2f} {profit:9.2f} {margin:7.2f}% {target}")
