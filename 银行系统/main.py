# coding= utf-8
from bank import Bank
from atm import ATM
from user import User
from card import Card
BANK = Bank()
atmMachine = ATM()

def main():
    while 1:
        atmMachine.atmInit()
        optionstr = input("请输入操作：")
        if optionstr == "1":
            pass
        elif optionstr == "2":
            atmMachine.shutdown()
            break
        elif optionstr == "3":
            atmMachine.addmoney()
        elif optionstr == "4":
            atmMachine.change_passwd(3)
if __name__ == '__main__':
    main()


