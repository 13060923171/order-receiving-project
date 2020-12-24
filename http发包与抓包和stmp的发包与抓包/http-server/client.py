import requests

#发包
def post_main():
    # headers = {
    #     "Content-Type":"application/json"
    # }
    name = input('请输入文本:')
    number = input('请输入数字:')
    english = input('请输入英文:')
    data = {
        'name': '%s' %name,
        'number': '%s' %number,
        'english':'%s' %english,
    }
    r = requests.post("http://127.0.0.1:5000/",data=data)
    print(r.text)

#抓包
def get_main():
    headers = {
        "Content-Type": "application/json"
    }
    url = 'http://127.0.0.1:5000/'
    html = requests.get(url,headers=headers)
    print(html.text)

if __name__ == '__main__':
    # post_main()
    get_main()
