# -*- coding: utf-8 -*-
from dataToNeo4jClass.create_data_neo4j import DataToNeo4j
import os
import pandas as pd

# 輸入excel表格位址 將資料轉成dataframe
os.chdir(' ')

invoice_data = pd.read_excel(' ', header=0, encoding='utf8')
print(invoice_data)

# get node data
def data_extraction():

    # 取出性別到list
    node_list_gender = []
    for i in range(0, len(invoice_data)):
        node_list_gender.append(invoice_data['性別'][i])
    # 去除重複名稱
    node_list_gender = list(set(node_list_gender))

    # 取出obj_name到list
    node_list_obj = []
    for i in range(0, len(invoice_data)):
        node_list_obj.append(invoice_data['obj_name'][i])
    # 去除重複名稱
    node_list_obj = list(set(node_list_obj))

    # 取出衣服種類到list
    node_list_kind = []
    for i in range(0, len(invoice_data)):
        node_list_kind.append(invoice_data['衣服種類'][i])
    # 去除重複名稱
    node_list_kind = list(set(node_list_kind))

    # 取出衣服細項到list
    node_list_some = []
    for i in range(0, len(invoice_data)):
        node_list_some.append(invoice_data['衣服細項'][i])
    # 去除重複名稱
    node_list_some = list(set(node_list_some))

    # 取出品項名稱到list
    node_list_item = []
    for i in range(0, len(invoice_data)):
        node_list_item.append(invoice_data['品項名稱'][i])
    # 去除重複名稱
    node_list_item = list(set(node_list_item))

    return node_list_gender, node_list_obj, node_list_kind, node_list_some, node_list_item

def relation_extraction():
    """make relationship"""

    links_dict = {}
    gender_list = []
    # obj_list = []
    kind_list = []
    some_list = []
    item_list = []
    # 放置各node的資料

    for i in range(0, len(invoice_data)):
        j = 0
        try:
            gender_list.append(invoice_data[invoice_data.columns[j]][i])
            # obj_list.append(invoice_data[invoice_data.columns[j+1]][i])
            kind_list.append(invoice_data[invoice_data.columns[j+2]][i])
            some_list.append(invoice_data[invoice_data.columns[j+3]][i])
            item_list.append(invoice_data[invoice_data.columns[j+4]][i])

        except:
            print("pop end")

    gender_list = [str(i) for i in gender_list]
    kind_list = [str(i) for i in kind_list]
    some_list = [str(i) for i in some_list]
    item_list = [str(i) for i in item_list]

    # 確認list資料
    print(gender_list)
    # print(obj_list)
    print(kind_list)
    print(some_list)
    print(item_list)

    # 將不同的資料建成一個graph
    links_dict['gender'] = gender_list
    # links_dict['obj'] = obj_list
    links_dict['kind'] = kind_list
    links_dict['some'] = some_list
    links_dict['item'] = item_list

    # data -> dataframe
    df_data = pd.DataFrame(links_dict)
    return df_data


# print graph
data_extraction()
relation_extraction()
create_data = DataToNeo4j()

# bulid node
create_data.create_node(data_extraction()[0],
                        data_extraction()[1],
                        data_extraction()[2],
                        data_extraction()[3],
                        data_extraction()[4])

# build nodes between relation
create_data.create_relation(relation_extraction())
print(relation_extraction())
