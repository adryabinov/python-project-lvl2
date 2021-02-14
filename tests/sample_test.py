# content of sample_test.py

import json
import os

import pytest

import gendiff.makediff
import gendiff.format
import gendiff.parser

file1_out = json.load(open(os.path.abspath('tests/fixtures/file1.json')))
file1_file2_diff = 'DIFF'
plain1_plain2_diff = open(os.path.abspath('tests/fixtures/plain_out.txt'))


@pytest.fixture(scope="function", params=[
("tests/fixtures/file1.json", file1_out),
("tests/fixtures/file1.yaml", file1_out),
("tests/fixtures/file1.yml", file1_out)
])

def param_test(request):
    return request.param
    
def test_gendiff_makediff_parse_file(param_test):
    (input, expected_output) = param_test
    result = gendiff.makediff.parse_file(input)
    assert result == expected_output


@pytest.fixture(scope="function", params=[
(("tests/fixtures/plain1.json", "tests/fixtures/plain2.json"), plain1_plain2_diff),
(("tests/fixtures/file1.json", "tests/fixtures/file2.json"), file1_file2_diff),
(("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml"), file1_file2_diff),
(("tests/fixtures/file1.yml", "tests/fixtures/file2.yml"), file1_file2_diff)
])


def param_test(request):
    return request.param


def test_gendiff_makediff_generate_diff(param_test):
    (input, expected_output) = param_test
    result = gendiff.makediff.generate_diff(input)
    assert result == expected_output
