from src.utils.file_handler import AbstractFileHandler, FileHandler
from src.widget.widget import Widget


def widget_writer_highly_coupled(widgets: list[Widget]):
    file_handler = FileHandler()
    lines: list[str] = [f"{widget.fizzbuzz}|{widget.cat_fact}|{widget.foobar}\n" for widget in widgets]
    file_handler.write_to_file(filename="widgets.txt", lines=lines)


def widget_writer(
    filename: str,
    widgets: list[Widget],
    file_handler: AbstractFileHandler,
):
    lines: list[str] = [f"{widget.fizzbuzz}|{widget.cat_fact}|{widget.foobar}\n" for widget in widgets]

    file_handler.write_to_file(filename=filename, lines=lines)
