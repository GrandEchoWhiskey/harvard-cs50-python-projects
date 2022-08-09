import emoji

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.__capacity = capacity
        self.__cookies = 0

    def __str__(self):
        res = ''
        for _ in range(self.__cookies):
            res += ':cookie:'
        return emoji.emojize(res)

    def deposit(self, n):
        self.__cookies += n
        if self.__cookies > self.__capacity:
            raise ValueError

    def withdraw(self, n):
        self.__cookies -= n
        if self.__cookies < 0:
            raise ValueError

    @property
    def capacity(self):
        return self.__capacity

    @property
    def size(self):
        return self.__cookies

j = Jar()
j.deposit(3)
print(str(j))