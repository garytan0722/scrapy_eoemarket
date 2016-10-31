# -*- coding: utf-8 -*-
import scrapy
from apk.items import ApkItem
class apkspider(scrapy.Spider):
    name = "app"
    allowed_domains = ["www.eoemarket.com","d2.eoemarket.com"]
    start_urls = []
    for i in range(5,7):
        link="http://www.eoemarket.com/soft/1_hot_unofficial_hasad_1_%d.html" %i
        start_urls.append(link)
    print(start_urls)
    def parse(self, response):
        res=response.xpath('//div[@class="classf_list_item_c"]/a/@href').extract()
        print (res)
        for i in range(len(res)):
            url="http://www.eoemarket.com"+res[i]
            print("URL:"+url)
            yield scrapy.Request(url, callback=self.parse_dir_contents)
    def parse_dir_contents(self, response):
        res=response.xpath('//span[@class="download_intr"]/a/@href').extract()
        
        yield scrapy.Request(res[0], callback=self.download)
        #
        #
    def download(self, response):
        #print("!!!!!")        
        #print (type(response))
        #print (re)
        link=response.url
        result=link.split("?")
        print result
        myitem = ApkItem()
        myitem["file_urls"]=[result[0]]
        yield myitem