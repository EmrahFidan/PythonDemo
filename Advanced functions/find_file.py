import os

def get_files_by_extension(directory, extension):
    """
    Get a dictionary of files and their directories with the given extension.

    Args:
        directory (str): The directory to search for files.
        extension (str): The file extension to look for.

    Returns:
        dict: A dictionary with file names as keys and their directories as values.
    """
    file_dict = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                file_dict[filename] = root
    return file_dict

def write_files_to_txt(file_dict, filename):
    """
    Write file names and directories to a text file.

    Args:
        file_dict (dict): A dictionary with file names as keys and their directories as values.
        filename (str): The name of the text file to write the information.
    """
    with open(filename, "w") as file:
        for filename, directory in file_dict.items():
            file.write(f"Dosya Direction {directory} Dosya Ismi: {filename}\n")

def main():
    desktop_directory = "D:\Masaüstü"

    pdf_files = get_files_by_extension(desktop_directory, ".pdf")
    txt_files = get_files_by_extension(desktop_directory, ".txt")
    mp4_files = get_files_by_extension(desktop_directory, ".mp4")

    write_files_to_txt(pdf_files, "pdf_dosyalari.txt")
    write_files_to_txt(txt_files, "txt_dosyalari.txt")
    write_files_to_txt(mp4_files, "mp4_dosyalari.txt")

if __name__ == "__main__":
    main()
