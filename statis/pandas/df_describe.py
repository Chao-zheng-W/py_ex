import pandas as pd
import numpy as np
d = [[2,4,6],[8,9.2,10],[1,5,7]]
df = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C'])
print(df)

print(df.mean(axis=0))  #按列算平均
print(np.mean(df,axis=0)) #可以使用numpy的函数
print(df.std())  #求标准差
print(df.describe())  #按列求出描述分析值