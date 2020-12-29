# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EstateInsightPipeline:
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.estate_set = set()

    def process_item(self, item, spider):
        mls_num = item['MLS#']
        if mls_num in self.estate_set:
            return None
        else:
            self.estate_set.add(mls_num)
            return item