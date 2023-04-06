#直接的透视表函数
import pandas as pd
detail = pd.read_excel('data\\ordertest.xlsx')
print(detail.head()) #显示前5条即可

#透视表
print(pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id',aggfunc='sum')).head()
#限定了行列的透视表
print(pd.pivot_table(detail[['order_id',"dishs_name",'counts']],index='order_id',columns="dishs_name",aggfunc='sum')).head()
#把空值改成0
print(pd.pivot_table(detail[['order_id',"dishs_name",'counts']],index='order_id',columns="dishs_name",aggfunc='sum',fill_value=0)).head()