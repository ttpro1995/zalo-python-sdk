# Zalo SDK for Python (v1)

[![N|Solid](https://developers.zalo.me/web/static/prodution/images/logo.png)](https://nodesource.com/products/nsolid)

## Installation
You can easily install this package by using pip
```
pip install zalo-python-sdk
```

## How to use
**Khởi tạo Zalo3rdAppClient**
```
from zalo.sdk.app import ZaloAppInfo, Zalo3rdAppClient

zalo_info = ZaloAppInfo(app_id=your app id, secret_key="your app secret")
zalo_3rd_app_client = Zalo3rdAppClient(zalo_info)
```

## Social API
**Lấy LoginUrl**
```
login_url = zalo_3rd_app_client.get_login_url()
```

**Lấy AccessToken**
```
code = 'put_your_code_here'
access_token = zalo_3rd_app_client.get_access_token(code)
```

**Thông tin người dùng**
```
profile = zalo_3rd_app_client.get('/me', token, {'fields': 'id, name, birthday, gender, picture'})
```

**Lấy danh sách tất cả bạn bè của người dùng đã sử dụng ứng dụng**
```
friends = zalo_3rd_app_client.get('/me/friends', token, {'offset': 10, 'limit': 50})
```

**Lấy danh sách bạn bè chưa sử dụng ứng dụng và có thể nhắn tin mời sử dụng ứng dụng**
```
invitable_friends = zalo_3rd_app_client.get('/me/invitable_friends', token, {
    'offset': '0',
    'limit': '10',
    'fields': 'id, name, birthday, gender, picture'
})
```

**Đăng bài viết**
```
post_feed = zalo_3rd_app_client.post('/me/feed', token, {
    'message': 'put_your_message_here',
    'link': 'https://developers.zalo.me/'
})
```

**Mời sử dụng ứng dụng**
```
send_app_request = zalo_3rd_app_client.post('/apprequests', token, {
    'message': 'put_your_message_here',
    'to': 'user '
})
```

**Gởi tin nhắn tới bạn bè**
```
send_message = zalo_3rd_app_client.post('/me/message', token, {
    'message': 'put_your_message_here',
    'to': 'user id',
    'link': 'https://developers.zalo.me/'
})
```

## Official Account Open API

**Khởi tạo ZaloOA**
```
from zalo.sdk.oa import ZaloOaInfo, ZaloOaClient

zalo_info = ZaloOaInfo(oa_id="put_your_oauth_code_here", secret_key="put_your_secret_key_here")
zalo_oa_client = ZaloOaClient(zalo_info)
```

**Lấy thông tin người theo dõi**
```
profile = zalo_oa_client.get('/getprofile', {'uid': user_id})
```

**Gửi tin nhắn text**
```id
data = {
    'uid': user_id,
    'message': 'hello there'
}
params = {'data': data}
send_text_message = zalo_oa_client.post('/sendmessage/text', params)
```

**Lấy trạng thái tin nhắn**
```
message_status = zalo_oa_client.get('/getmessagestatus', {'msgid': 'message_id'})
```

**Upload hình ảnh**
```
upload_photo_from_path = zalo_oa_client.post('/upload/image', {'file': path})
```

**Upload ảnh Gìf**
```
upload_gif = zalo_oa_client.post('/upload/gif', {'file': path})
```

**Gửi tin nhắn hình**
```
data = {
    'uid': user_id,
    'imageid': image_id,
    'message': 'team secret'
}
params = {
    'data': data
}
send_image_message = zalo_oa_client.post('/sendmessage/image', params)
```

**Gửi tin nhắn ảnh Gif**
```
data = {
    'uid': user_id,
    'width': 10,
    'height': 20,
    'imageid': gif_id
}
params = {
    'data': data
}
send_gif_message = zalo_oa_client.post('/sendmessage/gif', params)
```

**Gửi tin nhắn dạng liên kết**
```
links = [{
    'link': 'https://developers.zalo.me/',
    'linktitle': 'Zalo For Developers',
    'linkdes': 'Document For Developers',
    'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
}]
data = {
    'uid': user_id,
    'links': links
}
params = {
    'data': data
}
send_link_message = zalo_oa_client.post('/sendmessage/links', params)
```

**Gửi tin nhắn tương tác**
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
data = {
    'uid': user_id,
    'actionlist': action_list
}
params = {
    'data': data
}
send_action_message = zalo_oa_client.post('/sendmessage/actionlist', params)
```

**Gửi tin nhắn chăm sóc khách hàng**
```
templatedata = {
    "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
}
data = {
    'uid': user_id,
    'templateid': template_id,
    'templatedata': templatedata
}
params = {'data': data}
send_message_customer_care_by_user_id = zalo_oa_client.post('/sendmessage/cs', params)
```

**Gửi tin nhắn chăm sóc khách hàng tới số điện thoại**
```
templatedata = {
    "content":"Chào bạn, Chúc bạn một ngày vui vẻ!"
}
data = {
    'phone': phone,
    'templateid': template_id,
    'templatedata': templatedata
}
params = {
    'data': data
}
send_message_customer_care_by_phone = zalo_oa_client.post('/sendmessage/phone/cs', params)
```

**Gửi tin nhắn Sticker**
```
data = {
    'uid': user_id,
    'stickerid': 'sticker_id'
}
params = {'data': data}
send_sticker_message = zalo_oa_client.post('/sendmessage/sticker', params)
```

**Trả lời tin nhắn dạng text**
```
data = {
    'msgid': 'msg_id',
    'message': 'put_your_message_here'
}
params = {'data': data}
reply_text_message = zalo_oa_client.post('/sendmessage/reply/text', params)
```

**Trả lời tin nhắn dạng hình**
```
data = {
    'msgid': 'msg_id',
    'imageid': 'image_id',
    'message': 'put_your_message_here'
}
params = {'data': data}
reply_image_message = zalo_oa_client.post('/sendmessage/reply/image', params)
```

**Trả lời tin nhắn dạng liên kết**
```
data = {
    'msgid': 'msg_id',
    'links': ''
}
params = {'data': data}
reply_link_message = zalo_oa_client.post('/sendmessage/reply/links', params)
```

**Tạo QR Code**
```
data = {
    'qrdata': 'qrcode',
    'size': 10
}
params = {'data': data}
qrcode = zalo_oa_client.post('/qrcode', params)
```

## Official Account Open API Onbehalf
>Khi người dùng click vào link đăng nhập,
>Hệ thống sẽ thực hiện xử lý đăng nhập, và yêu cầu cấp quyền truy xuất thông tin của Offical Account,
>Sau khi người dùng đồng ý cấp quyền, hệ thống sẽ chuyển hướng về callback link đã đăng ký với app,
>Access token được hệ thống trả về và hiển thị trên callback link.

**Khởi tạo ZaloOaOnbehalf**
```
from zalo.sdk.app import ZaloAppInfo
from zalo.sdk.oa import ZaloOaOnbehalf

zalo_info = ZaloAppInfo(app_id=put_your_app_id_h, secret_key="put_your_secret_key_h")
zalo_info.callback_url = 'put_your_callback_url_h'
zalo_oa_on_behalf = ZaloOaOnbehalf(zalo_info)
```

**Lấy link đăng nhập**
```
login_url = zalo_oa_on_behalf.get_login_url()
```

**Lấy thông tin người quan tâm**
```
data = {
    'uid': user_id,
    'accessTok': access_token
}
params = {'data': data}
on_behalf_profile = zalo_oa_on_behalf.get('/onbehalf/getprofile', params)
```

**Lấy thông tin OA**
```
data = {
    'accessTok': access_token
}
params = {'data': data}
on_behalf_oa = zalo_oa_on_behalf.get('/onbehalf/getoa', params)
```

**Lấy đoạn hội thoại giữa người quan tâm và OA**
```
data = {
    'offset':0,
    'count': 1,
    'uid': user_id,
    'accessTok': access_token
}
params = {'data': data}
on_behalf_conversation = zalo_oa_on_behalf.get('/onbehalf/conversation', params)
```

**Lấy danh sách người quan tâm vừa chat với OA**
```
data = {
    'offset':0,
    'count': 1,
    'accessTok': access_token
}
params = {'data': data}
on_behalf_listrecentchat = zalo_oa_on_behalf.get('/onbehalf/listrecentchat', params)
```

**Gửi tin nhắn dạng text**
```
data = {
    'uid': user_id,
    'message': 'test',
    'accessTok': access_token
}
params = {'data': data}
on_behalf_send_text_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/text', params)
```

**Gửi tin nhắn dạng hình**
```
data = {
    'uid': user_id,
    'imageid': image_id,
    'message': 'Your image',
    'accessTok': access_token
}
params = {'data': data}
on_behalf_send_image_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/image', params)
```

**Gửi tin nhắn dạng liên kết**
```
links = [{
    'link': 'https://developers.zalo.me/',
    'linktitle': 'Zalo For Developers',
    'linkdes': 'Document For Developers',
    'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
}]
data = {
    'uid': user_id,
    'links': links,
    'accessTok': access_token
}
params = {'data': data}
send_link_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/links', params)
```

**Gửi tin nhắn tương tác**
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
data = {
    'uid': user_id,
    'accessTok': access_token,
    'actionlist': action_list
}
params = {'data': data}
on_behalf_send_action_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/actionlist', params)
```

**Gửi tin nhắn dạng Gif**
```
gif_id = '0d5E/ZSJfblTkacuv43H09bfRxUgXcP5+/TuAd7ZPvw='
data = {
    'uid': user_id,
    'imageid': gif_id,
    'width': 20,
    'height': 30,
    'accessTok': access_token
}
params = {'data': data}
on_behalf_send_gif_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/gif', params)
```

**Upload hình**
```
on_behalf_uplpad_image= zalo_oa_on_behalf.post('/onbehalf/upload/image', {
    'file': path_to_image,
    'accessTok': access_token
})
```

**Upload hình Gif**
```
on_behalf_upload_gif = zalo_oa_on_behalf.post('/onbehalf/upload/gif', {
    'file': path_to_gif,
    'accessTok': access_token
})
```

**Trả lời tin nhắn dạng text**
```
data = {
    'msgid': 'c159a5e84961613f3870',
    'message': 'test message',
    'accessTok': access_token
}
params = {'data': data}
reply_text_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/text', params)
```

**Trả lời tin nhắn dạng hình**
```
data = {
    'msgid': 'c159a5e84961613f3870',
    'message': 'test message',
    'imageid': image_id,
    'accessTok': access_token
}
params = {'data': data}
reply_image_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/image', params)
```

**Trả lời tin nhắn dạng liên kết**
```
links = [{
    'link': 'https://developers.zalo.me/',
    'linktitle': 'Zalo For Developers',
    'linkdes': 'Document For Developers',
    'linkthumb': 'https://developers.zalo.me/web/static/images/bg.jpg'
}]
data = {
    'msgid': message_id,
    'links': links,
    'accessTok': access_token
}
params = {'data': data}
reply_link_message = zalo_oa_on_behalf.post('/onbehalf/sendmessage/reply/links', params)
```

## Store API
**Khởi tạo ZaloStore**
```
from zalo.sdk.oa import ZaloOaInfo
from zalo.sdk.store import ZaloStoreClient

oa_info = ZaloOaInfo(oa_id=oa_id, secret_key=secret_key)
zalo_store_client = ZaloStoreClient(oa_info)
```

**Tạo sản phẩm**
```
photos = [{
    'id': photo_id
}]
data = {
    'name': 'put_your_product_name_here',
    'desc': 'put_your_description_here',
    'code': 'put_your_code_number_here',
    'price': 15000,
    'photos': photos,
    'display': 'show' # show | h,
    'payment': 2 # 2 - enable | 3 - disable
}
params = {'data': data}
product = zalo_store_client.post('/store/product/create', params)
```

**Chỉnh sửa sản phẩm**
```
photos = [{
    'id': photo_id
}]
update = {
    'name': 'put_your_product_name_here',
    'desc': 'put_your_description_here',
    'code': 'put_your_code_number_here',
    'price': 15000,
    'photos': photos,
    'display': 'show',  # show | hide
    'payment': 2  # 2 - enable | 3 - disable
}
data = {
    'productid': product_id,
    'product': update
}
params = {'data': data}
product_update = zalo_store_client.post('/store/product/update', params)
```

**Xóa sản phẩm**
```
params = {
    'productid': product_id
}
remove_product = zalo_store_client.post('/store/product/remove', params)
```

**Lấy thông tin sản phẩm**
```
data = {
    'productid': product_id
}
params = {'data': data}
get_product = zalo_store_client.get('/store/product/getproduct', params)
```

**Danh sách sản phẩm**
```
data = {
    'offset': 0,
    'count': 2
}
params = {'data': data}
get_list_product = zalo_store_client.get('/store/product/getproductofoa', params)
```

**Upload hình sản phẩm**
```
params = {'file': path_to_product_photo}
product_photo = zalo_store_client.post('/store/upload/productphoto', params)
```

**Tạo danh mục**
```
data = {
    'name': 'put_your_category_name_here',
    'desc': 'put_your_description_here',
    'photo': photo_id,
    'status': 0  # 0 - show | 1 - hide
}
params = {'data': data}
category = zalo_store_client.post('/store/category/create', params)
```

**Chỉnh sửa danh mục**
```
update = {
    'name': 'put_your_category_name_here',
    'desc': 'put_your_description_here',
    'photo': photo_id,
    'status': 0  # 0 - show | 1 - hide
}
data = {
    'categoryid': category_id,
    'category': update
}
params = {'data': data}
category = zalo_store_client.post('/store/category/update', params)
```

**Danh sách danh mục**
```
data = {
    'offset': 0,
    'count': 3
}
params = {'data': data}
get_list_category = zalo_store_client.get('/store/category/getcategoryofoa', params)
```

**Upload hình danh mục**
```
params = {'file': path_to_category_photo}
category_photo = zalo_store_client.post('/store/upload/categoryphoto', params)
```

**Chỉnh sửa đơn hàng**
```
update = {
    'name': 'put_your_category_name_here',
    'desc': 'put_your_description_here',
    'photo': photo_id,
    'status': 0  # 0 - show | 1 - hide
}
data = {
    'categoryid': category_id,
    'category': update
}
params = {'data': data}
category = zalo_store_client.post('/store/category/update', params)
```

**Danh sách đơn hàng**
```
data = {
    'offset': 0,
    'count': 10,
    'filter': 0
}
params = {'data': data}
get_list_order = zalo_store_client.get('/store/order/getorderofoa', params)
```

**Lấy thông tin đơn hàng**
```
params = {'orderid': order_id}
get_order = zalo_store_client.get('/store/order/getorder', params)
```

## Store API Onbehalf
>Khi người dùng click vào link đăng nhập,
>Hệ thống sẽ thực hiện xử lý đăng nhập, và yêu cầu cấp quyền truy xuất thông tin của Offical Account,
>Sau khi người dùng đồng ý cấp quyền, hệ thống sẽ chuyển hướng về callback link đã đăng ký với app,
>Access token được hệ thống trả về và hiển thị trên callback link.

**Khởi tạo ZaloStoreOnbehalf**
```
from zalo.sdk.app import ZaloAppInfo
from zalo.sdk.store import ZaloStoreOnbehalfClient

zalo_info = ZaloAppInfo(app_id=app_id, secret_key="secret_key")
zalo_info.callback_url = 'callback_url'
zalo_store_on_behalf_client = ZaloStoreOnbehalfClient(zalo_info)
```

**Lấy link đăng nhập**
```php
login_url = zalo_store_on_behalf_client.get_login_url()
```

**Tạo sản phẩm**
```
photos = [{
    'id': photo_id
}]
product = {
    'name': 'put_your_product_name_here',
    'desc': 'put_your_description_here',
    'code': 'put_your_code_number_here',
    'price': 15000,
    'photos': photos,
    'display': 'show',
    'payment': 2  # 2 - enable | 3 - disable
}
data = {'product': product, 'accessTok': access_token}
params = {'data': data}
product = zalo_store_on_behalf_client.post('/store/onbehalf/product/create', params)
```

**Chỉnh sửa sản phẩm**
```
photos = [{
    'id': photo_id
}]
product = {
    'name': 'put_your_product_name_here',
    'desc': 'put_your_description_here',
    'code': 'put_your_code_number_here',
    'price': 15000,
    'photos': photos,
    'display': 'show',
    'payment': 2  # 2 - enable | 3 - disable
}
data = {'productid': product_id, 'product': product, 'accessTok': access_token}
params = {'data': data}
update_product = zalo_store_on_behalf_client.post('/store/onbehalf/product/create', params)
```

**Xóa sản phẩm**
```
data = {'productid': product_id, 'accessTok': access_token}
params = {'data': data}
remove_product = zalo_store_on_behalf_client.post('/store/onbehalf/product/remove', params)
```

**Lấy thông tin sản phẩm**
```
data = {
    'productid': product_id,
    'accessTok': access_token
}
params = {'data': data}
get_product = zalo_store_on_behalf_client.get('/store/onbehalf/product/getproduct', params)
```

**Danh sách sản phẩm**
```
data = {
    'offset': 0,
    'count': 10,
    'accessTok': access_token
}
params = {'data': data}
get_list_product = zalo_store_on_behalf_client.get('/store/onbehalf/product/getproductofoa', params)
```

**Upload hình sản phẩm**
```
data = {'file': path_to_product_photo, 'accessTok': access_token}
upload_photo = zalo_store_on_behalf_client.post('/store/onbehalf/upload/productphoto', data)
```

**Tạo danh mục**
```php
category = {
    'name': 'put_your_category_name_here',
    'desc': 'put_your_description_here',
    'photo': photo_id,
    'status': 0  # 0 - show | 1 - hide
}
data = {'category': category, 'accessTok': access_token}
params = {'data': data}
category = zalo_store_on_behalf_client.post('/store/onbehalf/category/create', params)
```

**Chỉnh sửa danh mục**
```
category = {
    'name': 'put_your_category_name_here',
    'desc': 'put_your_description_here',
    'photo': 'b835603364748d2ad465',
    'status': 0  # 0 - show | 1 - hide
}
data = {
    'categoryid': '9387609a5edfb781eece',
    'category': category,
    'accessTok': access_token
}
params = {'data': data}
category = zalo_store_on_behalf_client.post('/store/onbehalf/category/update', params)
```

**Danh sách danh mục**
```
data = {
    'offset': 0,
    'count': 3,
    'accessTok': access_token
}
params = {'data': data}
get_list_category = zalo_store_on_behalf_client.get('/store/onbehalf/category/getcategoryofoa', params)
```

**Upload hình danh mục**
```
data = {'file': path_to_product_photo, 'accessTok': access_token}
upload_photo = zalo_store_on_behalf_client.post('/store/onbehalf/upload/categoryphoto', data)
```

**Chỉnh sửa đơn hàng**
```
data = {
    'orderid': order_id,
    'status': 2,
    'reason': 'put_your_reason_here',
    'cancelReason': 'put_your_reason_here',
    'accessTok': access_token
}
params = {'data': data}
update_order = zalo_store_on_behalf_client.post('/store/onbehalf/order/update', params)
```

**Danh sách đơn hàng**
```
data = {
    'offset': 0,
    'count': 10,
    'filter': 0,
    'accessTok': access_token
}
params = {'data': data}
get_list_order = zalo_store_on_behalf_client.get('/store/onbehalf/order/getorderofoa', params)
```

**Lấy thông tin đơn hàng**
```
data = {
    'orderid': order_id,
    'accessTok': access_token
}
params = {'data': data}
get_order = zalo_store_on_behalf_client.get('/store/onbehalf/order/getorder', params)
```

## Article API

**Khởi tạo ZaloArticle**
```
from zalo.sdk.article.ZaloArticleClient import ZaloArticleClient
from zalo.sdk.oa import ZaloOaInfo

oa_info = ZaloOaInfo(oa_id=oa_id, secret_key=secret_key)
zalo_article_client = ZaloArticleClient(oa_info)
```

**Tạo bài viết**
```
cover = {
    'coverType': 1,  # 0 (photo) | 1 (video)
    'coverView': 1,  # 1 (horizontal), 2 (vertical), 3 (square),
    'videoId': 'b0a710f62cb3c5ed9ca2',
    'status': 'show'
}
actionLink = {
    'type': 2,  # 0 (link to web), 1 (link to image), 2 (link to video), 3 (link to audio)
    'label': 'put_label_here',
    'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A'
}
paragraphText = {
    'type': 0,
    'content': 'put_content_here'
}
paragraphImage = {
    'type': 1,
    'url': 'https://upload.wikimedia.org/wikipedia/commons/7/71/2010-kodiak-bear-1.jpg',
    'caption': 'put_caption_here',
    'width': 500,
    'height': 300
}
paragraphVideo = {
    'type': 3,
    'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A',
    'category': 'youtube',
    'caption': 'put_caption_here'
}
relatedArticle = {
    'id': 'put_media_id_here'  # related article
}
media = {
    'title': 'put_title_here',
    'author': 'put_author_here',
    'cover': cover,
    'desc': 'put_description_here',
    'actionLink': actionLink,
    'body': [paragraphText, paragraphImage, paragraphVideo],
    'relatedMedias': [relatedArticle],
    'status': 'show'
}
media_create = zalo_article_client.post('/media/create', {
    'media': media
})
```

**Lấy Id của bài viết**
```
media_id = zalo_article_client.post('/media/verify', {
    'token': token
})
```

**Chỉnh sửa bài viết**
```
cover = {
    'coverType': 1,  # 0 (photo) | 1 (video)
    'coverView': 1,  # 1 (horizontal), 2 (vertical), 3 (square),
    'videoId': 'b0a710f62cb3c5ed9ca2',
    'status': 'show'
}
actionLink = {
    'type': 2,  # 0 (link to web), 1 (link to image), 2 (link to video), 3 (link to audio)
    'label': 'put_label_here',
    'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A'
}
paragraphText = {
    'type': 0,
    'content': 'put_content_here'
}
paragraphImage = {
    'type': 1,
    'url': 'https://upload.wikimedia.org/wikipedia/commons/7/71/2010-kodiak-bear-1.jpg',
    'caption': 'put_caption_here',
    'width': 500,
    'height': 300
}
paragraphVideo = {
    'type': 3,
    'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A',
    'category': 'youtube',
    'caption': 'put_caption_here'
}
relatedArticle = {
    'id': 'put_media_id_here'  # related article
}
media = {
    'title': 'put_title_here',
    'author': 'put_author_here',
    'cover': cover,
    'desc': 'put_description_here',
    'actionLink': actionLink,
    'body': [paragraphText, paragraphImage, paragraphVideo],
    'relatedMedias': [relatedArticle],
    'status': 'show'
}
media_update = zalo_article_client.post('/media/update', {
    'mediaid': media_id,
    'media': media
})
```

**Xóa bài viết**
```
media_remove = zalo_article_client.post('/media/remove', {
    'mediaid': media_id
})
```

**Lấy danh sách bài viết**
```
data = {
    'offset': 0,
    'count': 10
}
params = {
    'data': data
}
get_slice = zalo_article_client.get('/media/getslice', params)
```

**Broadcast bài viết**
```
target = {
    'gender': '1',
    'ages': '1,2,3',
}
data = {
    'mediaIds': [{'id': media_id}],
    'target': target
}
params = {
    'data': data
}
broadcast = zalo_article_client.post('/broadcast/medias', params)
```

**Upload video cho bài viết**
```
# Step 1 - Lấy link upload
videoName = 'test.mp4'
videoSize = 307118
data = {
    'videoName': videoName,
    'videoSize': videoSize
}
params = {'data': data}
link_upload_video = zalo_article_client.post('/media/upload/video', params)

# Step 2 - Upload file và lấy token
upload_link = link_upload_video['data']['uploadLink']
timestamp = link_upload_video['data']['time']
sig = link_upload_video['data']['sig']
app_id = link_upload_video['data']['appId']

params = {
    'appId': app_id,
    'file': '/home/cpu10142-local/Downloads/test.mp4',
    'timestamp': timestamp,
    'sig': sig
}
upload_video = zalo_article_client.upload_video('http://upload.media.zapps.vn/upload', params)

# Step 3 - Lấy id của video
data = {
    'token': upload_video['data']['token'],
    'videoName': videoName,
    'videoSize': videoSize,
    'time': timestamp,
    'sig': sig
}
params = {'data': data}
get_video_id = zalo_article_client.get('/media/getvideoid', params)

# step 4 - Kiểm tra trạng thái của video
video_id = get_video_id['data']['videoId']
data = {
    'videoId': video_id
}
params = {'data': data}
get_video_status = zalo_article_client.get('/media/getvideostatus', params)
```



## Authors

* **NtkDuy**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
