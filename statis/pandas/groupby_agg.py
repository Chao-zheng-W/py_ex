#分组聚合操作
import pandas as pd
import numpy as np
detail = pd.read_excel('data\\ordertest.xlsx')
print(detail.head()) #显示前5条即可

#分组聚合有点像数据透视表
detail_group = detail[['order_id','counts','amounts']].groupby(by='order_id') #以order_id作为分组依据
print(detail_group) #结果只能展示内存地址，需要配合agg使用

print(detail_group.agg('mean'))  #显示另外两列平均值，每桌点菜品平均数量，每桌菜品平均价格
print(detail_group.agg(['mean','sum']))
print(detail_group.agg({'counts':['mean', np.max],'amounts':'sum'}))
print(detail_group.agg(lambda x: sum(x)**2)) #使用匿名函数,返回groupby和的平方