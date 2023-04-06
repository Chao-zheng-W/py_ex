#连续数据，离散化
import pandas as pd
cut_test = pd.read_excel('data\\ordertest.xlsx')
print(cut_test)

#把amouts变成区间取值，等价于离散化
print(pd.cut(cut_test['amounts'],5))  #分割为5个区间

