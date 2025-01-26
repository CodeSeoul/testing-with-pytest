from src.utils.external_api_caller import AbstractApiCaller


# this mimics the function of the api that we
# are actually calling by finding the holiday by year and country
# obviously, this is not now the actual api works but it is a suitable and simplified replacement
class FakeApiCaller(AbstractApiCaller):
    _holidays = {
        (2024, "KR"): {"name": "christmas"},
        (2024, "JP"): {"name": "christmas"},
        (2024, "TW"): {"name": "christmas"},
    }

    def call_api(self, year: int, country_code: str) -> dict:
        return self._holidays[(year, country_code)]


def call_api_return_something(self, year: int, country_code: str) -> dict:
    return {"name": "new years"}


def call_api_return_something_else(self, year: int, country_code: str) -> dict:
    return {"name": "lunar new year"}


def return_1717(*args, **kwargs) -> int:
    return 1717


def return_1335(*args, **kwargs) -> int:
    return 1335
