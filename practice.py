import pandas as pd
import numpy as np

# maligent= pd.read_csv("maligent.csv")
# maligent_test = maligent[0:71]
# maligent_test.to_csv('maligent_test.csv', index=False)
# print(pd.read_csv("maligent_test.csv"))


# begnin= pd.read_csv("begnin.csv")
# print(begnin)
# begnin_test = begnin[0:41]
# begnin_test.to_csv('begnin_test.csv', index=False)
# print(pd.read_csv("begnin_test.csv",header=None))

train = pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
t = train.iloc[:,0:5].values
check=test.iloc[:,-1].values
# Y = train.iloc[:, -1].values
# y=[[i] for i in Y]
# for i in range(len(Y)):
#     y.append([Y[i]])

print(t)
# print(y)
# print(np.concatenate((x, y), axis=1))
