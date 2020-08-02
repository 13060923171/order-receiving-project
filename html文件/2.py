import re

def read(wenjian):
    with open('{}'.format(wenjian), 'r')as f:
        content = f.read()
        hrefs = re.compile('<a hre(.*?)</a>', re.S | re.I)
        href = hrefs.findall(content)
        count = 0
        for h in href:
            write(h)
            count +=1
            print(count)

def write(h):
    with open('paquneirong.text',"a+",encoding='utf8')as f:
        f.write(h)
        f.write(",\n")
        print("success")

if __name__ == '__main__':
    read("Hosp_TVcr_18_19_FL_KY_yearly_5402070.html")