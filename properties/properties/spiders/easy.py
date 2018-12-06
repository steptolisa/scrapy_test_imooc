# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from properties.items import PropertiesItem

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['www.imooc.com']
    # start_urls = ['https://bj.5i5j.com/ershoufang/?pmf_group=baidu&pmf_medium=cpc&pmf_plan=%E4%BA%8C%E6%89%8B%E6%88%BF%E9%80%9A%E7%94%A8%E8%AF%8D&pmf_unit=%E4%BA%8C%E6%89%8B%E6%88%BF%E6%88%BF%E6%BA%90&pmf_keyword=%E4%BA%8C%E6%89%8B%E6%88%BF&pmf_account=36&pmf_id=8807669335']
    start_urls = ["http://www.imooc.com/course/list"]

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[contains(text(),'下一页')]")),
        Rule(LinkExtractor(restrict_xpaths='/html/body//div[@class="course-card-container"]/a[@target="_blank"]'),
             callback='parse_item')
    )

    # def parse_item(self, response):
    #     i = {}
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i

    def parse_item(self, response):

        item = PropertiesItem()

        item['url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract()[0]

        yield item
