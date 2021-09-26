# 文档解析

# BS4 将HTML文档转化称一个树形结构，每个节点都是python对象，所有的对象可以分成4种

# Tag
# NavigableString
# BeautifulSoup
# Comment

import bs4

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

