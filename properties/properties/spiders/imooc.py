# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
import datetime
import socket
from scrapy.http import Request
from urllib import parse
# from scrapytest.CourseItems import CourseItem


class BasicSpider(scrapy.Spider):
    name = 'imooc'
    allowed_domains = ['www.imooc.com']
    # start_urls = ['https://bj.5i5j.com/ershoufang/?pmf_group=baidu&pmf_medium=cpc&pmf_plan=%E4%BA%8C%E6%89%8B%E6%88%BF%E9%80%9A%E7%94%A8%E8%AF%8D&pmf_unit=%E4%BA%8C%E6%89%8B%E6%88%BF%E6%88%BF%E6%BA%90&pmf_keyword=%E4%BA%8C%E6%89%8B%E6%88%BF&pmf_account=36&pmf_id=8807669335']
    start_urls = ["http://www.imooc.com/course/list"]

    def parse(self, response):

        item = PropertiesItem()



        for box in response.xpath('/html/body//div[@class="course-card-container"]/a[@target="_blank"]'):
            item['title'] = box.xpath('.//h3/text()').extract()[0]
            item['url'] = box.xpath('.//@href').extract()[0]
            item['img_url'] = 'http:' + box.xpath('.//@src').extract()[0]
            item['student'] = box.xpath('.//span[2]/text()').extract()[0]
            item['introduction'] = box.xpath('.//p/text()').extract()[0]
            yield item


        # url 跟进
        # 获取下一页url信息
        url_next = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
        if len(url_next):
            page = 'http://www.imooc.com' + url_next[0]
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
            # page_url = parse.urljoin(response.url, url_next[0])
            # yield scrapy.Request(page_url, callback=self.parse)
        # url 跟进结束
