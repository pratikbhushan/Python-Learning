marks = [56, 78, 95, 45, 100, 89, 70]

# Find:
# 1. The lowest marks
# 2. The roll number (i.e., index) of the student with lowest marks

lowest_marks = marks[0]
for minimum in marks:
    if minimum < lowest_marks:
        lowest_marks = minimum

print(lowest_marks)
