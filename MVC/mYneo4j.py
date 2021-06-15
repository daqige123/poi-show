# -*- coding: utf-8 -*-
from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.matching import RelationshipMatcher
import pandas as pd

# 连接数据库
graph = Graph("bolt://localhost:11012", username="neo4j", password="daqige666")


# 节点查询
mather = NodeMatcher(graph)
result = mather.match("Person", name="张三").first()
#print(result)
# (_0:Person {name: '\u5f20\u4e09'})


# 查询关系
relation_matcher = RelationshipMatcher(graph)
ret = relation_matcher.match(r_type="属于").first()
#print(ret)
# (张三)-[:认识 {}]->(李四)

# 直接运行cypher语句
ret = graph.run('match(n) return n').data()
#print(ret)
# [{'p': (_3:Person {name: '\u674e\u56db'})}]


def cyp():
    st = "MATCH (n:POI)-[r:位于商圈]->(m:SQ) WHERE m.name = '小寨' return r"
    sql1 = "Match (n:poi)<-[r]-(m:SQ{name:'小寨'}) return n, r"
    cyp = graph.run("MATCH (n:POI)-[r:位于商圈]->(m:SQ) WHERE m.name = '小寨' return r").data()
    df = pd.DataFrame(cyp)
    print(cyp)
    #print(df)
    return cyp
cyp()

