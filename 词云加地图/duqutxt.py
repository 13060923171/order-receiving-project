import re

def clearBlankLine():
    file1 = open('瑞金医院（微博）.txt', 'r',encoding="utf-8") # 要去掉空行的文件
    file2 = open('瑞金医院(微博).txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            # dierchi = re.compile("'@(.*?)'",re.S|re.I)
            # result = dierchi.findall(line)
            # print(result)
            # diyichi = re.compile("\['(.*?)'", re.S | re.I)
            # result = diyichi.findall(line)
            # print(result)
            if line == '\n':
                line = line.strip("\n")

            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
