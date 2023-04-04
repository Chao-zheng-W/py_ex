import os.path

#获取文件绝对路径
print(os.path.abspath('open_1.py'))

#判断文件是否在当前目录，返回布尔值
print(os.path.exists('open_1.py'),os.path.exists('open_4.py'))

#把文件添加到路径下
print(os.path.join('D:\\py_ex\py_ex\in_out put','open_1.py'))

#把文件和路径分离，返回一个元组
print(os.path.split('D:\\py_ex\py_ex\in_out put\open_1.py'))
#只提取文件
print(os.path.basename('D:\\py_ex\py_ex\in_out put\open_1.py'))
#只提取路径
print(os.path.dirname('D:\\py_ex\py_ex\in_out put\open_1.py'))

#获取文件名和扩展名
print(os.path.splitext('open_1.py'))