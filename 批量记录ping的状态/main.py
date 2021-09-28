import subprocess
import re
import pandas as pd
from tqdm import tqdm
import time



def read_excel():
    df = pd.read_excel("机构地址对应.xlsx").loc[:,['机构名称','主地址','备地址']]
    list_name = [str(n) for n in df['机构名称']]
    list_ip1 = [str(ip) for ip in df['主地址']]
    list_ip2 = [str(ip) for ip in df['备地址']]

    while True:
        print('ping主地址:')
        ping1(list_name,list_ip1)
        print('ping备地址:')
        ping2(list_name,list_ip2)
    # t1 = th.Thread(target=ping1,args=(list_name,list_ip1,))
    # t2 = th.Thread(target=ping2,args=(list_name,list_ip2,))
    # #开始线程保护
    # t1.setDaemon(True)
    # #开启线程
    # t1.start()
    # t2.setDaemon(True)
    # t2.start()
    # #加一个线程阻塞
    # t1.join()
    # t2.join()


def ping1(list_name,list_ip1):
    for i in tqdm(range(len(list_name))):
        status, result = subprocess.getstatusoutput("ping " + list_ip1[i] + " -n 20")
        print(result)
        # if '请求超时' in result:
        #     df = pd.DataFrame()
        #     df['机构名称'] = [list_name[i]]
        #     df['主地址'] = [list_ip1[i]]
        #     df['问题'] = ['请求超时']
        #     df['时间'] = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())]
        #     df.to_csv('有问题的ip记录.csv', index=None, header=None, mode='a+', encoding='gbk')
        df = pd.DataFrame()
        number = re.compile("(\d+)% 丢失")
        numbers = number.findall(result)
        if int(numbers[0]) >= 10:
            df['机构名称'] = [list_name[i]]
            df['主地址'] = [list_ip1[i]]
            df['丢包率(%)'] = [int(numbers[0])]
            df['时间'] = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())]
            df.to_csv('有问题的ip记录.csv', index=None, header=None, mode='a+', encoding='gbk')


def ping2(list_name,list_ip2):
    for i in tqdm(range(len(list_name))):
        status, result = subprocess.getstatusoutput("ping " + list_ip2[i] + " -n 20")
        # if '请求超时' in result:
        #     df = pd.DataFrame()
        #     df['机构名称'] = [list_name[i]]
        #     df['主地址'] = [list_ip2[i]]
        #     df['问题'] = ['请求超时']
        #     df['时间'] = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())]
        #     df.to_csv('有问题的ip记录.csv', index=None, header=None, mode='a+', encoding='gbk')
        print(result)
        df = pd.DataFrame()
        number = re.compile("(\d+)% 丢失")
        numbers = number.findall(result)
        if int(numbers[0]) >= 10:
            df['机构名称'] = [list_name[i]]
            df['主地址'] = [list_ip2[i]]
            df['丢包率(%)'] = [int(numbers[0])]
            df['时间'] = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())]
            df.to_csv('有问题的ip记录.csv', index=None, header=None, mode='a+', encoding='gbk')


if __name__ == '__main__':
    read_excel()




