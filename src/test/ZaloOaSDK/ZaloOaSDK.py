from src.main.com.vng.zalo.sdk.oa.ZaloOaClient import ZaloOaClient
from src.main.com.vng.zalo.sdk.oa.ZaloOaInfo import ZaloOaInfo

zalo_info = ZaloOaInfo(oa_id=579745863508352884, secret_key="pIJESQgIZtK4N1noHd8t")
zalo_oa_client = ZaloOaClient(zalo_info)

user_id = 3321115882543943283
# profile = zalo_oa_client.get_profile(user_id)
# print(profile)
#
# message_status = zalo_oa_client.get_message_status("79454f5f9a65cc3b9574")
# print(message_status)

# send_text_message = zalo_oa_client.send_text_message(3321115882543943283, "Hello there")
# print(send_text_message)

# phone = 841216861997
# template_id = "2c5599bda5f84ca615e9"
# data = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# send_message_customer_care_by_phone = zalo_oa_client.send_message_customer_care_by_phone(phone, template_id, data)
# print(send_message_customer_care_by_phone)

# template_id = "2c5599bda5f84ca615e9"
# data = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# send_message_customer_care_by_user_id = zalo_oa_client.send_message_customer_care_by_user_id(user_id, template_id, data)
# print(send_message_customer_care_by_user_id)

# action_list = [{
#     'action': 'oa.open.inapp',
#     'title': 'Send interactive messages',
#     'description': 'This is a test for API send interactive messages',
#     'thumb': 'https://developers.zalo.me/web/static/images/bg.jpg',
#     'href': 'https://developers.zalo.me',
#     'data': 'https://developers.zalo.me',
#     'popup': {
#         'title': 'Open Website Zalo For Developers',
#         'desc': 'Click ok to visit Zalo For Developers and read more Document',
#         'ok': 'ok',
#         'cancel': 'cancel'
#     }
# }]
# send_action_message = zalo_oa_client.send_action_message(user_id, action_list)
# print(send_action_message)

# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# send_link_message = zalo_oa_client.send_link_message(user_id, links)
# print(send_link_message)

path = "/home/cpu10142-local/Downloads/revanon2.jpg"
upload_photo_from_path = zalo_oa_client.upload_photo_from_absolute_path(path)
print(upload_photo_from_path)