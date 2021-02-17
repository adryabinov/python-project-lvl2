import os
import json
import yaml
from pathlib import Path


EXT_TO_LOADER = {
    '.yml': lambda x: yaml.load(open(x), Loader=yaml.FullLoader),
    '.yaml': lambda x: yaml.load(open(x), Loader=yaml.FullLoader),
    '.json': lambda x: json.load(open(x)),
}

supported_ext = list(EXT_TO_LOADER.keys())


def load_file(path):
    ext = Path(path).suffix
    if ext in supported_ext:
        return EXT_TO_LOADER[ext](os.path.abspath(path))
    raise ValueError(
            f"{ext} not in supported extensions {supported_ext}"
    )

