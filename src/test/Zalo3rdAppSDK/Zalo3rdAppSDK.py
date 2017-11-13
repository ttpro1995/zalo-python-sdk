import requests

from src.main.com.vng.zalo.sdk.app.Zalo3rdAppClient import Zalo3rdAppClient
from src.main.com.vng.zalo.sdk.app.ZaloAppInfo import ZaloAppInfo

zalo_info = ZaloAppInfo(app_id=2030223146967622095, secret_key="4B2qNrCXRmo16nPbAGM8")

# zalo_info = {
#     'app_id': 2030223146967622095,
#     'secret_key': "4B2qNrCXRmo16nPbAGM8",
#     'call_back_url': "http://dev1.demo-zc.zapps.vn/login/callback"
# }

zalo_3rd_app_client = Zalo3rdAppClient(zalo_info)
code = "mow9KvCvxWxQ1RKDnpteAP0Ic2Q14kjSqXFNIlGsrmoS5Q9Wu2o9JS4Nwnwh29iOlm3G5SuxqrBKAjKMjGsWSCumwqZcFjyujIYkAA0fsalyDzq9xbdBQg46uqw4P-GOWroUJFnJZqFfMUbRu1onMRy5fsA6UPL4wcw6I_G_v1kGEDzJZZoeCDKblW6QPECPvKIKTfbf_KY0H-z5hGN05F4RnaMQAj1yiJZYA-LghNMXHy51EIoGVqODsK4-PmHRLLSoBLuaH0qjSoS1H2eIRqfnR48z6GmiI6WTGcPyUH4O01P0AZFVGEq7loG"
access_token = zalo_3rd_app_client.get_access_token(code)
token = access_token['access_token']
expires_in = access_token['expires_in']
print(token)
print(expires_in)

# profile = zalo_3rd_app_client.get_profile(token, "id, name, birthdadsady, gender, pictudsadasre")
# print(profile)
#
friends = zalo_3rd_app_client.get_friends(token, 0, 10, "id,name,picture.type(large),gender,birthday")
print(friends)
#
# invitable_friends = zalo_3rd_app_client.get_invitable_friends(token, 0, 10, "id,name,picture.type(large),gender,birthday")
# print(invitable_friends)
#
# post_feed = zalo_3rd_app_client.post_feed(token, message="good morning", link="https://developers.zalo.me/docs/api/social-api/tai-lieu/dang-bai-viet-post-39")
# print(post_feed)

# send_app_request = zalo_3rd_app_client.send_app_request(token, "3242353675205151122", "testing")
# print(send_app_request)

send_message = zalo_3rd_app_client.send_message(token, 8063947237857451397, "Hi man !!!", "https://developers.zalo.me/docs/api/social-api/tai-lieu/dang-bai-viet-post-39")
print(send_message)