def insertion_sort_students(students):
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1

        # Move elements that are greater than key to one position ahead
        while j >= 0 and students[j]["grade"] > key["grade"]:
            students[j + 1] = students[j]
            j -= 1

        students[j + 1] = key  # Insert the student in the correct position

    return students

# List of students with their grades
students = [
    {"name": "Ahmed", "grade": 85},
    {"name": "Sara", "grade": 92},
    {"name": "Omar", "grade": 78},
    {"name": "Laila", "grade": 90},
    {"name": "Khaled", "grade": 88}
]

# Sorting students by grades
sorted_students = insertion_sort_students(students)

# Print the sorted list
print("Sorted Students by Grade:")
for student in sorted_students:
    print(student)
