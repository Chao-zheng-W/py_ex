import pandas as pd
d = [[2,4,6],[8,9.2,10],[1,5,7]]
df = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C'])
print(df)

#增加列或行
df['D']=25
df['E']=[1,2,3]
df.loc['d',:] = 30
print(df)

#删除列或行
df.drop('C',axis=1,inplace=True) #axis代表列维度；inplace表示直接作用原数据
print(df)
df1 = df.drop('d',axis=0,inplace=False)
print(df1)