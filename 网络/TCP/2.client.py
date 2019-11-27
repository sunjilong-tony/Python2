# coding= utf-8
import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 元组第一个元素为客户端要连接的服务器的ip地址，第二个参数为服务器的端口号
client.connect(("192.168.102.101", 8080))
def run(c):
    while True:
        data = c.recv(1024).decode("utf-8")
        print("服务器说：" + data)

# 创建接收线程
threading.Thread(target=run, args=(client,)).start()
while True:
    print("等待连接")
    data = input("请输入要发送给服务器的消息：")
    client.send(data.encode("utf-8"))
