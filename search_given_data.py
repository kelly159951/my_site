import json
import pymysql
from elasticsearch import Elasticsearch
import mysql.connector
es = Elasticsearch("http://localhost:9200")


def name_search(cin):
#只能完全匹配一个人名
    name_query={
        "query":{
            "match":{
                "author_name":{
                    "query":cin,
                    "fuzziness":2
                }
            }
        }
    }
    shell0=es.search(index="allpdf_1",body=name_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

def affiliation_search(cin):

    affiliation_query={
        "query":{
            "match":{"author_affiliation":cin}
        }
    }
    shell0=es.search(index="allpdf_1",body=affiliation_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result
    
def title_search(cin):
    title_query={
        "query":{
            "match":{
                "title":{
                    "query":cin,
                    "fuzziness":3
                }
            }
        }
    }
    shell0=es.search(index="allpdf_1",body=title_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result
    
def keywords_search(cin):
    keywords_query={
        "query":{
            "match":{
                "keywords":{
                    "query":cin,
                    "fuzziness":5
                }
            }
        }
    }
    shell0=es.search(index="allpdf_1",body=keywords_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result
    
def abstract_search(cin):
    abstract_query={
        "query":{
            "match":{
                "abstract":{
                    "query":cin,
                    "fuzziness":5
                }
            }
        }
    }
    shell0=es.search(index="allpdf_1",body=abstract_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

def journal_search(cin):
#只能完全匹配
    journal_query={
        "query":{
            "match":{"journal":cin}
        }
    }
    shell0=es.search(index="allpdf_1",body=journal_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

def doi_search(cin):
#只能完全匹配
    doi_query={
        "query":{
            "match":{"doi":cin}
        }
    }
    shell0=es.search(index="allpdf_1",body=doi_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

def publisher_search(cin):
#只能完全匹配
    publisher_query={
        "query":{
            "match":{"publisher":cin}
        }
    }
    shell0=es.search(index="allpdf_1",body=publisher_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

def all_search(cin):
    all_query={
        "query":{
           "bool": {
			    "should": [{
				    "multi_match": {
					    "query": cin,
					    "fields": ["keywords","title", "abstract"]
				    }
			    }]
		    }
        }
    }
    shell0=es.search(index="allpdf_1",body=all_query,filter_path=['hits.hits._source.title','hits.hits._source.author_name','hits.hits._source.keywords','hits.hits._source.abstract','hits.hits._source.journal','hits.hits._source.link',])
    shell1=shell0["hits"]
    shell2=shell1["hits"]
    result=[]
    for i in shell2:
        result.append(i["_source"])
    return result

print(name_search("R.W. Carlson"))




