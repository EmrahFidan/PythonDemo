# Lists to store students who failed and students who passed
failed_students = list()    # List to store students who failed
passed_students = list()    # List to store students who passed

# Function to calculate the grade and sort students into corresponding lists
def calculate_grade(line):
    # Remove the trailing newline character from the line
    line = line.rstrip("\n")
    elements = line.split(",")

    name = elements[0]
    grade1 = int(elements[1])
    grade2 = int(elements[2])
    grade3 = int(elements[3])

    # Calculate the final grade as a weighted average
    final_grade = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    # Determine the letter grade based on the final grade
    if final_grade >= 90:
        letter_grade = "AA"
    elif final_grade >= 85:
        letter_grade = "BA"
    elif final_grade >= 80:
        letter_grade = "BB"
    elif final_grade >= 75:
        letter_grade = "CB"
    elif final_grade >= 70:
        letter_grade = "CC"
    elif final_grade >= 65:
        letter_grade = "DC"
    elif final_grade >= 60:
        letter_grade = "DD"
    elif final_grade >= 55:
        letter_grade = "FD"
    else:
        letter_grade = "FF"

    # Append the student to the corresponding list based on their grade
    if letter_grade == "FF":
        failed_students.append(name + "------->" + str(final_grade) + "-------> " + letter_grade + "\n")
    else:
        passed_students.append(name + "------->" + str(final_grade) + "------> " + letter_grade + "\n")

    # Return the formatted string with the name, grade, and letter grade
    return name + "--------> " + str(final_grade) + "--------> " + letter_grade + "\n"

with open("File operations/file.txt", "r", encoding="utf-8") as file:
    grades_list = []

    # Calculate grades for each student and store them in a list
    for line in file:
        grades_list.append(calculate_grade(line))

# Write the calculated grades to the "notes.txt" file
with open("File operations/notes.txt", "w", encoding="utf-8") as file2:
    for grade in grades_list:
        file2.write(grade)

# Write the list of students who failed to the "eliminated.txt" file
with open("File operations/eliminated.txt", "w", encoding="utf-8") as file2:
    for failed_student in failed_students:
        file2.write(failed_student)

# Write the list of students who passed to the "passed.txt" file
with open("File operations/passed.txt", "w", encoding="utf-8") as file3:
    for passed_student in passed_students:
        file3.write(passed_student)
