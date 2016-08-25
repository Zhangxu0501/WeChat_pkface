#!/usr/bin/env python
# coding: utf-8
import urllib2
import urllib
import random


class Share():

    def __init__(self, dst1, dst2, scores):
        self.dst1 = dst1
        self.dst2 = dst2
        self.scores = scores

    def get(self):
        data = {}
        data['grades'] = self.scores
        data['img_url'] = self.dst2
        # data['img'] = f.read()
        data['img_user'] = self.dst1
        # 定义post的地址
        url = 'http://115.159.31.149:8000/score?grades=99'
        post_data = urllib.urlencode(data)

        # 提交，发送数据
        request = urllib2.Request(url)
        req = urllib2.urlopen(request)

        # 获取提交后返回的信息
        content = req.read()
        print content
        return content

if __name__ == '__main__':
    a = Share('https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/1.jpg', 'https://coding.net/u/zhu_tian_cheng/p/SybilPhotos/git/raw/master/img_670270549348332186.jpg', 85)
    a.get()
