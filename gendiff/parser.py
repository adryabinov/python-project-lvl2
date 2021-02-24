import json
import yaml


FORMAT_TO_PARSER = {
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
    'json': json.load,
}

input_formats = FORMAT_TO_PARSER.keys()


def parse_data(data, data_format):
    if data_format in input_formats:
        return FORMAT_TO_PARSER[data_format](data)
    raise ValueError(f"{data} not in supported formats:{''.join(input_formats)}")
