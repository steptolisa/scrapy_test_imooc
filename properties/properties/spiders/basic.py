# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import datetime
import socket

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://bj.5i5j.com/ershoufang/42002403.html']
    def parse(self, response):
        """ This is a function parses a scrapy.org page.

        @url https://scrapy.org/
        @returns items 1
        @scrapes title url spider date server
        """

        # self.log("title: %s" % response.xpath('title//text()').extract_first())
        l = ItemLoader(item=PropertiesItem(), response=response)
        # item['title'] = response.xpath('//title/text()').extract_first()


        l.add_xpath('title', '/html/body/div[1]/div/div[1]/a/text()')
        # 添加python计算得出的单个值， 而不是xpath，css 表达式
        l.add_value('spider', self.name)
        l.add_value('url', response.url)
        l.add_value('date', datetime.datetime.now())
        l.add_value('server', socket.gethostname())

        # {'title': ['Scrapy | A Fast and Powerful Scraping and Web Crawling Framework'],
         # 'url': ['https://scrapy.org']}



        return l.load_item()


