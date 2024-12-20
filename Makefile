build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

lint:
	poetry run ruff check brain_games

.PHONY: build publish package-install install brain-games brain-even lint

