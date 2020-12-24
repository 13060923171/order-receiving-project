with open('Text.txt','r',encoding='utf-8')as f:
    content = f.readlines()
    content_list = []
    for c in content:
        if '{한어}' in c or '{원문}' in c or '{전사}' in c:
            content_list.append(c)
cn_list = []
kr_list = []

for c_l in range(len(content_list)):
    if '{한어}' in content_list[c_l] and '{원문}' in content_list[c_l+1] and '{전사}' in content_list[c_l+2]:
        cn_list.append(content_list[c_l])
        kr_list.append(content_list[c_l+1])

for c in cn_list:
    c = c.replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').\
        replace('7','').replace('8','').replace('9','').replace('0','').replace('1','').replace('{한어}','')
    c = c.strip(' ').strip('\n').replace('	','')
    with open('Text_cn.txt','a+',encoding='utf-8')as f:
        f.write(c+'\n')

for c in kr_list:
    c = c.replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').\
        replace('7','').replace('8','').replace('9','').replace('0','').replace('1','').replace('{원문}','')
    c = c.strip(' ').strip('\n').replace('	','')
    with open('Text_kr.txt','a+',encoding='utf-8')as f:
        f.write(c+'\n')


