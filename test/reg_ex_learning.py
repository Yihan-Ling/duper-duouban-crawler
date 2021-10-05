# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

pat = re.compile("AA") # 此处的AA是正则表达式，用来去验证其他的字符串
# m = pat.search("ABC") # 此处是被校验的内容
m = pat.search("AABBCAA") # search the first one
print(m)

# 没有模式对象（pat)
m = re.search("asd","Aasd") #前面的是pattern，后面的是被校验的对象

# findall
m = re.findall("[A-Z]+", "AsoAiodjoDBIaDSANDo")
print(m)

# sub
m = re.sub("a", "A", "acsdadas") #第一个是pattern，用第二个来替换，第三个是对象
print(m)

# 在比较对象字符串的前面加上'r'，这样对象字符串就不会被转义了
a = r"\ajdskna.ad*+\'."
print(a)