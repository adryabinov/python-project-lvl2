# content of sample_test.py

import json
import os

import pytest

import gendiff.makediff
from gendiff.format import format_diff

diff = open('tests/fixtures/stylish-out')



@pytest.fixture(scope="function", params=[
("tests/fixtures/file1.json", "tests/fixtures/file2.json", diff.read()),
("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", diff.read()),
("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", diff.read())
])


def param_test(request):
    return request.param


def test_gendiff_makediff_generate_diff(param_test):
    (file1, file2, expected_output) = param_test
    result = format_diff(gendiff.makediff.generate_diff(file1, file2), 'stylish')
    assert result == expected_output
