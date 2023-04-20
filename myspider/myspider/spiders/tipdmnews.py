import scrapy
from myspider.items import MyspiderItem
import pandas as pd

class TipdmnewsSpider(scrapy.Spider):
    name = "tipdmnews"
    allowed_domains = ["www.tipdm.com"]
    start_urls = ["http://www.tipdm.com/gsxw/index.jhtml"]

    def parse(self, response):
        item = MyspiderItem()
        #item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/@data')  #ȡ���հ�
        item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/text()').extract()  #ȡ���ı�
        #item['title'] = response.xpath('//*[@id="t251"]/div/div[3]/h1/a/text()')  #ȡ��һ������ǩ

        return item
#δ���ùܵ���ֱ��ʹ������scrapy crawl tipdmnews -o test.csv
#���Ժ��鷳
