#enconding=utf-8
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1.1,0.1)
print(x)

plt.figure(num=1)  #第一环节：创建画布
plt.plot(x,x**2)   #第二环节：画出线
plt.plot(x,x**4)   #第二环节：依然在上面画布里，画出第二条线
plt.legend(['y=x^2','y=x^4',]) #第二环节：画图例，顺序和画线的顺序一致
plt.xlim(0,1)      #第二环节：限制x轴长度
plt.ylim(0,1)      #第二环节：限制y轴长度
plt.title('lines')  #第二环节：图标题
plt.xlabel("x axis")  #第二环节：x轴输入标题
plt.ylabel('y axis')  #第二环节：y轴输入标题


plt.show()         #第三环节：展示图像
plt.savefig('ex_1.png')  #第三环节：保存图像