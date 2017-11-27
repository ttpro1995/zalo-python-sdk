import json

import requests
import time

from zalo.sdk import APIConfig
from zalo.sdk.APIException import APIException
from zalo.sdk.utils.MacUtils import MacUtils


class ZaloBaseClient():
    def send_request(self, endpoint, params, method):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
        }
        headers.update(APIConfig.DEFAULT_HEADER)

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

    def load_file(self, path):
        if 'http' in path:
            file = requests.get(path, stream=True).content
        else:
            file = open(path, 'rb').read()
        if len(file) > APIConfig.MAXIMUM_FILE_SIZE:
            raise APIException("file size exceeded the maximum size permitted")
        return file

    def create_oa_params(self, data, oa_info):
        timestamp = int(round(time.time() * 1000))

        mac_content = ''
        for key, value in data.items():
            if type(value) is dict:
                data[key] = json.dumps(value)
            mac_content = data[key]

        params = {
            'oaid': oa_info.oa_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(oa_info.oa_id, mac_content, timestamp, oa_info.secret_key)
        }

        params.update(data)
        return params

    def create_on_behalf_params(self, data, app_info):
        timestamp = int(round(time.time() * 1000))

        mac_content = ''
        for key, value in data.items():
            if type(value) is dict:
                data[key] = json.dumps(value)
            mac_content = data[key]

        params = {
            'appid': app_info.app_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(app_info.app_id, mac_content, timestamp, app_info.secret_key)
        }

        params.update(data)
        return params