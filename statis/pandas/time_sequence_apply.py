#处理时间序列数据
import pandas as pd
time_test = pd.read_csv('data\\timetest.csv')

#未转换成Datatime，无法进行时间的加减
#print(time_test['lock_time']+pd.Timedelta(days=1))  #报错

time_test['lock_time']=pd.to_datetime(time_test['lock_time'])
print(time_test['lock_time'])
print(time_test['lock_time']+pd.Timedelta(days=1))  #转换成Database后就可以加减日期

#直接读取日期所在的年、月、周
print(time_test['lock_time'][0].year,time_test['lock_time'][0].week) #按照索引读取
print(time_test['lock_time'].dt.year,time_test['lock_time'].dt.week) #向量化读取
