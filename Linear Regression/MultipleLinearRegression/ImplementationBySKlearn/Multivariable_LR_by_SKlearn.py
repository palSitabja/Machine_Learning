## @Sitabja Pal, 06/10/18, Multiple Linear Regression using Sklearn package

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#import statsmodels.formula.api as sm

data=pd.read_csv('50_Startups.csv')
print(data.head())

##Data Preprocessing and Encoding Dummy Variable

x=data.iloc[:,:-1].values
y=data.iloc[:,4].values
labelencoder=LabelEncoder()
x[:,3]=labelencoder.fit_transform(x[:,3])
hotencoder=OneHotEncoder(categorical_features=[3])
x=hotencoder.fit_transform(x).toarray()
x=x[:,1:]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0) # train test split

## Regression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)
plt.scatter(x_test[:,2],y_test)
plt.scatter(x_test[:,2],y_pred)
plt.xlabel("R&D spent")
plt.ylabel("Profit")
plt.show()