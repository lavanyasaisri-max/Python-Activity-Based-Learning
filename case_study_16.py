"""Case 16: Multi-day tank level simulation with overflow and shortage checks."""
inflow = [1200, 900, 500, 0, 1800, 700]
outflow = [600, 800, 900, 700, 600, 1000]
capacity = 5000
threshold = 4000
level = 3200
first_threshold_interval = 0
print("MULTI-DAY WATER TANK SIMULATION")
print(f"Capacity: {capacity} L; starting level: {level} L; alert threshold: {threshold} L")
print("Day   Inflow  Outflow  Before  Overflow  Shortage  Ending  Status")
for i in range(len(inflow)):
    before = level
    raw_level = before + inflow[i] - outflow[i]
    overflow = max(0, raw_level - capacity)
    shortage = max(0, -raw_level)
    level = min(capacity, max(0, raw_level))
    if first_threshold_interval == 0 and level >= threshold:
        first_threshold_interval = i + 1
    status = "OVERFLOW" if overflow > 0 else ("SHORTAGE" if shortage > 0 else "NORMAL")
    if level < threshold and status == "NORMAL":
        status = "BELOW THRESHOLD"
    print(f"{i+1:3} {inflow[i]:8} {outflow[i]:8} {before:7} {overflow:9} {shortage:9} {level:7}  {status}")
if first_threshold_interval == 0:
    print("Threshold was not reached.")
else:
    print(f"First reaches threshold at interval/day {first_threshold_interval}.")
