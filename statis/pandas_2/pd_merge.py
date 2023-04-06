#通过主键连接两张数据框
import pandas as pd

dishtest = pd.read_excel('data\\dishtest.xlsx')
ordertest = pd.read_excel('data\\ordertest.xlsx')

print(pd.merge(ordertest,dishtest,how='left',on='dish_id'))  #通过菜名id连接两张表