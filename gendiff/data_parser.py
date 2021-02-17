import json
import yaml
import itertools


FORMAT_TO_PARSER = {
    'YAML': lambda x: yaml.load(x, Loader=yaml.FullLoader),
    'JSON': lambda x: json.load(x),
}

input_formats = FORMAT_TO_PARSER.keys()

SUFFIX_TO_FORMAT_MAP = {
    ('.yml', '.yaml'): 'YAML',
    ('.json',): 'JSON',
}

supported_suffixes = list(itertools.chain(*SUFFIX_TO_FORMAT_MAP.keys()))


def suffix_to_format(suffix):
    for suffix_list in SUFFIX_TO_FORMAT_MAP:
        if suffix in suffix_list:
            return SUFFIX_TO_FORMAT_MAP[suffix_list]
    raise ValueError(
        f"can\'t translate {suffix} to format, "
        f"sup this suffixes: {supported_suffixes}"
    )


def parse_data(data, data_format):
    if data_format in input_formats:
        return FORMAT_TO_PARSER[data_format](data)
    raise ValueError(f"{data} not in supported formats")
