# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DongGua.items import DongguaItem


class DongguaSpider(CrawlSpider):
    name = 'donggua'
    allowed_domains = ['immunet.cn']
    start_urls = ['http://immunet.cn/bdb/index.php/target/index?page=1']
    rules = (
        #符合http://immunet.cn/bdb/index.php/target/1的表达式
        Rule(LinkExtractor(allow=r'target/+\d'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'index?page=\d')),

    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        try:

            item = DongguaItem()
            url = response.url
            print('url11111111111111111111',url)
            # titles = response.xpath('//*[@id="se_unitMDAU"]/div/div/form/table[1]/tbody/tr/td/a').extract()[0]
            targetname = response.xpath('//td[@class="mdauCategory"]//a//text()').extract()
            print('targetname222222222222',targetname)

            targetid = response.xpath('//td[@class="mdauData"]//a/text()').extract()[0]
            print('id33333',targetid)

            # targettype = response.xpath('//table[2]/tbody/tr[2]/td[4]').xpath('string(.)').extract()
            targettype = response.xpath('//tbody[@class="content"]//tr//td[@class="mdauData"]/text()').extract()[0]
            print('type4444444',targettype)

            targetsequence = response.xpath('//table[@class="contentNB"]//tbody[@class="content"]//tr[3]//td[@class="mdauData"]//text()').extract()
            print('5555555555',targetsequence)

            targetsynonyms = response.xpath('//tbody[@class="content"]//tr[4]//td[@class="mdauData"]//text()').extract()
            print('66666666666',targetsynonyms)

            targetsource = response.xpath('//table[@class="contentNB"]//tbody[@class="content"]//tr[5]//td[@class="mdauData"]//text()').extract()
            print('7777',targetsource)

            targetstructure = response.xpath('//table[@class="contentNB"]//tbody[@class="content"]//tr[6]//td[@class="mdauData"]//text()').extract()
            print('88888',targetstructure)
            comments = response.xpath('//table[@class="contentNB"]//tbody[@class="content"]//tr[7]//td[@class="mdauData"]//text()').extract()
            print('99999',comments)

            item['url'] = url
            item['targetname'] = targetname
            item['targetid'] = targetid
            item['targettype'] = targettype
            item['targetsequence'] = targetsequence if targetsequence else None
            item['targetsynonyms'] = targetsynonyms if targetsynonyms else None
            item['targetsource'] = targetsource
            item['targetstructure'] = targetstructure
            item['comments'] = comments
            yield item

        except Exception as e:
            print('出错了:e==',e,response.url)

