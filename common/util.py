#-*- coding: UTF-8 -*-

import requests
import time
import hashlib
from urllib import parse

AppID = '1106858595'
AppKey = 'bNUNgOpY6AeeJjFu'
ApiUrl = 'https://api.ai.qq.com/fcgi-bin/face/face_detectface'


def getReqSign(params):
    url = ''
    for key in sorted(params.keys()):
        url += "%s=%s&" % (key, parse.quote(str(params[key]), safe=''))
    sign_str = url + 'app_key=' + AppKey
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest().upper()


def face_test(img_base64):
    params = {
        'app_id': AppID,
        'mode': 0,
        'time_stamp': int(time.time()),
        'nonce_str': int(time.time()),
        'image': img_base64.decode("utf-8")
    }
    params['sign'] = getReqSign(params)
    res = requests.post(
        ApiUrl,
        data=params
    )
    res_json = res.json()
    return res_json
