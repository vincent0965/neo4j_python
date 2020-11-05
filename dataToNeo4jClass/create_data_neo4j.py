# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship, NodeMatcher

class DataToNeo4j(object):

    """將excel的資料存入neo4j"""
    def __init__(self):
        """連接neo4j的post"""
        link = Graph(
                    "xxxxxxx",
                    username="xxxxxx",
                    password="xxxxxx"
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
                    node_list_sn,
                    node_list_name,
                    node_list_img,
                    node_list_des):

        """build node"""
        for gender in node_list_gender:
            gender_node = Node(self.gender, name=gender, gender=gender)
            self.graph.create(gender_node)
        for type in node_list_type:
            type_node = Node(self.type, name=type, type=type)
            self.graph.create(type_node)
        for sn in node_list_sn:
            sn_node = Node(self.sn,
                           name=sn,
                           product=sn,
                           Name=node_list_name[0],
                           Img=node_list_img[0],
                           Des=node_list_des[0])
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
        # 列出list 用eunmerate跑過找出全部的node(leaf)
        for i, leaf1 in enumerate(list(Matcher.match(self.sn))):
            # 抓出第一個葉子的name(eg:MF01...)
            for j, leaf2 in enumerate(list(Matcher.match(self.sn))):
                # 抓出第二個葉子的name
                idx = rel_data.columns.get_loc(leaf1['name']) - 1
                # 第一個node(leaf1)的id(找出leaf在rel_data的id)
                idx1 = rel_data.columns.get_loc(leaf2['name']) - 1
                # 第二個node(leaf2)的id
                if j != i:
                    # i != j 才會執行(同一個葉子不用自己連)
                    print(rel_data.values[idx][idx1])
                    rel_leaf = Relationship(leaf1, str(rel_data.values[idx][idx1]), leaf2)
                    self.graph.create(rel_leaf)

