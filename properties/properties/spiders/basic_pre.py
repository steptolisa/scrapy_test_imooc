# -*- coding: utf-8 -*-
import scrapy
from properties.itemsold import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import datetime
import socket
class BasicPreSpider(scrapy.Spider):
    name = 'basic_pre'
    allowed_domains = ['web']
    start_urls = ['https://scrapy.org/']

    def parse(self, response):
        """ This is a function parses a scrapy.org page.

        @url https://scrapy.org/
        @returns items 1
        @scrapes title url part_text date server
        """

        # self.log("title: %s" % response.xpath('title//text()').extract_first())
        l = ItemLoader(item=PropertiesItem(), response=response)
        # item['title'] = response.xpath('//title/text()').extract_first()


        l.add_xpath('title', '//title/text()')
        l.add_xpath('url', '//*[@id="link-logo"][@href]', re='(http.+?)"')
        l.add_xpath('part_text', '/html/body/div[2]/div/div[3]/div/div[1]/h3/text()', MapCompose(str.strip, str.title))
        # l.add_xpath('h', '/html/body/div[2]/div/div[3]/div/div[1]/h3/text()')
        # 添加python计算得出的单个值， 而不是xpath，css 表达式
        l.add_value('date', datetime.datetime.now())
        l.add_value('server', socket.gethostname())

        # {'title': ['Scrapy | A Fast and Powerful Scraping and Web Crawling Framework'],
         # 'url': ['https://scrapy.org']}



        return l.load_item()
