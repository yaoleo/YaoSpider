# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import re
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
from YaoSpider.items import EduItem


class EduSpider(scrapy.Spider):
    name = 'eduspider'

    url = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://cse.seu.edu.cn'

        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        #html = response.xpath('//html[]/text()').extract()
        html =  "".join([word.encode("utf-8") for word in response.text])
        htmlname = response.url
        f = open(htmlname[7:20]+".html","w")
        f.write(html)
        f.close()

        sel = Selector(response)
        urls = sel.xpath('//a/@href').extract()
        urls = [url for url in urls if url[-6:] == "edu.cn" or url[-7:] == "edu.cn/"]
        for url in urls:
            print 'yielding ',url
            yield scrapy.Request(url, callback=self.parse)
        print "success"


