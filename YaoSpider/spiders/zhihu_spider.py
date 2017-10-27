# -*- coding: utf-8 -*-
import scrapy,time
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy import FormRequest

class Login(Spider):

    name = 'zhihu_login'

    start_urls = ['https://www.zhihu.com' ]
    custom_settings = {'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3026.3 Safari/537.36'}


    def parse(self, response):
        formadata = {
            'password': 'zjy2580925?',
            'phone_num': '15754604139',
            'email': 'yaodi163@163.com'
        }
        return FormRequest.from_response(
                                  url='https://www.zhihu.com/login/{}'.format('phone_num'
                                                                          if formadata['phone_num'] else 'email'), # post 的网址
                                  method="POST", # 也是默认值, 其实不需要指定
                                  response=response,
                                  formxpath='//form[1]', # 使用第一个form, 其实就是默认的, 这里明确写出来
                                  formdata=formadata, # 我们填写的表单数据
                                  callback=self.after_login, # 登录完成之后的处理
                                  dont_click=True)

    def after_login(self,response):
        # 命令行调试代码
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        print "login_success"