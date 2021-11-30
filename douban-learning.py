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
    output_file_path = "douban_out.xls"
    save_data(data_list, output_file_path)

    #testing


# 全局变量
findLink = re.compile(r'<a href="(.*?)">')     #影片详情连接的正则表达式
findImage = re.compile(r'<img.*src="(.*?)"', re.S)  #re.S忽律换行符
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')


# 爬取网页
def crawl(url):
    datalist = []

    #爬取
    html = ""
    html_out = open("base_url.html", "wt")
    html_out.write(html)
    html_out.close()
    print("Crawling:")
    for i in range(10):
        html += askURL(url+str(25*i))
        print(str((i+1)*10) + "%")

    # 解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="item"):     #find_all()查找符合要求的字符串，形成列表
        data = []   #保存一部电影的所有信息
        item = str(item)

        link = re.findall(findLink, item)[0]     #正则表达式
        data.append(link)

        imgSrc = re.findall(findImage, item)[0]
        data.append(imgSrc)

        title = re.findall(findTitle, item)     #片名有中文和外文
        if(len(title) == 2):
            ctitle = title[0]
            data.append(ctitle)
            ftitle = title[1].replace("/", "")
            data.append(ftitle)
        else:
            data.append(title[0])
            data.append(" ")    #外国名留空

        rating = re.findall(findRating, item)[0]
        data.append(rating)

        inq = re.findall(findInq,item)
        if(len(inq) != 0):
            data.append(inq)
        else:
            data.append(" ")

        datalist.append(data)
    print(datalist)
    return datalist


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


    html_out = open("base_url.html", "at")
    html_out.write(html)
    html_out.close()

    return html



# 保存数据
def save_data(datalist, save_path):
    print("Saving to: "+ save_path)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影_Top250", cell_overwrite_ok=True)
    sheet.write(0, 0, "helloo")
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "影片评分", "概况")
    for i in range(len(col)):
        sheet.write(0,i,col[i])
    for i in range(250):
        if((i/250*100)%5==0):
            print(str((i/250*100))+"%")
        data = datalist[i]
        for j in range(len(col)):
            sheet.write(i+1, j, data[j])
    book.save(save_path)
    print("Saved")
    return None




if __name__ == "__main__":
    main()
