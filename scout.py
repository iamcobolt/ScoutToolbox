from pathlib import Path
from utils import *


def resume_function(output_path):
    """
    the main function which is used to help a scan resume based on a supplied incomplete scan folder.

    Args:
        output_path (str): The output path provided by the user.
    """
    if not output_path or output_path == './':
        print("Error: No scan foler provided to resume use -o [path] to add file.")
        exit(1)
    output_path = Path(output_path)
    log_file = output_path / 'log.txt'
    targets_file = output_path / 'targets.txt'
    if not (log_file.exists() and targets_file.exists()):
        print("Error: Existing scan files not found.")
        exit(1)
    print("Resuming the program...")


def process_targets(target, file_path, output_path):
    """
    Process the targets based on the provided target and file path.

    :param target: A single target provided as a string.
    :param file_path: A file path containing targets, one per line.
    :param output_path: The output path for storing invalid targets.
    :return: A list of processed and validated targets.
    """
    targets = []

    if target:
        if Target.validate_targets([target], output_path):
            targets.append(Target(target))
        else:
            print('No valid target found')

    if file_path:
        file_lines = read_file_into_array(file_path)
        for line in file_lines:
            if Target.validate_targets([line], output_path):
                targets.append(Target(line))
            else:
                print(f'No valid target found in line: {line}')

    return targets


def main():
    try:
        args = parse_arguments()
    except ValueError as e:
        print(f'Error: {str(e)}')
        parser = argparse.ArgumentParser(description="Python script template with command line arguments.")
        parser.print_help()
        return

    #Resume Functionality
    if args.resume:
        resume_function(args.output)

    #set the output path
    output_path = args.output

    # Check if the output directory exists, if not create it
    Path(output_path).mkdir(parents=True, exist_ok=True)

    targets = process_targets(args.target, args.file, output_path)
    for target in targets:
        print(target.target)
    print("Output path:", output_path)


if __name__ == "__main__":
    main()
