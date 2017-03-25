# baike_spider
基于慕课网python简单爬虫教学，环境为pydev和python3.5
#该部分收集输出内容，整理成文本形式写入到本地文件
#问题：这个部分中write函数仅接受str格式，另外summary无法写入为gbk格式，所以html格式就没有办法 = =，注意定义写入文本格式，可以减少报错 
# -*- coding:utf-8 -*-

class HtmlOutputer(object):  
    def __init__(self):  
        self.datas = []#收集列，所有输出数据都会置入到该列          
      
    def collect_data(self,data):#收集函数，将收集数据置入到收集列中
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):#写入本地文件函数
        fout = open('C:/Users/joeya/Desktop/b.txt','a',encoding='utf-8')#定义地址，读写状态，格式
        a = 1#加了一个简单的序数
        for data in self.datas:#for循环将集合列中数据遍历
            fout.write(str(a) + '  ')
            fout.write("%s"%data["url"] + '\n')
            fout.write("%s"%data["title"] + '\n')
            fout.write("%s"%data["summary"] + '\n\n')
            a = a + 1
        
        #以下为输出数据为html格式时的情况
        #fout.write("<html>")
        #fout.write("<body>")
        #fout.write("<table>")
        
        
            
            
        #for data in self.datas:
        #   fout.write("<tr>")
        #   fout.write("<td>%s</td>"%data["url"])
        #   fout.write('\n')
        #   #print(url)
        #   fout.write("<td>%s</td>"%data["title"])
        #   fout.write('\n')
        #   fout.write("<td>%s</td>"%data["summary"])
        #   fout.write('\n')
        #   #fout.write("<td>")
        #   #aaa = str(data["summary"])
        #   #fout.write(aaa)
        #   fout.write("</td>")
        #   fout.write("</tr>")
               
        #fout.write("</table>")
        #fout.write("</body>")
        #fout.write("</html>")
        #fout.close()
