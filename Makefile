


default: run
all: install run

install:
	setup 3.10 uv

run:
	.venv/bin/python main.py

test: lint
	.venv/bin/python -m pytest

lint:
	.venv/bin/python -m mypy ./main.py

clean:
	trash {./venv/,./.venv/}
