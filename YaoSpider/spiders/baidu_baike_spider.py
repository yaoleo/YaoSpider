# -*- coding: utf-8 -*-
import scrapy
from YaoSpider.items import BaiduBaikeItem


class BaiduBaikeSpider(scrapy.Spider):
    name = 'baidubaike'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://baike.baidu.com/item/%E8%8C%83%E5%86%B0%E5%86%B0'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        print "success"
        item = BaiduBaikeItem()

        name = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract()

        titles = response.xpath('//h2[@class="title-text"]/text()').extract()

        links = response.xpath('//a[@target="_blank"]/text()').extract()

        for title in titles:
            print title
        for link in links:
            print link
        print name[0].encode('utf-8')

