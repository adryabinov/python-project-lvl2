### Hexlet tests and linter status:
[![Actions Status](https://github.com/adryabinov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/adryabinov/python-project-lvl2/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/11aeb09c97585a10a336/maintainability)](https://codeclimate.com/github/adryabinov/python-project-lvl2/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/11aeb09c97585a10a336/test_coverage)](https://codeclimate.com/github/adryabinov/python-project-lvl2/test_coverage)
# Gendiff

Gendiff generate diff-log of 2 files in YAML or JSON.

## Installation

Python packaging and dependency management tool Poetry should be preinstalled.

```bash
make build
make package-install
```
[![asciicast](https://asciinema.org/a/Qli4WnKWLwFwykJktHDM6X4DW.svg)](https://asciinema.org/a/Qli4WnKWLwFwykJktHDM6X4DW)
## Usage
```bash
gendiff FIRST_PATH SECOND_PATH -format format(OPTIONAL)
```
work vs .json (JSON):

[![asciicast](https://asciinema.org/a/cgYbVBRLdYDLPnDrYJMnAkLZv.svg)](https://asciinema.org/a/cgYbVBRLdYDLPnDrYJMnAkLZv)


work vs .yml .yaml (YаML):

[![asciicast](https://asciinema.org/a/0wx8jBosiZ7A5aLn9PGPI4K6G.svg)](https://asciinema.org/a/0wx8jBosiZ7A5aLn9PGPI4K6G)
[![asciicast](https://asciinema.org/a/PnmXPz7WQ8TKFV5tbksW4N21o.svg)](https://asciinema.org/a/PnmXPz7WQ8TKFV5tbksW4N21o)


out formats: -format(-f) stylish(json-like, DEFAULT), json, plain:


stylish:

[![asciicast](https://asciinema.org/a/O3ZvjRTBvWr0CPAHPotOvZXR7.svg)](https://asciinema.org/a/O3ZvjRTBvWr0CPAHPotOvZXR7)


json:

[![asciicast](https://asciinema.org/a/kLxafvAwxUb32w1u84xQM75Im.svg)](https://asciinema.org/a/kLxafvAwxUb32w1u84xQM75Im)


plain:

[![asciicast](https://asciinema.org/a/mpz3Y12yVSchW1u9xgdkMdimA.svg)](https://asciinema.org/a/mpz3Y12yVSchW1u9xgdkMdimA)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT]
