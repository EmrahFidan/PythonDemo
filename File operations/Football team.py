def organize_footballers_by_team(input_file):
    # Create a dictionary to store footballers grouped by their teams
    footballers_by_team = {
        "Galatasaray": [],
        "Fenerbahçe": [],
        "Beşiktaş": []
    }

    # Read the input file and organize footballers into their respective teams
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            name, team = line.split(",")
            if team in footballers_by_team:
                footballers_by_team[team].append(line)

    return footballers_by_team


def write_to_file(footballers, output_file):
    # Write the footballers' data to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for player in footballers:
            file.write(player + "\n")


if __name__ == "__main__":
    # Define input and output file paths
    input_file_path = "File operations/footballer.txt"
    output_files_path = "File operations/"

    # Organize footballers by their teams
    footballers_by_team = organize_footballers_by_team(input_file_path)

    # Write each team's footballers to separate files
    for team, footballers in footballers_by_team.items():
        output_file_path = output_files_path + team.lower() + ".txt"
        write_to_file(footballers, output_file_path)
