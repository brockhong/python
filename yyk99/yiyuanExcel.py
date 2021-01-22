#！/usr/bin/env python
# https://yyk.99.com.cn/
from urllib import request
from bs4 import BeautifulSoup, NavigableString
import xlwt
import os
import sys
import time

from City import City
from District import District

#sys.setrecursionlimit(500000000)
from HospitalDetail1 import HospitalDetail1
from Province import Province

url = "https://yyk.99.com.cn"
html_encode = 'utf-8'
# 不添加头爬虫 报错
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def section_title_style():
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    font.color_index=0x30
    font.height= 0x00EE

    style.font = font
    border= xlwt.Borders()
    border.top =0x01
    style.borders = border
    pa = xlwt.Pattern()
    pa.SOLID_PATTERN=0x00
    pa.pattern_fore_colour=0x2A
    style.pattern =pa
    return style

def set_style():
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'Microsoft YaHei UI'
    font.bold = False
    font.color_index = 4
    font.height = 0x00EE
    style.font = font
    al = xlwt.Alignment()
    # 垂直对齐
    al.horz = al.HORZ_CENTER
    # 水平对齐
    al.vert = al.VERT_CENTER
    # 换行
    al.wrap = al.WRAP_AT_RIGHT
    style.alignment = al
    return style

def set_data1(f,dlist):


    for i in range(len(dlist)):
        if dlist[i].getname() == '直辖市':
            continue
            city =dlist[i].getcity()
            for j in range(len(city)):
                sheet1 = f.add_sheet(city[j].getname(), cell_overwrite_ok=True)
                print(city[j].getdurl())
                set_data(sheet1,url+city[j].getdurl())
        else:
            sheet1 = f.add_sheet(dlist[i].getname(), cell_overwrite_ok=True)
            set_data(sheet1, url + dlist[i].getdurl())
            break




def set_data(sheet1,url1):
    url_b = url1
    beijing = request.Request(url=url_b, headers=headers)
    rspbj = request.urlopen(beijing)
    cntbj = rspbj.read()
    bj = BeautifulSoup(cntbj.decode(html_encode,errors='ignore'), "html.parser")
    databj= bj.select('.box-bg .container .g-warp .m-box .m-table-2 > table > tr >td >a')


    hospitalName = []
    hospitalUrls = []
    for i in range(len(databj)):
        print("==============================="+str(i))
        print(databj[i]['title'])
        hospitalName.append(databj[i]['title'])
        hospitalUrls.append(databj[i]['href'])
        print(databj[i]['href'])

    heads = ['医院名称', '别名', '性质', '所在地区', '院长', '建立时间', '类型', '级别', '科室数量', '医护人数', '病床数量', '年内门诊', '是否医保', '地址', '医院简介',
             '省(直辖市)', '电话', '城市链接', '地区', '地区医院数量', '医院链接', '市区']
    for j in range(0, len(heads)):
        sheet1.write(0, j, heads[j], section_title_style())
    for i in range(len(databj)):
    #for i in range(1):
        row0 = sheet1.row(i+1)
        row0.write(0,hospitalName[i])
        hospitalDetail = getDetail(url+hospitalUrls[i]+'jianjie.html')
        lxx = connection(url + hospitalUrls[i] + 'lianxi.html')

        if not hospitalDetail or not hospitalDetail.gethospitalAlias():
            print(hospitalDetail)
        else:
            row0.write(1,hospitalDetail.gethospitalAlias())
            row0.write(2, hospitalDetail.getmedical())
            row0.write(3, hospitalDetail.getdistrict())
            row0.write(4, hospitalDetail.getpresidentName())
            row0.write(5, hospitalDetail.getyear())
            row0.write(6, hospitalDetail.gethospitalType())
            row0.write(7, hospitalDetail.gethospitalLevel())
            row0.write(8, hospitalDetail.getdepartmentCount())
            row0.write(9, hospitalDetail.getdncount())
            row0.write(10, hospitalDetail.getbeds())
            row0.write(12, hospitalDetail.getisMedicalInsurance())
            row0.write(14, hospitalDetail.getdetail())
            row0.write(15, sheet1.name)
            row0.write(18, hospitalDetail.getdistrict())
            row0.write(21, hospitalDetail.getcityName())
        if lxx is None or len(lxx) == 0:
            print(lxx)
        else:
            row0.write(13, lxx[5].split('：')[1])
            row0.write(16,lxx[0].split('：')[1])
            row0.write(20, lxx[4].split('：')[1])
        print(sheet1.name+"========="+str(i)+"=========="+hospitalDetail.getcityName())

def connection(url):
    lxx1 = []
    try:
        url_lianxi = url
        lianxi = request.Request(url=url_lianxi, headers=headers)
        rsplianxi = request.urlopen(lianxi)
        cntlianxi = rsplianxi.read()
        lx = BeautifulSoup(cntlianxi.decode(html_encode, errors='ignore'), "html.parser")

        datalx = lx.select('.contact-list >ul >li')

        for lxx in datalx:
            lxx1.append(lxx.text)
    except:
        print("Error: 读取联系信息出错 "+url)

    return lxx1

def getDetail(urld):
    hospitalDetail = HospitalDetail1()
    try:
        url_jianjie = urld
        beijing = request.Request(url=url_jianjie, headers=headers)
        rspbj = request.urlopen(beijing)
        cntbj = rspbj.read()
        bj = BeautifulSoup(cntbj.decode(html_encode, errors='ignore'), "html.parser")

        databjjj = bj.select('.wrapper .wrap-box .present-cont >table>tr ')
        # print(databjjj)

        details = []
        for jj in databjjj:
            databjtd = jj.select('td')
            xjmod = 0
            for xj in databjtd:
                #print(xj.text)  # 居然有此方法
                if xjmod % 2:
                    details.append(xj.text)
                # sm = re.search(r'([\u4e00-\u9fa5]|_)+','<td><span>医院别名</span></td>')
                # sm = re.search(r'([\u4e00-\u9fa5]|_)+', xj.string) 解析到  _ 报错
                # print(sm.group(0))
                xjmod = 1 + xjmod

        detail = bj.select('.present-nr >div ')
        hospitalDetail.setdetail(detail[0].text)
        medical = bj.select('.wrap-mn .wrap-grade .medical ')
        hospitalDetail.setmedical(medical[0].text)
        city = bj.select('.crumb > p >a')
        for i in range(len(city)):
            if city[i].text.find('市') >= 0:
                hospitalDetail.setcityName(city[i].text)
                break
        if not hospitalDetail.getcityName():
            hospitalDetail.setcityName(city[2].text)

        hospitalDetail.sethospitalAlias(details[0])
        hospitalDetail.setdistrict(details[1])
        hospitalDetail.setpresidentName(details[2])
        hospitalDetail.setyear(details[3])
        hospitalDetail.sethospitalType(details[4])
        hospitalDetail.sethospitalLevel(details[5])
        hospitalDetail.setdepartmentCount(details[6])
        hospitalDetail.setdncount(details[7])
        hospitalDetail.setbeds(details[8])
        hospitalDetail.setoutpatient(details[9])
        hospitalDetail.setisMedicalInsurance(details[10])
    except:
        print("Error: 读取联系信息出错 " + urld)

    return hospitalDetail

def getprovince():
    url = "https://yyk.99.com.cn/city.html"
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    cnt = rsp.read()
    soup = BeautifulSoup(cnt.decode(html_encode, errors='ignore'), "html.parser")
    datat = soup.select('.m-tab-bd .on .m-clump .clump-row')

    province = []
    for tt in datat:

        a = Province()
        a.setname(tt.contents[0].text)
        a.setdurl(tt.contents[0].contents[0]['href'])
        city = []
        for ttt in tt.contents[1].contents:
            if isinstance(ttt, NavigableString):
                print("true")
            else:
                b = City()
                b.setname(ttt.text)
                b.setdurl(ttt['href'])
                city.append(b)

        a.setcity(city)
        province.append(a)

    return province

def getDistrict():
    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)
    cnt = rsp.read()
    soup = BeautifulSoup(cnt.decode(html_encode, errors='ignore'), "html.parser")

    data = soup.select('.home-rcont > ul > li > a ')
    # 获取数据，其中select中的参数就是前面获取的路径
    # print(data)
    dlist = []

    for ss in data:
        d = District()
        d.name = ss.string
        d.durl = url + ss['href']
        dlist.append(d)

    return dlist


if __name__ == '__main__':
    print("===========start============")
    if os.path.exists(r'yiyuan1.xls'):
        os.remove(r'yiyuan1.xls')

    # 获取省份
    dlist = getprovince()
    #
    f = xlwt.Workbook()

    set_data1(f, dlist)

    f.save(r'yiyuan1.xls')
    # 创建sheet
