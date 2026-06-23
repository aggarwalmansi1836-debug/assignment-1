# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Input marks of 5 subjects
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)

# Calculate grade
grade = calculate_grade(average)

# Display result
print("\n----- Result -----")
print("Average Marks:", average)
print("Grade:", grade)
