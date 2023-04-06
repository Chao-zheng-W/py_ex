import pandas as pd

#读取excel文件
data_excel = pd.read_excel('data\\testdata3.xlsx',sheet_name='class2')
print(data_excel)


#写入excel文件
data_excel.to_excel('data\\todata3.xlsx',sheet_name='class2',index=None) #与csv，txt文件类似，多了sheet_name参数