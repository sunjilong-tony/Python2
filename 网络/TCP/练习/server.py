# coding= utf-8
import socket
import threading
from person import Person

userdict = {}
def run(clientSocket):
    while True:
        data = clientSocket.recv(1024).decode("utf-8")
        # "rigister#123#tony"
        # "talk#4566#nihao
        # 解析数据
        arr = data.split("#")
        print(arr)
        if arr[0] == "register":
            per = Person(clientSocket, arr[1], arr[2])
            print(per)
            userdict[arr[1]] = per
            print(userdict)
        elif arr[0] == "talk":
            # 找到当前用户的用户名
            name = None
            for account, per in userdict.items():
                if per.clientSocket is clientSocket:
                    name = per.name
                    break
            per = userdict.get(arr[1])
            friendSocket = per.clientSocket
            # 123说：你好
            friendSocket.send(name+":"+arr[2].encode("utf-8"))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.102.101", 8080))
server.listen(1000)
while True:
    clientSocket, ClientAddr = server.accept()
    print(ClientAddr)
    print(clientSocket)
    print(type(clientSocket))
    print(ClientAddr, "client连接成功")
    th1 = threading.Thread(target=run, args=(clientSocket,))
    th1.start()




