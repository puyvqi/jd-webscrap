from scrapy.spider import Spider
from scrapy import Request

class jdspider(Spider):
    name="jdspider"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0',
        'Accept':'text / html, application / xhtml + xml, image / jxr, * / *'
        ,'Accept-Encoding':' gzip, deflate',
        'Proxy-Connection':'Keep-Alive'
        ,'Upgrade-Insecure-Requests':'1'
    }
    def start_requests(self):
        yield Request("http://home.jd.com/",headers=self.headers,cookies={

   '__jda': '122270672.1000774111.1507954732.1507961585.1507966095.5',
   '__jdb': '122270672.1.1000774111|5.1507966095',
   '__jdc': '122270672',
   '__jdu': '1000774111',
   '__jdv': '122270672|dmp|dmp_155|cpc|dmp_155_85776_d237257887538ee5c2472a502d8b62d0d4db0a2_1507958108|1507958112118',
   '_pst': 'puyvqi',
   '_tp': 'xl8jzq9MQ2Bv7oFtDkMj3A%3D%3D',
   '3AB9D23F7A4B3C9B': '3WLMYW3YOYTOKBU3JFTMYIRR2QLF6JJXJ5FN4KISBMRIYWKZVZPE2N5MC4NXXIIURJPJ2XQV5J733A25GQKND3CTF4',
   'ceshi3.com': '000',
   'cn': '0',
   'dmpjs': 'dmp-d237257887538ee5c2472a502d8b62d0d4db0a2',
   'pin': 'puyvqi',
   'pinId': '6FqIMs_J6BQ',
   'thor': '9F8FC82E6CCC682990C5C8603F626685E0290418087B4F43CD65D60C6DCB4E0B8C0AE2BB46AEA10D80657F8A86AD9A2E29F141412A5D80F00948E628DCDE06ED3003EF1D4E238536C510F40E14CBA63FE7AF8B6CB648245FE0E1B52C139ADF38129A6D1A7D2AE3E2051AF076BA408CD8D5C0AFEC6B0231657EF2A13D1C0F722C',
   'TrackID': '1HtCfbxVuv7swEanvrpBiC3dKFWzjnJDSnwce4brSWYcTDhZM9IxwSfjyaWO5Pfy-ltMiIe3UVb5bysNkLIegulcPhESmShFBAcwB-Dr7wBVf2XUmYTcOsIDdstux0Sys',
   'unick': 'puyvqi',
   'unpl': 'V2_ZzNtbUZVEB0nCkZTK0lVB2JRGltLB0odIQgUA38ZWQBgVxBUclRCFXMURlVnGVkUZwAZXUtcRxRFCEdkexhdBGcHFl9AUHMldDhFVEsRbAVmAhNbRFJDFXU4dlNLKQxQO1tNMx4VHBZ0CEBkfBFfAG8HElRHZ0IlfQ5HVHMZWgJmM1kzQxpDFHQJQFJ%2bGVwFVwIiXg%3d%3d',
   'userInfoaccountclouds': '1',
   'user-key': 'c89c9f2d-f3b8-496f-bf45-8e4ef92889c3'

        })
    def parse(self, response):
        with open("jd-home.html",'wb')as f:
            f.write(response.body)