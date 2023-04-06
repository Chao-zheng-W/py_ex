#绘制折线图
import numpy as np
import  matplotlib.pyplot as plt

#编造数据
x_date =[]
for i in range(2010,2018):
    for j in ['第一季度','第二季度','第三季度','第四季度']:
        x_date.append(f'{i}年{j}')
x_date=np.array(x_date)
y_data = np.array([range(10,42),range(15,47),range(20,52)])


#绘制散点图
plt.figure(figsize=(8,8))

plt.rcParams['font.sans-serif']= 'SimHei'  #设置中文显示
plt.rcParams['axes.unicode_minus'] = False

plt.plot(x_date,y_data[0,:],marker='o',ls ='-')  #把scatter换成plot
plt.plot(x_date,y_data[1,:],linestyle= '-.')  #linestyle 和ls意思相同，表示线的样式
plt.plot(x_date,y_data[2,:],marker='D',linestyle= ':')
plt.xticks(range(0,32,4),x_date[range(0,32,4)],rotation=45) #设置横坐标的格式，不进行设置会很密;rotaion代表旋转
plt.ylabel('生产总值（亿元）')
plt.title('产业生产总值散点图')
plt.legend(['第一产业','第二产业','第三产业']) #图例顺序和绘图顺序一致

#plt.savefig('ex_2.png')
plt.show()