# -*- coding: utf-8 -*-
from dataToNeo4jClass.create_data_neo4j import DataToNeo4j
import os
import pandas as pd

# 輸入excel表格位址 將資料轉成dataframe
os.chdir('C:\\Users\\vincent\\Desktop\\neo4j_data')

node_data = pd.read_excel('./product_node.xlsx', header=0, encoding='utf8')
relation_data = pd.read_excel('./relationship_matrix.xlsx', header=0, encoding='utf8')

print(node_data)
print(relation_data)

# get node data
def data_extraction():

    # 取出性別到list
    node_list_gender = []
    for i in range(0, len(node_data)):
        node_list_gender.append(node_data['gender'][i])
    # 去除重複名稱
    node_list_gender = list(set(node_list_gender))

    # 取出型態到list
    node_list_type = []
    for i in range(0, len(node_data)):
        node_list_type.append(node_data['type'][i])
    # 去除重複名稱
    node_list_type = list(set(node_list_type))

    # 取出編號到list
    node_list_sn = []
    for i in range(0, len(node_data)):
        node_list_sn.append(node_data['sn'][i])
    # 去除重複名稱
    node_list_sn = list(set(node_list_sn))

    # 取出產品名稱到list
    node_list_name = []
    for i in range(0, len(node_data)):
        node_list_name.append(node_data['name'][i])
    # 去除重複名稱
    node_list_name = list(set(node_list_name))

    # 取出圖片網址到list
    node_list_img = []
    for i in range(0, len(node_data)):
        node_list_img.append(node_data['img'][i])
    # 去除重複名稱
    node_list_img = list(set(node_list_img))

    # 取出衣服說明到list
    node_list_des = []
    for i in range(0, len(node_data)):
        node_list_des.append(node_data['des'][i])
    # 去除重複名稱
    node_list_des = list(set(node_list_des))

    return node_list_gender, node_list_type, node_list_sn, node_list_name, node_list_img, node_list_des

# get relation
def relation_extraction():

    # links_dict = {}
    #
    # gender_list = []
    # type_list = []
    # sn_list = []
    # name_list = []
    # img_list = []
    # des_list = []
    # # 放置各node的資料
    #
    # for i in range(0, len(node_data)):
    #     j = 0
    #     try:
    #         gender_list.append(node_data[node_data.columns[j]][i])
    #         type_list.append(node_data[node_data.columns[j+1]][i])
    #         sn_list.append(node_data[node_data.columns[j+2]][i])
    #         name_list.append(node_data[node_data.columns[j+3]][i])
    #         img_list.append(node_data[node_data.columns[j+4]][i])
    #         des_list.append(node_data[node_data.columns[j+5]][i])
    #
    #     except:
    #         print("pop end")
    #
    # gender_list = [str(i) for i in gender_list]
    # type_list = [str(i) for i in type_list]
    # sn_list = [str(i) for i in sn_list]
    # name_list = [str(i) for i in name_list]
    # img_list = [str(i) for i in img_list]
    # des_list = [str(i) for i in des_list]
    #
    # # 將不同的資料建成一個graph
    # links_dict['gender'] = gender_list
    # links_dict['type'] = type_list
    # links_dict['sn'] = sn_list
    # links_dict['name'] = name_list
    # links_dict['img'] = img_list
    # links_dict['des'] = des_list

    # link_dict = {}
    # name_list = []
    # relation_list = []
    # name_list2 = []


    # data -> dataframe

    df_data = pd.DataFrame(node_data)
    rel_data = pd.DataFrame(relation_data)

    return df_data, rel_data


# print graph
data_extraction()
relation_extraction()
create_data = DataToNeo4j()

# bulid node
create_data.create_node(data_extraction()[0],
                        data_extraction()[1],
                        data_extraction()[2],
                        data_extraction()[3],
                        data_extraction()[4],
                        data_extraction()[5])

# build nodes between relation
create_data.create_relation(relation_extraction()[0], relation_extraction()[1])
print(relation_extraction())

