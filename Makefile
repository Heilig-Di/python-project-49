build:
	uv build

publish:
	uv publish --dry-run

package-install:
	uv tool install dist/*.whl

install:
	uv add

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-prime:
	uv run brain-prime

brain-progression:
	uv run brain-progression

lint:
	uv run ruff check brain_games

.PHONY: build publish package-install install brain-games brain-even lint brain-calc brain-gcd brain-prime brain-progression
