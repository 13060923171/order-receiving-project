import re

def clearBlankLine():
    lines_seen = set()
    file1 = open('C:\Users\96075\Desktop\医院词云\华西医院\华西医院(贴吧).txt', 'r',encoding="utf-8") # 要去掉空行的文件
    file2 = open('xinwenjian.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            # dierchi = re.compile("'@(.*?)'",re.S|re.I)
            # result = dierchi.findall(line)
            # print(result)
            # diyichi = re.compile("\['(.*?)'", re.S | re.I)
            # result = diyichi.findall(line)
            # print(result)
            #去掉空行
            # if line == '\n':
            line = line.strip("\n")
            if line not in lines_seen:
                file2.write(line+"\n")
                lines_seen.add(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
