import random

from src.utils.external_api_caller import AbstractApiCaller, ExternalApiCaller
from src.widget.widget import Widget


class WidgetFactory:
    def __init__(self, api_caller: AbstractApiCaller = ExternalApiCaller()):
        self.api_caller = api_caller

    def produce_widget(self, year: int = 2024, country_code: str = "KR") -> Widget:
        holida_name = self.api_caller.call_api(year=year, country_code=country_code)["name"]
        return Widget(
            fizzbuzz=random.randint(10, 99999),
            random_holiday_name=holida_name,
            foobar=False,
        )
