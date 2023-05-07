def add_target_to_array(target):
    """
    Adds the target string to the first position of the array.

    Args:
        target (str): The target string to add to the array.

    Returns:
        list: An array containing the target string.
    """
    targets = []
    if target:
        targets.append(target)
    return targets


def read_file_into_array(file_path):
    """
    Reads the contents of a file into an array of strings.

    Args:
        file_path (str): The path of the file to read.

    Returns:
        list: An array containing the lines from the file as strings.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]


def write_invalid_targets(output_path, invalid_targets):
    with open(f"{output_path}/invalid_targets.txt", "a") as f:
        for invalid_target in invalid_targets:
            f.write(f"{invalid_target}\n")
    print("Error: Invalid targets have been identified. Check the invalid_targets.txt and log files in the output directory.")