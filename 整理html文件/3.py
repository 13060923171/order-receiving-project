import re

def read():
    with open("url.text","r",encoding='utf8')as f:
        content = f.read()
        file_names = re.compile("&Row=(.*?)&Col", re.I | re.S)
        file_name = file_names.findall(content)
        for i in file_name:
            fine = str(str(5402070) +"_" + str(i)+ "_"+ str(3))
            print(fine)
            write_file(fine)

def write_file(file):
    with open('file.text',"a+",encoding='utf8')as f:
        f.write(file)
        f.write("\n")

if __name__ == '__main__':
    read()