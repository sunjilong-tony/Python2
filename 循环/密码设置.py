# coding= utf-8
password_list = ['!@#', '12345']
def account_login():
    tries = 3
    while tries > 0:
        password_input= input('请输入密码:')
        password_correct = password_input == password_list[-1] # 由于判断条件过长可以复制给一个变量，这样看起来代码整洁干净一些
        password_reset = password_input == password_list[0]
        if password_correct:
            print('login success!')
            break
        elif password_reset:
            new_password = input('请输入新的密码:')
            password_list.append(new_password)
            print('你的密码已经修改成功')
            account_login()
        else:
            print('输入错误')
        tries -= 1
    else:
        print('输入次数超限')
account_login()