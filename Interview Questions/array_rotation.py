def rotate_list(array):
    """
    Rotate the given list by the value of the first element.
    The first element represents the index of the new starting element.
    """
    old_start_index = array[0]
    new_start_index = [str(array[old_start_index])]

    current_index = old_start_index + 1
    array_length = len(array)

    while current_index % array_length != old_start_index:
        new_start_index.append(str(array[current_index % array_length]))
        current_index += 1

    return " ".join(new_start_index)

# Test cases
print(rotate_list([1, 2, 3, 4, 5]))
print(rotate_list([4, 6, 9, 7, 0, 4, 2, 1]))
