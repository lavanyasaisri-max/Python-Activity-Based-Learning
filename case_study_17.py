"""Case 17: Assessment trend and weak-subject analysis for sample students."""
students = ["Asha", "Ravi", "Mina"]
subjects = ["Math", "Physics", "Python"]
# Each row: one student; each subject has scores from three assessments.
scores = [
    [[62, 68, 74], [48, 52, 55], [70, 78, 84]],
    [[80, 76, 72], [66, 70, 69], [58, 64, 71]],
    [[45, 50, 58], [42, 39, 44], [60, 61, 59]],
]
weak_threshold = 50
print("STUDENT PERFORMANCE TREND ANALYSIS")
for student_index in range(len(students)):
    total_change = 0
    weak_count = 0
    print(f"\n{students[student_index]}")
    print("Subject    Test 1  Test 2  Test 3  Change  Trend")
    for subject_index in range(len(subjects)):
        first = scores[student_index][subject_index][0]
        second = scores[student_index][subject_index][1]
        third = scores[student_index][subject_index][2]
        change = third - first
        total_change += change
        if (first + second + third) / 3 < weak_threshold:
            weak_count += 1
        trend = "Improving" if first < second < third else ("Declining" if first > second > third else "Mixed")
        print(f"{subjects[subject_index]:10} {first:6} {second:7} {third:7} {change:7}  {trend}")
    if weak_count > 0:
        category = "NEEDS SUPPORT"
    elif total_change >= 15:
        category = "STRONG IMPROVEMENT"
    elif total_change < 0:
        category = "DECLINING OVERALL"
    else:
        category = "STEADY PERFORMANCE"
    print(f"Weak subjects (average below {weak_threshold}): {weak_count}; overall change: {total_change}; classification: {category}")
