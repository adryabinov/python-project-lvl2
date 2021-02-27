import pytest
import os
from pathlib import Path
from gendiff.comparator import generate_diff
from gendiff.parser import input_formats
from gendiff.formatter import output_formats as formats

FIXTURES_DIR = 'fixtures'


def make_path(file_name):
    dir_path = Path(__file__).absolute().parent
    return os.path.join(dir_path, FIXTURES_DIR, file_name)


def read_file(path):
    with open(path) as f:
        return f.read()


map_format_to_result = {}
for output_format in formats:
    map_format_to_result[output_format] = read_file(
        make_path(f'{output_format}_out')
    )


@pytest.mark.parametrize('input_format', input_formats)
def test_gendiff_format(input_format):
    file_path_1 = make_path(f'file1.{input_format}')
    file_path_2 = make_path(f'file2.{input_format}')
    for output_format in formats:
        diff = generate_diff(file_path_1, file_path_2, output_format)
        assert diff == map_format_to_result[output_format]


def test_gendiff_default_out():
    file_path_1 = make_path('file1.json')
    file_path_2 = make_path('file2.yaml')
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
