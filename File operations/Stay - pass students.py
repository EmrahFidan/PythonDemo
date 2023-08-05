# Constants for grade boundaries and corresponding letter grades
GRADE_BOUNDARIES = {
    90: "AA",
    85: "BA",
    80: "BB",
    75: "CB",
    70: "CC",
    65: "DC",
    60: "DD",
    55: "DF",
    50:  "FF",
}

# Function to calculate the grade based on the given scores
def calculate_grade(line):
    line = line.rstrip("\n")
    elements = line.split(",")
    name = elements[0]
    grade1 = int(elements[1])
    grade2 = int(elements[2])
    grade3 = int(elements[3])

    final_grade = grade1 * 0.3 + grade2 * 0.3 + grade3 * 0.4

    # Find the corresponding letter grade based on the calculated score
    for boundary, grade in GRADE_BOUNDARIES.items():
        if final_grade >= boundary:
            return f"{name} -----------------> {final_grade} ------------> {grade}\n"

    # If the score is below the lowest boundary, assign FF grade
    return f"{name} -----------------> {final_grade} ------------> FF\n"

# Function to write data to the specified output file
def write_to_file(data_list, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for item in data_list:
            try:
                file.write(item)
            except:
                pass

if __name__ == "__main__":
    # Define input file path and output files path
    input_file_path = "File operations/file.txt"
    output_files_path = "File operations/"

    # Lists to store calculated grades, staying students (kalanlar), and passing students (geçenler)
    calculate_note_list = []
    stayers_list = []
    passers_list = []

    # Read the input file and calculate grades for all students
    with open(input_file_path, "r", encoding="utf-8") as file:
        for line in file:
            calculate_note_list.append(calculate_grade(line))
            # Separate staying students (kalanlar) and passing students (geçenler) based on DF grade
            if "DF" in calculate_grade(line):
                stayers_list.append(calculate_grade(line))
            else:
                passers_list.append(calculate_grade(line))

    # Write the calculated grades to separate output files
    write_to_file(calculate_note_list, output_files_path + "notlar.txt")
    write_to_file(stayers_list, output_files_path + "stayers.txt")
    write_to_file(passers_list, output_files_path + "passers.txt")
