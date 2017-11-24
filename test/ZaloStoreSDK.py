from zalo.sdk.app.ZaloAppInfo import ZaloAppInfo
from zalo.sdk.article.ZaloArticleClient import ZaloArticleClient
from zalo.sdk.oa.ZaloOaClient import ZaloOaClient
from zalo.sdk.oa.ZaloOaInfo import ZaloOaInfo
from zalo.sdk.store.ZaloStoreClient import ZaloStoreClient
from zalo.sdk.store.ZaloStoreOnbehalfClient import ZaloStoreOnbehalfClient

oa_info = ZaloOaInfo(oa_id="2491302944280861639", secret_key="Tb418kOM4WJLQzwYGqqw")
zalo_store_client = ZaloStoreClient(oa_info)

# path_to_product_photo = "/home/cpu10142-local/Downloads/revanon2.jpg"
# params = {'file': path_to_product_photo}
# product_photo = zalo_store_client.post('/store/upload/productphoto', params)
# print product_photo

photo_id = 'c33883ad39ead0b489fb'
# photos = [{
#     'id': photo_id
# }]
# data = {
#     'name': 'dadasdasdas',
#     'desc': 'put_your_description_here',
#     'code': '123',
#     'price': 15000,
#     'photos': photos,
#     'display': 'show'
# }
# params = {'data': data}
# product = zalo_store_client.post('/store/product/create', params)
# print product

product_id = '5f6e253e017be825b16a'
# photos = [{
#     'id': photo_id
# }]
# update = {
#     'name': 'put_your_product_name_here',
#     'desc': 'put_your_description_here',
#     'code': 'put_your_code_number_here',
#     'price': 15000,
#     'photos': photos,
#     'display': 'show',  # show | hide
#     'payment': 2  # 2 - enable | 3 - disable
# }
#
# data = {
#     'productid': product_id,
#     'product': update
# }
# params = {'data': data}
# product_update = zalo_store_client.post('/store/product/update', params)

# data = {
#     'productid': product_id
# }
# params = {'data': data}
# get_product = zalo_store_client.get('/store/product/getproduct', params)
# print get_product
#
# params = {
#     'productid': product_id
# }
# remove_product = zalo_store_client.post('/store/product/remove', params)
# print remove_product
#
# data = {
#     'offset': 0,
#     'count': 2
# }
# params = {'data': data}
# get_list_product = zalo_store_client.get('/store/product/getproductofoa', params)
# print get_list_product
#
# data = {
#     'name': 'put_your_category_name_here',
#     'desc': 'put_your_description_here',
#     'photo': photo_id,
#     'status': 0  # 0 - show | 1 - hide
# }
# params = {'data': data}
# category = zalo_store_client.post('/store/category/create', params)
# print category

# category_id = '9387609a5edfb781eece'
# update = {
#     'name': 'put_your_category_name_here',
#     'desc': 'put_your_description_here',
#     'photo': photo_id,
#     'status': 0  # 0 - show | 1 - hide
# }
# data = {
#     'categoryid': category_id,
#     'category': update
# }
# params = {'data': data}
# category = zalo_store_client.post('/store/category/update', params)
# print category
#
# data = {
#     'offset': 0,
#     'count': 3
# }
# params = {'data': data}
# get_list_category = zalo_store_client.get('/store/category/getcategoryofoa', params)
# print get_list_category
#
# path_to_category_photo = "/home/cpu10142-local/Downloads/revanon2.jpg"
# params = {'file': path_to_category_photo}
# category_photo = zalo_store_client.post('/store/upload/categoryphoto', params)
# print category_photo
#
# data = {
#     'offset': 0,
#     'count': 10,
#     'filter': 0
# }
# params = {'data': data}
# get_list_order = zalo_store_client.get('/store/order/getorderofoa', params)
# print get_list_order
#
# order_id = '9541954bac0e45501c1f'
# params = {'orderid': order_id}
# get_order = zalo_store_client.get('/store/order/getorder', params)
# print get_order
#
zalo_info = ZaloAppInfo(app_id=1131677296116040198, secret_key="rbZ5wQ2tVUh7Y3y6Kxqe")
zalo_info.callback_url = 'https://smilesplz91.000webhostapp.com/'
zalo_store_on_behalf_client = ZaloStoreOnbehalfClient(zalo_info)
access_token = 'JabfuedgQXjgUIEHj8r22KSA4D3zZd47F0iyYEkRH0SO353tthiZVmT6Vlx8-2iaTqGoouF1VJLrRGwxWlqRSLnUGjYqgYv0IsL6gydq64exvt7VsNGwP5ayFIw_daINTmjiUA_1AC4092zwti5x_3GR6HUY_MtE0Nj6KhpXTyn5TgrnYDGYMG'

# login_url = zalo_store_on_behalf_client.get_login_url()
# print login_url
#
# photos = [{
#     'id': photo_id
# }]
# product = {
#     'name': 'dadasdasdas',
#     'desc': 'put_your_description_here',
#     'code': '123',
#     'price': 15000,
#     'photos': photos,
#     'display': 'show',
# }
# data = {'product': product, 'accessTok': access_token}
# params = {'data': data}
# product = zalo_store_on_behalf_client.post('/store/onbehalf/product/create', params)
# print product
#
# product_id = '14527c2f586ab134e87b'
# data = {
#     'productid': product_id,
#     'accessTok': access_token
# }
# params = {'data': data}
# get_product = zalo_store_on_behalf_client.get('/store/onbehalf/product/getproduct', params)
# print get_product

product_id = 'f2db968cb2c95b9702d8'
# photos = [{
#     'id': photo_id
# }]
# product = {
#     'name': 'put_your_product_name_here',
#     'desc': 'put_your_description_here',
#     'code': '123',
#     'price': 15000,
#     'photos': photos,
#     'display': 'show',
#     'payment': 2  # 2 - enable | 3 - disable
# }
# data = {'productid': product_id, 'product': product, 'accessTok': access_token}
# params = {'data': data}
# update_product = zalo_store_on_behalf_client.post('/store/onbehalf/product/create', params)
# print update_product

data = {'productid': product_id, 'accessTok': access_token}
params = {'data': data}
remove_product = zalo_store_on_behalf_client.post('/store/onbehalf/product/remove', params)
print remove_product


# data = {
#     'offset': 0,
#     'count': 10,
#     'accessTok': access_token
# }
# params = {'data': data}
# get_list_product = zalo_store_on_behalf_client.get('/store/onbehalf/product/getproductofoa', params)
# print get_list_product
# #
# path_to_product_photo = "/home/cpu10142-local/Downloads/revanon2.jpg"
# data = {'file': path_to_product_photo, 'accessTok': access_token}
# upload_photo = zalo_store_on_behalf_client.post('/store/onbehalf/upload/productphoto', data)
# print upload_photo
#
# category = {
#     'name': 'put_your_category_name_here',
#     'desc': 'put_your_description_here',
#     'photo': photo_id,
#     'status': 0  # 0 - show | 1 - hide
# }
# data = {'category': category, 'accessTok': access_token}
# params = {'data': data}
# category = zalo_store_on_behalf_client.post('/store/onbehalf/category/create', params)
# print category
#
# category = {
#     'name': 'put_your_category_name_here',
#     'desc': 'put_your_description_here',
#     'photo': 'b835603364748d2ad465',
#     'status': 0  # 0 - show | 1 - hide
# }
# data = {
#     'categoryid': '9387609a5edfb781eece',
#     'category': category,
#     'accessTok': access_token
# }
# params = {'data': data}
# category = zalo_store_on_behalf_client.post('/store/onbehalf/category/update', params)
# print category
#
# data = {
#     'offset': 0,
#     'count': 3,
#     'accessTok': access_token
# }
# params = {'data': data}
# get_list_category = zalo_store_on_behalf_client.get('/store/onbehalf/category/getcategoryofoa', params)
# print get_list_category
#
# path_to_product_photo = "/home/cpu10142-local/Downloads/revanon2.jpg"
# data = {'file': path_to_product_photo, 'accessTok': access_token}
# upload_photo = zalo_store_on_behalf_client.post('/store/onbehalf/upload/categoryphoto', data)
# print upload_photo
#
# data = {
#     'offset': 0,
#     'count': 10,
#     'filter': 0,
#     'accessTok': access_token
# }
# params = {'data': data}
# get_list_order = zalo_store_on_behalf_client.get('/store/onbehalf/order/getorderofoa', params)
# print get_list_order

order_id = '9541954bac0e45501c1f'
# data = {
#     'orderid': order_id,
#     'status': 2,
#     'reason': 'put_your_reason_here',
#     'cancelReason': 'put_your_reason_here',
#     'accessTok': access_token
# }
# params = {'data': data}
# update_order = zalo_store_on_behalf_client.post('/store/onbehalf/order/update', params)
# print update_order

# data = {
#     'orderid': order_id,
#     'accessTok': access_token
# }
# params = {'data': data}
# get_order = zalo_store_on_behalf_client.get('/store/onbehalf/order/getorder', params)