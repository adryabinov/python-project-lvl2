lint:
	poetry run flake8 gendiff

build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

.PHONY: lint build install publish