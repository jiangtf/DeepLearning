# -*- coding: utf-8 -*-
import requests
import json
import base64
from aip import AipOcr
import ssl
import urllib

from urllib.parse import unquote


APP_ID = '15382948'
API_KEY = 'g9cuLk9o30YWG5rFwtcigcvn'
SECRET_KEY = 'yYhiszR49AUIBvxZ0KhZDF8c5GpojbMI'


def get_file_content(filePath):
    """ 读取图片base64 """
    with open(filePath, 'rb') as fp:
        return base64.b64encode(fp.read())


def get_access_token():

    r = requests.post(
        url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    , headers={'Content-Type':'application/x-www-form-urlencoded'})
    print('text',r.text)
    j = json.loads(r.text)
    print('access_token',j.get('access_token'))
    return j.get('access_token')




    '''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    request = urllib.request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.urlopen(request)
    content = response.read()
    if(content):
        print(content)
    '''



def recognise_handwriting_pic(access_token, image_path):
    image = get_file_content(image_path)
    print(image)
    r = requests.post(
        #url='https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token=' + str(access_token),  手写识别
        url='https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + str(access_token), #高精度识别
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={'image': image})
    print(r.text)
    text = unquote(r.text, 'utf-8')
    #text=r.text.decode('utf-8')
    j = json.loads(text)
    print('j',j)
    words_result = j.get('words_result')
    for i in words_result:
        print(i.get('words'))




access_token = get_access_token()
recognise_handwriting_pic(access_token, image_path='D://pythonworkspace//DeepLearning//Chat3//my//4.png')
