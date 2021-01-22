# coding=utf-8
class District(object):
    def __init__(self):
        self.__name = ''
        self.__durl = ''

    def __str__(self):
        return '行政区：%s  url ：%s' \
               % (self.__name,
                  self.__durl
                  )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def durl(self):
        return self.__durl

    @durl.setter
    def durl(self, value):
        self.__durl = value

def main():
    a = District()
    a.name = "不是人"
    a.durl = "dd"
    print(a)


if __name__ == '__main__':
    main()
