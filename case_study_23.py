"""Case 23: Detect course time conflicts and room clashes using tuples."""
# Tuple format: (course, day, start period, end period, room); end is exclusive.
schedule = [
    ("Python", "Mon", 1, 3, "R101"),
    ("Math", "Mon", 3, 5, "R101"),
    ("Physics", "Mon", 2, 4, "R202"),
    ("English", "Tue", 1, 2, "R101"),
    ("Lab", "Tue", 1, 3, "R101"),
]
unavailable_rooms = [("Mon", 4, "R101"), ("Tue", 2, "R101")]
conflict_count = 0
print("STUDENT TIMETABLE CONFLICT DETECTION")
print("Course     Day  Start-End  Room")
for course, day, start, end, room in schedule:
    print(f"{course:10} {day:4} {start:2}-{end:2}       {room}")
print("\nChecks")
for i in range(len(schedule)):
    course_a, day_a, start_a, end_a, room_a = schedule[i]
    if start_a < 1 or end_a <= start_a:
        print(f"INVALID PERIOD: {course_a}")
        conflict_count += 1
    for j in range(i + 1, len(schedule)):
        course_b, day_b, start_b, end_b, room_b = schedule[j]
        if day_a == day_b and start_a < end_b and start_b < end_a:
            print(f"TIME CONFLICT: {course_a} and {course_b} on {day_a}")
            conflict_count += 1
            if room_a == room_b:
                print(f"  ROOM CLASH: both request {room_a}")
    for unavailable_day, unavailable_period, unavailable_room in unavailable_rooms:
        if day_a == unavailable_day and room_a == unavailable_room and start_a <= unavailable_period < end_a:
            print(f"UNAVAILABLE ROOM: {course_a} uses {room_a} during period {unavailable_period}")
            conflict_count += 1
if conflict_count == 0:
    print("Timetable is valid.")
else:
    print(f"Total detected issue(s): {conflict_count}")
