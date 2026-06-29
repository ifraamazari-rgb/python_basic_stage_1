# Dictionary of student names and marks
students = {
    "Ali": 85,
    "Ahmed": 78,
    "Sara": 92,
    
}

total = 0

for marks in students.values():
    total += marks

average = total / len(students)

print("Total Marks:", total)
print("Average Marks:", average)