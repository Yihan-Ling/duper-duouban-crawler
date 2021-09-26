# 文档解析

# BS4 将HTML文档转化称一个树形结构，每个节点都是python对象，所有的对象可以分成4种

# Tag
# NavigableString
# BeautifulSoup
# Comment

import bs4
import re

file =  open("./very_random_html.html", "rb")
html = file.read()
bs = bs4.BeautifulSoup(html, "html.parser")

# 1. Tag，只能拿到第一个
print(bs.title)
print(bs.a)
print(type(bs.a))

# 2. NavigableString，标签里的内容
print(bs.title.string)
print(type(bs.title.string))
print(bs.a.attrs) # 属性

# 3. BeautifulSoup，表示整个文档
print(type(bs))

# 4. Comment，特殊的NavigableString，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))

# -----------------------------------------------------------

# 文档的搜索

# (1) find_all

# 字符串过滤；会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
print(t_list)

# 正则表达式搜索：使用search()方法来匹配内容
t_list = bs.find_all(re.compile("a"))
print(t_list) # 只要含有'a'的就行

# 函数来搜素，根据函数的要求来搜索
def name_is_exsits(tag):
    return tag.has_attr("name")
t_list=bs.find_all(name_is_exsits)


# (2) kwargs 参数
t_list = bs.find_all(id="head")
t_list = bs.find_all(class_="true") #有class的tag

# (3) text 参数
t_list = bs.find_all(text=["Gardening Service", "Home Page"])
t_list = bs. find_all(text = re.compile("\d")) #含有数字的

#（4）limit 参数
t_list = bs.find_all("a",limit=3) #只要3个


# css选择器
t_list = bs.select('title') #通过标签来查找
t_list = bs.select(".TitleBackground") #通过class名来搜索
t_list = bs.select("#head") #通过id名来搜索
t_list = bs.select("a[class='TitleBackground']") #通过属性来查找
t_list = bs.select("head > title")
t_list = bs.select(".lPage ~ .hPage")
print(t_list[0].get_text())


# 文档的遍历

print(bs.head.contents)
print(bs.head.contents[3])