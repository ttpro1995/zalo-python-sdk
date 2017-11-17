

from src.main.sdk.oa.ZaloOaClient import ZaloOaClient
from src.main.sdk.oa.ZaloOaInfo import ZaloOaInfo

zalo_info = ZaloOaInfo(oa_id="579745863508352884", secret_key="pIJESQgIZtK4N1noHd8t")
zalo_oa_client = ZaloOaClient(zalo_info)

user_id = 3321115882543943283
profile = zalo_oa_client.get('/getprofile', {'uid': user_id})
print(profile)

message_status = zalo_oa_client.get('/getmessagestatus', {'msgid': 'a2c40ba0e3e3b4bdedf2'})
print(message_status)

send_text_message = zalo_oa_client.post('/sendmessage/text', {'uid': "3321115882543943283", 'message': 'hello there'})
print(send_text_message)

phone = 841216861997
template_id = "2c5599bda5f84ca615e9"
data = {
    "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
}
send_message_customer_care_by_phone = zalo_oa_client.post('/sendmessage/phone/cs', {
    'phone': phone,
    'templateid': template_id,
    'templatedata': data
})
print(send_message_customer_care_by_phone)

template_id = "2c5599bda5f84ca615e9"
data = {
    "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
}
send_message_customer_care_by_user_id = zalo_oa_client.post('/sendmessage/cs', {
    'uid': user_id,
    'templateid': template_id,
    'templatedata': data
})
print(send_message_customer_care_by_user_id)

action_list = [{
    'action': 'oa.open.inapp',
    'title': 'Send interactive messages',
    'description': 'This is a test for API send interactive messages',
    'thumb': 'https://developers.zalo.me/web/static/images/bg.jpg',
    'href': 'https://developers.zalo.me',
    'data': 'https://developers.zalo.me',
    'popup': {
        'title': 'Open Website Zalo For Developers',
        'desc': 'Click ok to visit Zalo For Developers and read more Document',
        'ok': 'ok',
        'cancel': 'cancel'
    }
}]
send_action_message = zalo_oa_client.post('/sendmessage/actionlist', {
    'uid': user_id,
    'actionlist': action_list
})
print(send_action_message)

links = [{
    'link': 'https://developers.zalo.me/',
    'linktitle': 'Zalo For Developers',
    'linkdes': 'Document For Developers',
    'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
}]
send_link_message = zalo_oa_client.post('/sendmessage/links', {
    'uid': user_id,
    'links': links
})
print(send_link_message)

path = "/home/cpu10142-local/Downloads/revanon2.jpg"
upload_photo_from_path = zalo_oa_client.post('/upload/image', {'file': path})
print(upload_photo_from_path)

image_id = 'c97c30e8f4951dcb4484'
send_image_message = zalo_oa_client.post('/sendmessage/image', {'uid': user_id, 'imageid': image_id, 'message': 'team secret'})
print(send_image_message)

path = "/home/cpu10142-local/Downloads/source1.gif"
upload_gif = zalo_oa_client.post('/upload/gif', {'file': path})
print(upload_gif)

image_id_gif = 'J434FMnDtKaa6Wx9ttS2XNgdSiLQSXjCgsMJiWn9kgo='
send_gif_message = zalo_oa_client.post('/sendmessage/gif', {
    'uid': user_id,
    'width': 10,
    'height': 20,
    'imageid': image_id_gif
})
print(send_gif_message)

upload_photo_from_url = zalo_oa_client.post('/upload/image', {'file': 'http://wiki.teamliquid.net/commons/images/1/1a/EG.png'})
print(upload_photo_from_url)