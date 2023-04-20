import scrapy
from myspider.items import MyspiderItem
import pandas as pd

class TipdmnewsSpider(scrapy.Spider):
    name = "tipdmnews"
    allowed_domains = ["www.tipdm.com"]
    start_urls = ["http://www.tipdm.com/gsxw/index.jhtml"]

    def parse(self, response):
        item = MyspiderItem()
        #item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/@data')  #取出空白
        item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/text()').extract()  #取出文本
        #item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/text()')  #取出一整个标签

        return item
#未启用管道，直接使用命令scrapy crawl tipdmnews -o test.csv
#调试很麻烦
