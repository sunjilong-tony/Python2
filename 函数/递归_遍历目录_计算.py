# coding= utf-8
import os


# 例遍目录（耗性能）
def alteration(path, sp=""):
    filelist = os.listdir(path)
    strfilelist = str(filelist)
    with open("./test1", "a") as temp:
        temp.write(strfilelist)
    sp += " "
    for i in filelist:
        abslist = os.path.join(path, i)
        if os.path.isdir(abslist):
            print("目录:%s" % abslist)
            alteration(abslist)
        else:
            print(sp + "文件：%s" % abslist)

alteration(r"E:/飞机大战")


