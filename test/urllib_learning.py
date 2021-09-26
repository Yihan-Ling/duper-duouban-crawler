import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 获取一个get请求
# response=urllib.request.urlopen("https://www.baidu.com").read().decode('utf-8')
# print(response)

# post request

# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"word"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

# response=urllib.request.urlopen("http://baidu.com",timeout=1)
# print(response.status) # like 404, 418(被发现是爬虫了）
# print(response.getheaders())
# print(response.getheader("Server"))

#想不被发现是爬虫
url = "https://www.douban.com"
headers = {
    #浏览器版本（伪装）
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))