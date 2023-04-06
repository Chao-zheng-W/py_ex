import pandas as pd
d = [[2,4,6],[8,9.2,10],[1,5,7]]
df = pd.DataFrame(d,index=['a','b','c'],columns=['A','B','C'])

##按照行列顺序查询数据框内元素
print(df['A'])  #查询单列数据
print(df[['A','B']])  #查询多列数据

#查询前面或后面几行数据
print("查询前面或后面几行数据")
print(df.head(2))  #查询前两行数据
print(df.tail(2))  #查询后两行数据

#也可以用索引，但是要iloc方法
print("也可以用索引，但是要iloc方法")
print(df)
print(df.iloc[0,2]) #第0行，第2列元素
print(df.iloc[0,:]) #第0行所有元素，列同理 返回series类型
print(df.iloc[1:3,0:2]) #第1-2行，第0-1列元素
print(df.iloc[1:3,0:])  #第1-2行，第0-最后列元素

##按照行列名称访问数据
print('按照行列名称访问数据')
print(df)
print(df.loc['a','C'])
print(df.loc['a',:])
print(df.loc['b':'c','A':'B']) #第1-2行，第0-1列元素;注意这里是左闭右闭区间
print(df.loc['b':'c','A':])  #第1-2行，第0-最后列元素

##内容相同，注意返回类型不同
print(df.iloc[:,0])
print(type(df.iloc[:,0]))  #Series类型
print(df.iloc[:,0:1])
print(type(df.iloc[:,0:1])) #DataFrame类型