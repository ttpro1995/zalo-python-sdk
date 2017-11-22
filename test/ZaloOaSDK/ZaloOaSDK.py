# coding=utf-8
from zalo.sdk.app.ZaloAppInfo import ZaloAppInfo
from zalo.sdk.oa.ZaloOaClient import ZaloOaClient
from zalo.sdk.oa.ZaloOaInfo import ZaloOaInfo
from zalo.sdk.oa.ZaloOaOnbehalf import ZaloOaOnbehalf

zalo_info = ZaloOaInfo(oa_id="579745863508352884", secret_key="pIJESQgIZtK4N1noHd8t")
zalo_oa_client = ZaloOaClient(zalo_info)

user_id = 3321115882543943283
profile = zalo_oa_client.get('/getprofile', {'uid': user_id})
print(profile)

message_status = zalo_oa_client.get('/getmessagestatus', {'msgid': 'a2c40ba0e3e3b4bdedf2'})
print(message_status)
#
# send_text_message = zalo_oa_client.post('/sendmessage/text', {'uid': "3321115882543943283", 'message': 'hello there'})
# print(send_text_message)
#
# phone = 841216861997
# template_id = "2c5599bda5f84ca615e9"
# data = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# send_message_customer_care_by_phone = zalo_oa_client.post('/sendmessage/phone/cs', {
#     'phone': phone,
#     'templateid': template_id,
#     'templatedata': data
# })
# print(send_message_customer_care_by_phone)
#
# template_id = "2c5599bda5f84ca615e9"
# data = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# send_message_customer_care_by_user_id = zalo_oa_client.post('/sendmessage/cs', {
#     'uid': user_id,
#     'templateid': template_id,
#     'templatedata': data
# })
# print(send_message_customer_care_by_user_id)
#
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
# send_action_message = zalo_oa_client.post('/sendmessage/actionlist', {
#     'uid': user_id,
#     'actionlist': action_list
# })
# print(send_action_message)
#
# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# send_link_message = zalo_oa_client.post('/sendmessage/links', {
#     'uid': user_id,
#     'links': links
# })
# print(send_link_message)
#
path = "/home/cpu10142-local/Downloads/revanon2.jpg"
upload_photo_from_path = zalo_oa_client.post('/upload/image', {'file': path})
print(upload_photo_from_path)
#
# image_id = 'c97c30e8f4951dcb4484'
# send_image_message = zalo_oa_client.post('/sendmessage/image', {'uid': user_id, 'imageid': image_id, 'message': 'team secret'})
# print(send_image_message)

# path = "/home/cpu10142-local/Downloads/source1.gif"
# upload_gif = zalo_oa_client.post('/upload/gif', {'file': path})
# print(upload_gif)

# image_id_gif = 'J434FMnDtKaa6Wx9ttS2XNgdSiLQSXjCgsMJiWn9kgo='
# send_gif_message = zalo_oa_client.post('/sendmessage/gif', {
#     'uid': user_id,
#     'width': 10,
#     'height': 20,
#     'imageid': image_id_gif
# })
# print(send_gif_message)
#
# upload_photo_from_url = zalo_oa_client.post('/upload/image', {'file': 'http://wiki.teamliid.net/images/1/1a/EG.png'})
# print(upload_photo_from_url)

# zalo_info = ZaloAppInfo(app_id=1131677296116040198, secret_key="rbZ5wQ2tVUh7Y3y6Kxqe")
# zalo_info.callback_url = 'https://smilesplz91.000webhostapp.com/'
# zalo_oa_on_behalf = ZaloOaOnbehalf(zalo_info)
#
# print zalo_oa_on_behalf.get_login_url()
#
# access_token = 'SUhRlZ1x4o1Lsf7D3HmxCdYfeen47mWy0wYEr58BFJmXgUBXL31c3Wtsz-L1UcHaRTloq2PeTaj2t_EdDdih2rVBYTG8EGeFDOoXYna8C2kzdj-Z_pbVSQN05Ep5KAOJ--PIxyD_gqQRec3bi0gSPRk4JEYwHuSm_eKGkbvP9iD4PXOnHLjY'
#
# on_behalf_profile = zalo_oa_on_behalf.get('/onbehalf/getprofile', {
#     'uid': user_id,
#     'accessTok': access_token
# })
# print on_behalf_profile
#
# on_behalf_oa = zalo_oa_on_behalf.get('/onbehalf/getoa', {
#     'accessTok': access_token
# })
# print on_behalf_oa
#
# on_behalf_conversation = zalo_oa_on_behalf.get('/onbehalf/conversation', {
#     'offset':0,
#     'count': 1,
#     'uid': user_id,
#     'accessTok': access_token
# })
# print on_behalf_conversation
#
# on_behalf_listrecentchat = zalo_oa_on_behalf.get('/onbehalf/listrecentchat', {
#     'offset':0,
#     'count': 1,
#     'accessTok': access_token
# })
# print on_behalf_listrecentchat
#
# path_to_image = '/home/cpu10142-local/Downloads/revanon2.jpg'
# on_behalf_uplpad_image= zalo_oa_on_behalf.post('/onbehalf/upload/image', {'file': path_to_image, 'accessTok': access_token})
# print on_behalf_uplpad_image
#
# path_to_gif = '/home/cpu10142-local/Downloads/source1.gif'
# on_behalf_upload_gif = zalo_oa_on_behalf.post('/onbehalf/upload/gif', {'file': path_to_gif, 'accessTok': access_token})
# print on_behalf_upload_gif
#
# on_behalf_send_text_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/text', {
#     'uid': user_id,
#     'message': 'test',
#     'accessTok': access_token
# })
#
# print on_behalf_send_text_message
#
# image_id = 'cf7ae802e87e0120586f'
# on_behalf_send_image_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/image', {
#     'uid': user_id,
#     'imageid': image_id,
#     'message': 'Your image',
#     'accessTok': access_token
# })
# print on_behalf_send_image_message
#
# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# send_link_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/links', {
#     'uid': user_id,
#     'links': links,
#     'accessTok': access_token
# })
# print(send_link_message)
#
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
# on_behalf_send_action_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/actionlist', {
#     'uid': user_id,
#     'accessTok': access_token,
#     'actionlist': action_list
# })
# print(on_behalf_send_action_message)
#
# gif_id = 'ot3olFyriQpzA+mN7tMBZJz5C23AqUtjv/bJSmu0Eh0='
# on_behalf_send_gif_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/gif', {
#     'uid': user_id,
#     'imageid': gif_id,
#     'width': 20,
#     'height': 30,
#     'accessTok': access_token
# })
# print on_behalf_send_gif_message