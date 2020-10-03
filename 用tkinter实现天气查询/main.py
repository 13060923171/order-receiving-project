import requests
#GUI界面需要调用的库
import tkinter as tk
#用于处理图片的
from PIL import Image,ImageTk


#设置图片的大小，并且调用
def get_image(file_name,width,height):
    #打开图片，并且定义宽与高
    img = Image.open(file_name).resize((width,height))
    #返回处理好的图片
    return ImageTk.PhotoImage(img)
#定义窗口的名称
win = tk.Tk()
#设置窗口title
win.title('天气查询系统')
#设置窗口的大小
win.geometry('500x500')
#设置画布的大小，作用于win这个窗口
canvas = tk.Canvas(win,height=500,width=500)
#导入图片
im_root = get_image('test.jpg',width=500,height=500)
#创建画布的图片
canvas.create_image(250,250,image=im_root)
canvas.pack()
#写一个调用API接口的函数
def spider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    }
    #city的数值从b1输入框调用
    city = b1.get()
    #处理用户输入的时间
    #规定三种格式都可以2018/10/1 2018年10月1日 2018-10-1
    #获取时间文本框的输入
    # date = b2.get()
    # if '/' in date:
    #     tm_list = date.split('/')
    # elif '-' in date:
    #     tm_list = date.split('-')
    # else:
    #     tm_list = re.findall(r'\d+',date)
    # #1-9月 前面加0
    # if int(tm_list[1]) <10:
    #     tm_list[1] = f'0{tm_list[1]}'
    #分析网页发现的规律 构造URL
    #直接访问有该有所有天气信息的页面 提高查询效率，注意一下，因为这里不是会员所以调用次数有限，一天只能调用100次，请各位手下留情
    url = f"http://apis.juhe.cn/simpleWeather/query?city={city}&key=2bd46fa7867fe9598989a6681d4b44a5"
    #返回一个json类型
    html = requests.get(url,headers=headers).json()
    #定位到当前最新日期
    result = html['result']['realtime']
    #输出信息格式化一下
    list = []
    info1 = ['温度：', '湿度：', '天气：', '风度：', '风向：','风力强度:','aqi:']
    for key, values in result.items():
        list.append(result[key])
    #将两个列表联合在一起输出
    datas = [i + j for i,j in zip(info1,list)]
    #最后将datas这个列表打印出来
    info = '\n'.join(datas)
    #先在文本框里面插入最新天气现象
    t.insert('insert','    {}最新天气现象     \n'.format(city))
    #再插入获取到的数据
    t.insert('insert',info)
    #最后将这些全部打印出来
    print(info)

#单行文本
L1 = tk.Label(win,bg='#6A0996',text='城市',font=('SimHei',12))
#位置
L1.place(x=85,y=100)
#单行文本框，可采集键盘输入
b1 = tk.Entry(win,font=('SimHei',12),show=None,width=35)
b1.place(x=140,y=100)
#设置查询按钮，点击调用爬虫函数来实现查询
a = tk.Button(win, bg='#A22B10', text="查询", width=25, height=2, command=spider)
a.place(x=160, y=140)
#设置多行文本框 宽 高 文本框中字体 选中文字时文字的颜色
t = tk.Text(win, width=30, height=9, font=("SimHei", 18), selectforeground='red')  # 显示多行文本
t.place(x=70, y=200)
#进入消息循环
win.mainloop()
