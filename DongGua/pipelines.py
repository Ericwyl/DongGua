# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from openpyxl import Workbook

# class DongguaPipeline(object):
#     def __init__(self):
#         print('__init__')
#         self.filename = open('DongGua.json',mode='w',encoding='utf-8')
#
#     def process_item(self, item, spider):
#         dict_str = dict(item)
#         json_text = json.dumps(dict_str,ensure_ascii=False)+'\n'
#         print('dict_str==',type(dict_str))
#         self.filename.write(json_text)
#         return item
#
#     def close_spider(self,spider):
#         print('close_spider...')
#         self.filename.close()
#
#     def _item(self,item,spider):
#         with open('DongGua.json','a') as f:
#             json.dump(dict(item), f ,ensure_ascii=False)
#             f.write('\n')
#         return item


# class ExcelPipeline(object):
#     def __init__(self):
#         self.wb = Workbook()
#         self.ws = self.wb.active
#         #设置镖头
#         self.ws.append(['targetname'],['targetid'],['targetsequence'],['targetsynonyms'],['targetsource'],['targetstructure']
#                        ,['comments'],['targettype'])
#
#     def process_item(self,item,spider):
#         line = [item['targetname'],item['targetid'],item['targetsequence'],item['targetsynonyms'],item['targetsource'],item['targetstructure'],item['comments'],item['targettype']]
#         self.ws.append(line)
#         self.wb.save('dg.xlsx')
#         return item



from scrapy.exporters import CsvItemExporter

class DongguaPipeline(object):
    def open_spider(self, spider):
        self.file = open("/home/ericwei/DongGua/exceldata.xlsx", "wb")
        self.exporter = CsvItemExporter(self.file,
        fields_to_export=["targetname", "targetid", "targetsequence","targetsynonyms","targetsource","targetstructure","comments","targettype"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


