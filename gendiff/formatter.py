from gendiff.formatters.stylish import format_diff as format_stylish
from gendiff.formatters.plain import format_diff as format_plain
from gendiff.formatters.json import format_diff as format_json

MAP_FORMAT_TO_FORMATTER = {
    'stylish': lambda x: format_stylish(x),
    'plain': lambda x: format_plain(x),
    'json': lambda x: format_json(x),
}


def format_diff(diff, formatter='stylish'):
    return MAP_FORMAT_TO_FORMATTER[formatter](diff)
