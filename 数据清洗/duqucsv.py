# import csv
# strr = "旅游管理"
# count = 0
# with open("shuju.csv","r",encoding='utf-8')as fp:
#     for line in fp:
#         if strr in line:
#             with open("旅游管理.txt","a+",encoding="utf8")as f:
#                 f.write(line)
#                 print(line)

# coding=utf-8
import re

s='1中文中文：123456aa哈哈哈bbcc'
print(re.match(u"[\u4e00-\u9fa5]+",s))            # None. 只从字符串的开始匹配，没有匹配上返回None,否则返回matchobject

pat='中文'
print(re.search(pat,s).group())                   # matchobject. 对整个字符串进行匹配，，没有匹配上返回None,否则返回matchobject

newpat='这里是中文内容'
news=re.sub(pat,newpat,s)                       # 正则部分替换，将s中的所有符合pat的全部替换为newpat，newpat也可以是函数
print(news)









