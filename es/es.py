#!/usr/bin/env python
# encoding: utf-8

# @author: adbibo
# @contact: laoliu.yin@gmail.com
# @file: es.py
# @time: 2018/7/17 下午4:09
# @desc:

import time
from os import walk

# import CSVOP
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class ElasticObj:
    def __init__(self, index_name, index_type, ip="127.0.0.1"):
        """
        :param index_name: 索引名称
        :param index_type: 索引类型
        """
        self.index_name = index_name
        self.index_type = index_type
        # 无用户名密码状态
        # self.es = Elasticsearch([ip])
        # 用户名密码状态
        self.es = Elasticsearch([ip], http_auth=('elastic', 'password'), port=9200)

    def create_index(self):
        """
        创建索引,创建索引名称为ott，类型为ott_type的索引
        :param ex: Elasticsearch对象
        :return:
        """
        # 创建映射
        _index_mappings = {
            "mappings": {
                self.index_type: {
                    "properties": {
                        "title": {
                            "type": "text",
                            "index": True,
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_max_word"
                        },
                        "date": {
                            "type": "text",
                            "index": True
                        },
                        "keyword": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "source": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "link": {
                            "type": "string",
                            "index": "not_analyzed"
                        }
                    }
                }

            }
        }
        if not self.es.indices.exists(index=self.index_name):
            res = self.es.indices.create(index=self.index_name, body=_index_mappings)
            print(res)

    def index_data(self):
        csv_dir = 'D:/work/ElasticSearch/exportExcels'
        file_name_list = []
        for (dir_path, dir_names, file_names) in walk(csv_dir):
            file_name_list.extend(file_names)
        total = 0
        for file in file_name_list:
            csv_file = csv_dir + '/' + file
            self.index_data_from_csv(csv_file)
            total += 1
            print(total)
            time.sleep(10)

    def index_data_from_csv(self, csv_file):
        """
        从CSV文件中读取数据，并存储到es中
        :param csv_file: csv文件，包括完整路径
        :return:
        """
        record_list = []
        with open(csv_file, 'r') as r_stream:
            for record in r_stream:
                record_list.append(record.split(','))
        index = 0
        doc = {}
        for item in record_list:
            if index > 1:  # 第一行是标题
                doc['title'] = item[0]
                doc['link'] = item[1]
                doc['date'] = item[2]
                doc['source'] = item[3]
                doc['keyword'] = item[4]
                res = self.es.index(index=self.index_name, doc_type=self.index_type, body=doc)
                print(res['result'])
            index += 1
            print("index data records: ".format(index))

    def index_data_from_example(self):
        """
        数据存储到es
        :return:
        """
        data_list = [
            {"date": "2017-09-13",
             "source": "慧聪网",
             "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
             "keyword": "电视",
             "title": "付费 电视 行业面临的转型和挑战"
             },
            {"date": "2017-09-13",
             "source": "中国文明网",
             "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
             "keyword": "电视",
             "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
             }
        ]
        for item in data_list:
            res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item)
            print(res['result'])

    def bulk_index_data(self):
        """
        用bulk将批量数据存储到es
        :return:
        """
        data_list = [
            {"date": "2017-09-13",
             "source": "慧聪网",
             "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
             "keyword": "电视",
             "title": "付费 电视 行业面临的转型和挑战"
             },
            {"date": "2017-09-13",
             "source": "中国文明网",
             "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
             "keyword": "电视",
             "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
             },
            {"date": "2017-09-13",
             "source": "人民电视",
             "link": "http://tv.people.com.cn/BIG5/n1/2017/0913/c67816-29533981.html",
             "keyword": "电视",
             "title": "中国第21批赴刚果（金）维和部隊启程--人民 电视 --人民网"
             },
            {"date": "2017-09-13",
             "source": "站长之家",
             "link": "http://www.chinaz.com/news/2017/0913/804263.shtml",
             "keyword": "电视",
             "title": "电视 盒子 哪个牌子好？ 吐血奉献三大选购秘笈"
             }
        ]
        ACTIONS = []
        i = 1
        for line in data_list:
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_id": i,  # _id 也可以默认生成，不赋值
                "_source": {
                    "date": line['date'],
                    "source": line['source'],
                    "link": line['link'],
                    "keyword": line['keyword'],
                    "title": line['title']}
            }
            i += 1
            ACTIONS.append(action)
            # 批量处理
        success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)
        print('Performed %d actions' % success)

    def delete_index_data(self, id):
        """
        删除索引中的一条
        :param id:
        :return:
        """
        res = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
        print(res)

    def get_data_by_id(self, id):
        res = self.es.get(index=self.index_name, doc_type=self.index_type, id=id)
        print(res['_source'])
        print('------------------------------------------------------------------')
        # # 输出查询到的结果
        for hit in res['hits']['hits']:
            # print hit['_source']
            print('\t'.join(
                [hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'],
                 hit['_source']['title']]))

    def get_data_by_body(self):
        doc = {
            "query": {
                "match": {
                    "keyword": "电视"
                }
            }
        }
        _searched = self.es.search(index=self.index_name, doc_type=self.index_type, body=doc)

        for hit in _searched['hits']['hits']:
            # print hit['_source']
            print(''.join(
                [hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'],
                 hit['_source']['title']]))


if __name__ == '__main__':
    # 建立ES链接
    obj = ElasticObj("ott", "ott_type", ip="localhost")
    # 插入示例数据
    # obj.index_data_from_example()

    # 查询
    obj.get_data_by_body()

# obj.create_index()
# obj.bulk_index_data()
# obj.index_data()
# obj.Delete_Index_Data(1)

# csv_file = 'D:/work/ElasticSearch/exportExcels/2017-08-31_info.csv'
# obj.index_data_from_csv(csv_file)
# obj.GetData(es)
