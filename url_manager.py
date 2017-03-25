# baike_spider
#基于慕课网python简单爬虫教学，环境为pydev和python3.5

#该部分建立新url集合和老url集合，使加载解析的都为新url
# -*- coding:utf-8 -*-

class UrlManager(object):  
      
    def __init__(self):#设立集合并且初始化 
        self.new_urls = set()  
        self.old_urls = set()  
          
    def add_new_url(self,url):#添加判断新url函数
        if url is None:  
            return#
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
   
    def add_new_urls(self,urls):#遍历解析出的url列
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
              
    def has_new_url(self):
        return len(self.new_urls) !=0
  
    def get_new_url(self):
        #print('from new url_manager')
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
