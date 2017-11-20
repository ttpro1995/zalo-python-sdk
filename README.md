# Zalo SDK for P (v1)

[![N|Solid](https://developers.zalo.me/web/static/prodution/images/logo.png)](https://nodesource.com/products/nsolid)

## Installation
You can easily install this package by using pip
```
pip install zalo-python-s
```

## How to use
**Create an instance of the Zalo class**
```
zalo_info = ZaloAppInfo(app_id=your app id, secret_key="your app secret")
zalo_3rd_app_client = Zalo3rdAppClient(zalo_info)
```

## Social API
**Get Login Url**
```
login_url = zalo_3rd_app_client.get_login_url()
```

**Get AccessToken**
```
code = 'put_your_code_here'
access_token = zalo_3rd_app_client.get_access_token(code)
```

**Get User Information**
```
profile = zalo_3rd_app_client.get('/me', token, {'fields': 'id, name, birthday, gender, picture'})
```

**Get Friends List Used App**
```
friends = zalo_3rd_app_client.get('/me/friends', token, {'offset': 10, 'limit': 50})
```

**Get Friends List UnUse App & Can Send Invite Message**
```
invitable_friends = zalo_3rd_app_client.get('/me/invitable_friends', token, {
    'offset': '0',
    'limit': '10',
    'fields': 'id, name, birthday, gender, picture'
})
```

**Post feed**
```
post_feed = zalo_3rd_app_client.post('/me/feed', token, {
    'message': 'put_your_message_here',
    'link': 'https://developers.zalo.me/'
})
```

**Send Invite To User To Use The App**
```
send_app_request = zalo_3rd_app_client.post('/apprequests', token, {
    'message': 'put_your_message_here',
    'to': 'user '
})
```

**Send A Message To Friends**
```
send_message = zalo_3rd_app_client.post('/me/message', token, {
    'message': 'put_your_message_here',
    'to': 'user id',
    'link': 'https://developers.zalo.me/'
})
```

## Official Account Open API

**Create an instance of the ZaloOA class**
```
zalo_info = ZaloOaInfo(oa_id="put_your_oauth_code_here", secret_key="put_your_secret_key_h")
zalo_oa_client = ZaloOaClient(zalo_info)
```

**Get Profile Follower**
```
profile = zalo_oa_client.get('/getprofile', {'uid': user_id})
```

**Send text message**
```id
send_text_message = zalo_oa_client.post('/sendmessage/text', {'uid': 'user_id', 'message': 'put_your_message_h'})
```

**Get message status**
```
message_status = zalo_oa_client.get('/getmessagestatus', {'msgid': 'message_id'})
```

**Upload image**
```
path = "path_to_your_image"
upload_photo_from_path = zalo_oa_client.post('/upload/image', {'file': path})
```

**Upload Image Gif**
```
path = "path_to_your_image"
upload_gif = zalo_oa_client.post('/upload/gif', {'file': path})
```

**Send image message**
```
send_image_message = zalo_oa_client.post('/sendmessage/image', {
    'uid': user_id,
    'imageid': image_id,
    'message': 'put_your_message_h'
})
```

**Send link message**
```
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
```

**Send interaction message**
```
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
```

**Get profile user followed OA**
```
profile = zalo_oa_client.get('/getprofile', {'uid': user_id})
```

**Send customer care message**
```
send_message_customer_care_by_phone = zalo_oa_client.post('/sendmessage/phone/cs', {
    'phone': phone,
    'templateid': template_id,
    'templatedata': data
})
```

**Send customer care message by phone number**
```
send_message_customer_care_by_user_id = zalo_oa_client.post('/sendmessage/cs', {
    'uid': user_id,
    'templateid': template_id,
    'templatedata': data
})
```

## Authors

* **NtkDuy**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
