import requests
from requests import Response


class AllRequests:

    @staticmethod
    def get(url: str = None, data: dict=None, headers=None, cookies=None):
        return AllRequests._send_request(url=url, data=data, headers=headers, cookies=cookies, request_method='GET')
    
    @staticmethod
    def _send_request(url: str, data: dict, headers: dict, cookies: dict, request_method: str) -> Response:

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if request_method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif request_method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif request_method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif request_method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad method {request_method}. Type: 'GET'/'POST'/'PUT or 'DELETE'.")
        return response
