import pandas as pd
date_txt = pd.read_csv('data\\testdata.txt',sep=' ') #源文件中是空格为分隔符
print(date_txt)

date_csv = pd.read_csv('data\\testdata2.csv',sep=',',encoding='utf-8')
print(date_csv)

#存储数据框到文件中
date_csv.to_csv('data\\todata.csv',index=None,header=None) #如果不需要首列索引，index;不需要列名称，header