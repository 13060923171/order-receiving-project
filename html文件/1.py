import re

def read():
    with open("paquneirong.text","r",encoding='utf8')as f:
        content = f.read()
        hrefs = re.compile('f="(.*?)"', re.S | re.I)
        href = hrefs.findall(content)
        creatives = re.compile('blank">(.*?),',re.S | re.I)
        creative = creatives.findall(content)
        count = 0
        for i in range(len(href)):
            if creative[i] == " ":
                continue
            else:
                url = href[i].replace("amp;","")
                name = creative[i].replace("&#39;","'").replace("amp;","").strip()
                count +=1
                print(url,name,count)
                write_url(url)
                write_name(name)

def write_url(url):
    with open('url.text',"a+",encoding='utf8')as f:
        f.write(url)
        f.write("\n")


def write_name(name):
    with open('name.text',"a+",encoding='utf8')as f:
        f.write(name)
        f.write("\n")





if __name__ == '__main__':
    read()