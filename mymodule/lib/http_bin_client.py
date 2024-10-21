from __future__ import annotations

import os
from typing import Any, Callable, NoReturn

import requests
from requests import Response


def handle_request_exceptions(func: Callable[..., Response]) -> Callable[..., Response]:
    def wrapper(*args: Any, **kwargs: Any) -> Response | NoReturn:
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise
        else:
            return response

    return wrapper


class HttpBinClient(object):
    SPLUNK_HOSTNAME: str | None = os.getenv("SPLUNK_HOSTNAME")
    SPLUNK_PORT: int | None = os.getenv("SPLUNK_PORT")
    BASE_URL = f"https://{SPLUNK_HOSTNAME}:{SPLUNK_PORT}"

    def __init__(self) -> None:
        self.session = requests.Session()

    def _make_request(self, endpoint: str) -> Response:
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        return self.session.get(url)

    @handle_request_exceptions
    def get_ip(self) -> Response:
        return self._make_request("/services/search/jobs/export")
