#哑变量处理
import pandas as pd
dummies_test = pd.read_excel('data\\dishtest.xlsx')
print(dummies_test)

print(pd.get_dummies(dummies_test['dish_name']))  #用0和1 把不像是变量的改成变量，