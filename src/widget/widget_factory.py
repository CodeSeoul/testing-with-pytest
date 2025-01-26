import random

from src.utils.external_api_caller import AbstractApiCaller
from src.widget.widget import Widget


class WidgetFactory:
    def __init__(self, api_caller: AbstractApiCaller):
        self.api_caller = api_caller

    def produce_widget(self) -> Widget:
        cat_fact = self.api_caller.call_api(2024, "KR")["name"]
        return Widget(
            fizzbuzz=random.randint(10, 99999),
            random_holiday_name=cat_fact,
            foobar=False,
        )
