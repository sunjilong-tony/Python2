# coding= utf-8
# tcp是建立在可靠连接，并且通信双方都可以流的发送数据相对于tcp，UDP则是面向无链接的协议
#使用udp，不用建立连接，主要只知道ip和端口，就可以发送，但不能保证数据是否能到达
#虽然传输不可靠，但速度快，对数据不可靠使用udp广播类型的软件使用较多
'''
服务器搭建                       客户端
socket()                         socket（）
bind()
recvfrom（）                      sendto（）
阻塞/等待客户端连接
处理服务请求
 send（）       返回数据           recv（）
 如果没有数据的发送
 close                             close
 '''
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("192.168.102.101", 8081))
while True:
    data, addr = server.recvfrom(1024)
    print("来至",addr,"的消息",data.decode("utf-8"))