import os

def get_grade(avg):
    if 90 <= avg <= 100:
        return "A"
    elif 81 <= avg < 90:
        return "B"
    elif 71 <= avg < 81:
        return "C"
    elif 61 <= avg < 71:
        return "D"
    elif 51 <= avg < 61:
        return "E"
    else:
        return "Fail"

# Input: number of students
num_students = int(input("Enter number of students: "))

# Minimum subjects
subject_count = 4
students = []
subject_names = []

for i in range(num_students):
    print(f"\nEnter details for Student {i+1}")
    name = input("Enter student name: ")
    subjects = []

    for j in range(1, subject_count + 1):
        subject_name = input(f"Subject {j} name: ")
        if i == 0:
            subject_names.append(subject_name)  # Only store once from first student
        mark = float(input(f"Marks in {subject_name}: "))
        subjects.append({'subject': subject_name, 'mark': mark})

    total = sum(sub['mark'] for sub in subjects)
    average = total / subject_count
    grade = get_grade(average)

    students.append({
        'name': name,
        'subjects': subjects,
        'total': total,
        'average': average,
        'grade': grade
    })

# Get terminal width
try:
    term_width = os.get_terminal_size().columns
except OSError:
    term_width = 100  # Default fallback

# Prepare header and rows
header = f"{'Student Name':<15}"
for sub in subject_names:
    header += f"{sub:<15}"
header += f"{'Total':<10}{'Average':<10}{'Grade':<10}"

line_len = len(header)
centered_line = lambda text: text.center(term_width)

# Display the final grade sheet
print("\n\n" + centered_line("=========== FINAL CONSOLIDATED GRADE SHEET ==========="))
print(centered_line(header))
print(centered_line("=" * line_len))

for student in students:
    row = f"{student['name']:<15}"
    for sub in student['subjects']:
        row += f"{sub['mark']:<15}"
    row += f"{student['total']:<10.2f}{student['average']:<10.2f}{student['grade']:<10}"
    print(centered_line(row))
