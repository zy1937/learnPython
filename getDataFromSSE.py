#-*- coding:utf-8 -*-
import urllib3
import urllib


url = 'http://www.sse.com.cn/market/stockdata/dividends/dividend/'
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

f = urllib.urlopen(url)

htmlData = f.read()




print("-----begin to get -------")
print(htmlData)

