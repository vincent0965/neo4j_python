# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship, NodeMatcher

class DataToNeo4j(object):

    """將excel的資料存入neo4j"""
    def __init__(self):
        """連接neo4j的post"""
        link = Graph(
                    "",
                    username="",
                    password=""
                    )

        self.graph = link

        # 定義label
        self.gender = '性別'
        self.type = '型態'
        self.sn = '編號'
        self.name = '商品名稱'
        self.img = '圖片'
        self.des = '說明'

        # delete all relaationship
        self.graph.delete_all()

    def create_node(self,
                    node_list_gender,
                    node_list_type,
                    thing):

        """build node"""
        for gender in node_list_gender:
            gender_node = Node(self.gender, name=gender, gender=gender)
            self.graph.create(gender_node)

        for type in node_list_type:
            type_node = Node(self.type, name=type, type=type)
            self.graph.create(type_node)

        # add more properties in each node
        for i in range(1, len(thing)):
            sn_node = Node(self.sn, name=thing[i][2], product=thing[i][2], Name=thing[i][3], Img=thing[i][4], Des=thing[i][5])
            self.graph.create(sn_node)

    def create_relation(self, df_data, rel_data):
        """build relationship"""
        Matcher = NodeMatcher(self.graph)
        # function of find node

        # build all nodes relation
        m = 0
        rel_data = rel_data.drop(columns=['sn'])
        for m in range(0, len(df_data)):
            try:
                # (node)-[:relation label]->(node)
                node1 = Matcher.match(self.gender, name=df_data['gender'][m], gender=df_data['gender'][m])
                node2 = Matcher.match(self.type, name=df_data['type'][m], type=df_data['type'][m])
                node3 = Matcher.match(self.sn, name=df_data['sn'][m], product=df_data['sn'][m])

                rel1 = Relationship(list(node1)[0], "is", list(node2)[0])
                self.graph.create(rel1)
                print("建立關係: {}".format(rel1))
                rel2 = Relationship(list(node2)[0], "is", list(node3)[0])
                self.graph.create(rel2)
                print("建立關係: {}".format(rel2))

            except AttributeError as e:
                print(e, m)

        # build most outside nodes relation
        # 列出list 用enumerate跑過找出全部的node(leaf)
        for i, leaf1 in enumerate(list(Matcher.match(self.sn))):
            # 抓出第一個葉子的name(eg:MF01...)
            for j, leaf2 in enumerate(list(Matcher.match(self.sn))):
                # 抓出第二個葉子的name
                idx = rel_data.columns.get_loc(leaf1['name']) - 1
                # 第一個node(leaf1)的id(找出leaf在rel_data的id)
                idx1 = rel_data.columns.get_loc(leaf2['name']) - 1
                # 第二個node(leaf2)的id
                if rel_data.values[idx][idx1] == 0:
                    # 如果關聯係數是0則不建關聯
                    pass
                else:
                    # i != j 才會執行(同一個node不用自己連)
                    rel_leaf1 = Relationship(leaf1, str(rel_data.values[idx][idx1]), leaf2)
                    self.graph.create(rel_leaf1)
                    print("建立leaf關聯: {}".format(rel_leaf1))
                    rel_leaf2 = Relationship(leaf2, str(rel_data.values[idx][idx1]), leaf1)
                    self.graph.create(rel_leaf2)
                    print("建立leaf關聯: {}".format(rel_leaf2))
                    # 雙向關聯
