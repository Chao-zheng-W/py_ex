from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://tipdm.com/"  #发起响应
rg = requests.get(url)
print(rg.status_code)      #查看状态码，200表示正常
#print(rg.text)            #打印str内容

soup = BeautifulSoup(rg.text,features='lxml')  #解析网页
#print(soup)  #打印soup内容，和rg.text一样

'''
可以直接打印标签，返回第一出现
print(soup.title)
print(soup.a)
print(soup.li)
'''

print(soup.select('html > head > title'))  #用大于号连接的绝对路径
print(soup.select('html > head > title')[0].text)  #这是一个列表，在外层取索引0，然后text

#需求是提取泰迪公司产品中心 六个产品
print(soup.select('div[class = "bd"] > a[class = "tit"]'))  #空列表，说明>要直接连接的，父子关系节点，爷孙关系就不行
print(soup.select('li > a[class = "tit"]'))                 #这个可以，因为是父子节点
print(soup.select('div[class = "bd"]  a[class = "tit"]'))   #用空格代替>,相对路径，父子关系节点，爷孙关系都可以


#存储
product_name_tag = soup.select('div[class = "bd"]  a[class = "tit"]')
product_name = []
for i in product_name_tag:
    product_name.append(i.text)
print(product_name)