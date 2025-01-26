import random
from typing import Callable

import pytest
from pytest import MonkeyPatch

from src.tests.fakes import (
    FakeApiCaller,
    call_api_return_something,
    call_api_return_something_else,
    return_1335,
    return_1717,
)
from src.utils.external_api_caller import AbstractApiCaller, ExternalApiCaller
from src.widget.widget import Widget
from src.widget.widget_factory import WidgetFactory

# in tests when we have a depdency, we can test it using 3 different methods


# you can also just use the code on its own but this is a poor way to test
def test_widget_factory_poorly():
    # set up
    factory = WidgetFactory(api_caller=ExternalApiCaller())

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.fizzbuzz > 9


# method 1 is stubbing.
# A stub is a replacement for a real method or function that provides predefined outputs
# here, we are stubbing the random int generation from the random library
# by using the monkeypatch class that pytest provides
def test_widget_factory_no_randomness(monkeypatch: MonkeyPatch):
    # set up
    def mock_randint(*args, **kwargs):
        return 999

    monkeypatch.setattr(random, "randint", mock_randint)

    factory = WidgetFactory(api_caller=ExternalApiCaller())

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.fizzbuzz == 999


# a further demonstration of stubbing where we stub the api call as well
def test_widget_factory_no_randomness_no_api_call(monkeypatch):
    # set up
    def mock_randint(*args, **kwargs):
        return 999

    monkeypatch.setattr(random, "randint", mock_randint)

    def mock_api_call(self, *args, **kwargs):
        return {"name": "christmas"}

    monkeypatch.setattr(ExternalApiCaller, "call_api", mock_api_call)

    factory = WidgetFactory(api_caller=ExternalApiCaller())

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.random_holiday_name == "christmas"
    assert widget.fizzbuzz == 999


def test_widget_factory_no_randomness_fake_api_caller(
    monkeypatch,
    fake_api_caller: AbstractApiCaller,  # set up
):
    # set up
    def mock_randint(*args, **kwargs):
        return 999

    monkeypatch.setattr(random, "randint", mock_randint)

    factory = WidgetFactory(api_caller=fake_api_caller)

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.random_holiday_name == "christmas"
    assert widget.fizzbuzz == 999


def test_widget_factory_fixtures_can_use_other_fixtures_and_more_conftests(
    widget_factory: WidgetFactory,  # set up
    monkeypatch_randint,  # set up
):
    # run code
    widget = widget_factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.random_holiday_name == "christmas"
    assert widget.fizzbuzz == 999


@pytest.mark.parametrize(
    "mock_call_api, expected_holiday_name",
    [
        (call_api_return_something, "new years"),
        (call_api_return_something_else, "lunar new year"),
    ],
)
@pytest.mark.parametrize(
    "mock_generate_randint, expected_int",
    [
        (return_1717, 1717),
        (return_1335, 1335),
    ],
)  # set up
def test_widget_factory_parameterize_functions(
    widget_factory: WidgetFactory,  # set up
    monkeypatch,  # set up
    mock_call_api: Callable,  # set up
    expected_holiday_name: str,  # set up
    mock_generate_randint: Callable,  # set up
    expected_int: int,  # set up
):
    # set up
    monkeypatch.setattr(FakeApiCaller, "call_api", mock_call_api)
    monkeypatch.setattr(random, "randint", mock_generate_randint)

    # run code
    widget = widget_factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.random_holiday_name) > 0
    assert widget.random_holiday_name == expected_holiday_name
    assert widget.fizzbuzz == expected_int
