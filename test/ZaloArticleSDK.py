# coding=utf-8
from zalo.sdk.oa.ZaloOaInfo import ZaloOaInfo
from zalo.sdk.article.ZaloArticleClient import ZaloArticleClient

oa_info = ZaloOaInfo(oa_id="2491302944280861639", secret_key="Tb418kOM4WJLQzwYGqqw")
zalo_article_client = ZaloArticleClient(oa_info)

data = {
    'offset': 0,
    'count': 10
}
params = {
    'data': data
}
get_slice = zalo_article_client.get('/media/getslice', params)

print get_slice
# cover = {
#     'coverType': 1,  # 0 (photo) | 1 (video)
#     'coverView': 1,  # 1 (horizontal), 2 (vertical), 3 (square),
#     'videoId': 'b0a710f62cb3c5ed9ca2',
#     'status': 'show'
# }
# actionLink = {
#     'type': 2,  # 0 (link to web), 1 (link to image), 2 (link to video), 3 (link to audio)
#     'label': 'put_label_here',
#     'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A'
# }
# paragraphText = {
#     'type': 0,
#     'content': 'put_content_here'
# }
# paragraphImage = {
#     'type': 1,
#     'url': 'https://upload.wikimedia.org/wikipedia/commons/7/71/2010-kodiak-bear-1.jpg',
#     'caption': 'put_caption_here',
#     'width': 500,
#     'height': 300
# }
# paragraphVideo = {
#     'type': 3,
#     'url': 'https://www.youtube.com/watch?v=jp3xBWgii8A&list=RDjp3xBWgii8A',
#     'category': 'youtube',
#     'caption': 'put_caption_here'
# }
# relatedArticle = {
#     'id': 'put_media_id_here'  # related article
# }
# media = {
#     'title': 'put_title_here',
#     'author': 'put_author_here',
#     'cover': cover,
#     'desc': 'put_description_here',
#     'actionLink': actionLink,
#     'body': [paragraphText, paragraphImage, paragraphVideo],
#     'relatedMedias': [relatedArticle],
#     'status': 'show'
# }
# media_create = zalo_article_client.post('/media/create', {
#     'media': media
# })
# print media_create

media_id = 'b10a9e1db4585d060449'
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

# token = 'HRulk/0fXcvRpVs3hMRplG0BKgaQSfCt96eybrQpWAIkmC82yPAFptGGJuRvuwkiSEPG8y6SOLrOn3ywcXzAIQ=='
# media_id = zalo_article_client.post('/media/verify', {
#     'token': token
# })
# print media_id

media_id = '629d70745b31b26feb20'
# media_remove = zalo_article_client.post('/media/remove', {
#     'mediaid': media_id
# })
# print media_remove

# target = {
#     'gender': '1',
#     'ages': '1,2,3',
# }
# data = {
#     'mediaIds': [{'id': media_id}],
#     'target': target
# }
# params = {
#     'data': data
# }
# broadcast = zalo_article_client.post('/broadcast/medias', params)
# print broadcast
# Step 1 - Lấy link upload
# videoName = 'test.mp4'
# videoSize = 307118
# data = {
#     'videoName': videoName,
#     'videoSize': videoSize
# }
# params = {'data': data}
# link_upload_video = zalo_article_client.post('/media/upload/video', params)
# print link_upload_video
#
# # Step 2 - Upload file và lấy token
# upload_link = link_upload_video['data']['uploadLink']
# timestamp = link_upload_video['data']['time']
# sig = link_upload_video['data']['sig']
# app_id = link_upload_video['data']['appId']
#
# params = {
#     'appId': app_id,
#     'file': '/home/cpu10142-local/Downloads/test.mp4',
#     'timestamp': timestamp,
#     'sig': sig
# }
# upload_video = zalo_article_client.upload_video('http://upload.media.zapps.vn/upload', params)
# print upload_video
#
# # Step 3 - Lấy id của video
# data = {
#     'token': upload_video['data']['token'],
#     'videoName': videoName,
#     'videoSize': videoSize,
#     'time': timestamp,
#     'sig': sig
# }
# params = {'data': data}
# get_video_id = zalo_article_client.get('/media/getvideoid', params)
# print get_video_id
#
# # step 4 - Kiểm tra trạng thái của video
# video_id = get_video_id['data']['videoId']
# data = {
#     'videoId': video_id
# }
# params = {'data': data}
# get_video_status = zalo_article_client.get('/media/getvideostatus', params)
# print get_video_status