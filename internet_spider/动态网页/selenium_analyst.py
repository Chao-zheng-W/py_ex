from lxml import etree
import pandas as pd

with open('page_source.txt','r',encoding='utf-8') as f:
    page_source= f.read()

#复习lxml_etree的用法，找到“精品力作”的书名
data = etree.HTML(page_source)

print(data.xpath('//div[@class="img"]/img/@src'))  #这个例子没有text，要直接获取标签属性
print(data.xpath('//div[@class="img"]/img/@alt'))

df = pd.DataFrame({"url":data.xpath('//div[@class="img"]/img/@src'),'name':data.xpath('//div[@class="img"]/img/@alt')})
df.drop(index=[16,17],inplace=True)
print(df)


