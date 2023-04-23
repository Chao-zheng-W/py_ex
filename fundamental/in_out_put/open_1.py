file = open('abc.txt','r')  #r表示以读方式打卡文件

'''以下代码不能同时运行产生效果
最好运行注释其他行
'''

print(file.read())  #读取全部内容
print(file.read(2))  #自读取两个字符
print(file.readline())  #读取第一行
print(file.readlines())  #按行读取存储在列表里
file.close()  #注意关闭资源

