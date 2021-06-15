# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.matching import RelationshipMatcher
import pandas as pd

# 连接数据库
graph = Graph("bolt://localhost:11007", username="neo4j", password="daqige666")


# 每个商圈的所有Poi数量, 关系图，返回节点和关系list
def TSAllPOI(TSName):
    s = " MATCH(n:POI)-[r1:特色是]->(t:TS), (n:POI)-[r2:位于商圈]->(s:SQ) where t.name= \'" + TSName + "\' return n.name, n.地址, s.name";
    #print(s)
    cyp = graph.run(s).data()
    #print(cyp)
    #df = pd.DataFrame(cyp)
    #print(df)
    list = []
    links = []

    for i in cyp:
        dict = {}
        dict["name"] = i["n.name"]
        dict["地址"] = i["n.地址"]
        dict["位于商圈"] = i["s.name"]
        dict["des"] = "name："+i["n.name"] + "  地址：" + i["n.地址"] +" 商圈名： "+ i["s.name"]
        list.append(dict)
        dict1 = {}
        dict1["source"] = i["n.name"]
        dict1["target"] = TSName
        dict1["name"] = "特色是"
        links.append(dict1)

    list.append({"name" : TSName})
    print("This is list: ")
    print(list)
    print(links)
    return list, links

# 属于该特色的所有Poi的地点, 关系图，返回节点和关系list
def SQAllPOI(SQName):

    s = "MATCH (n:POI)-[r:位于商圈]->(m:SQ) where m.name= \'" + SQName + "\' return n.name, n.地址, m.name"
    #print(s)
    cyp = graph.run(s).data()
    #print(cyp)
    #df = pd.DataFrame(cyp)
    #print(df)
    list = []
    links = []

    for i in cyp:
        dict = {}
        dict["name"] = i["n.name"]
        dict["地址"] = i["n.地址"]
        dict["des"] = "name："+i["n.name"] +", "+"地址：" + i["n.地址"]
        list.append(dict)
        dict1 = {}
        dict1["source"] = i["n.name"]
        dict1["target"] = SQName
        dict1["name"] = "位于商圈"
        links.append(dict1)

    list.append({"name" : SQName})
    print("This is list: ")
    # print(list)
    #print(links)
    return list, links




# 查询每个商圈的排名前3的种类list
def SQto3kind(SQName):

    a = "match (n:POI)-[r1]->(m:SQ{name:\'" + SQName + "\'}) ,(n:POI)-[r2]->(k:kind) return k.name , count(k.name) order by count(k.name) desc LIMIT 3"

    # print(s)
    cyp = graph.run(a).data()
    KindName = []
    Knumber = []
    for i in cyp:
        KindName.append(i['k.name'])
        Knumber.append(i['count(k.name)'])
    return KindName, Knumber

# 极坐标图
def SQ20():
    a = "match (n:POI)-[r]->(m:SQ) return m.name, count(n) order by count(n) desc LIMIT 21"
    cyp = graph.run(a).data()
    cyp = cyp[1:21]
    SQName = []
    KindName = []
    Knumber = []
    for i in cyp:
        SQName.append(i["m.name"])
        eachKname, eachKnumber = SQto3kind(i["m.name"])
        KindName.append(eachKname)
        Knumber.append(eachKnumber)
    for i in KindName:
        i[0],i[1], i[2] = i[2], i[0],i[1]
    for i in Knumber:
        i[0], i[1], i[2] = i[2], i[0], i[1]
    print(SQName)
    print(KindName)
    print(Knumber)
    return SQName, KindName, Knumber
#SQ20()

