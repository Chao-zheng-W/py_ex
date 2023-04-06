import pandas as pd

duptest = pd.read_csv('data\\duptest.csv',encoding='gbk')
print(duptest)

#检测缺失值
print(duptest.isnull())
print(duptest.notnull())

#处理缺失值
print(duptest.dropna(axis=0,how='all')) #删除有空值的行
print(duptest.dropna(axis=1,how='any')) #删除所有都为空值的列，在这个例子中啥也不剩
print(duptest.dropna(axis=0,how='all',subset=['order_id','dishs_name']))  #限定列中任何空值，删除行

#处理缺失值
print(duptest.fillna(method='bfill')) #用下面的值填充空值
