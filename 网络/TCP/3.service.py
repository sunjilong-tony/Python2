# coding= utf-8
import socket
import threading


def run(clientSocket, clientAddr):
    while True:
        # 1024 表示大小
        data = clientSocket.recv(1024).decode("utf-8")
        print("client say" + data)
        print(type(data))
        clientSocket.send(" ok ".encode("utf-8"))

'''
1.创建socket
AF_INET 表示ipv4协议
sock_stream 表示tcp协议
'''''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
2.绑定
# 参数为一个元组，元组第一个为本机的ip，第二位为端口号，使用8000以上的值，最大使用到655535
'''
server.bind(("192.168.102.101", 8080))
'''
3.监听，设置最大连接数
'''
server.listen(50)
'''
4.等待客户端的连接
'''
while True:
    # 客户端连接成功返回客户端的socket和客户端的ip地址
    clientSocket, clientAddr = server.accept()

    print(clientAddr, " 客户连接成功")
    print(clientSocket)
    print(server.accept())
    # 创建线程交互
    th = threading.Thread(target=run, args=(clientSocket, clientAddr))
    th.start()