# neo4j-python-pandas-py2neo-v3
利用pandas將excel中的數據取出，並根據不同需求將資料上傳到neo4j建立graph database

### 1.環境：  
python3.7.2  
windows10  
請先安裝requirements.txt
```
pip install -r requirements.txt
``` 

### 2.Pandas抽取excel数据

自訂函數data_extraction和函數relation_extrantion
分別取出建立知識圖譜的node跟relationship
先利用pandas將excel轉成dataframe的型態再進行操作  

### 3.建立知識圖譜需要的node與relationship 
1. create_data_neo4j.py  
2. clothes_neo4j.py

### 4.連接neo4j

先進入neo4j的網站下載資料庫主程式

https://neo4j.com/

在create_data_neo4j中定義路徑並呼叫

loacl端網址, user, password (在graph內自行設定)

```
graph anme = Graph(
                    "http://xxxxxx/xxxx",
                    username="xxxxxx",
                    password="xxxxxx"
                    )
```

