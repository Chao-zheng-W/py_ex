import pandas as pd
#Series系列
ser1 = pd.Series(['1','0.5','3'],index=['a','b','c'])
print(ser1)
ser2 = pd.Series({'a':[1,2,3],'b':[5,6,7]})
print(ser2)

#创建数据框
d = [[2,4,6],[8,9,10],[1,5,7]]
df1 = pd.DataFrame(d)
print(df1)
df2 = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C']) #可以放列表
print(df2)

df3 = pd.DataFrame(index=['1','2'],columns=['1','2'])  #生成空值的数据框
df4 = pd.DataFrame(0,index=['1','2'],columns=['1','2'])  #直接生成全为0的数据框
print(df3)
print(df4)

#数据框装字典
dic = {'object':['pen','box'],'color':['red','blue'],'price':[2,4]}
print(pd.DataFrame(dic))

