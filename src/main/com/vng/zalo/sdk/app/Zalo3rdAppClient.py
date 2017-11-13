import requests

from src.main.com.vng.zalo.sdk.APIConfig import APIConfig


class Zalo3rdAppClient:
    def __init__(self, app_info):
        self.app_info = app_info

    def get_login_url(self):
        login_endpoint = "https://oauth.zaloapp.com/v3/auth?app_id=%s&redirect_uri=%s" % (
            self.app_info.app_id, self.app_info.secret_key)
        return login_endpoint

    def get_access_token(self, oauth_code):
        accesstoken_endpoint = "https://oauth.zaloapp.com/v3/access_token";
        params = {
            'app_id': self.app_info.app_id,
            'app_secret': self.app_info.secret_key,
            'code': oauth_code
        }
        response = requests.get(url=accesstoken_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def get_profile(self, access_token, fields):
        get_profile_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/me"
        params = {
            'access_token': access_token,
            'fields': fields
        }
        response = requests.get(url=get_profile_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def get_friends(self, access_token, offset, limit, fields):
        get_friends_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/me/friends"
        params = {
            'access_token': access_token,
            'offset': offset,
            'limit': limit,
            'fields': fields
        }
        response = requests.get(url=get_friends_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def get_invitable_friends(self, access_token, offset, limit, fields):
        get_invitable_friends_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/me/invitable_friends"
        params = {
            'access_token': access_token,
            'offset': offset,
            'limit': limit,
            'fields': fields
        }
        response = requests.get(url=get_invitable_friends_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def post_feed(self, access_token, message, link):
        post_feed_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/me/feed"
        params = {
            'access_token': access_token,
            'message': message,
            'link': link
        }
        response = requests.post(url=post_feed_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def send_app_request(self, access_token, to_user_ids, message):
        send_app_request_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/apprequests"
        params = {
            'access_token': access_token,
            'to': ','.join(map(str, to_user_ids)),
            'message': message
        }
        print(params)
        response = requests.post(url=send_app_request_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def send_message(self, access_token, to_user_id, message, link):
        send_message_endpoint = "https://graph.zalo.me/" + APIConfig.DEFAULT_3RDAPP_API_VERSION + "/me/message"
        params = {
            'access_token': access_token,
            'to': to_user_id,
            'message': message,
            'link': link
        }
        response = requests.post(url=send_message_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()