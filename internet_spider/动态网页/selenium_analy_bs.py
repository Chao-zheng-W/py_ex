from bs4 import BeautifulSoup
import pandas as pd

with open('page_source.txt','r',encoding='utf-8') as f:
    page_source= f.read()

#复习lxml_etree的用法，找到“精品力作”的书名
soup = BeautifulSoup(page_source,features='lxml')

print(soup.select('div[class = "img"]  img'))  #就是这个东西
bookname = [ i['alt'] for i in soup.select('div[class = "img"]  img')]
url = [ i['src'] for i in soup.select('div[class = "img"]  img')]

df = pd.DataFrame({"url":url,'name':bookname})
df.drop(index=[16,17],inplace=True)
print(df)

