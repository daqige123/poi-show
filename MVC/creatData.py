import pymysql
import numpy as np
from math import radians, sin, cos, asin, sqrt
pymysql.install_as_MySQLdb()

# 用来保存训练用的tsv(head, trail)
train = []
kind_name = []

# 记录所有的kind
# def kind_name(self):
# def write_file (save_dir, file_name):
#     with open(file_name, "w", )


conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='daqige666',
        db='citypoi',
        charset='utf8')
conn.ping(reconnect=True)  # 防止sql长时间连接断开
cursor = conn.cursor()
sql = "select * from `19spr新城poi` GROUP BY KIND_NAME "
cursor.execute(sql)

# 所有执行sql后的结果保存在results中，这是一个可迭代对象。

results = cursor.fetchall()
f = open("./poidata/kind_name.txt", "w", encoding='utf-8')
for index, poi in enumerate(results):
    print("第{}条数据".format(index), poi[3])
    f.write(poi[3])
    f.write("\n")
    kind_name.append(poi[3])

print(kind_name)
cursor.close()
conn.close()


# 和高德api误差大概为千分之一，高德108， 函数107.91， 高德6107 ，函数6100
def haversine_dis(lon1, lat1, lon2, lat2):
    # 将十进制转为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    aa = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(aa))
    r = 6371  # 地球半径，千米
    return c * r * 1000


test1 = haversine_dis(108.97287, 34.28266, 109.02611, 34.24989)



# print(test1)