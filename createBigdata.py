#code=utf8
#-*-coding:UTF-8-*-
#createBigfile.py

import sys
import datetime
import time
import csv
import random

sex = [u'男',u'女']
educationBackgroud = [u'大专',u'本科',u'硕士',u'研究生',u'博士',u'博士后',u'高中']
codeRange = range(ord('a'),ord('z'))
intRange = range(0, 9)
alphaRange = [chr(x) for x in codeRange]
alphaRangeUpper = [chr(x).upper() for x in codeRange]

# 59 * 365
daysMax = 21535
theDay = datetime.date(1949,1,1)

def getSex():
    global sex
    return sex[random.randint(0,1)]

def getBrithdayAndAge():
    global daysMax,theDay
    eday = random.randint(1,daysMax)
    mDate = theDay+datetime.timedelta(days=eday)
    return {"birthday":mDate.strftime('%m%d'), "age":int(datetime.date.today().year - mDate.year)}

def getAddressAndArea():
    area = [[u"华北", u"河北石家庄"], [u"华北", u"河北唐山"], [u"华北", u"河北秦皇岛"], [u"华北", u"河北邯郸"], [u"华北", u"河北邢台"],
            [u"华北", u"河北保定"], [u"华北", u"河北张家口"], [u"华北", u"河北承德"], [u"华北", u"河北沧州"], [u"华北", u"河北廊坊"], [u"华北", u"河北衡水"],
            [u"西北", u"山西太原"], [u"西北", u"山西大同"], [u"西北", u"山西阳泉"], [u"西北", u"山西长治"], [u"西北", u"山西晋城"], [u"西北", u"山西朔州"],
            [u"西北", u"山西晋中"], [u"西北", u"山西运城"], [u"西北", u"山西忻州"], [u"西北", u"山西临汾"], [u"西北", u"山西吕梁"],
            [u"西北", u"内蒙古呼和浩特"], [u"西北", u"内蒙古包头"], [u"西北", u"内蒙古乌海"], [u"西北", u"内蒙古赤峰"], [u"西北", u"内蒙古通辽"],
            [u"西北", u"内蒙古鄂尔多斯"], [u"西北", u"内蒙古呼伦贝尔"], [u"西北", u"内蒙古巴彦淖尔"], [u"西北", u"内蒙古乌兰察布"], [u"西北", u"内蒙古兴安盟"],
            [u"西北", u"内蒙古锡林郭勒盟"], [u"西北", u"内蒙古阿拉善盟"], [u"东北", u"辽宁沈阳"], [u"东北", u"辽宁大连"], [u"东北", u"辽宁鞍山"],
            [u"东北", u"辽宁抚顺"], [u"东北", u"辽宁本溪"], [u"东北", u"辽宁丹东"], [u"东北", u"辽宁锦州"], [u"东北", u"辽宁营口"], [u"东北", u"辽宁阜新"],
            [u"东北", u"辽宁辽阳"], [u"东北", u"辽宁盘锦"], [u"东北", u"辽宁铁岭"], [u"东北", u"辽宁朝阳"], [u"东北", u"辽宁葫芦岛"], [u"东北", u"吉林长春"],
            [u"东北", u"吉林吉林市"], [u"东北", u"吉林四平"], [u"东北", u"吉林辽源"], [u"东北", u"吉林通化"], [u"东北", u"吉林白山"], [u"东北", u"吉林松原"],
            [u"东北", u"吉林白城"], [u"东北", u"吉林延边朝鲜族自治州"], [u"东北", u"黑龙江哈尔滨"], [u"东北", u"黑龙江齐齐哈尔"], [u"东北", u"黑龙江鸡西"],
            [u"东北", u"黑龙江鹤岗"], [u"东北", u"黑龙江双鸭山"], [u"东北", u"黑龙江大庆"], [u"东北", u"黑龙江伊春"], [u"东北", u"黑龙江佳木斯"],
            [u"东北", u"黑龙江大兴安岭地区"], [u"华中", u"江苏南京"], [u"华中", u"江苏无锡"], [u"华中", u"江苏徐州"], [u"华中", u"江苏淮安"],
            [u"华中", u"江苏盐城"], [u"华中", u"江苏扬州"], [u"华中", u"江苏镇江"], [u"华中", u"江苏泰州"], [u"华中", u"江苏宿迁"], [u"华中", u"浙江杭州"],
            [u"华中", u"浙江宁波"], [u"华中", u"浙江温州"], [u"华中", u"浙江嘉兴"], [u"华中", u"浙江湖州"], [u"华中", u"湖南长沙"], [u"华中", u"湖南株洲"],
            [u"华中", u"湖南湘潭"], [u"华中", u"湖南衡阳"], [u"华中", u"湖南邵阳"], [u"华中", u"湖南岳阳"], [u"华中", u"湖南常德"], [u"华中", u"湖南张家界"],
            [u"东南", u"广东广州"], [u"东南", u"广东韶关"], [u"东南", u"广东深圳"], [u"东南", u"广东珠海"], [u"东南", u"广东汕头"], [u"东南", u"广东佛山"],
            [u"东南", u"广东江门"], [u"东南", u"广东湛江"], [u"东南", u"广东茂名"], [u"东南", u"广东肇庆"], [u"东南", u"广东惠州"], [u"东南", u"广东梅州"],
            [u"东南", u"广东汕尾"], [u"东南", u"广东河源"], [u"东南", u"广东阳江"], [u"东南", u"广东清远"], [u"东南", u"广东东莞"], [u"东南", u"广东中山"],
            [u"东南", u"广东潮州"], [u"东南", u"广东揭阳"], [u"东南", u"广东云浮"], [u"西南", u"广西南宁"], [u"西南", u"广西柳州"], [u"西南", u"广西桂林"],
            [u"西南", u"广西梧州"], [u"西南", u"广西北海"], [u"西南", u"广西防城港"], [u"西南", u"广西钦州"], [u"西南", u"广西贵港"], [u"西南", u"广西玉林"],
            [u"西南", u"广西百色"], [u"西南", u"广西贺州"], [u"西南", u"广西河池"], [u"西南", u"广西来宾"], [u"西南", u"海南海口"], [u"西南", u"海南三亚"],
            [u"西南", u"海南三沙"], [u"西南", u"海南儋州"], [u"西南", u"海南五指山"], [u"西南", u"四川成都"], [u"西南", u"四川自贡"],
            [u"西南", u"四川攀枝花"], [u"西南", u"四川泸州"], [u"西南", u"四川德阳"], [u"西南", u"四川绵阳"], [u"西南", u"四川广元"], [u"西南", u"四川遂宁"],
            [u"西南", u"四川内江"], [u"西南", u"四川乐山"], [u"西南", u"四川南充"], [u"西南", u"四川眉山"], [u"西南", u"四川宜宾"], [u"西南", u"四川广安"],
            [u"西南", u"四川达州"], [u"西南", u"四川雅安"], [u"西南", u"四川巴中"], [u"西南", u"贵州贵阳"], [u"西南", u"贵州六盘水"], [u"西南", u"贵州遵义"],
            [u"西南", u"贵州安顺"], [u"西南", u"贵州毕节"]]
    length = len(area) - 1
    return area[random.randint(0,length)]

def getPhone():
    network = ['133','135','136','139','188','189','175','131']
    i = 0
    stringint = ''
    while i < 8:
        stringint += str(intRange[random.randint(0,8)])
        i += 1
    return str(network[random.randint(0, len(network)-1)])+stringint

def email():
    domain = ['@sina.com','@qq.com','@163.com','@126.com','@gmail.com','@outlook.com']
    return randomString(random.randint(5,10))+domain[random.randint(0,5)]

## 小写随机

def randomStrlower(length):
    global codeRange, alphaRange
    stringRandom = ''
    for i in range(length):
        stringRandom += alphaRange[random.randint(0,i)]
    return stringRandom

## 【a-zA-Z0-9】随机

def randomString(length):
    global codeRange, alphaRange, alphaRangeUpper
    stringRandom = ''
    listData = alphaRange + alphaRangeUpper + range(0,9)
    lenList = len(listData) - 1
    for i in range(length):
        stringRandom += str(listData[random.randint(0,lenList)])
    return stringRandom

def getEducationBackgroud():
    global educationBackgroud
    return educationBackgroud[random.randint(0, 1)]

def getopenid():
    return randomString(6)+'-'+randomString(21)

def getOrderDate():
    eday = random.randint(60, 365)
    mDate = datetime.date(datetime.date.today().year-1,1,1) + datetime.timedelta(days=eday)
    return mDate.strftime('%Y-%m-%d')

def getPreference():
    area = [u'火车站',u'机场',u'码头',u'KTV',u'度假酒店',u'超市',u'加油站',u'电影院',u'美容院',u'滑雪场',u'体育馆',u'医院',u'学校',u'靶场',u'篮球场',u'商场']
    return area[random.randint(0,len(area)-1)]

def getFrquentlyArea():
    area = [u'上海虹桥火车站',u'上海虹桥机场',u'铜锣湾码头',u'香港KTV',u'泰国度假酒店',u'伊斯坦布尔车站',u'喀布尔车站',u'三亚7星高级酒店',u'广州快捷酒店',u'台湾垦丁民宿',u'巴黎戴高乐机场',u'南京机场',u'北京三里屯商场',u'三亚度假村',u'普罗旺斯酒店',u'北海道酒店']
    return area[random.randint(0,len(area)-1)]


def insertBasicData(filename, num=1000):
    f1 = open(filename +  datetime.date.today().strftime('%m%d')
 +'.csv', 'wb')
    title = u"ID, 性别, 年龄, 联系地址, 地区, 手机号, email, 生日, 学历, openID\n"

    f1.write(title.encode('gbk'))
    i = 0
    str = ''
    while i < num:
        i += 1
        ## 出生日期
        bri = getBrithdayAndAge()
        areainfo = getAddressAndArea()
        # 生成基础数据
        str = u"%i, %s, %d, %s, %s, %s, %s, %s, %s, %s\n"%(i, getSex(), bri['age'],areainfo[1], areainfo[0], getPhone(), email(), bri['birthday'], getEducationBackgroud(), getopenid())
        f1.write(str.encode('gbk'))
        # 行为数据
    f1.close()


## 行为数据
def insertActionData(filename, num=1000):
    f1 = open(filename + datetime.date.today().strftime('%m%d')
+'.csv', 'wb')
    title = u"ID, 下单总金额, 下单总次数, 上次下单时间, 消费偏好, 最近一次消费时间, 常访点\n"
    f1.write(title.encode('gbk'))
    i = 0
    str = ''
    payTotal = range(1000,10000)
    count = range(1, 25)
    while i < num:
        i += 1
        # 行为数据
        str = u"%i, %d, %d, %s, %s, %s, %s \n"%(i, random.randint(10000, 40000), random.randint(1, 20),getOrderDate(), getPreference(), getOrderDate(), getFrquentlyArea() )
        f1.write(str.encode('gbk'))
    f1.close()

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    start = time.time()
    insertBasicData('basic')
    insertActionData('action')

    end = time.time()
    print(" use time:%d"%(end-start))
