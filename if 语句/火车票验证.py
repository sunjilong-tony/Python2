# coding= utf-8
# 1.定义布尔布尔类型否有火车票has_ticket
has_ticket = True
# 2.定义定义刀的长度knife_length表示刀的长度.单位：麗米
knife_length = 30
# 3.首先是否有票，如果有，才安检
if has_ticket == True:
    print("有票，可以安检")
    if knife_length > 20:
        print("刀太长，无法上车")
    elif knife_length <= 20:
        print("安检通过")
# 4.安检时.检查刀的长度.判断《这20歷米
#    如果超过20屋米，不允许上车
#    如果超过20屋米，允许上车
# 5 如栗没有车蒙.不允终道门
else:
    print("没有车票，不能上车")
