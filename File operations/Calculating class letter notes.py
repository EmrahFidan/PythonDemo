def calculate_grade(line):
    # Remove the trailing newline character from the line
    line = line.rstrip("\n")
    
    # Split the line into name, and three grades using commas as separators
    name, grade1, grade2, grade3 = line.split(",")
    
    # Convert grade strings to integers
    grade1 = int(grade1)
    grade2 = int(grade2)
    grade3 = int(grade3)
    
    # Calculate the final grade as a weighted average
    final_grade = grade1 * 0.3 + grade2 * 0.3 + grade3 * 0.4
    
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
    
    # Return the formatted string with the name and corresponding letter grade
    return f"{name} ------------------> {letter_grade}\n"


def process_grades(input_file, output_file):
    try:
        # Read input file and calculate grades for each line
        with open(input_file, "r", encoding="utf-8") as file:
            eklenecekler_listesi = [calculate_grade(line) for line in file]
        
        # Write the calculated grades to the output file
        with open(output_file, "w", encoding="utf-8") as file2:
            for line in eklenecekler_listesi:
                file2.write(line)
    
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define input and output file paths
    input_file_path = "File operations/file.txt"
    output_file_path = "File operations/notes.txt"
    
    # Process the grades from the input file and write to the output file
    process_grades(input_file_path, output_file_path)
