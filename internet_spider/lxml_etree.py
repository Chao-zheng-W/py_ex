from lxml import etree
import requests
import pandas as pd

url = "http://tipdm.com/"  #发起响应
rg = requests.get(url)
print(rg.status_code)      #查看状态码，200表示正常
#print(rg.text)            #打印str内容

dom = etree.HTML(rg.text)   #结构化数据

#print(dom)                 #显示内存地址
print(dom.xpath('/html/head/title/text()'))  #绝对路径写法,获取<title>文本

#需求是提取泰迪公司产品中心 六个产品和描述
#先检索产品
print(dom.xpath('//a'))  #绝对路径写法，获取到了一堆，但是我们只要六个，所以缩小检索条件
print(dom.xpath('//a[@class = "tit"]'))   #确实六个
print(dom.xpath('//a[@class = "tit"]/text()'))  #看看内容
product_name = dom.xpath('//a[@class = "tit"]/text()')
#检索描述
print(dom.xpath('//p[@class = "desc"]'))          #获取到了一堆，但是我们只要六个，所以缩小检索条件
print(dom.xpath('//li/p[@class = "desc"]'))       #确实六个
print(dom.xpath('//li/p[@class = "desc"]/text()'))  #看看内容
product_desc = dom.xpath('//li/p[@class = "desc"]/text()')

#数据框形式形式存储，成为结构化数据
data = {
    'product_name': product_name,
    'product_desc': product_desc
}

df = pd.DataFrame(data)
df.to_csv('lxml_etree_data.csv',encoding='utf-8-sig',index=None)