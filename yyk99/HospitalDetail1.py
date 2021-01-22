# coding=utf-8
class HospitalDetail1(object):
    def __init__(self):
        self.__hospitalAlias=''
        self.__district=''
        self.__presidentName=''
        self.__year=''
        self.__hospitalType=''
        self.__hospitalLevel=''
        self.__departmentCount=''
        self.__dncount=''
        self.__beds=''
        self.__outpatient=''
        self.__isMedicalInsurance=''
        self.__detail = ''
        self.__medical = '' #性质
        self.__cityName = ''

    def __str__(self):
        return '医院别名：%s  行政区：%s  院长名：%s 建造年份：%s' \
               ' 医院类型：%s 医院等级：%s  科室数量：%s 医护数量：%s' \
               ' 床数量：%s 年门诊量：%s  是否医保：%s  详情：%s 城市：%s'\
               % (self.__hospitalAlias,
                  self.__district,
                  self.__presidentName,
                  self.__year,
                  self.__hospitalType,
                  self.__hospitalLevel,
                  self.__departmentCount,
                  self.__dncount,
                  self.__beds,
                  self.__outpatient,
                  self.__isMedicalInsurance,
                  self.__detail,
                  self.__cityName
                  )

    def getcityName(self):
        return self.__cityName

    def setcityName(self, value):
        self.__cityName = value

    def getmedical(self):
        return self.__medical

    def setmedical(self, value):
        self.__medical = value

    def getdetail(self):
        return self.__detail


    def setdetail(self, value):
        self.__detail = value



    def gethospitalAlias(self):
        return self.__hospitalAlias


    def sethospitalAlias(self, value):
        self.__hospitalAlias = value


    def getdistrict(self):
        return self.__district


    def setdistrict(self, value):
        self.__district = value


    def getpresidentName(self):
        return self.__presidentName


    def setpresidentName(self, value):
        self.__presidentName = value


    def getyear(self):
        return self.__year


    def setyear(self, value):
        self.__year = value


    def gethospitalType(self):
        return self.__hospitalType


    def sethospitalType(self, value):
        self.__hospitalType = value


    def gethospitalLevel(self):
        return self.__hospitalLevel


    def sethospitalLevel(self, value):
        self.__hospitalLevel = value


    def getdepartmentCount(self):
        return self.__departmentCount


    def setdepartmentCount(self, value):
        self.__departmentCount = value

    def getdncount(self):
        return self.__dncount


    def setdncount(self, value):
        self.__dncount = value

    def getbeds(self):
        return self.__beds


    def setbeds(self, value):
        self.__beds = value


    def getoutpatient(self):
        return self.__outpatient


    def setoutpatient(self, value):
        self.__outpatient = value


    def getisMedicalInsurance(self):
        return self.__isMedicalInsurance


    def setisMedicalInsurance(self, value):
        self.__isMedicalInsurance = value

def main():
    a = HospitalDetail1()
    a.sethospitalAlias ("不是人")
    a.setdetail("dd")
    print(a)

if __name__ == '__main__':
    main()