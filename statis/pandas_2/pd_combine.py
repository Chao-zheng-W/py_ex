#实现数据合并，把空值给覆盖
import pandas as pd
import numpy as np

d1= {'ID':[1,np.nan,3],'computer':['win7','win8','win10'],'core':['i5',np.nan,'i3']}
d2= {'ID':[3,4,np.nan],'computer':['win11',np.nan,'win10'],'core':['i9','i5','i3']}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

print(df1.combine_first(df2))  #用df2把df1的空值覆盖，要保证两张表的列名称是一致的

