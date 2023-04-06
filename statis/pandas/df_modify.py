#修改数据框中的元素
import pandas as pd
d = [[2,4,6],[8,9.2,10],[1,5,7]]
df = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C'])

#修改直接发生在原数据框上，所以最好确认或者备份
print(df)
df.loc['a','A']=100
print(df) #修改单个元素
#df.loc[:,'B'] = 20  #修改整列元素,报错版本不兼容
#df.loc[:,'B'] = [1,2,3]  #修改整列元素,报错版本不兼容
print(df)
