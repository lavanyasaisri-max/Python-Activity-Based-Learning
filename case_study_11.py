"""Case 11: Subject pass rules and limited grace marks."""
subjects = ["Mathematics", "Physics", "Programming", "English"]
marks = [78, 34, 39, 65]
pass_marks = [35, 35, 40, 35]
maximum_marks = [100, 100, 100, 100]
grace_limit = 2
grace_used = 0
final_marks = []
passed_all = True
total = 0
print("EXAMINATION RESULT AND GRACE-MARK VALIDATION")
print("Subject         Original  Grace  Final  Result")
for i in range(len(subjects)):
    grace = 0
    if marks[i] < pass_marks[i] and pass_marks[i] - marks[i] <= grace_limit - grace_used:
        grace = pass_marks[i] - marks[i]
        grace_used += grace
    final = marks[i] + grace
    if final > maximum_marks[i]:
        final = maximum_marks[i]
    final_marks.append(final)
    total += final
    result = "PASS" if final >= pass_marks[i] else "FAIL"
    if result == "FAIL":
        passed_all = False
    print(f"{subjects[i]:15} {marks[i]:8} {grace:6} {final:6}  {result}")
average = total / len(subjects)
if not passed_all:
    classification = "FAIL"
elif average >= 75:
    classification = "DISTINCTION"
elif average >= 60:
    classification = "FIRST CLASS"
elif average >= 50:
    classification = "SECOND CLASS"
else:
    classification = "PASS CLASS"
print(f"Grace marks used: {grace_used}/{grace_limit}")
print(f"Total: {total}/{sum(maximum_marks)}; average: {average:.2f}%")
print("Final classification:", classification)
