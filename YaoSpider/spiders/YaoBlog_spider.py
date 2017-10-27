# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
class BlogSpider(Spider):
    name = 'yaoleo'
    start_urls = ['https://yaoleo.github.io']
    def parse(self, response):
        #titles = response.xpath('//a[@class="post-title-link"]/text()').extract()

        #print response.xpath('//a[@class="post-title-link"]/text()')
       # for title in titles:
            #print title.strip()
        print "yaoleo"
        heads = response.xpath('//h1/text()').extract()
        for head in heads:
            print head