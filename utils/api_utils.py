import json
import requests
import curlify

from logger.logger import Logger
from requests import Session


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)
        Logger.info(f"Request: {curlify.to_curl(response.request)}")
        Logger.debug(f"Request kwargs: {kwargs}")

        try:
            body = json.dumps(response.json(), indent=2)
        except ValueError:
            body = response.text

        Logger.info(
            f"Response status code={response.status_code}, "
            f"elapsed_time={response.elapsed},\n{body}\n"
        )

        return response

    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        self.session = Session()
        self.session.headers.update(headers or {})
        self.url = url

    @log_response
    def get(self, url_endpoint, **kwargs):
        return self.session.get(self.url + url_endpoint, **kwargs)

    @log_response
    def post(self, url_endpoint, **kwargs):
        return self.session.post(
            self.url + url_endpoint,
            **kwargs
        )
