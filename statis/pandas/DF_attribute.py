#数据框属性
import pandas as pd
d = [[2,4,6],[8,9.2,10],[1,5,7]]
df2 = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C']) #可以放列表
print(df2)
print('------------------------------------')
print(df2.index)
print(df2.shape)
print(df2.values)
print(df2.dtypes)