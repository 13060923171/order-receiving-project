def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
n = eval(input("请输入一个正整数："))
print(isOdd(n))