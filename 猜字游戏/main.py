#coding=utf-8

#猜字游戏

#导入随机数
import random


#判断数的大小与答案的大小
def guess_judge(num):
    #写一个循环函数
    while(True):
        #计分器
        count =0
        print('请注意你只要10次机会，超过5次没有成功既失败')
        #循环十次，超过10次就意味着失败
        for i in range(1,11):
            #调用函数
            guess_judge_num = get_input_num()
            #判断函数
            if (guess_judge_num == num):
                print("太棒了，答对了")
                count +=1
                print("你当前的得分{}".format(count))
                if count ==3:
                    print("恭喜你闯关成功")
                    break
            elif (guess_judge_num > num):
                print("比答案大，再猜")
                print('请注意你还有{}机会'.format(10-int(i)))
            else:
                print("比答案小，再猜")
                print('请注意你还有{}机会'.format(10-int(i)))


#获取输入的数字
def get_input_num():
    while (True):
        a = input("请输入一个0到10的数：")
        #防错机制，防止输入错误函数直接终止程序
        try:
            guess_judge_num = int(a)
        except:
            print("输入不合法，请重新输入")
            continue
            #设置输入值的大小，可以根据个人喜爱来改
        if (guess_judge_num <0 or guess_judge_num >10):
            print("请重新输入一个0到10的数")
            continue
        else:
            break
    return guess_judge_num


#开始或者退出游戏
print("猜数游戏开始啦")
while (True):
    #答案，随机数字大小
    num = random.randint(0, 10)
    guess_judge(num)
    str = input("请输入R继续下一轮游戏，输入其他退出:")
    if(str == "R"):
        print("新一轮游戏开始，请准备")
    else:
        print("游戏退出")
        break
