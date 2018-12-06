# coding:utf-8
# python 3.6

__author__ = 'dht'
__creattm = '20181206'
__usefor__ = ''


import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    # 通过抓取图片的url获取一个Request用于下载
    def get_media_requests(self, item, info):
        # 返回Requet根据图片url下载
        yield scrapy.Request(item['img_url'])

    # 当下载请求完成后执行该方法
    def item_completed(self, results, item, info):
        # 获取下载地址
        image_path = [x['path'] for ok, x in results if ok]
        # 判断是否成功
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_path'] = image_path
        return item