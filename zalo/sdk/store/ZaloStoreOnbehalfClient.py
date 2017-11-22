import json
import time

from zalo.sdk import APIConfig

from zalo.sdk.ZaloBaseClient import ZaloBaseClient
from zalo.sdk.utils.MacUtils import MacUtils


class ZaloStoreOnbehalfClient(ZaloBaseClient):
    def __init__(self, app_info):
        self.app_info = app_info

    def get(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_params(data)
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        print endpoint
        if 'file' in data:
            print data['file']
            file = self.load_file(data['file'])
            timestamp = int(round(time.time() * 1000))
            params = {
                'appid': self.app_info.app_id,
                'data': data['accessTok'],
                'timestamp': timestamp,
                'mac': MacUtils.build_mac(self.app_info.app_id, data, timestamp, self.app_info.secret_key)
            }

            return self.upload_file(endpoint, params, file)
        params = self.create_params(data)
        return self.send_request(endpoint, params, 'POST')

    def create_params(self, data):
        timestamp = int(round(time.time() * 1000))

        mac_content = ''
        for key, value in data.items():
            if type(value) is dict:
                data[key] = json.dumps(value)
            mac_content = data[key]

        params = {
            'appid': self.app_info.app_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.app_info.app_id, mac_content, timestamp, self.app_info.secret_key)
        }

        params.update(data)
        print params
        return params