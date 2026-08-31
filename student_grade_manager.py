def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("================================")
print("     STUDENT GRADE MANAGER")
print("================================")

student_name = input("Enter student name: ")

maths_mark = int(input("Enter Maths mark: "))
science_mark = int(input("Enter Science mark: "))
english_mark = int(input("Enter English mark: "))

total_marks = maths_mark + science_mark + english_mark
average_marks = total_marks / 3

grade = calculate_grade(average_marks)

print()
print("================================")
print("        STUDENT DETAILS")
print("================================")

print("Student name:", student_name)
print("Maths mark:", maths_mark)
print("Science mark:", science_mark)
print("English mark:", english_mark)
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Grade:", grade)