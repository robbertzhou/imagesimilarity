from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import os
from django.shortcuts import redirect, reverse
import imagecomparer.image.searchfile as sf
import jwt
import imagecomparer.yolopractise.eda as eda

# Create your views here.
def index(request):
    # users = User.objects.all()
    # article = Article.objects.all()
    return render(request, 'myupload/index.html', locals())


def login(request):
    return  render(request, 'login.html')


def upload(request):
    return render(request, 'upload/upload.html')
    # if request.method == 'GET':
    #     return render(request, 'upload/upload.html')
    # else:
    #     name = request.POST.get('name')
    #     pic = request.FILES.get('avator')
    #
    #     media_root = settings.MEDIA_ROOT  # media
    #     allow_upload = settings.ALLOW_UPLOAD  # ALLOW_UPLOAD
    #     # path = 'upload/{}/{}/{}/'.format(datetime.now().year, datetime.now().month, datetime.now().day)
    #     '{:02d}'.format
    #     path = 'upload/{}/{}/{}/'.format(datetime.now().year, '{:02d}'.format(datetime.now().month),
    #                                      '{:02d}'.format(datetime.now().day))
    #     full_path = media_root + '/' + path
    #
    #     # full_path = 'media/upload/2019/12/20'
    #     if not os.path.exists(full_path):  # 判断路径是否存在
    #         os.makedirs(full_path)  # 创建此路径
    #
    #     # 要不要改图片的名字 生成hash
    #     # 这块要不要判断图片类型 .jpg .png .jpeg
    #     # '/../../../myviews/setting.py'
    #     print(pic)
    #     print(full_path)
    #     print(full_path + pic.name)
    #     if pic.name.split('.')[-1] not in allow_upload:
    #         return HttpResponse('fail')
    #
    #     with open(full_path + '/' + pic.name, 'wb') as f:
    #         for c in pic.chunks():  # 相当于切片
    #             f.write(c)
    #
    #     # User.objects.create(name=name, avator=path + pic.name)
    #     return redirect('myupload:index')

def uu(request):
    pic = request.FILES.get('avator')

    media_root = settings.MEDIA_ROOT  # media
    allow_upload = settings.ALLOW_UPLOAD  # ALLOW_UPLOAD
    # path = 'upload/{}/{}/{}/'.format(datetime.now().year, datetime.now().month, datetime.now().day)
    '{:02d}'.format
    path = 'upload/{}/{}/{}/'.format(datetime.now().year, '{:02d}'.format(datetime.now().month),
                                     '{:02d}'.format(datetime.now().day))
    full_path = media_root + '/' + path

    # full_path = 'media/upload/2019/12/20'
    if not os.path.exists(full_path):  # 判断路径是否存在
        os.makedirs(full_path)  # 创建此路径

    # 要不要改图片的名字 生成hash
    # 这块要不要判断图片类型 .jpg .png .jpeg
    # '/../../../myviews/setting.py'
    # print(pic)
    # print(full_path)
    # print(full_path + pic.name)
    if pic.name.split('.')[-1] not in allow_upload:
        return HttpResponse('fail')

    with open(full_path + '/' + pic.name, 'wb') as f:
        for c in pic.chunks():  # 相当于切片
            f.write(c)
    sf.searchfile(full_path + '/' + pic.name)
    # User.objects.create(name=name, avator=path + pic.name)
    return HttpResponse(sf.searchfile(full_path + '/' + pic.name))

def showbox(request):
    return render(request, 'displayimage.html')

def sb(request):
    name = request.GET.get('name')
    name = name.replace('\\n','\n')
    result = eda.alsy(name)
    return render(request, 'displayimage.html', {'src': result})


def dashboard(request):
    # You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file
    METABASE_SITE_URL = "http://10.0.100.210:3000"
    METABASE_SECRET_KEY = "97fe107d486269231d7a6cf8c4d48041f150a7e1687b19c96a79ec1dcf1d8cac"

    payload = {
        "resource": {"dashboard": 1},
        "params": {

        }
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=true&titled=true"
    return HttpResponse("ewwe")


METABASE_SITE_URL = "http://10.0.100.210:3000"
METABASE_SECRET_KEY = "97fe107d486269231d7a6cf8c4d48041f150a7e1687b19c96a79ec1dcf1d8cac"

payload = {
        "resource": {"dashboard": 1},
        "params": {

        }
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=true&titled=true"
print(iframeUrl)

