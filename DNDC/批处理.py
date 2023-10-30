#核心思路是以站点为基础取数，不然会变得非常复杂，嵌套出了3维甚至更高的数组
import numpy as np
import os

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def match_station(list,station):     #定义一个函数，可以把符合要求的站点都提取出来
    station_index=np.where(list[:,0] == station) #取出原数据.txt第一列，找到站点station的索引行
    return station_index

def index_to_volumn(station_index,list):  #前一个参数是match_station的结果，后一个参数是直接从.txt读出的原值
    rank = 0
    for j in station_index:     #第二个循环遍历站点的每个索引，并且在.txt文件中找到
        rank += 1                           #rank作为辅助，第一次拿到的值作为起始数组，后面的都往上面叠加
        if rank==1:
            result=list[j,:]
        else:
            result=np.vstack((result,list[j,:]))  #得到单个站点单个月份的所有数据
    return result

def tem_result_fun(tem_path,station):  #读取改造温度文件,放到一个array里
    rank = 0
    for i in findAllFile(tem_path):
        tem = np.loadtxt(i, usecols=(0, 8, 9), dtype=int)  # 读取温度文件
        rank += 1
        if rank == 1:
            tem_result = index_to_volumn(match_station(tem, station), tem)
        else:
            tem_result = np.vstack((tem_result, index_to_volumn(match_station(tem, station), tem)))  # 单个站点所有月份叠加，即单个站点全年数据
    return tem_result

def pre_result_fun(pre_path,station):  #读取改造降水文件,放到一个array里
    rank = 0
    for i in findAllFile(pre_path):
        pre = np.loadtxt(i, usecols=(0,9), dtype=int)  #读取降水文件
        rank += 1
        if rank == 1:
            pre_result = index_to_volumn(match_station(pre, station), pre)
        else:
            pre_result = np.vstack((pre_result, index_to_volumn(match_station(pre, station), pre)))  # 单个站点所有月份叠加，即单个站点全年数据
    return pre_result

def add_fun(tem_result,pre_result):      #水平连接，添加列号
    total_result=np.hstack((tem_result[:,1:],pre_result[:,1:]))       #把降水和温度数据水平连接
    index=np.arange(1,len(total_result)+1).reshape(len(total_result),1)
    total_index_result=np.hstack((index,total_result))                #在最前列添加序号
    return total_index_result

for j in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)),j))
    try:
        os.mkdir(j + ".\结果")  # 在年份路径下创建结果文件夹
    except:
        pass
    tem_path = os.path.join(j, '温度\\')
    pre_path = os.path.join(j, '降水\\')
    print(tem_path)

    station=[59321,59320,59322,59130,59129,59125,59127,
             59126,59124,59122,59137,59134,59133,59131,
             58928,58929,58934,58938,58936,58946,58944,58942]
    for i in station:
        try:
            tem_result=tem_result_fun(tem_path,i)
            pre_result=pre_result_fun(pre_path,i)
            total_index_result=add_fun(tem_result,pre_result)
            result_path=os.path.join(j,f'结果\\{i}.txt')
            print(f'开始写入{j}的  {i}.txt')
            np.savetxt(result_path,total_index_result,fmt='%d') #写入txt文件
        except:
            pass