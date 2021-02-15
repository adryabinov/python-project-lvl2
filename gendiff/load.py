import os
import json
import yaml
from pathlib import Path


EXT_TO_LOADER = {
    '.yml': lambda x: yaml.load(open(x), Loader=yaml.FullLoader),
    '.yaml': lambda x: yaml.load(open(x), Loader=yaml.FullLoader),
    '.json': lambda x: json.load(open(x)),
}


def load_file(path):
    ext = Path(path).suffix
    return EXT_TO_LOADER[ext](os.path.abspath(path))
