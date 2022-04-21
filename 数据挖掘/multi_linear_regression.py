import pandas as pd
import numpy as np

dataset = pd.read_csv('../datasets/50_Startups.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : ,  4 ].values
Z = dataset.iloc[ : ,  0 ].values
print("X:")
print(X[:10])
print("Y:")
print(Y)
dataset.head(5)

# missing value fill
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=0.0, strategy="mean")
imputer = imputer.fit(X[ : , 0:3])
X[ : , 0:3] = imputer.transform(X[ : , 0:3])
print(X)

# category feature numeric

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder = LabelEncoder()
print("original:")
print(X[:10])
#print(X[: , 3])
X[: , 3] = labelencoder.fit_transform(X[ : , 3])
#print(X[: , 3])
print("labelencoder:")
print(X[:10])
ct = ColumnTransformer([( "encoder", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)
#onehotencoder = OneHotEncoder(categorical_features = [3])
#X = onehotencoder.fit_transform(X).toarray()
print("onehot:")
print(X[:10])


#
X1 = X[: , 1:]


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y, test_size = 0.2, random_state = 0)
print(X_test)
print(Y_test)
print(X1_test)
print(Y1_test)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
regressor1 = LinearRegression()
regressor1.fit(X1_train, Y1_train)


y_pred = regressor.predict(X_test)
y1_pred = regressor1.predict(X1_test)

print(y_pred)
print(y1_pred)