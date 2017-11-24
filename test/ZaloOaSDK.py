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
#
# message_status = zalo_oa_client.get('/getmessagestatus', {'msgid': 'a2c40ba0e3e3b4bdedf2'})
# print(message_status)
#
# data = {
#     'uid': "3321115882543943283",
#     'message': 'hello there'
# }
# params = {'data': data}
# send_text_message = zalo_oa_client.post('/sendmessage/text', params)
# print(send_text_message)
#
# phone = 841216861997
# template_id = "2c5599bda5f84ca615e9"
# templatedata = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# data = {
#     'phone': phone,
#     'templateid': template_id,
#     'templatedata': templatedata
# }
# params = {
#     'data': data
# }
# send_message_customer_care_by_phone = zalo_oa_client.post('/sendmessage/phone/cs', params)
# print(send_message_customer_care_by_phone)
#
# template_id = "2c5599bda5f84ca615e9"
# templatedata = {
#     "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
# }
# data = {
#     'uid': user_id,
#     'templateid': template_id,
#     'templatedata': templatedata
# }
# params = {'data': data}
# send_message_customer_care_by_user_id = zalo_oa_client.post('/sendmessage/cs', params)
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
# data = {
#     'uid': user_id,
#     'actionlist': action_list
# }
# params = {
#     'data': data
# }
# send_action_message = zalo_oa_client.post('/sendmessage/actionlist', params)
# print(send_action_message)
#
# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# data = {
#     'uid': user_id,
#     'links': links
# }
# params = {
#     'data': data
# }
# send_link_message = zalo_oa_client.post('/sendmessage/links', params)
# print(send_link_message)
#
# path = "/home/cpu10142-local/Downloads/revanon2.jpg"
# upload_photo_from_path = zalo_oa_client.post('/upload/image', {'file': path})
# print(upload_photo_from_path)
# image_id = 'a644cf30af4c46121f5d'
# data = {
#     'uid': user_id,
#     'imageid': image_id,
#     'message': 'team secret'
# }
# params = {
#     'data': data
# }
# send_image_message = zalo_oa_client.post('/sendmessage/image', params)
# print(send_image_message)
#
# path = "/home/cpu10142-local/Downloads/source1.gif"
# upload_gif = zalo_oa_client.post('/upload/gif', {'file': path})
# print(upload_gif)

# gif_id = 'lvEZTbLh8iVJ6a7vojOmJSQrdY24X2h7EpLqYGLjbJw='
# data = {
#     'uid': user_id,
#     'width': 10,
#     'height': 20,
#     'imageid': gif_id
# }
# params = {
#     'data': data
# }
# send_gif_message = zalo_oa_client.post('/sendmessage/gif', params)
# print(send_gif_message)
#
# upload_photo_from_url = zalo_oa_client.post('/upload/image', {'file': 'http://wiki.teamliquid.net/commons/images/1/1a/EG.png'})
# print(upload_photo_from_url)

# data = {
#     'uid': user_id,
#     'stickerid': 'sticker_id'
# }
# params = {'data': data}
# send_sticker_message = zalo_oa_client.post('/sendmessage/sticker', params)
# print send_sticker_message
#
# data = {
#     'msgid': 'msg_id',
#     'message': 'put_your_message_here'
# }
# params = {'data': data}
# reply_text_message = zalo_oa_client.post('/sendmessage/reply/text', params)
# print reply_text_message
#
# data = {
#     'msgid': 'msg_id',
#     'imageid': 'image_id',
#     'message': 'put_your_message_here'
# }
# params = {'data': data}
# reply_image_message = zalo_oa_client.post('/sendmessage/reply/image', params)
# print reply_image_message
#
# data = {
#     'msgid': 'msg_id',
#     'links': ''
# }
# params = {'data': data}
# reply_link_message = zalo_oa_client.post('/sendmessage/reply/links', params)
# print reply_link_message
#
# data = {
#     'qrdata': 'qrcode',
#     'size': 10
# }
# params = {'data': data}
# qrcode = zalo_oa_client.post('/qrcode', params)
# print qrcode

zalo_info = ZaloAppInfo(app_id=1131677296116040198, secret_key="rbZ5wQ2tVUh7Y3y6Kxqe")
zalo_info.callback_url = 'https://smilesplz91.000webhostapp.com/'
zalo_oa_on_behalf = ZaloOaOnbehalf(zalo_info)

print zalo_oa_on_behalf.get_login_url()

access_token = 'CbMhijRTGWeMPU71wxfg63iMqe2YkLaMG1V-sBIiR1Pa4fIdWOuDRdjKlAANo04u3L_objVnLpWqICRpvF8vVnLwYfVUfGnE0a6EvAFxEaJxiBcGEWWOQgXtyyDj_c0xXa2YbNsX36tnR-6N3A5VKCLGr_fmdKbYy328lsw1Ks1cNKSmr-CAI0'

# data = {
#     'uid': user_id,
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_profile = zalo_oa_on_behalf.get('/onbehalf/getprofile', params)
# print on_behalf_profile
#
# data = {
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_oa = zalo_oa_on_behalf.get('/onbehalf/getoa', params)
# print on_behalf_oa
#
# data = {
#     'offset':0,
#     'count': 1,
#     'uid': user_id,
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_conversation = zalo_oa_on_behalf.get('/onbehalf/conversation', params)
# print on_behalf_conversation
#
# data = {
#     'offset':0,
#     'count': 1,
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_listrecentchat = zalo_oa_on_behalf.get('/onbehalf/listrecentchat', params)
# print on_behalf_listrecentchat
#
# path_to_image = '/home/cpu10142-local/Downloads/revanon2.jpg'
# on_behalf_uplpad_image= zalo_oa_on_behalf.post('/onbehalf/upload/image', {
#     'file': path_to_image,
#     'accessTok': access_token
# })
# print on_behalf_uplpad_image
#
# path_to_gif = '/home/cpu10142-local/Downloads/source1.gif'
# on_behalf_upload_gif = zalo_oa_on_behalf.post('/onbehalf/upload/gif', {
#     'file': path_to_gif,
#     'accessTok': access_token
# })
# print on_behalf_upload_gif
#
# data = {
#     'uid': user_id,
#     'message': 'test',
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_send_text_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/text', params)
# print on_behalf_send_text_message
#
# image_id = 'd5adeda38ddf64813dce'
# data = {
#     'uid': user_id,
#     'imageid': image_id,
#     'message': 'Your image',
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_send_image_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/image', params)
# print on_behalf_send_image_message
#
# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# data = {
#     'uid': user_id,
#     'links': links,
#     'accessTok': access_token
# }
# params = {'data': data}
# send_link_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/links', params)
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
# data = {
#     'uid': user_id,
#     'accessTok': access_token,
#     'actionlist': action_list
# }
# params = {'data': data}
# on_behalf_send_action_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/actionlist', params)
# print(on_behalf_send_action_message)
#
# gif_id = '0d5E/ZSJfblTkacuv43H09bfRxUgXcP5+/TuAd7ZPvw='
# data = {
#     'uid': user_id,
#     'imageid': gif_id,
#     'width': 20,
#     'height': 30,
#     'accessTok': access_token
# }
# params = {'data': data}
# on_behalf_send_gif_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/gif', params)
# print on_behalf_send_gif_message

# message_id = 'c159a5e84961613f3870'
# data = {
#     'msgid': 'c159a5e84961613f3870',
#     'message': 'test message',
#     'accessTok': access_token
# }
# params = {'data': data}
# reply_text_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/text', params)
# print reply_text_message
#
# image_id = 'f650ba7ede02375c6e13'
# data = {
#     'msgid': 'c159a5e84961613f3870',
#     'message': 'test message',
#     'imageid': image_id,
#     'accessTok': access_token
# }
# params = {'data': data}
# reply_image_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/image', params)
# print reply_image_message
#
# links = [{
#     'link': 'https://developers.zalo.me/',
#     'linktitle': 'Zalo For Developers',
#     'linkdes': 'Document For Developers',
#     'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
# }]
# data = {
#     'msgid': message_id,
#     'links': links,
#     'accessTok': access_token
# }
# params = {'data': data}
# reply_link_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/links', params)
# print reply_link_message