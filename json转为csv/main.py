import json
import pandas as pd

with open('lagou.json','r',encoding='utf-8')as f:
    content = json.load(f)

list_name = []
list_pay = []
list_site = []
list_company = []
list_welfare = []
list_function = []
for c in content:

    name = c['岗位名称']

    name = name.split('-')[0].replace("（南京）","")
    list_name.append(name)
    pay = c['薪资']
    pay = str(pay)
    list_pay.append(pay)
    site = c['工作地点']
    list_site.append(site)
    company = c['公司名称']
    list_company.append(company)
    welfare = c['职位福利'].replace('**','')

    list_welfare.append(welfare)
    requested = c['任职要求']

    requested = c['任职要求'].replace('<br>','').replace('\n','').replace('<br/>','').replace('<p>','').replace('【岗位职责】','岗位职能：').replace('岗位职责：','岗位职能：') \
        .replace('工作职责:：','岗位职能：').replace('工作职责:','岗位职能：').replace('职位描述：','岗位职能：').replace('岗位要求：','岗位职能：') \
        .replace('职责：','岗位职能：').replace('工作岗位职能：','岗位职能：').replace('岗位亮点：','岗位职能：').replace('工作内容：','岗位职能：').replace('备注：','岗位职能：')
    requested = str(requested).split("岗位职能：")[1].strip(' ').replace('</p>','').replace('岗位说明：','')
    #机械压缩
    filelist2 = []
    temp1 = requested.strip('\n')
    temp2 = temp1.lstrip('\ufeff')
    temp3 = temp2.strip('\r')
    char_list = list(temp3)  # 把字符串转化列表自动按单个字符分词了
    list1 = []
    list1.append(char_list[0])
    list2 = ['']
    # 记录要删除的索引
    del1 = []
    i = 0
    while (i < len(char_list)):
        i = i + 1
        # 这里是对后面没有词汇的时候对列表1和列表2判断一次重复
        if i == len(char_list):
            if list1 == list2:
                m = len(list2)
                for x in range(i - m, i):
                    del1.append(x)
        else:
            if char_list[i] == list1[0] and list2 == ['']:
                list2[0] = char_list[i]  # 这里初始化用append会让lisr2初始化为['','**']
            elif char_list[i] != list1[0] and list2 == ['']:
                list1.append(char_list[i])

            # 触发判断
            elif char_list[i] != list1[0] and list2 != ['']:
                if list1 == list2 and len(list2) >= 2:
                    m = len(list2)
                    # 删除列表2里的内容，列表1本来的内容不用再去判断重复了
                    for x in range(i - m, i):
                        del1.append(x)
                    list1 = ['']
                    list2 = ['']
                    list1[0] = char_list[i]
                else:
                    list2.append(char_list[i])

            # 触发判断
            elif char_list[i] == list1[0] and list2 != ['']:
                if list1 == list2:
                    m = len(list2)
                    # 删除列表2里的内容，列表1需要再去和后面的词汇继续判断重复
                    for x in range(i - m, i):
                        del1.append(x)
                    list2 = ['']
                    list2[0] = char_list[i]
                else:
                    # 逻辑对书本上进行了修改，书上是清空列表1和2，就是保留现在列表1和2内容不做删除，这里只保留1，列表2内容还需要做对比
                    list1 = list2
                    list2 = ['']
                    list2[0] = char_list[i]

    a = sorted(del1)  # 从数字更大的索引删起，这样就不用考虑元素删除后索引的变化问题
    t = len(a) - 1
    while (t >= 0):
        del char_list[a[t]]
        t = t - 1
    str1 = ''.join(char_list)
    str2 = str1.strip()
    list_function.append(str2)


def get_csv():
    df = pd.DataFrame()
    df['公司名称'] = list_company
    df['岗位名称'] = list_name
    df['工资报酬'] = list_pay
    df['工作地点'] = list_site
    df['职位福利'] = list_welfare
    df['岗位职能'] = list_function
    df.to_csv('拉钩网数据分析.csv',mode='w',encoding='gbk')

def qinxi_csv():
    df = pd.read_csv('拉钩网数据分析.csv',encoding='gbk')
    # 查看数据集大小
    print(df.shape)
    #查看数据集是否有缺少
    print(df.isnull())


if __name__ == '__main__':
    get_csv()
    qinxi_csv()


