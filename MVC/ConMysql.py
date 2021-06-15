import pymysql
import numpy as np
pymysql.install_as_MySQLdb()


conn = pymysql.Connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'daqige666',
        db = 'citypoi',
        charset = 'utf8')

# // var points = [
#         // { weight: 8, lnglat:["116.408032","39.909729"], "name": '北京'},
#         // { weight: 8, lnglat:["121.461743","31.231584"], "name": '上海'},
#         // { weight: 8, lnglat:["113.265942","23.08983"], "name": '广州'},
#         // { weight: 8, lnglat:["104.059399","30.562253"], "name": '成都'},
#         // { weight: 1, lnglat: ["108.939621", "34.343147"] },
#         // { weight: 1, lnglat: ["112.985037", "23.15046"] },
#         // ...
#     // ]

#
# select count(*)  from  `15spr新城poi`   t15  where  t15.pid  NOT IN(select  pID  from `14spr新城poi` );

# 得到每一个种类的需要的字段

def EveryKindDoSQL(sql, style):
    conn.ping(reconnect=True)  # 防止sql长时间连接断开
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    mypoints = []  # 点的可视化数据
    reli = []    # 热力图的数据
    relideng = []
    relijian = []
    for row in results:
        dict1 = {}   # 每一轮的点数据
        lnglat = [ ]
        lnglat.append(row[5])
        lnglat.append(row[6])
        dizhi = row[10]
        name = row[9]
        id = row[0]
        dict1['id'] = id
        dict1["name"] = name
        dict1["dizhi"] = dizhi
        dict1["lnglat"] = lnglat
        dict1["style"] = style
        mypoints.append(dict1)

        # 热力图数据格式{"lng": 116.191031, "lat": 39.988585, "count": 10},
        relidict = {}
        relidict["lng"] = row[5]
        relidict["lat"] = row[6]
        relidict["count"] = 1
        reli.append(relidict)
        # print(dict1)
        # print(',')
    cursor.close()
    # print(mypoints)
    return mypoints, reli


def getdata(years, kinds):

    years0 = str(years[0]) + "spr新城poi"
    years1 = str(years[1]) + "spr新城poi"

    zen = []
    deng = []
    jian = []
    relisumzen = []
    relisumjian = []
    relisumdeng = []
    # 按种类来执行sql
    for i in kinds:

        # print("这是遍历的sql".format(), i)
        y0_y1_zen = "select * from " + years1 + " as t1 where t1.pid NOT IN (select PID from " + years0 + ") and t1.CLASS_NAME = " + "'" + i + "'"
        y0_y1_deng = "select * from " + years0 + " as t1 where t1.pid IN (select PID from " + years1 + ") and t1.CLASS_NAME = " + "'" + i + "'"
        y0_y1_jian = "select * from " + years0 + " as t1 where t1.pid not in(select PID from " + years1 + ") and t1.CLASS_NAME = " + "'" + i + "'"
        print(y0_y1_zen)
        print(y0_y1_deng)
        print(y0_y1_jian)
        EveryZen, Everyrelizen = EveryKindDoSQL(y0_y1_zen, 0)
        zen = zen + EveryZen
        relisumzen = relisumzen + Everyrelizen


        EveryDeng, Everyrelideng = EveryKindDoSQL(y0_y1_deng, 1)
        deng = deng + EveryDeng
        relisumdeng = relisumdeng +Everyrelideng

        Everyjian, Everyrelijian = EveryKindDoSQL(y0_y1_jian, 2)
        jian += Everyjian
        relisumjian = Everyrelijian

    conn.close()


    return zen, deng, jian, relisumzen, relisumdeng, relisumjian

# kinds = ['科研及技术服务', '农、林、牧、渔业']
# years = [16, 19]
# getdata(years, kinds)