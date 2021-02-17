import argparse
from gendiff.formatter import output_formats


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--format',
                        '-f',
                        default='stylish',
                        choices=output_formats,
                        help='set format of output')
    return parser.parse_args()
