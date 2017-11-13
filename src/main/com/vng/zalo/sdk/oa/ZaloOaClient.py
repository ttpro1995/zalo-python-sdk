import json

import os
import requests

from src.main.com.vng.zalo.sdk.APIConfig import APIConfig
import time

from src.main.com.vng.zalo.sdk.utils.MacUtils import MacUtils


class ZaloOaClient:
    def __init__(self, oa_info):
        self.oa_info = oa_info

    def get_profile(self, user_id):
        get_profile_endpoint = "%s/%s/getprofile" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        timestamp = int(round(time.time() * 1000))
        params = {
            'oaid': self.oa_info.oa_id,
            'uid': user_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, user_id, timestamp, self.oa_info.secret_key)
        }
        response = requests.get(get_profile_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def get_message_status(self, msgid):
        get_message_status_endpoint = "%s/%s/getmessagestatus" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        timestamp = int(round(time.time() * 1000))
        params = {
            'oaid': self.oa_info.oa_id,
            'msgid': msgid,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, msgid, timestamp, self.oa_info.secret_key)
        }
        response = requests.get(get_message_status_endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()

    def send_text_message(self, user_id, message):
        send_text_message_endpoint = "%s/%s/sendmessage/text" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        data = {
            'uid': user_id,
            'message': message
        }
        return self.send_message_request(send_text_message_endpoint, json.dumps(data))

    def send_message_customer_care_by_phone(self, phone, template_id, template_data):
        send_message_customer_care_by_phone_endpoint = "%s/%s/sendmessage/phone/cs" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        data = {
            'phone': phone,
            'templateid': template_id,
            'templatedata': template_data
        }
        return self.send_message_request(send_message_customer_care_by_phone_endpoint, json.dumps(data))

    def send_message_customer_care_by_user_id(self, user_id, template_id, template_data):
        send_message_customer_care_by_user_id_endpoint = "%s/%s/sendmessage/cs" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        data = {
            'uid': user_id,
            'templateid': template_id,
            'templatedata': template_data
        }
        return self.send_message_request(send_message_customer_care_by_user_id_endpoint, json.dumps(data))

    def send_action_message(self, user_id, action_list):
        send_action_message_endpoint = "%s/%s/sendmessage/actionlist" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        data = {
            'uid': user_id,
            'actionlist': action_list
        }
        return self.send_message_request(send_action_message_endpoint, json.dumps(data))

    def send_link_message(self, user_id, links):
        send_link_message_endpoint = "%s/%s/sendmessage/links" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        data = {
            'uid': user_id,
            'links': links
        }
        return self.send_message_request(send_link_message_endpoint, json.dumps(data))

    def upload_photo_from_absolute_path(self, path):
        upload_photo_from_absolute_path_endpoint = "%s/%s/upload/image" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION)
        print(os.path.getsize(path))
        file = open(path, 'rb')
        return self.upload_photo(upload_photo_from_absolute_path_endpoint, file)

    def upload_photo(self, endpoint, file):
        timestamp = int(round(time.time() * 1000))
        params = {
            'oaid': self.oa_info.oa_id,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, timestamp, self.oa_info.secret_key)
        }
        print(params)
        response = requests.post(endpoint, data={'file': file}, params=params, headers=APIConfig.create_default_header(), stream=True)
        print(response)
        return response.json()

    def send_message_request(self, endpoint, data):
        timestamp = int(round(time.time() * 1000))
        params = {
            'oaid': self.oa_info.oa_id,
            'data': data,
            'timestamp': timestamp,
            'mac': MacUtils.build_mac(self.oa_info.oa_id, data, timestamp, self.oa_info.secret_key)
        }
        response = requests.post(endpoint, params=params, headers=APIConfig.create_default_header())
        return response.json()
