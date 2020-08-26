#先初始化n的值为0
n = 0
#用input函数来赋予t的值为变量，最后用eval输出数值
t = eval(input("请输入一个正整数预计值:"))
#写一个无线循环判断语句,True表示为真，这样可以一直重复循环
while True:
    ##用input函数来赋予s的值为变量，最后用eval输出数值
    s = eval(input("请输入一个0-9之间整数:"))
    #每当执行一次n加一
    n +=1
    #判断语句，如果s的值大于t的值，那么用print函数格式化输出文字
    if s>t:
        print("遗憾，太大了")
    # 判断语句，如果s的值小于t的值，那么用print函数格式化输出文字
    elif s<t:
        print("遗憾，太小了")
    #最后，用format函数来赋予Print语句中需要变量的值，计算最终结果，并且跳出循环
    else:
        print("预计{}次,你猜中了！".format(n))
        break