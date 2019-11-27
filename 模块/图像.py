# coding= utf-8
from PIL import Image
import random
# 打开图片
im = Image.open("E:/飞机大战/demo/background.png")
# 查看图片的信息
print(im.format, im.size, im.mode)
# 查看图像
im.show()
# 设置图片的大小(元组)
im.thumbnail((150, 100))
# 保存新的图片
im.save("11.png", "png")
