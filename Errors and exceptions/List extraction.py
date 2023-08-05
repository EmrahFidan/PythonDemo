def print_numeric_strings(input_list):
    """
    Prints the numeric strings found in the given list.

    Args:
        input_list (list): A list of strings.

    """
    for item in input_list:
        if item.isdigit():
            print(item)

liste = ["345", "sadas", "324a", "14", "kemal", "558484", "emrah"]
print_numeric_strings(liste)
