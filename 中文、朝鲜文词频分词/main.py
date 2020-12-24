import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import pandas as pd
from konlpy.tag import Kkma
from konlpy.utils import pprint
import matplotlib as mpl

mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
def write():
    with open('Text.txt', 'r', encoding='utf-8')as f:
        content = f.readlines()
        content_list = []
        for c in content:
            if '{한어}' in c or '{원문}' in c or '{전사}' in c:
                content_list.append(c)
    cn_list = []
    kr_list = []

    for c_l in range(len(content_list)):
        if '{한어}' in content_list[c_l] and '{원문}' in content_list[c_l + 1] and '{전사}' in content_list[c_l + 2]:
            cn_list.append(content_list[c_l])
            kr_list.append(content_list[c_l + 1])

    for c in cn_list:
        c = c.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', ''). \
            replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('1', '').replace('{한어}', '')
        c = c.strip(' ').strip('\n').replace('	', '')
        with open('Text_cn.txt', 'a+', encoding='utf-8')as f:
            f.write(c + '\n')

    for c in kr_list:
        c = c.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', ''). \
            replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('1', '').replace('{원문}', '')
        c = c.strip(' ').strip('\n').replace('	', '')
        with open('Text_kr.txt', 'a+', encoding='utf-8')as f:
            f.write(c + '\n')

def read():
    #汉语
    with open('Text_cn.txt','r',encoding='utf-8')as f:
        content = f.readlines()
    n_list = []
    f_pos_list = []
    for c in content:
        c = str(c)
        c = c.strip("\n")
        #统计每个句子中两种语言的词数量
        seg_list = jieba.cut("{}".format(c))
        word_list = "/".join(seg_list)
        print(word_list)
        print(word_list.count('/'))
        words = pseg.cut("{}".format(c))
        words_list = []
        flag_list = []
        #每个句子的汉语名词
        for word, flag in words:
            #汉语词性统计
            flag_list.append(flag)
            if flag == 'n':
                words_list.append(word)
        f_pos_list.append(flag_list)
        n_list.append(words_list)

    #朝鲜
    with open('Text_kr.txt','r',encoding='utf-8')as f:
        content1 = f.readlines()
    kkma = Kkma()
    k_n_list = []
    k_pos_list = []
    for c1 in content1:
        c1 = str(c1)
        c1 = c1.strip("\n")
        #统计每个句子中两种语言的词数量
        seg_list1 = kkma.morphs(u'{}'.format(c1))
        pprint(seg_list1)
        print(len(seg_list1))
        #每个句子的朝鲜语名词
        seg_list2 = kkma.nouns(u'{}'.format(c1))
        k_n_list.append(seg_list2)
        #朝鲜语词性统计
        seg_list3 = kkma.pos(u'{}'.format(c1))
        for s in range(len(seg_list3)):
            s = seg_list3[s][1]
            k_pos_list.append(s)

    download(n_list,k_n_list)
    mat_plt1(f_pos_list)
    mat_plt2(k_pos_list)

#输出到Excel表
def download(n_list,k_n_list):
    df = pd.DataFrame()
    df['中文名词'] = n_list
    df['朝鲜名词'] = k_n_list
    df.to_excel('名词列表.xls')
    mat_plt()

#汉语和朝鲜语前20项名词统计
def mat_plt():
    n_count_dict = {}
    k_count_dict = {}
    list1 = []
    list2 = []
    data_1 = []
    labels_1 = []
    data_2 = []
    labels_2 = []
    df = pd.read_excel('名词列表.xls').loc[:,['中文名词', '朝鲜名词']]
    #汉语前20名词统计
    for n in df['中文名词']:
        n = n.replace("'",'').replace('[','').replace(']','')
        list1.append(n)
    word = ','.join(list1)
    d = word.split(',')
    for d_l in d:
        n_count_dict[d_l] = n_count_dict.get(d_l,0)+1
    ls = list(n_count_dict.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(1,21):
        a = ls[i][0].strip(' ')
        labels_1.append(a)
        b = ls[i][1]
        data_1.append(b)
    plt.bar(range(len(data_1)), data_1, tick_label=labels_1)
    plt.savefig('test1.jpg')
    plt.show()

    #朝鲜前20项名词统计
    for n in df['朝鲜名词']:
        n = n.replace("'",'').replace('[','').replace(']','')
        list2.append(n)
    word1 = ','.join(list2)
    d1 = word1.split(',')
    for d_l in d1:
        k_count_dict[d_l] = k_count_dict.get(d_l,0)+1
    ls1 = list(k_count_dict.items())
    ls1.sort(key=lambda x: x[1], reverse=True)
    for i in range(1,21):
        c = ls1[i][0].strip(' ')
        labels_2.append(c)
        d = ls1[i][1]
        data_2.append(d)
    plt.bar(range(len(data_2)), data_2, tick_label=labels_2)
    plt.savefig('test2.jpg')
    plt.show()

#汉语词性统计
def mat_plt1(flag_list):
    labels_1 = []
    data_1 = []
    d_1 = {}
    for f in flag_list:
        for i in f:
            d_1[i] = d_1.get(i, 0) + 1
    ls = list(d_1.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(ls)):
        a = ls[i][0]
        labels_1.append(a)
        b = ls[i][1]
        data_1.append(b)
    plt.bar(range(len(data_1)), data_1, tick_label=labels_1)
    plt.savefig('test3.jpg')
    plt.show()

#朝鲜语词性统计
def mat_plt2(k_pos_list):
    labels_1 = []
    data_1 = []
    d_1 = {}
    for f in k_pos_list:
        d_1[f] = d_1.get(f, 0) + 1
    ls = list(d_1.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(ls)):
        a = ls[i][0]
        labels_1.append(a)
        b = ls[i][1]
        data_1.append(b)
    plt.bar(range(len(data_1)), data_1, tick_label=labels_1)
    plt.savefig('test4.jpg')
    plt.show()


if __name__ == '__main__':
    #先调用写函数，生成文本
    # write()
    #再调用读函数，生成图片以及Excel
    read()