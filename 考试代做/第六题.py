#第7题
num = 0
a = input("请输入一串字符: ")
for k in a:
    if k.isdigit():
        num += 1
print('数字的个数是:', num)

