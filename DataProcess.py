#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
from elasticsearch import Elasticsearch
import time
host = "10.245.142.213"
port = 9200
index = "au_pkt_dns"
field = "i_domain"
# time_window = "\"range\": {'@timestamp': {'gt': 'now-5m'}}"
time_window = "\"range\": {'@timestamp': {'lt': '0'}}"


def result_append(result, records):
    for record in records:
        result.append(record['_source']['i_domain'])


print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))
es = Elasticsearch([{"host": host, "port": port}])
query = es.search(
    index=index,
    scroll="1m",
    size=100,
    filter_path=['_scroll_id', 'hits.total', 'hits.hits._source.i_domain']
)

scroll_id = query['_scroll_id']
total = query['hits']['total']['value']
records = query['hits']['hits']
result = []

result_append(result=result, records=records)

for i in range(0, int(total/100)+1):
    records = es.scroll(scroll_id=scroll_id, scroll="1m")['hits']['hits']
    result_append(result=result, records=records)

print(len(result))
print(result)
print(time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(time.time())))
# print(scroll_id)
# print(total)
# print(records)
# print(result)

# es.scroll()



# with open('./BLACKLIST/hello.txt', 'w', newline='', encoding='utf-8') as flow:
#     # csv_writer = csv.writer(flow)
#     flow.writelines('hello world')
#     # csv_writer.writerow(haha)



