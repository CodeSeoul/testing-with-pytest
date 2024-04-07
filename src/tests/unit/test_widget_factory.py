import random
from typing import Callable
import requests

import pytest

from src.tests.fakes import (
    FakeApiCaller,
    call_api_return_something,
    call_api_return_something_else,
    return_1717,
    return_1335,
)
from src.utils.external_api_caller import ExternalApiCaller, AbstractApiCaller
from src.widget.widget import Widget
from src.widget.widget_factory import WidgetFactory


def test_widget_factory_poorly():  # poor unit test, should be an integration test
    # class MockResponse:
    #     def json(self):
    #         return [{"text": "cats are fluffy"}]
    #
    # def mock_get(*args, **kwargs):
    #     return MockResponse()
    #
    # monkeypatch.setattr(requests, "get", mock_get)

    # set up
    factory = WidgetFactory(api_caller=ExternalApiCaller())

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.cat_fact) > 0
    assert widget.fizzbuzz > 9


def test_widget_factory_no_randomness(monkeypatch):
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
    assert len(widget.cat_fact) > 0
    assert widget.fizzbuzz == 999


def test_widget_factory_no_randomness_no_api_call(monkeypatch):
    # set up
    def mock_randint(*args, **kwargs):
        return 999

    monkeypatch.setattr(random, "randint", mock_randint)

    def mock_api_call(self):
        return {"text": "cats puke hairballs"}

    monkeypatch.setattr(ExternalApiCaller, "call_api", mock_api_call)

    factory = WidgetFactory(api_caller=ExternalApiCaller())

    # run code
    widget = factory.produce_widget()

    # verify
    assert isinstance(widget, Widget)
    assert widget.foobar is False
    assert len(widget.cat_fact) > 0
    assert widget.cat_fact == "cats puke hairballs"
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
    assert len(widget.cat_fact) > 0
    assert widget.cat_fact == "cool cat fact"
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
    assert len(widget.cat_fact) > 0
    assert widget.cat_fact == "cool cat fact"
    assert widget.fizzbuzz == 999


@pytest.mark.parametrize(
    "mock_call_api, expected_cat_fact",
    [
        (call_api_return_something, "cats have 9 lives"),
        (call_api_return_something_else, "cats are liquid"),
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
    expected_cat_fact: str,  # set up
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
    assert len(widget.cat_fact) > 0
    assert widget.cat_fact == expected_cat_fact
    assert widget.fizzbuzz == expected_int
