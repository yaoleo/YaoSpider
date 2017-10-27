# coding: utf-8
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # 爬虫标识 一个project里必须唯一

    def start_requests(self):# 初始请求 可以是列表 也可以是 生成函数
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 每个初始Url完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数
        # 该方法负责  解析返回的数据(response data)，
        #           提取数据(生成item)以及
        #           生成需要进一步处理的URL的 Request 对象。
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)