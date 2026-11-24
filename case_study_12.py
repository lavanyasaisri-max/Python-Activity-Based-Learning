"""Case 12: Minimum future classes needed to reach attendance eligibility."""
scenarios = [("Attend every future class", [1]), ("Attend 4 of each 5 classes", [1, 1, 1, 1, 0]), ("Attend 3 of each 5 classes", [1, 1, 1, 0, 0])]
classes_held = 40
classes_attended = 28
threshold = 75.0
print("ATTENDANCE RECOVERY COMPUTATION")
print(f"Current attendance: {classes_attended}/{classes_held} = {classes_attended/classes_held*100:.2f}%")
print(f"Eligibility threshold: {threshold:.1f}%")
for label, pattern in scenarios:
    additional = 0
    if sum(pattern) / len(pattern) * 100 < threshold and classes_attended / classes_held * 100 < threshold:
        print(f"{label}: threshold cannot be reached because future attendance is below the threshold.")
        continue
    future_attended = 0
    while (classes_attended + future_attended) / (classes_held + additional) * 100 < threshold:
        if pattern[additional % len(pattern)] == 1:
            future_attended += 1
        additional += 1
        if additional > 10000:
            break
    if additional > 10000:
        print(f"{label}: threshold cannot be reached under this attendance rate.")
    else:
        attended_after = classes_attended + future_attended
        held_after = classes_held + additional
        print(f"{label}: {additional} future class(es), {future_attended} attended; final attendance {attended_after}/{held_after} = {attended_after/held_after*100:.2f}%")
