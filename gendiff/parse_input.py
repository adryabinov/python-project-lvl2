import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--format', '-f', help='set format of output')

    return parser.parse_args()

