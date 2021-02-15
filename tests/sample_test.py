# content of sample_test.py

from gendiff import generate_diff


def test_gendiff_compare_plain_is_empty():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json', 'plain') == ''


def test_gendiff_stylish_default():
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json', 'stylish') == \
           generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file1.json')


def test_gendiff_yaml_load():
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'stylish') == \
           generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')


def test_gendiff_plain():
    out = open('tests/fixtures/plain_out')
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'plain') == out.read()


def test_gendiff_stylish():
    out = open('tests/fixtures/stylish_out')
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == out.read()


def test_gendiff_json():
    out = open('tests/fixtures/json_out')
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'json') == out.read()
