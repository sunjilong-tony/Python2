# coding= utf-8
class User(object):
    def __init__(self, name, cardID, phone):
        self.name = name
        self.cardID = cardID
        self.phone = phone
        self.cardDict = {}

