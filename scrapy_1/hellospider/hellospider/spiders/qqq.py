# -*- coding: utf-8 -*-
import scrapy


class QqqSpider(scrapy.Spider):
    name = 'qqq'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
