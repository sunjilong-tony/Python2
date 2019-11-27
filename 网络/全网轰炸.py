# coding= utf-8
import socket


info = b'my name is tony'

for i in range(256):
    ip = "192.168.102.101"
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(info, ("192.168.102.101", 8081))