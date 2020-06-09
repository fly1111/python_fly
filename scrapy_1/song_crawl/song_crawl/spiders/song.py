# -*- coding: utf-8 -*-
import scrapy

from song_crawl.items import SongCrawlItem

class SongSpider(scrapy.Spider):
    name = 'song'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            songcrawl = SongCrawlItem()
            songcrawl['serial_number']=i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            songcrawl['movie_name']=i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//span[1]/text()").extract_first()
            content=i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[1]/text()").extract()
            content_s = []
            for i_content in content:
                content_s.append( i_content.replace(" ",""))
                
            songcrawl['introduce'] ="".join(content_s)
            songcrawl['star']=i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            songcrawl['evaluate']=i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            songcrawl['describe']=i_item.xpath(".//span[@class='inq']/text()").extract_first()
            yield songcrawl
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
