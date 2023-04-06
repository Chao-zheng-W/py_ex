#交叉表函数，性质和透视表类似，但功能更专一
import pandas as pd
detail = pd.read_excel('data\\ordertest.xlsx')
print(detail.head()) #显示前5条即可

print(pd.crosstab(index=detail['order_id'],columns=detail['dishs_name']))  #表示频率，是否点了这个菜
#返回点了菜的数量平方
print(pd.crosstab(index=detail['order_id'],columns=detail['dishs_name'],values=detail['counts'],aggfunc=lambda x:sum(x)**2))
