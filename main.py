# -*- coding: utf-8 -*-

import time
import base64
import wda
from PIL import (Image, ImageGrab)
from logbook import Logger, StreamHandler
import sys
from common import util

StreamHandler(sys.stdout).push_application()
log = Logger('Logbook')
wdaClient = wda.Client()
tantan_session = wdaClient.session('com.yaymedialabs.putong')
Beauty = 70  # 魅力值
Age = 16  # 年龄
Gender = 30  # 趋近于0，表示女性


def main():
    while True:
        print('==============================')
        log.info('探探机器人自动喜欢中...')
        wdaClient.screenshot('iphone_screen.png')
        iphone_screen = Image.open('./iphone_screen.png')
        img_face = iphone_screen.crop((34, 215, 1208, 1560))  # 获取探探照片，原始尺寸: 34, 215, 1208, 1560
        img_face = img_face.resize((300, 340), Image.ANTIALIAS)
        current_time = str(int(round(time.time() * 1000)))
        save_file_name = './face/img_face' + current_time + '.png'
        img_face.save(save_file_name)
        img_question = open(save_file_name, 'rb')
        img_data = img_question.read()
        img_data = base64.b64encode(img_data)
        res = util.face_test(img_data)
        if res['ret'] != 0:
            log.error('图片处理失败...')
            tantan_session.tap(465, 2028)
            continue
        data = res['data']['face_list'][0]
        if data['beauty'] > Beauty and data['age'] > Age and data['gender'] < Gender:
            log.info('发现漂亮妹子💖💖💖️...')  # 780 180
            tantan_session.tap(780, 2028)
        else:
            log.info('自动忽略️...')  # 780 180
            tantan_session.tap(465, 2028)
        time.sleep(2)


if __name__ == '__main__':
    main()
