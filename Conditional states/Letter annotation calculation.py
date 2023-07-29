# Constants defining the weights
VIZE1_WEIGHT = 0.3
VIZE2_WEIGHT = 0.3
FINAL_WEIGHT = 0.4

def calculate_letter_grade():
    # Get input for the first and second quizzes, and the final exam
    midterm1 = int(input("QUIZ 1:"))
    midterm2 = int(input("QUIZ 2:"))
    final = int(input("FINAL:"))

    # Calculate the weighted grade
    weighted_grade = midterm1 * VIZE1_WEIGHT + midterm2 * VIZE2_WEIGHT + final * FINAL_WEIGHT

    # Convert the weighted grade to a letter grade and print it to the screen
    if weighted_grade >= 90:
        print("AA")
    elif weighted_grade >= 85:
        print("BA")
    elif weighted_grade >= 80:
        print("BB")
    elif weighted_grade >= 75:
        print("CB")
    elif weighted_grade >= 70:
        print("CC")
    elif weighted_grade >= 65:
        print("DC")
    elif weighted_grade >= 60:
        print("DD")
    elif weighted_grade >= 55:
        print("FD")
    else:
        print("FF")

if __name__ == "__main__":
    # Run the function
    calculate_letter_grade()
