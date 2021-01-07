from PIL import Image

#判断文件是否可以打开
def isbad(path):
    bad = True
    try:
        Image.open(path).verify()  # 判断图片是否损坏
    except:
        bad = False
    return bad

#转换文件格式
def translate(path):
    if isbad(path):
        try:
            str = path.rsplit(".", 1)
            output_path = str[0] + ".png"  # 输出文件名称
            im = Image.open(path)
            im.save(output_path)  # 保存目标文件
            return True
        except:
            return False
    else:
        return False

print(translate('sample8.png'))

