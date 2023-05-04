import argparse
import ipaddress
import validators
from pathlib import Path
from furl import furl
from validators import ValidationFailure


def is_valid_ip_address(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False


def is_valid_network_block(block):
    try:
        ipaddress.ip_network(block, strict=False)
        return True
    except ValueError:
        return False


def is_valid_host(host):
    if host.startswith('[') and host.endswith(']'):
        host = host[1:-1]

    if is_valid_ip_address(host) or validators.domain(host):
        return True
    return False


def is_valid_url(parsed_url):
    url_validation_result = validators.url(parsed_url.url)
    if url_validation_result is None:
        return False
    elif url_validation_result:
        if parsed_url.url:
            return True
        else:
            return False
    else:
        return False


def is_valid_domain(domain_or_url):
    try:
        parsed_url = furl(domain_or_url)
        host = parsed_url.host
        scheme = parsed_url.scheme

        if not host:
            raise ValueError("Error: Invalid or missing host in the URL.")

        if not is_valid_url(parsed_url):
            raise ValueError("Error: Invalid URL value detected")

        if not is_valid_host(host):
            raise ValueError("Error: Invalid domain name or IP address in the URL.")

        return True

    except ValueError as e:
        if 'INVALID_HOST_CHARS' in str(e):
            print("Error: Invalid characters in the host.")
        else:
            print(e)
        return False



def validate_targets(targets, output_path):
    valid_targets = []
    invalid_targets = []

    for tgt in targets:
        if is_valid_ip_address(tgt):
            valid_targets.append(tgt)
        elif is_valid_network_block(tgt):
            network = ipaddress.ip_network(tgt, strict=False)
            for ip in network:
                valid_targets.append(str(ip))
        elif is_valid_domain(tgt):
            parsed_url = furl(tgt)
            host = parsed_url.host
            if host.startswith('[') and host.endswith(']'):
                host = host[1:-1]
            if is_valid_ip_address(host):
                valid_targets.append(tgt)
            else:
                valid_targets.append(tgt)
        else:
            invalid_targets.append(tgt)

    if invalid_targets:
        with open(f"{output_path}/invalid_targets.txt", "w") as f:
            for invalid_target in invalid_targets:
                f.write(f"{invalid_target}\n")
        print("Error: Invalid targets have been identified. Check the invalid_targets.txt and log files in the output directory.")

    if not valid_targets:
        print("No valid target or file path provided.")
    else:
        print("Valid targets:", valid_targets)

    return valid_targets


def parse_arguments():
    parser = argparse.ArgumentParser(description="Python script template with command line arguments.")
    parser.add_argument('-R', '--resume', action='store_true', help='Resume the program if exists.')
    parser.add_argument('-t', '--target', type=str,
                        help='Target string to be saved in the first position of the array.')
    parser.add_argument('-f', '--file', type=str, help='File location to read into an array of strings.')
    parser.add_argument('-sA', '--scan-appsec', type=str,
                        help='Preform only Appsec related functionality, will not attempt to identify and exploit services using other protocols such as RDP or SSH')
    parser.add_argument('-sX', '--scan-external', type=str,
                        help='Preform only external Netpen related functionality, will identify some web scanning but will not attempt to authenticate or identify more advanced web application findings')
    parser.add_argument('-sI', '--scan-internal', type=str,
                        help='Preform only Internal Netpen related functionality, will identify some ')
    parser.add_argument('-o', '--output', type=str, default='./',
                        help='Define the folder to create the scout folder in. Defaults to the local folder.')
    args, unknown = parser.parse_known_args()
    if len(unknown) == 0 and len(
            vars(args)) == 1:  # Check if there are any arguments other than the default output path
        parser.print_help()
        exit(0)
    return args


def resume_function(output_path):
    """
    A sample function to simulate resuming the program.

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
        targets.append(target)

    if file_path:
        file_lines = read_file_into_array(file_path)
        targets.extend(file_lines)

    valid_targets = validate_targets(targets, output_path)

    return valid_targets


def main():
    args = parse_arguments()
    if args.resume:
        resume_function(args.output)
    output_path = args.output

    # Check if the output directory exists, if not create it
    Path(output_path).mkdir(parents=True, exist_ok=True)

    targets = process_targets(args.target, args.file, output_path)
    print("Targets:", targets)
    print("Output path:", output_path)


if __name__ == "__main__":
    main()
