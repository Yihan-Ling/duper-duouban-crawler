#-*- codeing = utf-8 -*-
import sys
import urllib.request, urllib.error #指定URL，获取网页数据
from bs4 import BeautifulSoup   #网页解析，获取数据
import re   #正则表达式，文字匹配
import xlwt #excel操作
import sqlite3  #进行SQLite数据库操作
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    base_url = "https://movie.douban.com/top250?start="
    #1.爬取网页
    data_list = crawl(base_url)

    #2.保存数据
    # output_file_path="douban_out.xls"
    output_file_path = ".\\douban_out.xls"
    save_data(output_file_path)

    #testing


# 爬取网页
def crawl(url):
    data = []

    #爬取
    for i in range(10):
        html = askURL(url+str(25*i))
        # 解析数据



    return data


#得到指定一个网页的信息
def askURL(url):

    # 伪装一下下
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
    }

    req = urllib.request.Request(url=url, headers=headers)
    html = ""

    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    html_out = open("base_url.html", "w")
    html_out.write(html)
    html_out.close()

    return html



# 保存数据
def save_data(save_path):

    return None




if __name__ == "__main__":
    main()