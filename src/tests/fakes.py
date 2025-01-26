from src.utils.external_api_caller import AbstractApiCaller


class FakeApiCaller(AbstractApiCaller):
    def call_api(self, year: int, country_code: str) -> dict:
        return {"name": "christmas"}


def call_api_return_something(self, year: int, country_code: str) -> dict:
    return {"name": "new years"}


def call_api_return_something_else(self, year: int, country_code: str) -> dict:
    return {"name": "lunar new year"}


def return_1717(*args, **kwargs) -> int:
    return 1717


def return_1335(*args, **kwargs) -> int:
    return 1335
