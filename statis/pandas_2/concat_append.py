#实现数据框堆叠
import pandas as pd

d1= {'ID':[1,2,3],'computer':['win7','win8','win10'],'core':['i5','i7','i3']}
d2= {'ID':[3,4,5],'computer':['win11','win7','win10'],'core':['i9','i5','i3']}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print(pd.concat([df1,df2])) #默认是纵向堆叠
print(pd.concat([df1,df2],axis=1))

#如果数据框不一样
df1['tmp']=5
print(pd.concat([df1,df2],join='outer')) #取并集，用空值补齐
print(pd.concat([df1,df2],join='inner')) #取交集


