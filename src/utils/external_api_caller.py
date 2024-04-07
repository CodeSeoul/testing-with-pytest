import abc

import requests


class AbstractApiCaller(abc.ABC):
    @abc.abstractmethod
    def call_api(self) -> dict:
        raise NotImplementedError()


class ExternalApiCaller(AbstractApiCaller):
    def __init__(self, url: str = "https://cat-fact.herokuapp.com"):
        self.url = url

    def call_api(self) -> dict:
        res = requests.get(url=f"{self.url}/facts")
        return res.json()[0]
