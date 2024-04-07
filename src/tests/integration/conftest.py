import os

import pytest


def clear_files():
    files_and_dirs: list[str] = os.listdir()
    for path in files_and_dirs:
        if ".txt" in path:
            os.remove(path)


@pytest.fixture
def clear_folder_of_txt_files():
    clear_files()
    try:
        yield
    finally:
        clear_files()
