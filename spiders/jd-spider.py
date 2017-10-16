import re
import json
from scrapy import Request
from scrapy.spiders import Spider

class jdSpider(Spider):
    name = 'jd'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv16416&productId=5025518&score=0&sortType=5&page=5&pageSize=10&isShadowSku=0&fold=1'
        yield Request(url, headers=self.headers)
    def parse(self, response):
        url=response.url
        productid = re.search(r'productId=(\d+)',response.url).group(1)

        pagenum=re.search(r'page=(\d+)',url).group(1)
        nextpage=int(pagenum)+1
        if nextpage>105:
            return
        with open(productid+"_"+pagenum+".txt",'wb')as f:
            f.write(response.body)
        sub="page="+str(nextpage)
        next_url = re.sub(r'page=\d+', sub, response.url)
        yield Request(next_url, headers=self.headers)