import abc


class AbstractFileHandler(abc.ABC):
    @abc.abstractmethod
    def write_to_file(self, filename: str, lines: list[str]):
        raise NotImplementedError()


class FileHandler(AbstractFileHandler):
    def write_to_file(self, filename: str, lines: list[str]):
        with open(filename, "a+") as f:
            for line in lines:
                f.write(line)
