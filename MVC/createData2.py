import pymysql
from math import radians, sin, cos, asin, sqrt

if __name__ == '__main__':
    # 链接mysql数据库
    db = pymysql.connect(host="localhost", user="root", password="daqige666", db="citypoi", port=3306)
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    file_name1 = "糕点、面包零售"
    file_name2 = "汽车销售及服务"
    sql1 = "SELECT * FROM 19spr新城poi where  KIND_NAME = " + "'" + file_name1 + "'"
    print(sql1)
    sql2 = "SELECT * FROM 19spr新城poi where  SUB_CLASS_NAME = " + "'" + file_name2 + "'"
    # sql1 = "SELECT * FROM 19spr新城poi where  KIND_NAME = '电影院' "
    # sql2 = "SELECT * FROM 19spr新城poi where  KIND_NAME = 'KTV' "
    cur.execute(sql1)
    results1 = cur.fetchall()
    cur.execute(sql2)
    results2 = cur.fetchall()
    # print(results)

    # 和高德api误差大概为千分之一，高德108， 函数107.91， 高德6107 ，函数6100
    def haversine_dis(lon1, lat1, lon2, lat2):
        # 将十进制转为弧度
        lon1 = float(lon1)
        lat1 = float(lat1)
        lon2 = float(lon2)
        lat2 = float(lat2)
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine公式
        d_lon = lon2 - lon1
        d_lat = lat2 - lat1
        aa = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
        c = 2 * asin(sqrt(aa))
        r = 6371  # 地球半径，千米
        return c * r * 1000

    save_file = "./poidata/trainFu/" + file_name1 + '-' + file_name2+".txt"
    f = open(save_file, "w", encoding='utf-8')
    train = []
    for i in range(len(results1) - 1):
        for j in range(i+1, len(results2)):
            if haversine_dis(results1[i]["GEOMETRY#SDO_POINT#X"], results1[i]["GEOMETRY#SDO_POINT#Y"], results2[j]["GEOMETRY#SDO_POINT#X"], results2[j]["GEOMETRY#SDO_POINT#Y"]) < 600:

                f.write(results1[i]["NAME"] + '\t' + results2[j]["NAME"] + '\t' + "0")
                f.write("\n")
                print(results1[i]["NAME"], results2[j]["NAME"])

    cur.close()
    db.close()
