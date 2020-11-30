# coding=utf-8
from flask import Flask, jsonify, render_template
from py2neo import Node, Graph, Relationship, NodeMatcher
from py2neo.matching import RelationshipMatcher
import pandas as pd
import random

graph = Graph(
                "http://localhost:7474",
                username="neo4j",
                password="12345")

app = Flask(__name__)
# flask struct

@app.route('/')
# 建立路由，指向網頁
def post():
    """與fasttext交互"""
    # 接收數據(fasttext的資料)
    selection_name = "經典款圓領"
    selection_name2 = "FU05"

    # get 1 dimension match node (upper <=> lower <=> full)
    # nodes_data1 = graph.run(
    #     "MATCH (n:編號)-->(p:編號) WHERE p.name=~'.*" + selection_name2 + ".*' RETURN n").data()
    # a = pd.DataFrame(nodes_data1)

    # get 1 dimension match node (upper <=> lower <=> full)
    k = random.uniform(0, 1)
    l = 1
    m = round(k, l)
    m = str(m)
    nodes_data1 = graph.run(
        "MATCH (n:`編號` {name: '" + selection_name2 + "'}) match (n)-[:`" + m + "`]->(p)<-[:is]-(:`型態`) RETURN p").data()
    a = pd.DataFrame(nodes_data1)

    Name_list1 = []
    Img_list1 = []

    for i in range(2):
        Name_list1.append(a.loc[i, "p"]["Name"])
        Img_list1.append(a.loc[i, "p"]["Img"])
        i += 1

    # Name_list1 = list(set(Name_list1))
    # Img_list1 = list(set(Img_list1))

        # print(b)
        # print(c)
        # print(a.loc[1,"n"]["Name"], a.loc[1,"n"]["Img"])

    # ==============================================================================
    # get 2 dimension match node (same kind of clothes)
    k = random.uniform(0, 1)
    l = 1
    m = round(k, l)
    m = str(m)
    print(m)
    nodes_data_all = graph.run(
        "MATCH (p:編號 {name:'" + selection_name2 + "'})-[:is]-(q:型態)-[r:is]-(n:編號) return n").data()
        # "MATCH (n:`編號` {name: '" + selection_name2 + "'})<--(:`型態`)-->(p) RETURN p").data()
        # "MATCH (n:編號)-[:`" + m + "`]->(p) WHERE n.name=~'.*" + selection_name2 + ".*' RETURN n").data()
    a = pd.DataFrame(nodes_data_all)

    # print(a)
    # print("*"*100)

    Name_list2 = []
    Img_list2 = []

    for i in range(2):
        Name_list2.append(a.loc[i, "n"]["Name"])
        Img_list2.append(a.loc[i, "n"]["Img"])
        i += 1

    # Name_list2 = list(set(Name_list2))
    # Img_list2 = list(set(Img_list2))

        # print(b)
        # print(c)
        # print(a.loc[1,"n"]["Name"], a.loc[1,"n"]["Img"])


    return render_template('index.html', data1=Name_list1, data2=Img_list1, data3=Name_list2, data4=Img_list2)

if __name__ == '__main__':
    app.run(debug=True)
    # flask框架

