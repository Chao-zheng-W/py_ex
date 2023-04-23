file = open('abc_new.txt','w')  #w表示以写方式打卡文件，如果没有则创建,如果有就覆盖掉
file.write('python')
file.close()  #注意关闭资源

file = open('abc_new.txt','a')  #与w不同，是后面追加
file.write('python')
file.close()  #注意关闭资源

'''除了r,a,w还有
rb:按照二进制读取，可用于图片形式的文件
wb:同上
a+:读写模式打开，兼备r和w的功能
'''