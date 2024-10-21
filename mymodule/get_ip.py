#!/usrr/bin/env python

from lib.http_bin_client import HttpBinClient
from requests import Response


def get_ip() -> Response:
    client = HttpBinClient()
    response = client.get_ip()
    return response


if __name__ == "__main__":
    response = get_ip()
    print(response.json())
