# coding= utf-8
import os
import collections


def deep(path):
    queue = collections.deque()
    # 进队
    queue.append(path)
    while len(queue) != 0:
        # 数据出队
        dirpath = queue.popleft()
        filelist = os.listdir(dirpath)
        for i in filelist:
            fileabslist = os.path.join(dirpath,i)
            # 判断是否是目录，是就进队，不是就打印
            if os.path.isdir(fileabslist):
                print("目录：%s" % i)
                queue.append(fileabslist)
            else:         # 打印普通文件
                print("普通：%s" %i)


deep(r"E:/飞机大战")