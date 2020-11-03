# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship

class DataToNeo4j(object):

    """將excel的資料存入neo4j"""
    def __init__(self):
        """連接neo4j的post"""
        link = Graph(
                    "http://localhost:xxxx",
                    username="neo4j",
                    password="xxxx"
                    )
        self.graph = link

        # 定義label
        self.invoice_gender = '性別'
        self.invoice_obj = 'obj'
        self.invoice_kind = '種類'
        self.invoice_some = '細項'
        self.invoice_item = '品項名稱'
        # delete all relaationship
        self.graph.delete_all()

    def create_node(self,
                    node_list_gender,
                    node_list_obj,
                    node_list_kind,
                    node_list_some,
                    node_list_item):
        """build node"""
        for gender in node_list_gender:
            gender_node = Node(self.invoice_gender, name=gender)
            self.graph.create(gender_node)
        for obj in node_list_obj:
            obj_node = Node(self.invoice_obj, name=obj)
            self.graph.create(obj_node)
        for kind in node_list_kind:
            kind_node = Node(self.invoice_kind, name=kind)
            self.graph.create(kind_node)
        for some in node_list_some:
            some_node = Node(self.invoice_some, name=some)
            self.graph.create(some_node)
        for item in node_list_item:
            item_node = Node(self.invoice_item, name=item)
            self.graph.create(item_node)

    def create_relation(self, df_data):
        """build relationship"""

        m = 0
        for m in range(0, len(df_data)):
            try:
                # (node1)-[:relationahip label]->(node2)
                rel = Relationship(self.graph.find_one(label=self.invoice_gender, property_key='gender', property_value=df_data['gender'][m]),
                                   df_data['kind'][m],
                                   self.graph.find_one(label=self.invoice_some, property_key='some', property_value=df_data['some'][m]))

                self.graph.create(rel)

            except AttributeError as e:
                print(e, m)