from GetCsvColumn import CsvFile,EXCLUDE
import pandas as pd


def csvwenjian(id):
    #先用一个列表把我们想要的内容给确定下来
    list = []
    list.append(csvfile.get_column('lat',ID='{}'.format(id), state=[1]))
    content = list[0]
    list2 = []
    list2.append(csvfile.get_column('lon',ID='{}'.format(id), state=[1]))
    context = list2[0]
    #然后再把对应的内容用CSV保存下来
    a = [x for x in content]
    b = [x for x in context]
    dataframe = pd.DataFrame({'lat':a,'lon':b})
    dataframe.to_csv(r"{}.csv".format(id),sep=',')
    print('执行完毕')

if __name__ == '__main__':
    #需要读取的csv的名字
    csvfilename = '试验_13.csv'
    csvfile = CsvFile(csvfilename)
    csvwenjian(input("请输入你要搜索的id:"))









