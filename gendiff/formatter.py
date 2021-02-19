from gendiff.formatters.stylish import format_dict as format_stylish
from gendiff.formatters.plain import format_dict as format_plain
from gendiff.formatters.json import format_dict as format_json

FORMAT_TO_FORMATTER = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}

output_formats = FORMAT_TO_FORMATTER.keys()


def format_dict(diff, output_format='stylish'):
    if output_format in output_formats:
        return FORMAT_TO_FORMATTER[output_format](diff)
    raise ValueError(
        f"{output_format} not in supported format's {''.join(output_formats)}"
    )
