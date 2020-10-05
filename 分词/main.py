import pandas as pd
import jieba

data = pd.read_excel('调查问卷主观问题回答(1).xls')
data90 = data['第90题']
data91 = data['第91题']
data92 = data['第92题']
data93 = data['第93题']
data94 = data['第94题']
data95 = data['第95题']
data96 = data['第96题']
data97 = data['第97题']
data98 = data['第98题']
data99 = data['第99题']
data100 = data['第100题']
data101 = data['第101题']

zidian = data90+data91+data93+data94+data95+data96+data97+data98+data99+data100+data101
# for i in zidian:
#     with open('文本.txt',"a+",encoding='utf-8')as f:
#         f.write(str(i)+'\n')
with open('文本.txt','r',encoding='utf-8')as f:
    content = f.read()
excludes = {'nan'}
words = jieba.cut(content,cut_all=True)
counts = {}
for word in words:
    if len(word) ==1 or word == 'nan':
        continue
    else:
        counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
list1 = []
list2 = []
for i in range(len(items)):
    word,count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
    list1.append(word)
    list2.append(count)
df = pd.DataFrame()
df['词语'] = list1
df['频率'] = list2
try:
    df.to_csv("词语频次.csv", mode="a+", header=None, index=None, encoding="utf-8")
    print("写入成功")
except:
    print("当页数据写入失败")