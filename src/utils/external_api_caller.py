import abc

import requests


class AbstractApiCaller(abc.ABC):
    @abc.abstractmethod
    def call_api(self, year: int, country_code: str) -> dict:
        raise NotImplementedError()


class ExternalApiCaller(AbstractApiCaller):
    def __init__(self, url: str = "https://date.nager.at/api/v3/publicholidays/:Year/:CountryCode"):
        self.url = url

    def call_api(self, year: int, country_code: str) -> dict:
        url = self.url.replace(":Year", str(year)).replace(":CountryCode", country_code)
        res = requests.get(url=url)
        return res.json()[0]
