# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
import scrapy
import os
import urllib

class HtmlSpider(Spider):
    name = 'htmlspider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://www.baidu.com/'
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse,headers=self.headers)

    def parse(self, response):
        page = response.url.split("/")[-2]
        if not (os.path.isdir('./html')):
            os.mkdir('./html')
        filename = 'quotes-%s.html' % page
        images=response.xpath('//img/@src').extract()
        self.log("********************"+str(images))
        for imageurl in images:
            imagename=imageurl.split('/')[-1]
            with urllib.request.urlopen("http:"+imageurl)as imaf:
                data=imaf.read()
                f=open("./html/"+imagename, 'wb')
                f.write(data)
                f.close()
        with open("./html/"+filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


