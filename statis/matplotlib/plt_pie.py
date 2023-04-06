#绘制饼图
import numpy as np
import  matplotlib.pyplot as plt

#编造数据
x_date =[]
for i in range(2010,2018):
    for j in ['第一季度','第二季度','第三季度','第四季度']:
        x_date.append(f'{i}年{j}')
x_date=np.array(x_date)
y_data = np.array([range(10,42),range(15,47),range(20,52)])

#画图
plt.figure(figsize=(8,8))

plt.rcParams['font.sans-serif']= 'SimHei'  #设置中文显示
plt.rcParams['axes.unicode_minus'] = False

plt.pie(y_data[0,0:4],labels=x_date[0:4],explode=[0.1,0.1,0.1,0.1],autopct='%1.1f%%')  #使用pie函数;explode代表扇形离圆心的距离;autopct='%1.1f%%'代表保留一位小数的比例

plt.show()

