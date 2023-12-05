import json
import pymysql
from elasticsearch import Elasticsearch
import mysql.connector

es = Elasticsearch("http://localhost:9200")
pdf_mappings = {
     "settings": {
        "index": {
            "analysis": {
                "analyzer": {
                    "my_analyze": {
                        "type": "pattern",
                        "pattern": ";"
                    },
                    "my_analyze_2":{
                        "type": "pattern",
                        "pattern": ","
                    }
                }
            }
        }
    },
    "mappings" : {
        "properties": {
            "id":{
                "type":"keyword",
            },

            "author_name":{
                "type": "text",
                "analyzer":"my_analyze"
            },
            "author_affiliation": {
               "type": "text",
                "analyzer":"my_analyze"
            },
            "title": {
                "type": "text",
                "analyzer": "stop",
                "boost": "2.0"
            },
            "keywords": {
                "type": "text",
                "analyzer": "stop",
                "boost":"1.7"
            },
            "abstract":{
                "type":"text",
                "analyzer":"stop",
                "boost":"1.5"
            },
            "doi": {
                "type": "keyword"
            },
                    "publisher": {
                        "type": "keyword",
                    },
                    "journal":{
                        "type":"keyword",
                    },
                    "issn":{
                        "type":"keyword",
                    },
                    "firstpage":{
                        "type":"integer",
                        "index":"false"
                    },
                    "lastpage":{
                        "type":"integer",
                        "index":"false"
                    },
                    "volume":{
                        "type":"integer",
                        "index":"false"
                    },
            "link":{
                "type":"keyword",
                "index":"false"
            }
        }
    }
}
es.indices.create(index='test_time_out', body=pdf_mappings)
try:
    conn = mysql.connector.connect(host='127.0.0.1',
                            port=3306,
                            user='root',
                            passwd='Zty@20040530',
                            charset='utf8',
                            db='100_pdf',
                            #table="daxue"
                            )
    cursor = conn.cursor()
except:
    print('Fail to connect to the database.')

cursor.execute('SELECT * FROM 100_pdf_metadata')
content = cursor.fetchall()

# 导入数据
id=0
for i in content:
    elem = {
        "id": i[0],
        "keywords": i[4],
        "author_name": i[6],
        "author_affiliation": i[7],
        "lastpage": i[8],
        "link": i[9],
        "abstract":i[10],
        "title":i[11],
        "volume":i[12],
        "journal":i[14],
        "issn":i[15],
        "firstpage":i[16],
        "publisher":i[17],
        "doi":i[18]
        # "bookmard_count": int(i[6])
    }
    es.index(index="test_time_out", id=id, body=elem)
    id += 1


