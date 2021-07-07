from removebg import RemoveBg
import os
rmbg = RemoveBg("wtyBVBRCNeZThu41YsvdNLZ8", "error.log") # 引号内是你获取的API
path = '%s/picture'%os.getcwd() #图片放到程序的同级文件夹 picture 里面
for pic in os.listdir(path):
    rmbg.remove_background_from_img_file("%s\%s"%(path,pic))