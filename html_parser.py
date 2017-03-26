# baike_spider
#基于慕课网python简单爬虫教学，环境为pydev和python3.5
#解析器的主要作用为解析页面，获取页面内容及新的url
# -*- coding:utf-8 -*-

import re
class HtmlParser(object):#构造方法
    def _get_new_urls(self, page_url, soup):#把解析页面中的新url加入到url集合
        new_urls = set()#建立没有解析的url集合
        zhengze = re.compile(r'''<a target=_blank href="(/item/.*?)"''', re.S)#匹配短url的正则表达式
        links = re.findall(zhengze,soup)#获取短链接
        for link in links:
            new_url = link#这里是beautifulsoup错误，修改原代码之后的结果，所以有点突兀
            rooturl = 'http://baike.baidu.com'#补足url
            new_full_url = str(rooturl) + str(new_url)  #page_url与不完全的url整合成与page_url相似的url 
            new_urls.add(new_full_url)    #完全的url加入到新url集合中
        return new_urls
      
    def _get_new_data(self, page_url, soup):#该函数用于获取页面title及summary
        res_data = {}#字典数据类型，里面存放的是键值对
        res_data["url"] = page_url
        zztitle = re.compile(r'''<title>(.*?)_百度百科</title>''', re.S)#title匹配正则
        zzsummary = re.compile(r'''<meta name="description" content="(.*?)">''', re.S)#summary匹配正则
        title_node = re.findall(zztitle,soup)
        res_data["title"] = title_node#获取title内容
        summary_node = re.findall(zzsummary,soup)
        res_data["summary"] = summary_node#获取summary的内容
        return res_data #返回数据，包括页面地址，该页面title和summary
  
    def parse(self,page_url,html_cont):#调度解析函数
        if page_url is None or html_cont is None:#确认url
            return
        soup = html_cont
        new_urls = self._get_new_urls(page_url,soup)#解析得到的新url
        new_data = self._get_new_data(page_url,soup)#解析得到当页的数据
        return new_urls, new_data
        
        
###以下是修改版
# -*- coding:utf-8 -*-
#beautifulsoup的问题尚未解决，错误表示为引用的函数缺失，可能为版本问题，网上搜索结果为python2.*才有这种问题，但是使用的是python3.5，很气
#报错为No module named 'html.entities'
#问题成功解决-----At last, I found it's just because I have a file also named "html.py", in the same directory of the script file.
#Therefore, when BeautifulSoup "from html.entities import codepoint2name", it throw exception......------原来是新建的文件重名0-0
#from bs4 import BeautifulSoup
#此处由于beautisoup的原因无法解析网页，故重新定义函数进行网页解析
import re

class HtmlParser(object):   
      
    def _get_new_urls(self, page_url, soup):  
        new_urls = set()
        #<a target=_blank href="/item/%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80">
        zhengze = re.compile(r'''<a target=_blank href="(/item/.*?)"''', re.S) 
        links = re.findall(zhengze,soup)#获取所有标签名称为a的链接，这里用re嵌入了正则表达式   /item/%E6%9C%BA%E5%99%A8%E8%AF%AD%E8%A8%80 
        #print(links)
        for link in links:
            #new_url = link["href"]#获取不完全链接
            new_url = link
            #print("bad")
            rooturl = 'http://baike.baidu.com'
            new_full_url = str(rooturl) + str(new_url)#page_url与不完全的url整合成与page_url相似的url  
            new_urls.add(new_full_url)#完全的url加入到新url集合中  
        #print(new_urls)
        return new_urls
      
    def _get_new_data(self, page_url, soup):
        res_data = {}#字典数据类型，里面存放的是键值对。url= ？？title = ？？就像C中的结构体  
        #url
        res_data["url"] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #<title>Python_百度百科</title>
        zztitle = re.compile(r'''<title>(.*?)_百度百科</title>''', re.S)
        zzsummary = re.compile(r'''<meta name="description" content="(.*?)">''', re.S)
        #title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")#先找到标题为dd的节点，再找大它的子节点中标题为h1的节点  
        title_node = re.findall(zztitle,soup)
        res_data["title"] = title_node#获取title内容  
        #<div class="lemma-summary" label-module="lemmaSummary">  
        #summary_node = soup.find("div", class_="lemma-summary")#找到包含summary的节点  
        summary_node = re.findall(zzsummary,soup)
        res_data["summary"] = summary_node#获取summary的内容  
        #print(res_data)
        return res_data #返回数据，包括页面地址，该页面title和summary
  
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:  
            return
        #soup = BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")#建立beautifulsoup对象，进行页面解析  
        #soup = request.urlopen(html_cont)#通过request函数经行解析
        #soup = soup.read().decode('utf-8')#读取该页面
        #print(4)#排除问题
        soup = html_cont
        #print(5)
        new_urls = self._get_new_urls(page_url,soup)#解析得到的新url
        #print(6)
        new_data = self._get_new_data(page_url,soup)#解析得到当页的数据  
        #print(7)
        return new_urls, new_data

