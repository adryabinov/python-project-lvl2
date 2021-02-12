import gendiff.formatters.stylish
import gendiff.formatters.plain
import gendiff.formatters.json

MAP_FORMAT_TO_FORMATTER = {
    'stylish': lambda x: gendiff.formatters.stylish.format(x),
    'plain': lambda x: gendiff.formatters.plain.format(x),
    'json': lambda x: gendiff.formatters.json.format(x),
}


def format(data, formatter='stylish'):
    return MAP_FORMAT_TO_FORMATTER[formatter](data)
