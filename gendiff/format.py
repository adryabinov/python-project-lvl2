import gendiff.formatters.stylish
import gendiff.formatters.plain
import gendiff.formatters.json

MAP_FORMAT_TO_FORMATTER = {
    'stylish': lambda x: gendiff.formatters.stylish.format_data(x),
    'plain': lambda x: gendiff.formatters.plain.format_data(x),
    'json': lambda x: gendiff.formatters.json.format_data(x),
}


def format_data(data, formatter='stylish'):
    return MAP_FORMAT_TO_FORMATTER[formatter](data)
