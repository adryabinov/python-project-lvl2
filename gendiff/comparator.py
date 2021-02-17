from gendiff.loader import load_file
from gendiff.formatter import format_diff
from gendiff.diff_tree_maker import make_diff


def generate_diff(path1, path2, formatter='stylish'):
    data1 = load_file(path1)
    data2 = load_file(path2)
    return format_diff(make_diff(data1, data2), formatter)
