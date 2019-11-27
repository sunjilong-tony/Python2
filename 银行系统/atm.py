# coding= utf-8
num = 3
class ATM(object):
    def __init__(self):
        self.account = "1"
        self.passwd = 1
        self.money = 0
        self.isActive = True

    def atmInit(self):
        print("===============================")
        print("           登录（1）           ")
        print("++++++++++++关机（2）++++++++++")
        print("===========提额（3）===========")
        print("===========改密（4）===========")

    def welcome(self):
        print("===============================")
        print("           插卡（1）           ")
        print("++++++++++++开户（2）++++++++++")
        print("===========补卡（3）===========")
        print("===========返回（4）===========")

    def optionView(self, name, cardID):
        print("===============================")
        print("用户名：%s     卡号：%d    " % (name, cardID))
        print("查询（1）转账（2）")
        print("存款（3）取款（4）")
        print("改密（5）注销（6）")
        print("锁定（7）解锁（8）")
        print("退卡（9）")
        print("===============================")
    def addmoney(self):
        money =int(input("请输入提额的钱： "))
        self.money += money
        if not self.isActive:
            self.isActive = True
    def shutdown(self):
        pass
    def change_passwd(self, num):
        if num == 1:
            return
        oldpasswd = int(input("请输入旧密码："))
        if oldpasswd == self.passwd:
            newpasswd = int(input("请输入新密码："))
            newpasswd1 = int(input("请确认再次新密码："))
            if newpasswd == newpasswd1:
                print("修改成功")
            else:
                print("修改失败")
        elif oldpasswd != self.passwd:
            print("密码错误")
            while num > 0:
                chice = int(input("请确认是否需要修改密码（1为确认0为取消)"))
                if chice == 0:
                    break
                elif chice == 1:
                    self.change_passwd(num-1)
                    num -= 1
                else:
                    print("没有输入正确")