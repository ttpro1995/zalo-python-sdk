import json
import time

from zalo.sdk import APIConfig

from zalo.sdk.ZaloBaseClient import ZaloBaseClient
from zalo.sdk.utils.MacUtils import MacUtils


class ZaloOaOnbehalf(ZaloBaseClient):
    def __init__(self, app_info):
        self.app_info = app_info

    def get_login_url(self):
        login_endpoint = "https://oauth.zaloapp.com/page/login?app_id=%s&redirect_uri=%s" % (
            self.app_info.app_id, self.app_info.callback_url)
        return login_endpoint

    def get(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        timestamp = int(round(time.time() * 1000))

        params = {
            'appid': self.app_info.app_id,
            'data': json.dumps(data),
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.app_info.app_id, json.dumps(data), timestamp, self.app_info.secret_key)
        }
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        timestamp = int(round(time.time() * 1000))
        params = {
            'appid': self.app_info.app_id,
            'data': json.dumps(data),
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.app_info.app_id, json.dumps(data), timestamp, self.app_info.secret_key)
        }

        if 'file' in data:
            file = self.load_file(data['file'])
            data.pop('file', None)
            return self.upload_file(endpoint, params, file)
        else:
            return self.send_request(endpoint, params, 'POST')