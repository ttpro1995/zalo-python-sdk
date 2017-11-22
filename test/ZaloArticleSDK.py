from zalo.sdk.oa.ZaloOaInfo import ZaloOaInfo
from zalo.sdk.article.ZaloArticleClient import ZaloArticleClient

oa_info = ZaloOaInfo(oa_id="2491302944280861639", secret_key="Tb418kOM4WJLQzwYGqqw")
zalo_article_client = ZaloArticleClient(oa_info)
#
# get_slice = zalo_article_client.get('/media/getslice', {
#     'offset': 0,
#     'count': 10
# })
#
# print get_slice
# cover = {
#     'coverType': 1,  # 0 (photo) | 1 (video)
#     'coverView': 1,  # 1 (horizontal), 2 (vertical), 3 (square),
#     'videoId': 'put_your_video_id_here',
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
#
videoName = 'test.mp4'
videoSize = 310000
data = {
    'videoName': videoName,
    'videoSize': videoSize
}
params = {'data': data}
link_upload_video = zalo_article_client.post('/media/upload/video', params)
print link_upload_video

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
print upload_video

# params = {
#     'token': upload_video['data']['token'],
#     'videoName': videoName,
#     'videoSize': videoSize,
#     'time': timestamp,
#     'sig': sig
# }
# get_video_id = zalo_article_client.get('/media/getvideoid', params)