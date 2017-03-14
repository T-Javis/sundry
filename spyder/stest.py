# -*- coding: utf-8 -*-
'''
import urllib2  
response = urllib2.urlopen('http://www.baidu.com/')  
html = response.read()  
print html


import urllib2    
#req = urllib2.Request('http://www.baidu.com')
req = urllib2.Request('ftp://example.com/')      
response = urllib2.urlopen(req)    
the_page = response.read()    
print the_page 


import urllib    
import urllib2    
  
url = 'http://www.someserver.com/register.cgi'    
    
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }    
  
data = urllib.urlencode(values) # 编码工作  
req = urllib2.Request(url, data)  # 发送请求同时传data表单  
response = urllib2.urlopen(req)  #接受反馈的信息  
the_page = response.read()  #读取反馈的内容 



import urllib2    
import urllib  
  
data = {}  
  
data['name'] = 'WHY'    
data['location'] = 'SDU'    
data['language'] = 'Python'  
  
url_values = urllib.urlencode(data)    
print url_values  
  
name=Somebody+Here&language=Python&location=Northampton    
url = 'http://www.example.com/example.cgi'    
full_url = url + '?' + url_values  
  
data = urllib2.open(full_url)  



import urllib    
import urllib2    
  
url = 'http://www.someserver.com/cgi-bin/register.cgi'  
  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }    
  
headers = { 'User-Agent' : user_agent }    
data = urllib.urlencode(values)    
req = urllib2.Request(url, data, headers)    
response = urllib2.urlopen(req)    
the_page = response.read() 









# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：百度贴吧爬虫  
#   版本：0.1  
#   作者：why  
#   日期：2013-05-14  
#   语言：Python 2.7  
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。  
#   功能：下载对应页码内的所有页面并存储为html文件。  
#---------------------------------------  
   
import string, urllib2  
   
#定义百度函数  
def baidu_tieba(url,begin_page,end_page):     
    for i in range(begin_page, end_page+1):  
        sName = string.zfill(i,5) + '.html'#自动填充成六位的文件名  
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'  
        f = open(sName,'w+')  
        m = urllib2.urlopen(url + str(i)).read()  
        f.write(m)  
        f.close()  
   
   
#-------- 在这里输入参数 ------------------  
  
# 这个是山东大学的百度贴吧中某一个帖子的地址  
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
  
bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))  
begin_page = int(raw_input(u'请输入开始的页数：\n'))  
end_page = int(raw_input(u'请输入终点的页数：\n'))  
#-------- 在这里输入参数 ------------------  
   
  
#调用  
baidu_tieba(bdurl,begin_page,end_page)

'''


# -*- coding: utf-8 -*-    
     
import urllib2    
import urllib    
import re    
import thread    
import time    
  
    
#----------- 加载处理糗事百科 -----------    
class Spider_Model:    
        
    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False    
    
    # 将所有的段子都扣出来，添加到列表中并且返回列表    
    def GetPage(self,page):    
        myUrl = "http://m.qiushibaike.com/hot/page/" + page    
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrl, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()    
        #encode的作用是将unicode编码转换成其他编码的字符串    
        #decode的作用是将其他编码的字符串转换成unicode编码    
        unicodePage = myPage.decode("utf-8")    
    
        # 找出所有class="content"的div标记    
        #re.S是任意匹配模式，也就是.可以匹配换行符    
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)    
        items = []    
        for item in myItems:    
            # item 中第一个是div的标题，也就是时间    
            # item 中第二个是div的内容，也就是内容    
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])    
        return items    
    
    # 用于加载新的段子    
    def LoadPage(self):    
        # 如果用户未输入quit则一直运行    
        while self.enable:    
            # 如果pages数组中的内容小于2个    
            if len(self.pages) < 2:    
                try:    
                    # 获取新的页面中的段子们    
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except:    
                    print '无法链接糗事百科！'    
            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):    
        for items in nowPage:    
            print u'第%d页' % page , items[0]  , items[1]    
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break    
            
    def Start(self):    
        self.enable = True    
        page = self.page    
    
        print u'正在加载中请稍候......'    
            
        # 新建一个线程在后台加载段子并存储    
        thread.start_new_thread(self.LoadPage,())    
            
        #----------- 加载处理糗事百科 -----------    
        while self.enable:    
            # 如果self的page数组中存有元素    
            if self.pages:    
                nowPage = self.pages[0]    
                del self.pages[0]    
                self.ShowPage(nowPage,page)    
                page += 1    
    
    
#----------- 程序的入口处 -----------    
print u"""  
---------------------------------------  
   程序：糗百爬虫  
   版本：0.3  
   作者：why  
   日期：2014-06-03  
   语言：Python 2.7  
   操作：输入quit退出阅读糗事百科  
   功能：按下回车依次浏览今日的糗百热点  
---------------------------------------  
"""  
    
    
print u'请按下回车浏览今日的糗百内容：'    
raw_input(' ')    
myModel = Spider_Model()    
myModel.Start()



















































































































































