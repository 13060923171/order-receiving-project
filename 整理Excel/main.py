import pandas as pd


list = []
with open("id.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list.append(c)
list2 = []
with open("MQB CNS3.0.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list2.append(c)
list3 = []
with open("37W CNS3.0.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list3.append(c)
list4 = []
with open("37W CRS3.0.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list4.append(c)
list5 = []
with open("ICAS.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list5.append(c)
list6 = []
with open("FPK ENTRY.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list6.append(c)
list7 = []
with open("Med_Col.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list7.append(c)
list8 = []
with open("FPK_Basic_Medium.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list8.append(c)
list9 = []
with open("FPK_Basic_8.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list9.append(c)
list10 = []
with open("ilD.txt", "r", encoding="utf8")as f:
    content = f.readlines()
    for c in content:
        c = c.strip("\n")
        list10.append(c)
list11 = []
for i in range(1,2077,1):
    list11.append(i)
def dowload_csv(i):
    # path = '任务表.xlsx'
    data = pd.DataFrame({'shujub':list2,'shujud':list3,'shujuf':list4,'shujuh':list5,
                         'shujuj':list6,'shujul':list7,'shujun':list8,'shujup':list9,'shujur':list10},index=list11,columns=['shujub','shujud','shujuf','shujuh','shujuj','shujul','shujun','shujup','shujur'])

    data['shujub'] = data['shujub'].apply(str)
    data['shujud'] = data['shujud'].apply(str)
    data['shujuf'] = data['shujuf'].apply(str)
    data['shujuh'] = data['shujuh'].apply(str)
    data['shujuj'] = data['shujuj'].apply(str)
    data['shujul'] = data['shujul'].apply(str)
    data['shujun'] = data['shujun'].apply(str)
    data['shujup'] = data['shujup'].apply(str)
    data['shujur'] = data['shujur'].apply(str)
    d1 = data.loc[data[:,"shujub","shujuf"].str.contains(i)]
    d1.loc[:,"shujud"] = i
    d1 = d1.loc[:, ['shujub',"shujud",'shujuf']]
    print(d1)
    # d1.to_csv("MQB CNS3.0.csv", mode="a+", header=None, index=None, encoding="gbk")
    # d2 = data.loc[data['shujud'].str.contains(i)]
    # d2.loc[:, "shujuf"] = i
    # d2 = d2.loc[:, ['shujud', "shujuf"]]
    # print(d2)
    # try:
    #     d2.to_csv("37W CNS3.0.csv", mode="a+", header=None, index=None, encoding="gbk")
    # except:
    #     print("出错")
    # d3 = data.loc[data['shujuf'].str.contains(i)]
    # d3.loc[:, "shujuh"] = i
    # d3 = d3.loc[:, ['shujuf', "shujuh"]]
    # print(d3)
    # d3.to_csv("37W CRS3.0.csv", mode="a+", header=None, index=None, encoding="gbk")
    # d4 = data.loc[data['shujuh'].str.contains(i)]
    # d4.loc[:, "shujuj"] = i
    # d4 = d4.loc[:, ['shujuh', "shujuj"]]
    # print(d4)
    # try:
    #     d4.to_csv("ICAS.csv", mode="a+", header=None, index=None, encoding="gbk")
    # except:
    #     print("出错")
    # d5 = data.loc[data['shujuj'].str.contains(i)]
    # d5.loc[:, "shujul"] = i
    # d5 = d5.loc[:, ['shujuj', "shujul"]]
    # print(d5)
    # d5.to_csv("FPK ENTRY.csv", mode="a+", header=None, index=None, encoding="gbk")
    # d6 = data.loc[data['shujul'].str.contains(i)]
    # d6.loc[:, "shujun"] = i
    # d6 = d6.loc[:, ['shujul', "shujun"]]
    # print(d6)
    # try:
    #     d6.to_csv("Med_Col.csv", mode="a+", header=None, index=None, encoding="gbk")
    # except:
    #     print("出错")
    # d7 = data.loc[data['shujun'].str.contains(i)]
    # d7.loc[:, "shujup"] = i
    # d7 = d7.loc[:, ['shujun', "shujup"]]
    # print(d7)
    # d7.to_csv("FPK_Basic_Medium.csv", mode="a+", header=None, index=None, encoding="gbk")
    # d8 = data.loc[data['shujup'].str.contains(i)]
    # d8.loc[:, "shujur"] = i
    # d8 = d8.loc[:, ['shujup', "shujur"]]
    # print(d8)
    # d8.to_csv("FPK_Basic_8.csv", mode="a+", header=None, index=None, encoding="gbk")
    d9 = data.loc[data['shujur'].str.contains(i)]
    d9.loc[:, "shujud"] = i
    d9 = d9.loc[:, ['shujur', "shujud"]]
    print(d9)
    d9.to_csv("ilD.csv", mode="a+", header=None, index=None, encoding="gbk")

if __name__ == '__main__':
    # for i in list:
    #     dowload_csv(i)
    dowload_csv("a089")