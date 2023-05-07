import argparse


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
    if len(unknown) == 0 and len(vars(args)) == 1:
        # Check if there are any arguments other than the default output path
        raise ValueError('No arguments provided.')
    return args
