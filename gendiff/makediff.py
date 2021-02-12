import os
import json
import yaml
from pathlib import Path

EXTENTIONS_MAP = {
    '.yml':lambda x:yaml.load(open(x)),
    '.yaml':lambda x:yaml.load(open(x)),
    '.json':lambda x:json.load(open(x)),
}

def generate_diff(path1, path2):

    return diff


def parse_file(path):
    ext = Path(path).suffix
    return EXTENTIONS_MAP[ext](os.path.abspath(path))