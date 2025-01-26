#!/bin/sh -e
set -x

uv run ruff format .
uv run mypy --check-untyped-defs -p src