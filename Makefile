.PHONY: install check test

install:
	uv sync

check:
	uv run pytest

test:
	uv run pytest
