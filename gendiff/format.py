import gendiff.formatters.stylish
import gendiff.formatters.plain
import gendiff.formatters.json

MAP_FORMAT_TO_FORMATTER = {
    'stylish': lambda x: gendiff.formatters.stylish.format_diff(x),
    'plain': lambda x: gendiff.formatters.plain.format_diff(x),
    'json': lambda x: gendiff.formatters.json.format_diff(x),
}


def format_diff(diff, formatter='stylish'):
    return MAP_FORMAT_TO_FORMATTER[formatter](diff)
