# coding= utf-8
'''
服务器搭建                       客户端
socket()                         socket（）
bind()
listen()
accept()
阻塞/等待客户端连接              connect()
recv（）                          send（）
处理服务请求
 send（）       返回数据           recv（）
 如果没有数据的发送
 close                               close
 '''

"""
s.bind()　　　绑定地址(ip地址,端口)到套接字,参数必须是元组的格式例如：s.bind(('127.0.0.1',8009))

s.listen(5)　　开始监听，5为最大挂起的连接数

s.accept()　　被动接受客户端连接，阻塞，等待连接

客户端套接字函数

s.connect()　　连接服务器端，参数必须是元组格式例如：s.connect(('127,0.0.1',8009))

公共用途的套接字函数

s.recv(1024)　　接收TCP数据，1024为一次数据接收的大小

s.send(bytes)　　发送TCP数据，python3发送数据的格式必须为bytes格式

s.sendall()　　完整发送数据，内部循环调用send

s.close()　　关闭套接字

  conn, addr = server.accept() # 就是等待的意思
  #conn就是客户端连过来的时候，在服务器端为其生成的一个连接实例
"""

import  socket

socket.socket(socket.AF_INET,)