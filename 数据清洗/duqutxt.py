import re
from tqdm import tqdm
list= []
with open("stopword.txt","r",encoding="utf-8")as f:
    for line in f.readlines():
        line = line.strip('\n')
        list.append(line)
def clearBlankLine(i):
    file1 = open('整理文件.txt', 'r',encoding="utf-8")
    file2 = open('整理好的内容.txt', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            line = line.replace(i,"")
            file2.write(line)
            # line = line.replace("英语","").replace("薪聘","").replace("高","").replace("顺德区","").replace("旅游销售\\\\","") \
            #     .replace("去哪儿", "").replace("网","").replace("旅游在线","").replace("客服","").replace("门店","").replace("全球","") \
            #     .replace("包住宿", "").replace("月薪","").replace("携程","").replace("8500","").replace("8K","").replace("旅游产品专员\\\\","") \
            #     .replace("急聘", "").replace("康养","").replace("7000+","").replace("酒店","").replace("薪","").replace("招聘","") \
            #     .replace("同业", "").replace("无经验","").replace("+","").replace("轻松","").replace("工作","").replace("旅行海外","") \
            #     .replace("同业", "").replace("无经验", "").replace("+", "").replace("轻松", "").replace("工作", "").replace(
            #     "旅行海外", "") \
            #     .replace("泰语", "").replace("客服", "").replace("主管", "").replace("门店", "").replace("扶贫", "").replace(
            #     "旅行海外", "") \
            #     .replace("高铁", "").replace("资深", "").replace("，", "").replace("轻松", "").replace("工作", "").replace(
            #     "旅行海外", "") \
            #     .replace("同业", "").replace("无经验", "").replace("+", "").replace("轻松", "").replace("工作", "").replace(
            #     "旅行海外", "") \
                # line = line.replace("0.1","1").replace("0.2","2").replace("0.3","3").replace("0.4","4") \
            #     .replace("0.5", "5").replace("0.6","6").replace("0.7","7").replace("0.8","8").replace("0.9","9")
            # line = line.replace("'","").replace("\\xa0","").replace("***","").\
            #     replace(",","").replace("★","").replace("◆","").replace("（","").\
            #     replace("）","").replace("【","").replace("】","").replace("\\n","").\
            #     replace('[','').replace(']',"").replace("...","").replace('\\\\',"/")
            # line = line.strip(" ")
            # line = line.replace("1.20k","12k").replace("1.40k","14k").replace\
            #     ("1.50k","15k").replace("1.30k","13k").replace("10-150k/年","10-15k").\
            #     replace("8-150k/年","8-15k").replace("15-200k/年","15-20k").\
            #     replace("200元/天","6k").replace("1.5千以下","1.5k").\
            #     replace("300元/天","9k").replace("100元/天","3k").replace("150元/天","4.5k").\
            #     replace("7-120k/年","7-12k").replace("30-400k/年","3-4k").replace("20-300k/年","2-30k").replace("8-100k/年","8-10k").replace("8-200k/年","8-20k")
            # line = line.replace("1-","1k-").replace("2-","2k-").replace("3-","3k-").\
            #     replace("6-","6k-").replace("5-","5k-").replace("4-","4k-").replace("7-","7k-").replace("8-","8k-").replace("9-","9k-").replace("0-","0k-")
            # line = line.replace("A轮","民营公司").replace("B轮","民营公司").\
            #     replace("D轮及以上","国有企业").replace("天使轮","民营公司").\
            #     replace("C轮","民营公司").replace("未融资","民营公司").replace("不需要融资","合资")
            # line = line[0:2]
            # line = line.replace("哈尔","哈尔滨").replace("大兴","大兴安岭").replace("防城","防城港").replace("呼和","呼和浩特").\
            #     replace("呼伦","呼伦贝尔").replace("葫芦","葫芦岛").replace("红河","红河州").replace("景德","景德镇").replace("克拉","克拉玛依")\
            #     .replace("喀什","喀什地区").replace("马鞍","马鞍山").replace("牡丹","牡丹江").replace("秦皇","秦皇岛").replace("齐齐","齐齐哈尔").\
            #     replace("七台","七台河").replace("黔东","黔东南").replace("石家","石家庄").replace("神农","神农架").replace("双鸭","双鸭山")\
            #     .replace("石河","石河子").replace("图木","图木舒克").replace("五指","五指山").replace("乌鲁","乌鲁木齐").replace("西双","西双版纳")\
            #     .replace("张家","张家界").replace("驻马","驻马店")
            # line = line.replace("0k","0").replace("1k","1").replace("2k","2").replace("3k","3").replace("4k","4")\
            #     .replace("5k","5").replace("6k","6").replace("7k","7").replace("8k","8").replace("9k","9")
            # line = line.replace("1-1","1-1千/月").replace("1-2","1-2千/月").replace("1-3","-3千/月").replace("1-4","1-4千/月").\
            #     replace("1-5","1-5千/月").replace("1-6","1-6千/月").replace("1-7","1-7千/月").replace("1-8","1-8千/月").\
            #     replace("1-9","1-9千/月").replace("2-3","2-3千/月").replace("2-4","2-4千/月").\
            #     replace("2-5","2-5千/月").replace("2-6","2-6千/月").replace("2-7","2-7千/月").replace("2-8","2-8千/月").\
            #     replace("2-9","2-9千/月").replace("3-4","3-4千/月").\
            #     replace("3-5","3-5千/月").replace("3-6","3-6千/月").replace("3-7","3-7千/月").replace("3-8","3-8千/月").\
            #     replace("3-9","3-9千/月").\
            #     replace("5-5","5-5千/月").replace("5-6","5-6千/月").replace("5-7","5-7千/月").replace("5-8","5-8千/月").\
            #     replace("5-9","5-9千/月").replace("6-6","6-6千/月").replace("6-7","6-7千/月").replace("6-8","6-8千/月").\
            #     replace("6-9","6-9千/月").replace("7-7","7-7千/月").replace("7-8","7-8千/月").\
            #     replace("7-9","7-9千/月").replace("8-8","8-8千/月").\
            #     replace("8-9","8-9千/月").\
            #     replace("4-5","4-5千/月").replace("4-6","4-6千/月").replace("4-7","4-7千/月").replace("4-8","4-8千/月").\
            #     replace("4-9","4-9千/月")
            # line = line.replace("20-4万/月0","2-4万/月")\
            #     .replace("-35","-3.5万/月").replace("-38","-3.8万/月").replace("-55","-5.5万/月").replace("-25","-2.5万/月").\
            #     replace("-36","-3.6万/月").replace("-26","-2.6万/月").replace("-27","-2.7万/月").replace("-28","-2.8万/月").\
            #     replace("-29","-2.9万/月").replace("-24","-2.4万/月").replace("-23","-2.3万/月").replace("-22","-2.2万/月").\
            #     replace("-21","-2.1万/月").replace("-31","-3.1万/月").replace("-32","-3.2万/月").replace("-33","-3.3万/月").\
            #     replace("-34","-3.4万/月").replace("-37","-3.7万/月").replace("-39","-3.9万/月").replace("-50","-5万/月").\
            #     replace("-60","-6万/月")
            # line = line.replace("-10","-1万/月").replace("-11","-1.1万/月").replace("-12","-1.2万/月").replace("-13","-1.3万/月").\
            #     replace("-14","-1.4万/月").replace("-15","-1.5万/月").replace("-16","-1.6万/月").replace("-17","-1.7万/月").replace("-18","-1.8万/月").\
            #     replace("-19","-1.9万/月").replace("-20","-2万/月").replace("-30","-3万/月").replace("-40","-4万/月")
            # line = line.replace("2千/月.2万/月","2.2万/月").replace("千/月万/月","万/月").\
            #     replace("1千/月.2万/月","1.2万/月").replace("1千/月.5万/月","1.5万/月").replace("3千/月.5万/月","3.5万/月")



    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    for i in tqdm(list):
        clearBlankLine(i)
