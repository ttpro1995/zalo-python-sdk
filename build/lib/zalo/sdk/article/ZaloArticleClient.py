from zalo.sdk import APIConfig

from zalo.sdk.ZaloBaseClient import ZaloBaseClient


class ZaloArticleClient(ZaloBaseClient):
    def __init__(self, oa_info):
        self.oa_info = oa_info

    def get(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_oa_params(data, self.oa_info)
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, data):
        endpoint = "%s/%s/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_oa_params(data, self.oa_info)
        return self.send_request(endpoint, params, 'POST')

    def upload_video(self, endpoint, params):
        file = open(params.pop('file', None), 'rb')
        response = self.upload_file(endpoint, params, file)
        return response

