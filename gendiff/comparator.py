import os
from itertools import chain
from pathlib import Path
from gendiff.parser import parse_data
from gendiff.formatter import format_dict
from gendiff.diff_tree_maker import make_diff

SUFFIX_TO_FORMAT = {
    ('.yml', '.yaml'): 'yaml',
    ('.json',): 'json',
}

supported_suffixes = list(chain(*SUFFIX_TO_FORMAT.keys()))


def suffix_to_format(suffix):
    for suffix_list in SUFFIX_TO_FORMAT:
        if suffix in suffix_list:
            return SUFFIX_TO_FORMAT[suffix_list]
    raise ValueError(
        f"can\'t translate {suffix} to format, "
        f"sup this suffixes: {supported_suffixes}"
    )


def generate_diff(path1, path2, formatter='stylish'):
    data1 = open(os.path.abspath(path1))
    data2 = open(os.path.abspath(path2))

    format1 = suffix_to_format(Path(path1).suffix.lower())
    format2 = suffix_to_format(Path(path2).suffix.lower())

    parsed_data1 = parse_data(data1, format1)
    parsed_data2 = parse_data(data2, format2)

    diff = make_diff(parsed_data1, parsed_data2)
    formatted_diff = format_dict(diff, formatter)

    return formatted_diff
