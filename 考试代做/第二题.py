#一个无限循环 True表示为真
while True:
    #用input函数赋予TempStr变量
    TempStr = input("请输入带有符号的温度值:")
    #判断语句，如果这个值为空值，那么用break函数退出循环
    if TempStr == "":
        print("你想退出系统")
        break
    #如果判断tempstr最后一个字符在f与F之间那么执行下面的C的语句，并且计算结果
    elif TempStr[-1] in ["F","f"]:
        #开始计算tempstr从开始到倒数第二位数字先通过eval转化为数字，然后再先减32，最后得出的结果除以1.8
        C = (eval(TempStr[0:-1]) -32)/1.8
        #用print函数格式化输出，并且保留2位有效数字
        print("转换后的温度是{:.2f}C".format(C))
        # 如果判断tempstr最后一个字符在C与c之间那么执行下面的f的语句，并且计算结果
    elif TempStr[-1] in ["C","c"]:
        # 开始计算tempstr从开始到倒数第二位数字先通过eval转化为数字，然后先乘以1.8得出的结果再加上32
        F = 1.8*eval(TempStr[0:-1])+32
        # 用print函数格式化输出，并且保留2位有效数字
        print("转换后的温度是{:.2f}f".format(F))
    else:
        print("输入的格式有误")