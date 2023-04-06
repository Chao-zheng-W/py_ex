import pandas as pd

duptest = pd.read_csv('data\\duptest.csv',encoding='gbk')
print(duptest)

#给数据按条件去重
print(duptest.drop_duplicates()) #默认是所有列一致时，就删除。第9和2重复，默认保留前面的，保留了2
print(duptest.drop_duplicates(subset=['order_id','dishs_name'],keep='last')) #限定相似的列，一致则删除，保留最后一个