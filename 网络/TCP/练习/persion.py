# coding= utf-8
class Person(object):
    def __init__(self, clientSocket, account, name):
        self.clientSocket = clientSocket
        self.account = account
        self.name = name

