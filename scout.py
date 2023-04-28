import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Python script template with command line arguments.")
    parser.add_argument('-R', '--resume', action='store_true', help='Resume the program if exists.')
    parser.add_argument('-t', '--target', type=str, help='Target string to be saved in the first position of the array.')
    parser.add_argument('-f', '--file', type=str, help='File location to read into an array of strings.')
    parser.add_argument('-o', '--output', type=str, default='./', help='Output path to save as a variable. Defaults to the local folder.')
    args, unknown = parser.parse_known_args()
    if len(unknown) == 0 and len(vars(args)) == 1:  # Check if there are any arguments other than the default output path
        parser.print_help()
        exit(0)
    return args


def resume_function():
    """
    A sample function to simulate resuming the program.
    """
    print("Resuming the program...")

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

def process_targets(target, file_path):
    """
    Processes target strings from the given target and file_path arguments.

    Args:
        target (str): The target string to add to the array.
        file_path (str): The path of the file containing target strings.

    Returns:
        list: An array containing the target strings.
    """
    targets = add_target_to_array(target)

    if file_path:
        file_lines = read_file_into_array(file_path)
        targets.extend(file_lines)

    return targets

def main():
    args = parse_arguments()

    if args.resume:
        resume_function()

    targets = process_targets(args.target, args.file)
    output_path = args.output

    print("Targets:", targets)
    print("Output path:", output_path)

if __name__ == "__main__":
    main()
    