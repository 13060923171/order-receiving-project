import jieba
import pandas as pd
import numpy
import csv
def read_txt_file():

    with open("整理文件.txt", 'r', encoding='utf8') as f:
        return f.read()

def write_txt_file(txt):
    with open("要添加的词.txt", 'w', encoding='utf8') as f:
        f.write(txt)


data = {}
content = read_txt_file()
segment = jieba.lcut(content)
words_df=pd.DataFrame({'segment':segment})
stopwords=pd.read_csv("stopword.txt",index_col=False,quoting=3,sep=" ",names=['stopword'],encoding='utf-8')
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
words_stst = words_df.groupby('segment').agg(计数=pd.NamedAgg(column='segment', aggfunc='size')).reset_index().sort_values(
    by='计数', ascending=False)
print(words_df)
# print(words_stst["segment"])
# write_txt_file(words_stst["segment"])
# df = pd.DataFrame()
# df["数据"] = words_stst["segment"]
# try:
#     df.to_csv("内容.csv", mode="a+", header=None, index=None, encoding="gbk")
#     print("写入成功")
# except:
#     print("当页数据写入失败")
# print(words_df)

# sw_path='stopword.txt'
# stopws=[]
# with open(sw_path,'r',encoding='utf-8') as f:
#     for line in f.readlines():
#         line=line.strip('\n')
#         print(line)
#         if(line==''):
# #             continue
# #         else:
# #             stopws.append(line)
# print(stopws)
# print(len(stopws))
# with open(sw_path,'w',encoding='utf-8') as f:
#     f.write('\n'.join(stopws))