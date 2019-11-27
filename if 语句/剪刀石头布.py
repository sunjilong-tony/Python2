# coding= utf-8

import random
while 1:
    player = int(input("请输入您的选择 石头（1）剪刀（2）布（3）："))
    computer = random.randint(1, 3)
    print("player 输入%d，computer 输入%d " % (player, computer))
    if (player ==1 and computer == 2) \
            or (player == 2 and computer == 3) \
            or (player == 3 and computer == 1):
        print("您厉害")

    elif player == computer:
        print("您和我想一样")
    else:
        print("您输了，请再接再厉")
