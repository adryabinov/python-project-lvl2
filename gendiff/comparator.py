import os
from gendiff.data_parser import suffix_to_format
from gendiff.data_parser import parse_data
from pathlib import Path
from gendiff.formatter import format_diff
from gendiff.diff_tree_maker import make_diff


def generate_diff(path1, path2, formatter='stylish'):
    data1 = open(os.path.abspath(path1))
    data2 = open(os.path.abspath(path2))

    format1 = suffix_to_format(Path(path1).suffix.lower())
    format2 = suffix_to_format(Path(path2).suffix.lower())

    parsed_data1 = parse_data(data1, format1)
    parsed_data2 = parse_data(data2, format2)

    diff = make_diff(parsed_data1, parsed_data2)
    formated_diff = format_diff(diff, formatter)

    return formated_diff
