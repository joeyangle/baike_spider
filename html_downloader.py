# baike_spider
基于慕课网python简单爬虫教学，环境为pydev和python3.5
#该部分为网页下载器
#下载器就是把网页扒下来，很简单

# -*- coding:utf-8 -*-
from urllib import request     
class HtmlDownloader(object):
    def download(self,url):#定义下载函数
        if url is None:
            return None
        #request = urllib2.Request(url)
        #request.add_header("user-agent", "Mozilla/5.0")
        response = request.urlopen(url)          
        if response.getcode() != 200:
            return None
        outt = response.read().decode('utf-8')
        #print(outt)
        return outt
