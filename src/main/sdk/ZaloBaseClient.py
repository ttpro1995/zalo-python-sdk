import requests
from src.main.sdk import APIConfig
from src.main.sdk.APIException import APIException


class ZaloBaseClient():
    def send_request(self, endpoint, params, method):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            **APIConfig.DEFAULT_HEADER
        }

        if method == 'GET':
            response = requests.get(url=endpoint, params=params, headers=headers)
        elif method == 'POST':
            response = requests.post(url=endpoint, data=params, headers=headers)
        else:
            raise APIException("method is not supported")
        if response.status_code != 200:
            raise APIException(response.text, response.status_code, method)
        return response.json()

    def upload_file(self, endpoint, params, file):
        response = requests.post(endpoint, files={'file': file}, data=params, headers=APIConfig.DEFAULT_HEADER)
        if response.status_code != 200:
            raise APIException(response.text, response.status_code)
        return response.json()