# coding= utf-8
import os


def get_dir(path):
    stack_list = []
    stack_list.append(path)
    while len(stack_list) != 0:
        # 从栈中取数据
        dir_path = stack_list.pop()
        print(dir_path + "11111111")
        # 目录下所有的文件
        filelist = os.listdir(dir_path)
        # 处理每个文件，如果是普通文件则打印
        # 出来，如果是目录则将该目录继续压栈
        for filename in filelist:
            fileabslist = os.path.join(dir_path, filename)
            if os.path.isdir(fileabslist):
                # 是目录就压栈
                print("目录：%s" % filename)
                stack_list.append(fileabslist)
            else:         # 打印普通文件
                print("普通：%s" % filename)


get_dir(r"E:/飞机大战")
