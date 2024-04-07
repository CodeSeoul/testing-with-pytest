from src.utils.external_api_caller import AbstractApiCaller


class FakeApiCaller(AbstractApiCaller):
    def call_api(self) -> dict:
        return {"text": "cool cat fact"}


def call_api_return_something(self) -> dict:
    return {"text": "cats have 9 lives"}


def call_api_return_something_else(self) -> dict:
    return {"text": "cats are liquid"}


def return_1717(*args, **kwargs) -> int:
    return 1717


def return_1335(*args, **kwargs) -> int:
    return 1335
