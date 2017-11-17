import requests

from src.main.sdk import APIConfig
from src.main.sdk.ZaloBaseClient import ZaloBaseClient


class Zalo3rdAppClient(ZaloBaseClient):
    def __init__(self, app_info):
        self.app_info = app_info

    def get_login_url(self):
        login_endpoint = "https://oauth.zaloapp.com/v3/auth?app_id=%s&redirect_uri=%s" % (
            self.app_info.app_id, self.app_info.secret_key)
        return login_endpoint

    def get_access_token(self, oauth_code):
        accesstoken_endpoint = "https://oauth.zaloapp.com/v3/access_token"
        params = {
            'app_id': self.app_info.app_id,
            'app_secret': self.app_info.secret_key,
            'code': oauth_code
        }
        response = requests.get(url=accesstoken_endpoint, params=params, headers=APIConfig.DEFAULT_HEADER)
        return response.json()

    def get(self, url, access_token, params):
        endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + url
        params['access_token'] = access_token
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, access_token, params):
        endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + url
        params['access_token'] = access_token
        return self.send_request(endpoint, params, 'POST')