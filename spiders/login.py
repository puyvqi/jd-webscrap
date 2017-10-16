import json
import re
from scrapy import Request
from scrapy.spider import Spider
from scrapy.http import FormRequest
class loginspider(Spider):
    name = 'login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows N'
                      'T 6.1; Win64; x64) AppleW'
                      'ebKit/537.36 (KHTML, like Gecko) Ch'
                      'rome/53.0.2785.143 Safari/537.36',

    }
    def start_requests(self):
        yield Request("https://github.com/login",headers=self.headers,callback=self.parse)
    def parse(self,response):
        return FormRequest.from_response(response=response,formdata={'login':'729276581@qq.com','password':'a8694586'},callback=self.login)
    def login(self,response):
        with open("loginpage3.html",'wb')as f:
            f.write(response.body)

            return
