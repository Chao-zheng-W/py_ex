#walk遍历函数
import os
path = os.getcwd()
lst_files = os.walk(path)
print(lst_files) #无法直接输出,需要遍历

for test in lst_files:
    print(test)  #按照dirpath, dirname, filename顺序保存元组，并且每一个层级在一个元组里。
    for i in test:  #顺序是路径，再文件夹名，文件名
        print(i)

print('---------------第二种遍历方法-----------')

#或者是直接遍历
for dirpath,dirname,filename in lst_files:
    print('------------')
    print(dirpath)
    print(dirname)
    print(filename)


