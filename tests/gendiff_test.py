import pytest
import os
from pathlib import Path
from gendiff.comparator import generate_diff
from gendiff.data_parser import supported_suffixes as suffixes
from gendiff.formatter import output_formats as formats

FIXTURES_DIR_REL = 'fixtures'


def make_path_to(file_name):
    self_dir_path = Path(__file__).absolute().parent
    return os.path.join(self_dir_path, FIXTURES_DIR_REL, file_name)


def read_file_in(path):
    f = open(path)
    return f.read()


map_format_to_result = {}
for _ in formats:
    map_format_to_result[_] = read_file_in(
        make_path_to(f'{_}_out')
    )


@pytest.mark.parametrize('suffix', suffixes)
def test_gendiff_all_supported_suffix(suffix):
    file_path_1 = make_path_to(f'file1{suffix}')
    file_path_2 = make_path_to(f'file2{suffix}')
    for output_format in formats:
        diff = generate_diff(file_path_1, file_path_2, output_format)
        assert diff == map_format_to_result[output_format]


def test_gendiff_stylish_out_default():
    file_path_1 = make_path_to('file1.json')
    file_path_2 = make_path_to('file2.yaml')
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
