import re
import requests
import threadpool
from shujuku import sess,Biao

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Host": "stradegy.kantarmediana.com",
    "Cookie": "ASP.NET_SessionId=z5y32b23gya55w23iihssl1q; __APPVERSION=3ca95b44-f7c5-4704-a222-59a58672e8b7; BIGipServerPRD_HTTP_stradegy_pool=3516180672.20480.0000; __TIMEDIFF=480; TNSMI_DestroyedStateId=; AUTHTOKEN=; ONENTER=",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}


def read():
    with open('Hosp_TVcr_18_19_FL_KY_yearly_5402070.html','r')as f:
        content = f.read()
        hrefs = re.compile('<a href="(.*?)"',re.S|re.I)
        href = hrefs.findall(content)
        urls = []
        for i in range(len(href)):
            url = href[i].replace("amp;","")
            print(url)
            urls.append(([url,],None))
            get_response(url)
        # pool = threadpool.ThreadPool(100)
        # reque = threadpool.makeRequests(get_response, urls)
        # for r in reque:
        #     pool.putRequest(r)
        # pool.wait()
            # # try:
            #     biao = Biao(
            #         Link=url
            #     )
            #     sess.add(biao)
            #     sess.commit()
            #     print('commit')
            # except Exception as e:
            #     print("rollback", e)
            #     sess.rollback()




def get_url(url):
    html = requests.get(url,headers = headers)
    if html.status_code ==200:
        contect = html.text
        years = re.compile('<span id="layout__content__timePeriod">(.*?)</span></td>',re.S|re.I)
        year = years.findall(contect)
        try:
            biao = Biao(
                Year=year
            )
            sess.add(biao)
            sess.commit()
            print('commit')
        except Exception as e:
            print("rollback", e)
            sess.rollback()

def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Host": "stradegy.kantarmediana.com",
        "Cookie": "ASP.NET_SessionId=z5y32b23gya55w23iihssl1q; __APPVERSION=3ca95b44-f7c5-4704-a222-59a58672e8b7; BIGipServerPRD_HTTP_stradegy_pool=3516180672.20480.0000; __TIMEDIFF=480; TNSMI_DestroyedStateId=; AUTHTOKEN=; ONENTER=",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    data = {
        "__LAYOUT": "TNSMI.WBI.Common.Web.Layouts.NewWindowLayout,TNSMI.WBI.Common, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null",
        "__EVENTTARGET": "layout:_content:_list:_ctl0:_creative:_creativePanel",
        "__EVENTARGUMENT": "LOAD"
    }
    html = requests.post(url, headers=headers, data=data)
    content = html.text
    titles = re.compile('Title:(.*?)</span></span>', re.I | re.S)
    title = titles.findall(content)
    products= re.compile('Product:(.*?)<',re.I|re.S)
    product = products.findall(content)
    types = re.compile('<br>:(.*?)</span></span></td>', re.I | re.S)
    type = types.findall(content)
    print(title,product,type)
    try:
        biao = Biao(
            TVcreative=title,
            Brand = product,
            Type = type
        )
        sess.add(biao)
        sess.commit()
        print('commit')
    except Exception as e:
        print("rollback", e)
        sess.rollback()
if __name__ == '__main__':
    read()

