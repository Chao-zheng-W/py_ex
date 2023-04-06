#处理时间序列数据
import pandas as pd
time_test = pd.read_csv('data\\timetest.csv')
print(time_test)

time_test2 = pd.to_datetime(time_test['lock_time']) #转换成Datatime类型
print(time_test2)

print(time_test["start_time"])
time_test["start_time"] = pd.to_datetime(time_test['start_time']) #也可以放回原数据框中
print(time_test["start_time"])  #从object转换成Datatime类型

print(pd.DatetimeIndex(time_test['lock_time']))
print(pd.DatetimeIndex(time_test2))

print(pd.PeriodIndex(time_test['lock_time'],freq="H"))  #以时间为间隔
print(pd.PeriodIndex(time_test['lock_time'],freq="D"))  #以时间为间隔
print(pd.PeriodIndex(time_test['lock_time'],freq="Y"))  #以时间为间隔

