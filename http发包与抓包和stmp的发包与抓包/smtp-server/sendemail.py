# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import xlrd
import sys


def send_mail(receiver):
    host_server = 'smtp.qq.com'  # QQ邮箱的SMTP服务器
    sender_qq = '960751327'  # 发件人的QQ号码
    pwd = 'fdrrjmiqqnaubdcj'  # QQ邮箱的授权码
    sender_qq_mail = '960751327@qq.com'  # 发件人邮箱地址

    data = xlrd.open_workbook('filename.xlsx')  # 打开文件
    table = data.sheets()[0]
    content = []
    content = table.row_values(0)
    mail_content = str(content[0]) + ' ' + str(content[1]) + ' ' + str(content[2]) + ' ' + str(content[3])  # 邮件正文内容
    mail_title = '测试文件'  # 设置邮件标题

    smtp = SMTP_SSL(host_server)  # SSL 登录
    smtp.set_debuglevel(0)  # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.ehlo(host_server)  # 连接服务器
    smtp.login(sender_qq, pwd)  # 邮箱登录

    msg = MIMEText(mail_content, "plain", 'utf-8')  # 填写正文内容
    msg["Subject"] = Header(mail_title, 'utf-8')  # 填写邮件标题
    msg["From"] = sender_qq_mail  # 发送者邮箱地址
    msg["To"] = receiver  # 接收者邮件地址

    try:
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())  # 发送邮件函数
        smtp.quit()  # 发送邮件结束
        print("Successfully Send！")  # 输出成功标志
    except:
        print("The sever is busy,please continue later.")


if __name__ == "__main__":
    try:
        receiver = sys.argv[1]
    except:
        receiver = '313281592@qq.com'  # 收件人邮箱地址
    send_mail(receiver)  # 调用函数，发送邮件

    #这个邮箱就会收到我发送邮件的内容