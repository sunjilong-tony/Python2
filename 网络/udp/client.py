# coding= utf-8
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
    data = input("请输入发送的信息")
    client.sendto((data.encode("utf-8")), ("192.168.102.101", 8081))
