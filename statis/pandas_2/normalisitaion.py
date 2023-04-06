#数据标准化
import pandas as pd
stander_test = pd.read_excel('data\\outlier_test.xlsx')
print(stander_test)

#min_max_scaler
def min_max_scaler(x):
    y = (x-x.min()) / (x.max()-x.min())
    return y
print(stander_test.agg(min_max_scaler))

#stander_scaler
def stander_scaler(x):
    y = (x-x.mean())/x.std()
    return y
print(stander_test.agg(stander_scaler))

#decimal_scaler
def decimal_scaler(x):
    import numpy as np
    k = np.ceil( np.log10(x.abs().max()))
    y = x/10**k
    return y
print(stander_test.agg(decimal_scaler))
