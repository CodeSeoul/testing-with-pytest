import random

import pytest

from src.tests.fakes import FakeApiCaller
from src.utils.external_api_caller import AbstractApiCaller
from src.widget.widget import Widget
from src.widget.widget_factory import WidgetFactory


@pytest.fixture
def fake_api_caller() -> AbstractApiCaller:
    return FakeApiCaller()


@pytest.fixture
def widget_factory(fake_api_caller: AbstractApiCaller) -> WidgetFactory:
    return WidgetFactory(api_caller=fake_api_caller)


@pytest.fixture
def monkeypatch_randint(monkeypatch):
    def mock_randint(*args, **kwargs):
        return 999

    monkeypatch.setattr(random, "randint", mock_randint)


@pytest.fixture
def widgets() -> list[Widget]:
    return [
        Widget(
            fizzbuzz=1,
            cat_fact="fact1",
            foobar=True,
        ),
        Widget(
            fizzbuzz=2,
            cat_fact="fact2",
            foobar=False,
        ),
        Widget(
            fizzbuzz=3,
            cat_fact="fact3",
            foobar=True,
        ),
    ]
