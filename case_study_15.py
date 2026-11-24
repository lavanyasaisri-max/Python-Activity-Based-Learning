"""Case 15: Parking charges using 24-hour times and simple daily cap rules."""
vehicles = ["Car", "Motorcycle", "Car"]
entries = ["08:20", "22:15", "09:00"]
exits = ["11:05", "01:10", "09:00"]
rates_per_hour = [("Car", 30), ("Motorcycle", 15)]
daily_cap = [("Car", 240), ("Motorcycle", 120)]
print("SMART PARKING FEE MANAGEMENT")
print("Entry and exit use 24-hour HH:MM. Any started hour is charged; overnight spans midnight.")
for i in range(len(vehicles)):
    entry_parts = entries[i].split(":")
    exit_parts = exits[i].split(":")
    entry_hour = int(entry_parts[0])
    entry_minute = int(entry_parts[1])
    exit_hour = int(exit_parts[0])
    exit_minute = int(exit_parts[1])
    valid = 0 <= entry_hour < 24 and 0 <= exit_hour < 24 and 0 <= entry_minute < 60 and 0 <= exit_minute < 60
    if not valid:
        print(f"Vehicle {i+1}: INVALID TIME")
    else:
        start = entry_hour * 60 + entry_minute
        end = exit_hour * 60 + exit_minute
        if end < start:
            end += 24 * 60
        duration = end - start
        hours = (duration + 59) // 60
        rate = 0
        cap = 0
        for category, value in rates_per_hour:
            if category == vehicles[i]:
                rate = value
        for category, value in daily_cap:
            if category == vehicles[i]:
                cap = value
        fee = min(hours * rate, cap)
        print(f"Vehicle {i+1} ({vehicles[i]}): {entries[i]} to {exits[i]}, {duration//60}h {duration%60}m, charged hours={hours}, fee=Rs {fee:.2f}")
