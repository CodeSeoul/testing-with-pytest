import os.path


from src.utils.file_handler import FileHandler
from src.widget.widget import Widget
from src.widget.widget_writer import widget_writer


def test_widget_writer(
    widgets: list[Widget],  # set up
):
    filename = "widgets.txt"

    # run code
    widget_writer(filename=filename, widgets=widgets, file_handler=FileHandler())

    # verify
    assert os.path.exists(filename)


def test_widget_writer_terribly():
    filename = "widgets.txt"
    # verify
    assert os.path.exists(filename)


def test_widget_writer_with_setup_teardown(
    widgets: list[Widget],  # set up
    clear_folder_of_txt_files,  # set up and tear down
):
    filename = "widgets.txt"

    # run code
    widget_writer(filename=filename, widgets=widgets, file_handler=FileHandler())

    # verify
    assert os.path.exists(filename)
