import json
import requests
import pandas as pd

'''两种逆向分析方法获取到url
第一种：
通过在network，所有的包里面查找关键字，得到url

第二种：
查看网页源代码，找到程序员留下的注释。
比如这个例子中，在源代码中搜索“精品力作”，
可以得到注释  //获取精品力作列表
'''

url = 'https://www.ptpress.com.cn/masterpiece/getMasterpieceListForPortal'
rg = requests.get(url)

#print(rg.text)
#print(type(rg.text))

#str数据不好处理，改成dict
data = json.loads(rg.text)
#print(type(data))
#print(data)

'''
#遍历出图片url 和书名
picture_url=[]
bookname = []
for i in data['data']:
    picture_url.append(i['picPath'])
    bookname.append(i['bookName'])

dict = {'picture_url':picture_url,'bookname':bookname}
df = pd.DataFrame(dict)
df.to_csv('reverse_analysise.csv',encoding='utf-8')
'''

#更快捷的方法遍历和保存
picture_url = [i['picPath'] for i in data['data']]  #列表推导式
bookname = [i['bookName'] for i in data['data']]
df = pd.DataFrame({'picture_url':picture_url,'bookname':bookname})
df.to_csv('reverse_analysise.csv',encoding='utf-8',index=None)
