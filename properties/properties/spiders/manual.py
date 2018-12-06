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
    allowed_domains = ['www.imooc.com']
    # start_urls = ['https://bj.5i5j.com/ershoufang/?pmf_group=baidu&pmf_medium=cpc&pmf_plan=%E4%BA%8C%E6%89%8B%E6%88%BF%E9%80%9A%E7%94%A8%E8%AF%8D&pmf_unit=%E4%BA%8C%E6%89%8B%E6%88%BF%E6%88%BF%E6%BA%90&pmf_keyword=%E4%BA%8C%E6%89%8B%E6%88%BF&pmf_account=36&pmf_id=8807669335']
    start_urls = ["http://www.imooc.com/course/list"]

    def parse(self, response):

        # get the next index URLs and yield Requests
        next_selector = response.xpath("//a[contains(text(),'下一页')]/@href")
        for url in next_selector.extract():
            yield Request(parse.urljoin(response.url, url))
        item_selector = response.xpath('/html/body//div[@class="course-card-container"]/a[@target="_blank"]//@href')
        for url in item_selector.extract():
            yield Request(parse.urljoin(response.url, url), callback=self.parse_item)


    def parse_item(self, response):

        item = PropertiesItem()

        item['url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract()[0]

        yield item
