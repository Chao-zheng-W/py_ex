#绘制箱线图
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

plt.boxplot(y_data.T,labels=['第一产业','第二产业','第三产业'],notch=True)  #按列绘制数据，所以要转置;notch表示中位数是否有缺口，美观性
plt.show()