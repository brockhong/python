# coding=utf-8
from City import City

class Province(object):
    def __init__(self):
        self.__name = ''
        self.__durl = ''
        self.__city = City()

    def __str__(self):
        return '行政区：%s  url ：%s' \
               % (self.__name,
                  self.__durl
                  )


    def getname(self):
        return self.__name


    def setname(self, value):
        self.__name = value


    def getdurl(self):
        return self.__durl


    def setdurl(self, value):
        self.__durl = value

    def getcity(self):
        return self.__city

    def setcity(self, value):
        self.__city = value

def main():
     a = City()
     print(a)


if __name__ == '__main__':
    main()
