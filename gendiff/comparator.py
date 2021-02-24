import os
from pathlib import Path
from gendiff.parser import parse_data
from gendiff.formatter import format_tree
from gendiff.tree import make_diff


def generate_diff(path1, path2, formatter='stylish'):
    data1 = open(os.path.abspath(path1))
    data2 = open(os.path.abspath(path2))

    format1 = get_format(path1)
    format2 = get_format(path2)

    parsed_data1 = parse_data(data1, format1)
    parsed_data2 = parse_data(data2, format2)

    diff = make_diff(parsed_data1, parsed_data2)
    formatted_diff = format_tree(diff, formatter)

    return formatted_diff


def get_format(path):
    return Path(path).suffix.lower()[1:]
