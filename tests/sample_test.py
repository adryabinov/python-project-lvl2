# content of sample_test.py

import pytest
import json
import yaml
import os

import gendiff.parse_input
import gendiff.makediff
import gendiff.makeout

file1_out = json.load(open(os.path.abspath('tests/fixtures/file1.json')))


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

