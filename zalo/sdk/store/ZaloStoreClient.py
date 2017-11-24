import json
import time

from zalo.sdk import APIConfig

from zalo.sdk.ZaloBaseClient import ZaloBaseClient
from zalo.sdk.utils.MacUtils import MacUtils


class ZaloStoreClient(ZaloBaseClient):
    def __init__(self, oa_info):
        self.oa_info = oa_info

    def post(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        if 'file' in data:
            print data['file']
            file = self.load_file(data['file'])
            timestamp = int(round(time.time() * 1000))
            params = {
                'oaid': self.oa_info.oa_id,
                'timestamp': timestamp,
                'mac': MacUtils.build_mac(self.oa_info.oa_id, timestamp, self.oa_info.secret_key)
            }
            return self.upload_file(endpoint, params, file)
        params = self.create_oa_params(data, self.oa_info)
        return self.send_request(endpoint, params, 'POST')

    def get(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_oa_params(data, self.oa_info)
        return self.send_request(endpoint, params, 'GET')