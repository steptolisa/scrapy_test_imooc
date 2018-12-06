# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import datetime
import socket
from scrapy.http import Request
from urllib import parse

class BasicSpider(scrapy.Spider):
    name = 'manual'
    allowed_domains = ['web']
    start_urls = ['https://bj.5i5j.com/ershoufang/?pmf_group=baidu&pmf_medium=cpc&pmf_plan=%E4%BA%8C%E6%89%8B%E6%88%BF%E9%80%9A%E7%94%A8%E8%AF%8D&pmf_unit=%E4%BA%8C%E6%89%8B%E6%88%BF%E6%88%BF%E6%BA%90&pmf_keyword=%E4%BA%8C%E6%89%8B%E6%88%BF&pmf_account=36&pmf_id=8807669335']

    def parse(self, response):

        # Get the next index URLs and yield Requests
        next_selector = response.xpath('/html/body//a[@class="cPage"]/@href')
        for url in next_selector.extract():
            yield Request(parse.urljoin(response.url, url))

        # get item URLs and yield Requests
        item_selector = response.xpath('/html/body//h3/a/@href')
        for url in item_selector.extract():
            yield Request(parse.urljoin(response.url, url), callback=self.parse_item)



    def parse_item(self, response):
        """ This is a function parses a scrapy.org page.

        @url https://scrapy.org/
        @returns items 1
        @scrapes title url spider date server
        """

        # self.log("title: %s" % response.xpath('title//text()').extract_first())
        l = ItemLoader(item=PropertiesItem(), response=response)
        # item['title'] = response.xpath('//title/text()').extract_first()


        # l.add_xpath('title', '/html/body/div[1]/div/div[1]/a/text()')
        # 添加python计算得出的单个值， 而不是xpath，css 表达式
        l.add_value('spider', self.name)
        l.add_value('url', response.url)
        l.add_value('date', datetime.datetime.now())
        l.add_value('server', socket.gethostname())

        # {'title': ['Scrapy | A Fast and Powerful Scraping and Web Crawling Framework'],
         # 'url': ['https://scrapy.org']}



        return l.load_item()
