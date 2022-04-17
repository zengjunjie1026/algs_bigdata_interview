import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('../datasets/studentscores.csv')
print(dataset)
df = dataset.sort_values("Scores",ascending=False)
print(df)
dataset.head(30)

X = dataset.iloc[ 0: 25,   : 1 ].values
Y = dataset.iloc[ 0: 25, -1: ].values
print("X:",X)
print("Y:",Y)

from sklearn.model_selection import train_test_split
#拆分数据，0.25作为测试集
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)
print(X_train,X_test)
print(Y_train,Y_test)


from sklearn.linear_model import LinearRegression
#使用训练集对模型进行训练
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)


Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

#散点图
plt.scatter(X_train , Y_train, color = 'red')
#线图
plt.plot(X_train , regressor.predict(X_train), 'bo-')
plt.show()


#散点图
plt.scatter(X_test , Y_test, color = 'red')
#线图
plt.plot(X_test ,Y_pred, 'bo-')
plt.show()


print(X_test,Y_test)