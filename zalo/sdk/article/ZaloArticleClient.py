import json
import time

import requests

from zalo.sdk import APIConfig
from zalo.sdk.APIException import APIException

from zalo.sdk.ZaloBaseClient import ZaloBaseClient
from zalo.sdk.utils.MacUtils import MacUtils


class ZaloArticleClient(ZaloBaseClient):
    def __init__(self, oa_info):
        self.oa_info = oa_info

    def get(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        timestamp = int(round(time.time() * 1000))
        params = {
            'oaid': self.oa_info.oa_id,
            'data': json.dumps(data),
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, json.dumps(data), timestamp, self.oa_info.secret_key)
        }
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        timestamp = int(round(time.time() * 1000))
        mac_content = ''
        for key,value in data.items():
            data[key] = json.dumps(value)
            mac_content = data[key]
        params = {
            'oaid': self.oa_info.oa_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, mac_content, timestamp, self.oa_info.secret_key)
        }
        params.update(data)
        return self.send_request(endpoint, params, 'POST')

    def upload_video(self, endpoint, params):
        file = open(params['file'], 'rb').read()
        params.pop('file', None)
        print params
        response = self.upload_file(endpoint, params, file)
        return response
