#!/bin/sh -e
set -x

uv run ruff check --fix .
uv run mypy --check-untyped-defs -p src