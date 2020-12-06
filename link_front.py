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
    # selection_name = "經典款圓領"
    selection_name = "MU02"

    # get 1 dimension match node (upper <=> lower <=> full)
    # nodes_data1 = graph.run(
    #     "MATCH (n:編號)-->(p:編號) WHERE p.name=~'.*" + selection_name2 + ".*' RETURN n").data()
    # a = pd.DataFrame(nodes_data1)

    Name_list1 = []
    Img_list1 = []

    nodes_data_all = graph.run(
        "MATCH (n:編號 {name:'" + selection_name + "'}) return n").data()
    b = pd.DataFrame(nodes_data_all)

    for j in range(1):
        Name_list1.append(b.loc[j, "n"]["Name"])
        Img_list1.append(b.loc[j, "n"]["Img"])


    # get 1 dimension match node (upper <=> lower <=> full)
    k = random.uniform(0, 1)
    l = 1
    m = round(k, l)
    m = str(m)
    nodes_data1 = graph.run(
        "MATCH (n:`編號` {name: '" + selection_name + "'}) match (n)-[:`" + m + "`]->(p)<-[:is]-(:`型態`) RETURN p").data()
    a = pd.DataFrame(nodes_data1)

    for i in range(2):
        Name_list1.append(a.loc[i, "p"]["Name"])
        Img_list1.append(a.loc[i, "p"]["Img"])
        i += 1

        # print(a.loc[1,"n"]["Name"], a.loc[1,"n"]["Img"])

    # ==============================================================================
    # get 2 dimension match node (same kind of clothes)
    nodes_data_all = graph.run(
        "MATCH (p:編號 {name:'" + selection_name + "'})-[:is]-(q:型態)-[r:is]-(n:編號) return n").data()
        # "MATCH (n:`編號` {name: '" + selection_name2 + "'})<--(:`型態`)-->(p) RETURN p").data()
        # "MATCH (n:編號)-[:`" + m + "`]->(p) WHERE n.name=~'.*" + selection_name2 + ".*' RETURN n").data()
    a = pd.DataFrame(nodes_data_all)

    for i in range(1):
        Name_list1.append(a.loc[i, "n"]["Name"])
        Img_list1.append(a.loc[i, "n"]["Img"])
        i += 1

    nodes_data_all = graph.run(
        "MATCH (n:編號 {name:'" + selection_name + "'}) return n").data()
    b = pd.DataFrame(nodes_data_all)

    for j in range(1):
        Name_list1.append(b.loc[j, "n"]["Name"])
        Img_list1.append(b.loc[j, "n"]["Img"])

    return render_template('index.html', data1=Name_list1, data2=Img_list1)

if __name__ == '__main__':
    app.run(debug=True)
    # flask框架

