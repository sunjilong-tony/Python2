# coding= utf-8
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.102.101", 8080))
def run(client):
    while True:
        data = client.recv(1024).decode("utf-8")
        print("服务器说"+ data)
th1 = threading.Thread(target=run, args=(client,))
th1.start()

def run2(client):
    while True:
        #456#你好
        data = input("请输入要说的话：")
        data = "talk#" + data
        client.send(data.encode("utf-8"))
th2 = threading.Thread(target=run2, args=(client,))
th2.start()
#
client.send("register#456#to".encode("utf-8"))
th1.join()
th2.join()
